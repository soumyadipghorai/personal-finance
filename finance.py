import pandas as pd 
import numpy as np 
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go


class PersonalFinance : 
    
    def __init__(self) : 

        self.main_data = 'data/bangalore  - item.csv'
        self.additional_data = 'data/bangalore  - Total_spending.csv'

        ################# ? for automatically extract data from excel sheet #######################
        # self.sheet_id = '1JkDMZ_sdU0aoRP9EI3hkfiER3iSVYYQpC-CGzK9NNAc'
        # self.main_sheet_name = 'item'
        # self.additional_sheet_name = 'Total_spending'
        # self.main_data = f'https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={main_sheet_name}'

    def read_data(self, data) : 
        if data == 'primary' :
            df = pd.read_csv(self.main_data)

            ################# ? for automatically extract data from excel sheet #######################
            # link = f'https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.main_sheet_name}'
            # df = pd.read_csv(link)
            # df.dropna(axis = 1, inplace = True)

        return df
 
    def preprocess_dataframe(self) : 
        
        ################# ? for automatically extract data from excel sheet #######################
        # link = f'https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.main_sheet_name}'
        # df = pd.read_csv(link)
        # df.dropna(axis = 1, inplace = True)
        
        df = pd.read_csv(self.main_data)
        
        df.rename({
                'date ' : 'date',
                'item_name ' : 'item_name',
                'item_category ' : 'item_category',
                'price ' : 'price'    
                }, axis = 1, inplace = True)

        df.dropna(inplace = True)
        date = df.date.str.split('/', expand =True)

        df['month'] = date[0]
        df['day'] = date[1]
        df['year'] = date[2]

        df.year = pd.to_numeric(df.year)
        df.month = pd.to_numeric(df.month)
        df.day = pd.to_numeric(df.day)

        df.date = pd.to_datetime(df.date)

        month_name = []
        
        date_dict = { 
            1 : 'Jan', 2 : 'Feb', 3 : 'Mar', 4 : 'Apr', 
            5 : 'May', 6 : 'Jun', 7 : 'Jul', 8 : 'Aug',
            9 : 'Sep', 10 : 'Oct', 11 : 'Nov', 12 : 'Dec'
        }

        for i in range(len(df)) : 
            month_name.append(date_dict[df.month.iloc[i]])

        df['month_name'] = month_name
        
        return df 

    def plot_expenses(self, value) :
        
        df = self.preprocess_dataframe()
        
        if value == 'date' : 
            date_df = df.groupby(['date'])['price'].sum().reset_index()
            fig = go.Figure(
                data=go.Scatter(x=date_df['date'], 
                y=date_df['price'],
                mode='lines',
                line_color='#eb4034')
            )

            fig.update_layout(plot_bgcolor="white")
            return fig

        elif value == 'month' : 
            dummy_df = df.groupby(['month', 'month_name', 'item_category'])['price'].sum().reset_index()
            dummy_df = dummy_df[(dummy_df.month_name != 'Dec') & (dummy_df.month_name != 'Nov')]

            fig = go.Figure()
            counter, color_list = 0, ['#67001f', '#b2182b', '#d6604d', '#f4a582', '#fddbc7', '#b59f9f', '#d1e5f0']
            month_list = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

            # * due to some sorting issues while plotting I have used predefined month names rather than using df month names 
            for category in dummy_df.item_category.unique() :
                temp_df = dummy_df[dummy_df.item_category == category]
                temp_df.sort_values(by='month', inplace = True)
                fig.add_trace(go.Bar(
                    # x=temp_df.month_name,
                    x = month_list[:len(dummy_df.month.unique())],
                    y=temp_df.price,
                    name= category,
                    marker_color= color_list[counter]
                ))

                counter += 1 
            
            monthly_spending_df = df.groupby(['month', 'month_name'])['price'].sum().reset_index()
            monthly_spending_df = monthly_spending_df[
                (monthly_spending_df.month_name != 'Dec') & (monthly_spending_df.month_name != 'Nov')
            ]
            curr_month = monthly_spending_df['price'].iloc[len(monthly_spending_df)-1]
            prev_month = monthly_spending_df['price'].iloc[len(monthly_spending_df)-2]
            percent = 100*((curr_month - prev_month)/prev_month)

            fig.update_layout(plot_bgcolor="white", barmode='group')
            return fig, round(percent,2), monthly_spending_df

    def share_of_category(self) : 
        df = self.preprocess_dataframe()
        category_df = df.groupby(['item_category'])['price'].sum().reset_index()
        fig = px.pie(
            category_df, values = 'price', names = 'item_category', 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
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

        ################# ? for automatically extract data from excel sheet #######################
        # link = f'https://docs.google.com/spreadsheets/d/{self.sheet_id}/gviz/tq?tqx=out:csv&sheet={self.additional_sheet_name}'
        # df = pd.read_csv(link)
        # df.dropna(axis = 1, inplace = True)
        
        df = pd.read_csv(self.additional_data)
        df = df.T.reset_index()
        total_expense = df[0].iloc[4]
        df = df.drop(4)
        fig = px.pie(
            df, names = 'index', values = 0, 
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        return fig, total_expense

    def plot_treemap(self) : 
        df = self.preprocess_dataframe()
        dummy_df = df.rename(columns = {'price' : 'total spending'})
        fig = px.treemap(
            dummy_df, path = [px.Constant('total spending'), 'item_name'], color='total spending',
            values = 'total spending', color_continuous_scale='reds',
        )

        return fig
