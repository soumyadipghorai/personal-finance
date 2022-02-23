from re import L
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go

class Demo : 
    def __init__(self) :
        self.location = 'data/bangalore  - item.csv' 
    
    def read_csv(self) : 
        df = pd.read_csv(self.location)
        return df

    def plot_box_plot(self,feature) : 
        df = self.read_csv()
        dummy_df = df[df['item_category '] == feature]
        fig = px.box(dummy_df, y = 'price ')
        return fig