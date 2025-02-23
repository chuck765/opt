from pyqubo import Array, Constraint, Placeholder
import neal
import openjij as oj
from dataclasses import dataclass
from typing import List

from modules.dataclass import Problem, Node

@dataclass
class ModelRouteFeedParam():
    obj_feed: float           = 1.0
    onehot_city_feed: float   = 1.0
    onehot_order_feed: float  = 1.0
    fixed_feed :float         = 1.0


@dataclass
class ModelRouteAnnealingParam():
    sampler: str                    = "neal"
    num_reads: int                  = 1
    beta_min: float                 = 0.1
    beta_max: float                 = 1000.0
    num_sweeps: int                 = 1000
    

class ModelRoute():
    """ルート最適化
    """
    problem : Problem                         = None
    nodes   : Node                            = None
    dist_matrix : dict                        = None       
    feed_param : ModelRouteFeedParam          = None
    annealing_param: ModelRouteAnnealingParam = None
    route : List[List[int]]                   = None
    
    def __init__(self, problem: Problem, nodes: Node, dist_matrix: dict):
        self.problem = problem
        self.nodes = nodes
        self.dist_matrix = dist_matrix
        self.feed_param = ModelRouteFeedParam()
        self.annealing_param = ModelRouteAnnealingParam()
    
    def is_neal(self):
        return self.annealing_param.sampler == 'neal'
    
    def is_jij(self):
        return self.annealing_param.sampler == 'jij'
    
    def define_spin(self):
        """スピンを定義
        """
        # スピン: 都市iをj番目に移動するかどうか
        dimension = self.problem.dimension
        x = Array.create('x', shape=(dimension,dimension), vartype='BINARY')
        return x

    def get_objectives(self, x):
        """目的関数を取得
        2点間の距離がなるべく近い点を選択したい
        """
        dimension = self.problem.dimension
        dist_matrix = self.dist_matrix
        obj_dist = 0
        for i in range(dimension):
            for j in range(dimension):
                if i == j:
                    continue
                obj_dist += dist_matrix[(i, j)]*x[i][j]*x[int((i+1)%dimension)][j]
        return obj_dist

    def get_constraints(self, x):
        """制約条件を取得
        """
        
        dimension = self.problem.dimension
        # 制約条件1: 各都市は1回は訪問すること
        H1 = 0
        for i in range(dimension):
            H1 += Constraint((sum(x[i][j] for j in range(dimension)) - 1)**2, "H1_{0}".format(i))
        
        # 制約条件2 : 1度に訪れる都市は1つであること
        H2 = 0
        for j in range(dimension):
            H2 += Constraint((sum(x[i][j] for i in range(dimension)) - 1)**2, "H2_{0}".format(j))
        
        # 制約条件3 : 地点ID=1 が開始地点であること (eil51限定制約)
        H3 = Constraint((x[0][0] - 1)**2, "H3_0")
        
        return H1, H2, H3

    def to_optimize(self):
        """最適化実行
        """
        
        # 定式化
        x = self.define_spin()
        obj_dist = self.get_objectives(x)
        H1, H2, H3 = self.get_constraints(x)
        H = Placeholder("obj1")*obj_dist + Placeholder("p1")*H1 + Placeholder("p2")*H2 + Placeholder("p3")*H3
        model = H.compile()
        
        # 重み設定・QUBO生成
        obj1 = self.feed_param.obj_feed
        p1 = self.feed_param.onehot_city_feed
        p2 = self.feed_param.onehot_order_feed
        p3 = self.feed_param.fixed_feed
        feed_dict = {"obj1": obj1, "p1": p1, "p2": p2, "p3": p3}
        qubo, _ = model.to_qubo(feed_dict=feed_dict)
        
        # アニーリング
        num_reads = self.annealing_param.num_reads
        num_sweeps = self.annealing_param.num_sweeps
        beta_min = self.annealing_param.beta_min
        beta_max = self.annealing_param.beta_max
        if self.is_neal():
            sampler = neal.SimulatedAnnealingSampler()
            result = sampler.sample_qubo(qubo, num_reads=num_reads, num_sweeps=num_sweeps, beta_range=[beta_min, beta_max])
        if self.is_jij():
            sampler = oj.SASampler()
            result = sampler.sample_qubo(qubo, num_reads=num_reads, num_sweeps=num_sweeps, beta_min=beta_min, beta_max=beta_max)
        
        # 結果の加工
        dimension = self.problem.dimension
        route = result.record[0][0].reshape(dimension, dimension)
        self.route = route
    
    def check(self, model, sampleset, feed_dict):
        """制約充足チェック

        Args:
            model ( _cpp_pyqubo.Model): コンパイル済のモデル
            sampleset (dimod.sampleset.SampleSet): アニーリング結果
            feed_dict (dict): 項ごとの係数

        Returns:
            list: 制約充足チェック結果
        """
        decoded_samples = model.decode_sampleset(sampleset=sampleset, feed_dict=feed_dict)
        checks = []
        for sample in decoded_samples:
            checks.append(sample.constraints(only_broken=True))
        return checks