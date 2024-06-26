import plotly.graph_objects as go

def visualize(office_address_exist_list):

    x_coords = [row.coordinate[0] for row in office_address_exist_list]
    y_coords = [row.coordinate[1] for row in office_address_exist_list]

    # 散布図の作成
    fig = go.Figure(data=go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='markers',
        marker=dict(size=10, color='blue', symbol='circle')
    ))

    # レイアウトの設定
    fig.update_layout(
        title='サンプル散布図',
        xaxis_title='X 軸',
        yaxis_title='Y 軸',
        showlegend=False
    )

    # グラフの表示
    fig.show()