import base64

import streamlit as st
import joblib
import pandas as pd
from datetime import datetime
import time
import streamlit as st
import joblib
from idolizer import nlp_dooer
from PIL import Image

from PIL import Image

st.title(" 😇 Welcome to the IDOLIZER  😇", anchor=None)

st.subheader(":100:You come to the place where your dreams come true:100:", anchor=None)

col1, col2 = st.columns(2)

# cv_txt = st.text_area('👇Please copy-paste your cv text format👇')
cv_txt = col1.text_area('👇Please copy-paste your cv text format👇')

# st.write('The current cv is', cv_txt)

# job_post_txt = st.text_area('👇Please copy-paste your job post requirements👇')
job_post_txt = col2.text_area('👇Please copy-paste your job post requirements👇')

col_1, col_2, col_3 = st.columns(3)

if col_3.button('Predict'):

    if job_post_txt == '':
        col_3.write("Please copy-paste your cv text and your job post requirements")

    elif job_post_txt != '':

        d = {'JOB POST': [job_post_txt]}
        df_x = pd.DataFrame(data=d)
        df_x1 = nlp_dooer(df_x)
        model = joblib.load('idolizer_model.pkl')
        label = model.predict(df_x1['JOB POST'])

        if label == 0:
            col_3.write("DATA ANALYST")
            col_3.write("Recommended course:")
            col_3.write('https://www.miuul.com/data-analyst-path')
            col_3.write("%10 Indirim kodu 👇 IDOLIZER2022")

        elif label == 2:
            col_3.write("DATA SCIENTIST")
            col_3.write("Recommended course:")
            col_3.write('https://www.miuul.com/data-scientist')
            col_3.write("%10 Indirim kodu 👇 IDOLIZER2022")

        elif label == 1:
            col_3.write("DATA ENGINEER")
            col_3.write("Recommended course:")
            col_3.write('https://www.miuul.com/data-engineer-path')
            col_3.write("%10 Indirim kodu 👇 IDOLIZER2022")

if col_1.button('Explore Yourself'):

    if cv_txt == '':
        col_1.write("Please copy-paste your cv text.")

    elif cv_txt != '':

        d_ = {'JOB POST': [cv_txt]}
        df_x_ = pd.DataFrame(data=d_)
        df_x1_ = nlp_dooer(df_x_)
        model = joblib.load('idolizer_model.pkl')
        label_ = model.predict_proba(df_x1_['JOB POST'])
        label_ = pd.DataFrame(label_, columns=["DATA ANALYST", "DATA ENGINEER", "DATA SCIENTIST"]).T
        label_.rename(columns={0: "Probabilities"}, inplace=True)
        label_.sort_values("Probabilities", ascending=False, inplace=True)
        col_1.write(label_)
        col_1.write(label_.index[0])
        role = label_.index[0]
        if role == "DATA ANALYST":
            # displaying the image on streamlit app
            image1 = Image.open('atilla.jpeg')
            col_1.image(image1, caption='Bir Atilla YARDIMCI olma yolundasınız.🚀')

        elif role == "DATA SCIENTIST":
            # displaying the image on streamlit app
            image2 = Image.open('vahit.jpeg')
            col_1.image(image2, caption='Bir Vahit KESKİN olma yolundasınız.🎤 ')

        elif role == "DATA ENGINEER":
            # displaying the image on streamlit app
            image3 = Image.open('erkan.jpeg')
            col_1.image(image3, caption='👀Bir Erkan ŞİRİN olma yolundasınız.👀')

# user-name & password part

# def text_field(label, columns=None, **input_params):
#     c1, c2 = st.columns(columns or [1, 4])
#
#     # Display field name with some alignment
#     c1.markdown("##")
#     c1.markdown(label)
#
#     # Sets a default key parameter to avoid duplicate key errors
#     input_params.setdefault("key", label)
#
#     # Forward text input parameters
#     return c2.text_input("", **input_params)


# username = text_field("Username")
# password = text_field("Password", type="password")  # Notice that you can forward text_input parameters naturally

# select a date
# dt, padding = st.columns([10, 35])
# dt.date_input("")
# padding.write("")


# show current date

# image = Image.open('background_photo.jpeg')
#
# st.image(image, caption='Enter any caption here')


# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode()
#
#
# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#      <style>
#      .stApp {
#        background-image: url("data:image/png;base64,%s");
#        background-size: cover;
#      }
#      </style>
#      ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)
#
#
# set_background('photo_2.jpeg')

#
# new_title = '<p style="font-family:sans-serif; color:White; font-size: 40px;">Welcome to the IDOLIZER</p>'
# st.markdown(new_title, unsafe_allow_html=True)
#
# new_subheader = '<p style="font-family:sans-serif; color:White; font-size: 20px;">You come to the place where your dreams come true</p>'
# st.markdown(new_subheader,unsafe_allow_html=True)


