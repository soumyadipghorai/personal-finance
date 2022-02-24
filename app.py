import streamlit as st
from finance import PersonalFinance as pf

df = pf()
 
PAGE_CONFIG = {"page_title":"Personal Finance", 
            #    "page_icon":image, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.sidebar.markdown("## Controls")
# sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Predictions', 'Q&A'])
sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Q&A'])

if sidebar_main == 'About the Project' : 
    st.title('Personal Finance Dashboard')
    st.markdown("""
        ##### Since when I moved to Bangalore I've been monitoring my expenses and this is my dashboard 
    """)
    st.image('static/compressed_heroimage.gif', caption = 'Personal Finance')

    st.markdown("""
    ###### The dataset looks some what like this 
    """)
    st.dataframe(df.read_data('primary').head())
 
elif sidebar_main == 'EDA' : 
    st.title('Expense dashboard')
    sidebar_sub = st.sidebar.radio('Navigation', ['Expense', 'Category', 'boxplot', 'total expenses', 'treemap'])
    
    data = df.preprocess_dataframe()

    st.markdown(
            """
            ##### After preprocessing the data looks like this
            """
        )
    st.dataframe(data.head())
    if sidebar_sub == 'Expense' : 

        st.markdown(
            """
            ##### Check the expenses 
            """
        )
        # col1, col2, col3 = st.columns(3)
        col1, col2 = st.columns(2)
        with col1 : 
            daily = st.button('Daily') 

        with col2 :  
            monthly = st.button('Monthly')
        # with col3 : 
        #     val2 = st.button('click me once more')
        
        if monthly : 
            st.plotly_chart(df.plot_expenses('month'))

        else : 
            st.plotly_chart(df.plot_expenses('date'))

    elif sidebar_sub == 'Category' :
        st.markdown(
            """
            ##### Category wise expenses 
            """
        ) 
        st.plotly_chart(df.share_of_category())

    elif sidebar_sub == 'boxplot' : 
        st.markdown(
            """
            ##### Category wise boxplot 
            """
        ) 
        col1, col2 = st.columns(2)
        with col1 : 
            food = st.button('food') 

        with col2 :  
            travel = st.button('travel')
        if travel :
            st.plotly_chart(df.plot_boxplot('travel'))
        else: 
            st.plotly_chart(df.plot_boxplot('food'))

    elif sidebar_sub == 'total expenses' : 
        st.markdown(
            """
            ##### Total Expenses 
            """
        ) 
        st.plotly_chart(df.total_spending()[0])
        st.write('Total amount spent is ',df.total_spending()[1])

    else : 
        st.markdown(
            """
            ##### Spending on items 
            """
        ) 
        st.plotly_chart(df.plot_treemap())

# elif sidebar_main == 'Predictions' : 
#     pass 

else : 
    # dropdown
    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on food :')
    with col2 :
        check = st.button('check', key = 1)
    
    if check : 
        st.write('I ate ', df.find_max('food')[0], ' on ', df.find_max('food')[2].date(), ' with ', df.find_max('food')[1])
    
    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on travel :')
    with col2 :
        check = st.button('check', key = 2)
    
    if check : 
        st.write('I used ', df.find_max('travel')[0], ' on ', df.find_max('travel')[2].date(), ' for ', df.find_max('travel')[1])

    col1, col2 = st.columns(2)
    with col1 :
        st.write('Max amount spent on wants :')
    with col2 :
        check = st.button('check', key = 3)
    
    if check : 
        st.write('I have done ', df.find_max('wants')[0], ' on ', df.find_max('wants')[2].date(), ' for ', df.find_max('wants')[1])

footer="""
    <style>
        a:link , a:visited{
            color: blue;
            background-color: transparent;
            text-decoration: underline;
        }

        a:hover,  a:active {
            color: red;
            background-color: transparent;
            text-decoration: underline;
        }

        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: white;
            color: black;
            text-align: center;
        }
    </style>
    <div class="footer">
        <p>Developed with ❤️ by <a style= text-align: center;'><b>Soumyadip Ghorai</b></a></p>
        <p><a href = 'https://datascience-dailys.herokuapp.com/' target = '_blank'>github</a></p>
    </div>
"""
st.markdown(footer,unsafe_allow_html=True)