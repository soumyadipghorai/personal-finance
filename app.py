import streamlit as st
from finance import PersonalFinance as pf

df = pf()

st.sidebar.markdown("## Controls")
# sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Predictions', 'Q&A'])
sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Q&A'])


if sidebar_main == 'About the Project' : 
    st.title('Personal Finance Dashboard')
    st.markdown("""
        ##### Since when I moved to Bangalore I've been monitoring my expanses and this is my dashboard 
    """)
    st.image('static/hero.gif', caption = 'Personal Finance')

    st.markdown("""
    ###### The dataset looks some what like this 
    """)
    st.dataframe(df.read_data('primary').head())
 
elif sidebar_main == 'EDA' : 
    st.title('Expsnse dashboard')
    sidebar_sub = st.sidebar.radio('Navigation', ['Expense', 'Category', 'boxplot', 'total expanses'])
    
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
            ##### Check the expanses 
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
            st.plotly_chart(df.plot_expanses('month'))

        else : 
            st.plotly_chart(df.plot_expanses('date'))

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

    else : 
        st.markdown(
            """
            ##### Total Expanses 
            """
        ) 
        st.plotly_chart(df.total_spending()[0])
        st.write('Total amount spent is ',df.total_spending()[1])

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