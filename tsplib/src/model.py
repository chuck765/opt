from pyqubo import Array, Constraint, Placeholder
import neal
import openjij as oj

class TspModel():
    """TSPのモデル・定式化生成クラス
    """
    
    def define_spin(self, data):
        """スピンを定義

        Args:
            data (tsplib_data.TSP): TSPデータ

        Returns:
            Array.create: スピン変数
        """
        # スピン: 都市iをj番目に移動するかどうか
        x = Array.create('x', shape=(data.dimension,data.dimension), vartype='BINARY')
        return x

    def _get_objectives(self, spin, data, dist_matrix):
        """目的関数を取得

        Args:
            spin (Array.create): スピン変数
            data (tsplib_data.TSP): TSPデータ
            dist_matrix (list): 2地点間の距離マトリクス

        Returns:
            cpp_pyqubo.Add: 目的関数変数
        """
        # 目的関数
        S = 0
        for i in range(data.dimension):
            for j in range(data.dimension):
                S += dist_matrix[i][j]*spin[i][j]*spin[int((i+1)%data.dimension)][j]
        return S

    def _get_constraints(self, spin, data):
        """制約条件を取得

        Args:
            spin (Array.create): スピン変数
            data (tsplib_data.TSP): TSPデータ

        Returns:
            cpp_pyqubo.Add: 制約条件変数
        """
        # 制約条件1: 各都市は1回は訪問すること
        H1 = 0
        for i in range(data.dimension):
            H1 += Constraint((sum(spin[i][j] for j in range(data.dimension)) - 1)**2, "H1_{0}".format(i))
        
        # 制約条件2 : 1度に訪れる都市は1つであること
        H2 = 0
        for j in range(data.dimension):
            H2 += Constraint((sum(spin[i][j] for i in range(data.dimension)) - 1)**2, "H2_{0}".format(j))
        
        # 制約条件3 : 地点ID=1 が開始地点であること (eil51限定制約)
        H3 = Constraint((spin[0][0] - 1)**2, "H3_0")
        
        return H1, H2, H3

    def get_model(self, data, dist_matrix):
        """モデルを作成

        Args:
            data (tsplib_data.TSP): TSPデータ
            dist_matrix (list): 2地点間の距離マトリクス

        Returns:
            _cpp_pyqubo.Model: コンパイル済のモデル
        """
        
        # スピン: 都市iをj番目に移動するかどうか
        x = self.define_spin(data)
        
        # 目的関数
        S = self._get_objectives(x, data, dist_matrix)

        # 制約条件
        H1, H2, H3 = self._get_constraints(x, data)
    
        # コンパイル
        H = Placeholder("s1")*S + Placeholder("p1")*H1 + Placeholder("p2")*H2 + Placeholder("p3")*H3
        model = H.compile()
        
        return model
    
    def get_feed(self, s1=1.0, p1=1.0, p2=1.0, p3=1.0):
        """重み係数を取得

        Args:
            s1 (float): s1の係数. Defaults to 1.0.
            p1 (float): p1の係数. Defaults to 1.0.
            p2 (float): p2の係数. Defaults to 1.0.
            p3 (float): p3の係数. Defaults to 1.0.

        Returns:
            dict: 項ごとの係数
        """
        return {"s1": s1, "p1": p1, "p2": p2, "p3": p3}
    
    def to_qubo(self, model, feed_dict):
        """qubo, offsetを取得

        Args:
            model ( _cpp_pyqubo.Model): コンパイル済のモデル
            feed_dict (dict): 項ごとの係数

        Returns:
            dict: quboデータ
            float: オフセット値
        """
        qubo, offset = model.to_qubo(feed_dict=feed_dict)
        return qubo, offset
    
    def annealing(self, sampler="neal", qubo=None, num_reads=1, num_sweeps=1000, beta_min=0.1, beta_max=1000.0):
        """アニーリング関数

        Args:
            sampler (str): ソルバー指定 neal=neal. oj=openJij. Defaults to "neal".
            qubo (dict): quboデータ. Defaults to None.
            num_reads (int): 試行回数. Defaults to 1.
            num_sweeps (int): アニーリングステップ数. Defaults to 1000.
            beta_min (float): ベータ最小値. Defaults to 0.1.
            beta_max (float): ベータ最大値. Defaults to 1000.0.

        Raises:
            Exception: 使用不可のソルバー名を指定した場合の例外

        Returns:
            dimod.sampleset.SampleSet: アニーリング結果
        """
        if sampler == "neal":
            sampler = neal.SimulatedAnnealingSampler()
            result = sampler.sample_qubo(qubo, num_reads=num_reads, num_sweeps=num_sweeps, beta_range=[beta_min, beta_max])
        elif sampler == "oj":
            sampler = oj.SASampler()
            result = sampler.sample_qubo(qubo, num_reads=num_reads, num_sweeps=num_sweeps, beta_min=beta_min, beta_max=beta_max)
        else:
            raise Exception("Not Found Solver.")
        return result
    
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