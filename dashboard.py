#!/usr/bin/env python
# coding: utf-8


# In[318]:


# Import required libraries
import pandas as pd
from jupyter_dash import JupyterDash
import dash_cytoscape as cyto
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np


# In[319]:


df=pd.read_csv("LSTMCVresults.csv")
df1=pd.read_csv("OservedAndSimulation.csv")
df2=pd.read_csv("NSE_LSTM.csv")


# In[320]:


import numpy as np
np.mean(df2["NSE_Test"])


# In[321]:


Data={"LSTM":{"Results":df,"OnS":df1,"NSE":df2},
     "GRU":{"Results":df,"OnS":df1,"NSE":df2},
     "SimpleRNN":{"Results":df,"OnS":df1,"NSE":df2},
     }


# In[322]:


def lineplot(Model,Data1):
    lineplot=px.line(Data[Model]["Results"],x="Date",y=Data1,color="Category",template = 'plotly_dark',
                     title="Observed, Training and Testing Discharge Data")
    return lineplot
def reg_test_discharge_fig(Model):
    reg_test_discharge_fig = px.scatter(Data[Model]["OnS"], x='Simulated', y='Observed',
                                        trendline="ols",
                                        template = 'plotly_dark',
                                        title='Regression Plot between Observed and Simulated River Discharge')
    #reg_test_discharge_fig.update_layout(autosize=False,width=500,height=500)
    return reg_test_discharge_fig
#reg_test_discharge_fig()


# In[ ]:





# In[323]:


def Dashboard():
    # Import required libraries
    import pandas as pd
    import dash
    import dash_html_components as html
    import dash_core_components as dcc
    from dash.dependencies import Input, Output
    import plotly.express as px

    # Create a dash application
    #app = dash.Dash(__name__)
    # Create a dash application
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    app = JupyterDash(__name__, external_stylesheets=external_stylesheets)

    # Build dash app layout
    app.layout = html.Div(children=[ html.H1('Marshyandi River Discharge Simulation',
                                             style={'textAlign': 'center', 'color': '#503D36','font-size': 30}),
                                    ################################
                                    html.Div(["Choose Model:",dcc.Dropdown(id="select model",options=[{"label":"LSTM","value":"LSTM"},
                                                                            {"label":"GRU","value":"GRU"},{"label":"SimpleRNN","value":"SimpleRNN"}],
                                                                           value="LSTM",style={'height':'35px', 'font-size': 20,"width":"50%"})]),


                                    html.Br(),
                                    html.Br(), 
                                    html.Div(id="NSE"),

                                    html.Br(),
                                    ###
                                    dcc.Graph(id='Test_Run1'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run2'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run3'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run4'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run5'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run6'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run7'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run8'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run9'),
                                    html.Br(),
                                    dcc.Graph(id='Test_Run10'),
                                    html.Br(),    
                                    dcc.Graph(id='Regplot'),
                                    html.Br()
                                   ])

    # Callback decorator
    @app.callback([
        Output(component_id='NSE', component_property='children'),
        Output(component_id='Test_Run1', component_property='figure'),
        Output(component_id='Test_Run2', component_property='figure'),
        Output(component_id='Test_Run3', component_property='figure'),
        Output(component_id='Test_Run4', component_property='figure'),
        Output(component_id='Test_Run5', component_property='figure'),
        Output(component_id='Test_Run6', component_property='figure'),
        Output(component_id='Test_Run7', component_property='figure'),
        Output(component_id='Test_Run8', component_property='figure'),
        Output(component_id='Test_Run9', component_property='figure'),
        Output(component_id='Test_Run10', component_property='figure'),
        Output(component_id='Regplot', component_property='figure')

    ],
    Input(component_id='select model', component_property='value'))

    # Computation to callback function and return graph
    def get_graph(Model):
        NSE= "The Average Nash–Sutcliffe for 10 fold Cross Validation is "        +str(round(np.mean(Data[Model]["NSE"]["NSE_Test"]),2))
        fig1 = lineplot(Model,"Test_run1")
        fig2 = lineplot(Model,"Test_run2")
        fig3 = lineplot(Model,"Test_run3")
        fig4 = lineplot(Model,"Test_run4")
        fig5 = lineplot(Model,"Test_run5")
        fig6 = lineplot(Model,"Test_run6")
        fig7 = lineplot(Model,"Test_run7")
        fig8 = lineplot(Model,"Test_run8")
        fig9 = lineplot(Model,"Test_run9")
        fig10 = lineplot(Model,"Test_run10")
        fig11= reg_test_discharge_fig(Model)
        ###
        return[NSE,fig1,fig2,fig3,fig4,fig5,fig6,fig7,fig8,fig9,fig10,fig11]
    # Run the app
    if __name__ == '__main__':
        return app.run_server(mode='inline', port=8030)


# In[ ]:




