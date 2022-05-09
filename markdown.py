def aboutpage() : 
    text = """
            ### About This Project

            Since when I moved to Bangalore I've been monitoring my expenses. Every night I used to fill the data in an Excel sheet. And this is my personal finance dashboard where I have plotted various charts representing my spendings...

            ----------------------------

            #### Approach : 

            * So Initially I have used an .ipynb file to do the preprocessing and do some visualization

            * Then I have made another file finance.py to implement all the functions related to preprocessing and plotting

            * I have imported the same file in app.py and used it along with streamlit to build the app.

            ------------------------------

            #### How to run? 

            > To run the app you need to download this repository along with the required libraries and it the command line you have to write streamlit run app.py to run. 

            > it might ask for your email once...

            ------------------------------- 

            #### Further work : 

            * I have tried connecting this app with a google sheet thus it gets updated automatically but it actually became slow by that. So I removed that feature 
            * The data is very small so its not sufficient for predictions, Maybe I'll do it later. 
            * I keep on adding small features like new Q&A and spending hikes...

            -------------------------------
            #### Technologies used : 

            * python library - numpy, pandas, seaborn, matplotlib, streamlit
            * version control - git 
            * backend - streamlit
            * concept - OOP

            #### Tools and Services : 
            * IDE - Vs code 
            * Application Deployment - Heroku
            * Code Repository - GitHub

            You can find the repository [here](https://github.com/soumyadipghorai/personal-finance) 

            -----------------------
            ###### If you Liked this project the you can consider connecting with me on [LinkedIn](https://www.linkedin.com/in/soumyadip-ghorai/) 

            """

    return text

def footerSection() : 
    text = """
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
                    background-color: transparent;
                    color: black;
                    text-align: center;
                }
            </style>
            <div class="footer">
                <p>Developed with ❤️ by <a style= text-align: center;'><b>Soumyadip Ghorai</b></a></p>
                <p><a href = 'https://github.com/soumyadipghorai/personal-finance' target = '_blank'>github</a></p>
            </div>
        """
    return text 
def headerSection() : 
    text = """
            <style>
                .responsive {
                    max-width: 100%;
                    height: auto;
                }
            </style>
            <div class="banner-image">
                <img src="https://www.trioticz.com/wp-content/uploads/2021/10/3012b5fa53a077ca0b26f5ceb39ab633-1.gif" alt="banner image"  class="responsive">
            </div>
        """
    return text 