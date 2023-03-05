from PIL import Image
from streamlit_option_menu import option_menu
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components

#Setting the Page Configuration
#img = Image.open('./images/favicon.png')
#st.set_page_config(page_title='News Recommender Engine' , page_icon=img , layout="centered",initial_sidebar_state="expanded")

#Designing the footer and MainMenu creating the skeleton of the website.
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: visible;}
            footer:after{
                background-color:#a873b0;
                font-size:12px;
                font-weight:5px;
                height:30px;
                margin:1rem;
                padding:0.8rem;
                content:'Copyright © 2022 : Hamna Qaseem 👩‍💻';
                display: flex;
                align-items:center;
                justify-content:center;
                color:white;
            }
            header {visibility: hidden;}
            </style>
            """

st.markdown(hide_st_style, unsafe_allow_html=True)

st.markdown(hide_st_style, unsafe_allow_html=True)

#Loading the animation of the streamlit lottie
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# URLS of all the lottie animation used
lottie_coding = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_bb9bkg1h.json")
lottie_contact =load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_dhcsd5b5.json")
lottie_loadLine =load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_yyjaansa.json")
lottie_github =load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_S6vWEd.json")

#Sidebar Designing And Functioning
with st.sidebar:
    selected = option_menu(
                menu_title="NEWS ARTICLE Recommender",  # required
                options=["Home", "About Me", "💻 About Website"],  # required
                icons=["house", "person-square", "website"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
                 styles={
                "container": {"padding": "5!important", "background-color": "#0E1117" , "Font-family":"Monospace"},
                "icon": {"color": "#A0CFD3", "font-size": "25px"},
                "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px","Font-family":"Monospace"},
                "nav-link-selected": {"background-color": "#90EE90"},
                }
                )
    # Adding Functionality to the sidebar on the basis of option being selected from the main menu.
    if selected == "Home":
        st.empty()


                  
    # Adding Functionality to the sidebar on the basis of option being selected from the main menu.
    if selected == "Home":
        st.empty()

    # The About And Portfolio Section.
    if selected == "About Me":
        st.markdown("""
        <div style='
            background-color:#a873b0; 
            padding:1rem;
            font-size:17px;
            border-radius:8px;
            text-align: justify;
           '>
            I am a fresher currently doing my Bachelor's in Data Science.I have keen interest in website designing and developing.I am from from Pakistan.In addition, I have deep interest and aptitude in telling stories with data.
        </div>
        <br>
       """
                    , unsafe_allow_html=True, )

