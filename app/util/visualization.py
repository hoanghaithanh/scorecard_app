import plotly.graph_objects as go

def create_gauge_chart(credit_score, min_score, max_score):
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=credit_score,
        mode="gauge+number+delta",
        # title={'text': "Your Credit Score"},
        gauge={'axis': {'range': [min_score, max_score]},
               'bar': {'color': "#DC143C"},
               'steps': [
                    {'range': [min_score, 0], 'color': "#FF6347"},
                    {'range': [0, 1500], 'color': "gold"},
                    {'range': [1500, max_score], 'color': "#9ACD32"},
                   ]
               },
        ))
    fig.update_layout(title=dict(text="Your Credit Score", font=dict(size=50),
                                 x=0.5, y=1, xanchor='center', yanchor='top'))

    return fig