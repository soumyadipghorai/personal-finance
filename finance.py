import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


class PersonalFinance : 
    
    def __init__(self) : 
        self.main_data = 'data/bangalore  - item.csv'
        self.additional_data = 'data/bangalore  - Total_spending.csv'

    def read_data(self, data) : 
        if data == 'primary' :
            df = pd.read_csv(self.main_data)
        return df

    def preprocess_dataframe(self) : 
        df = pd.read_csv(self.main_data)
        df.rename({
                'date ' : 'date',
                'item_name ' : 'item_name',
                'item_category ' : 'item_category',
                'price ' : 'price'    
                }, axis = 1, inplace = True)

        date = df.date.str.split('/', expand =True)

        df['month'] = date[0]
        df['day'] = date[1]
        df['year'] = date[2]

        df.year = pd.to_numeric(df.year)
        df.month = pd.to_numeric(df.month)
        df.day = pd.to_numeric(df.day)

        df.date = pd.to_datetime(df.date)

        date_dict = { 1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 5 : 'May',
                     6 : 'Jun', 7 : 'Jul', 8 : 'Aug', 9 : 'Sep', 10 : 'Oct',
                      11 : 'Nov', 12 : 'Dec'}

        for i in range(len(df)) : 
            df.month.iloc[i] = date_dict[df.month.iloc[i]]
        
        return df 

    def plot_expanses(self, value) :
        df = self.preprocess_dataframe()
        if value == 'date' : 
            date_df = df.groupby(['date'])['price'].sum().reset_index()
            fig = go.Figure(data=go.Scatter(x=date_df['date'], y=date_df['price'] ,mode='lines',line_color='#eb4034'))

        elif value == 'month' : 
            dummy_df = df.groupby([value])['price'].sum().reset_index()
            fig = go.Figure(data=[go.Bar(x=dummy_df[value], y=dummy_df.price)])
            fig.update_traces(marker_color='rgb(255, 27, 0)')

        fig.update_layout(plot_bgcolor="white")
        return fig

    def share_of_category(self) : 
        df = self.preprocess_dataframe()
        category_df = df.groupby(['item_category'])['price'].sum().reset_index()
        fig = px.pie(category_df, values = 'price', names = 'item_category', color_discrete_sequence=px.colors.sequential.RdBu)
        return fig

    def plot_boxplot(self, feature) :
        df = self.preprocess_dataframe()
        dummy_df = df[df.item_category == feature]
        # fig = px.box(dummy_df, x = 'price')
        fig = go.Figure(data=[go.Box(x=dummy_df.price)])
        fig.update_traces(marker_color='rgb(255, 27, 0)')
        fig.update_layout(plot_bgcolor="white", title = feature.capitalize())
        return fig

    def find_max(self, category) : 
        df = self.preprocess_dataframe()
        dummy_df = df[df.item_category == category]
        final_df = dummy_df[dummy_df.price == dummy_df.price.max()]
        return final_df['item_name'].iloc[0], final_df['price'].iloc[0], final_df['date'].iloc[0]

    def total_spending(self) : 
        df = pd.read_csv(self.additional_data)
        df = df.T.reset_index()
        total_expanse = df[0].iloc[4]
        df = df.drop(4)
        fig = px.pie(df, names = 'index', values = 0, color_discrete_sequence=px.colors.sequential.RdBu)
        return fig, total_expanse