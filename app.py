import streamlit as st
from finance import PersonalFinance
import markdown as md
df = PersonalFinance()
 
PAGE_CONFIG = {"page_title":"Personal Finance", 
            #    "page_icon":image, 
               "layout":"centered", 
               "initial_sidebar_state":"auto"}

st.set_page_config(**PAGE_CONFIG)

st.sidebar.markdown("## Controls")
# sidebar_main = st.sidebar.selectbox('Navigation', ['About the Project', 'EDA', 'Predictions', 'Q&A'])
sidebar_main = st.sidebar.selectbox('Navigation', ['Home', 'EDA', 'Q&A', 'About the Project'])
 
if sidebar_main == 'Home' : 
    st.title('Personal Finance Dashboard')
    st.markdown("""
        ##### Since when I moved to Bangalore I've been monitoring my expenses and this is my dashboard 
    """)
    
    # * unable to use direct images due to library issue 
    # st.image('static/compressed_heroimage.gif', caption = 'Personal Finance')
    banner = md.headerSection()
    st.markdown(banner,unsafe_allow_html=True)
    
    st.markdown("""
    ###### The dataset looks some what like this 
    """)
    st.dataframe(df.read_data('primary').tail())
 
elif sidebar_main == 'EDA' : 
    st.title('Expense dashboard')
    sidebar_sub = st.sidebar.radio('Navigation', ['Expense', 'Category', 'boxplot', 'total expenses', 'treemap'])
    
    data = df.preprocess_dataframe().tail()

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
        
        col1, col2 = st.columns(2)
        with col1 : 
            daily = st.button('Daily') 

        with col2 :  
            monthly = st.button('Monthly')
        
        if monthly : 
            st.plotly_chart(df.plot_expenses('month')[0])
            # st.dataframe(df.plot_expenses('month')[2])
            percent = df.plot_expenses('month')[1]

            if percent > 0 : 
                st.write('which is ',percent,'%',' higher than prev month')
            else : 
                st.write('which is ',abs(percent),'%',' lower than prev month')

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
        col1, col2, col3 = st.columns(3)
        with col1 : 
            food = st.button('food') 

        with col2 :  
            travel = st.button('travel')
        
        with col3 :  
            wants = st.button('wants')

        if travel :
            st.plotly_chart(df.plot_boxplot('travel'))
        if wants :
            st.plotly_chart(df.plot_boxplot('wants'))
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

elif sidebar_main == 'About the Project' : 
    st.markdown(
            md.aboutpage()
        ) 

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
        st.write('I have spent on ', df.find_max('wants')[0], ' on ', df.find_max('wants')[2].date(), ' for ', df.find_max('wants')[1])

footer = md.footerSection()
st.markdown(footer,unsafe_allow_html=True) 