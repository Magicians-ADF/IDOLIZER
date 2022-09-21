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

job_post_txt = col2.text_area('👇Please copy-paste your job post requirements👇')

col_1, col_2, col_3 = st.columns(3)

st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #0099ff;
    color:#ffffff;
}

</style>""", unsafe_allow_html=True)

if col_1.button('Explore Yourself, Who are you really actually?'):

    if cv_txt == "":
        col_1.write("Please copy-paste your cv text.")

    elif cv_txt != "":

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

if col_2.button('Which skills do you need to get this job?  👀'):

    if (cv_txt == "") and (job_post_txt == ""):
        col_2.write("Please copy-paste your cv text and job post")

    elif (cv_txt != "") and (job_post_txt == ""):
        col_2.write("Please copy-paste your job post")

    elif (cv_txt == "") and (job_post_txt != ""):
        col_2.write("Please copy-paste your cv text ")

    elif (cv_txt != "") and (job_post_txt != ""):

        d = {'JOB POST': [job_post_txt]}
        df_x = pd.DataFrame(data=d)
        df_x1 = nlp_dooer(df_x)

        d_ = {'JOB POST': [cv_txt]}
        df_x_ = pd.DataFrame(data=d_)
        df_x1_ = nlp_dooer(df_x_)

        model = joblib.load('idolizer_model.pkl')
        label = model.predict(df_x1['JOB POST'])

        if label == 0:
            col_2.write("ROLE: DATA ANALYST")
            DATA_ANALYST_SKILL_SET = ["dashboard", "data models", "build models", "deploy models", "modeling",
                                      "communication", "statistical methods", "statistics", "Periscope", "Tableau",
                                      "Looker", "Snowflake", "SQL", "reporting", "Tracking KPI’s", "forecast",
                                      "Power Bl", "technical design", "Excel", "SAP", "decision-making",
                                      "analytical thinking",
                                      "problem solving", "Google sheets", "MySQL", "R", "python", "SQL", "Sql",
                                      "Python" "analyzing", "visualizing", "large data sets", "statistical methods",
                                      "analytics", "Microsoft Word",
                                      "Power Point", "VBA", "DAX", "Qlik", "Power Query", "machine learning",
                                      "web analytics", "Data Studio",
                                      "Access and analyse data from our data warehouse using SQL",
                                      "relational databases",
                                      "non-relational databases", "bridge between technical and non-technical",
                                      "Qualtrics", "Alchemer", "Survey Monkey", "data-driven decision making",
                                      "Extract",
                                      "manipulate and visualize data to find and understand patterns",
                                      "strategic decisions with experimentation and in-depth analyses",
                                      "Develop data models", "Quicksight", "data extraction and analysis",
                                      "Google Firebase", "A/B testing", "metric design", "linear regression",
                                      "logistic regression", "exploratory data analyses", "test hypotheses",
                                      "ad-hoc queries", "building predictive models", "AWS", "dbt", "Redshift",
                                      "BigQuery", "Fullstory", "Adobe Analytics", "Python programming",
                                      "libs (Numpy, Pandas, Matplotlib, Seaborn, scipy)",
                                      "NoSQL", "NoSQL Database Technologies ( Cassandra, HBase, MongoDB )", "DataOps",
                                      "Interpreting", "Analyzing and Deriving Insights from Data",
                                      "Statistical Procedures and Analysis",
                                      "Data Visualizations (Matplotlib, Seaborn)", "Data Science Project Lifecycles",
                                      "problem-solving",
                                      "Oracle", "MATLAB", "data mining", "segmentation", "market share analysis",
                                      "Defining success metrics", "Oracle BI", "MS Office", "Amazon Web Services",
                                      "SQL procedures", "LTV", "CAC", "campaign uplift", "churn", "retention",
                                      "acquisition", "user behaviour funnels", "data preparation",
                                      "define metrics/KPIs",
                                      "customer lifetime valu", "CLTV", "A/B or multivariate testing",
                                      "Next Best Action", "Reporting automation", "analyze/develop datamart",
                                      "data discovery",
                                      "statistical data analysis", "Airflow", "AWS Glue", "AWS",
                                      "GCP" "Python automation scripting", "Databricks", "Build the data assets",
                                      "Google analytics",
                                      "Heap", "HTML", "APIs", "SAS", "Teradata", "Hadoop", "GCP",
                                      "Google Cloud Platform", "RDBMS", "AWS", "Amazon Web Services", "Azure"]

            DATA_ANALYST_SKILL_SET = [x.lower() for x in DATA_ANALYST_SKILL_SET]

            job_skill_set = []
            for skill in DATA_ANALYST_SKILL_SET:
                if skill in df_x1["JOB POST"][0]:
                    job_skill_set.append(skill.title())
            cv_skill_set = []
            for skill in DATA_ANALYST_SKILL_SET:
                if skill in df_x1_["JOB POST"][0]:
                    cv_skill_set.append(skill.title())

            gain_skills = list(set(job_skill_set) - set(cv_skill_set))

            col_2.write(f"Empower yourself follow skills to get this job:👇")
            for i in gain_skills:
                col_2.write(f"- {i}")

        elif label == 2:
            col_2.write("ROLE: DATA SCIENTIST")
            DATA_SCIENCE_SKILL_SET = ["SQL", "Python", "PostgreSQL", "Redshift", "Python",
                                      "Programming skills in object-oriented programming languages",
                                      "Java", "R", "CI/CD", "Github", "Jenkins", "Experience in database management",
                                      "building and running resilient", "microservices", "Spring",
                                      "AWS", "GCP", "Azure", "Kubernetes", "GIT", "Scala", "C++", "Java", "NoSQL",
                                      "Hadoop", "Hive", "Spark", "BigQuery", "Microsoft Azure",
                                      "Docker", "MLOps", "DEVOPS", "dev-ops", "ML-ops", "Scrum/Kanban boards",
                                      "structured and unstructured data in cloud ecosystems", "MLaaS",
                                      "large-scale production environments on AWS/ GCP",
                                      "software development engineering skills", "Deep knowledge of ML lifecycle",
                                      "statistical methodologies", "A/B testing",
                                      "practical usage of ML libraries and scientific stack", "scikit", "matplotlib",
                                      "pandas", "xgboost",
                                      "CI/CD tools like Jenkins", "Apache Airflow", "Airflow", "mlflow", "sagemaker",
                                      "sagemaker", "vertex-ai", "Azure Data Factory",
                                      "MLlib", "scikit-learn", "Azure ML", "CI/CD", "DevOps", "microservices", "CD4ML",
                                      "DVC", "CML", "Bento", "SageMaker", "MLFlow", "Comet",
                                      "DataRobot", "KubeFlow", "Elixir", "Go", "Bash", "Engineer",
                                      "system design/architecture", "software development cycle", "CI/CD", "TDD",
                                      "monitoring/logging", "cloud engineering", "use and deploy cloud services",
                                      "deploy machine learning workflows", "TensorFlow", "PyTorch",
                                      "HTK", "Kaldi", "Julius", "Sphinx", "Git", "signal processing", "time series",
                                      "Attention-based models", "RNNs and CNNs",
                                      "Natural language processing models", "NLP", "model deployment pipelines",
                                      "Machine Learning models", "Machine Learning infrastructure",
                                      "Keras", "Unix", "Nomad", "GCP", "Google Cloud Platform", "RDBMS", "AWS",
                                      "Amazon Web Services", "Azure"]

            DATA_SCIENCE_SKILL_SET = [x.lower() for x in DATA_SCIENCE_SKILL_SET]
            job_skill_set = []
            for skill in DATA_SCIENCE_SKILL_SET:
                if skill in df_x1["JOB POST"][0]:
                    job_skill_set.append(skill.title())
            cv_skill_set = []
            for skill in DATA_SCIENCE_SKILL_SET:
                if skill in df_x1_["JOB POST"][0]:
                    cv_skill_set.append(skill.title())

            gain_skills = list(set(job_skill_set) - set(cv_skill_set))

            col_2.write(f"Empower yourself follow skills to get this job:👇")
            for i in gain_skills:
                col_2.write(f"- {i}")

        elif label == 1:
            col_2.write("ROLE: DATA ENGINEER")
            DATA_ENGINEER_SKILL_SET = ["SQL", "Spark", "Hadoop", "Hive", "Presto", "Python", "Java", "C ++", "Scala",
                                       "Shell" "Script"
                                       "ETL", "ELT", "GCP", "Google Cloud Platform", "RDBMS", "AWS",
                                       "Amazon Web Services", "Azure", "PostgreSQL", "API engineering",
                                       "SQLAlchemy", "AWS Lambda", "AWS Redshift", "NoSQL", "Kafka", "Elasticsearch",
                                       "Snowflake", "Athena",
                                       "MySQL", "Linux", "Unix", "Apache Beam", "Apache Flink", "Cassandra", "Impala",
                                       "Experience with microservices", "REST APIs", "Git",
                                       "GitLab", "Oracle", "Elasticsearch", "MongoDB", "Airflow", "Azkaban", "Luigi",
                                       "CI/CD", "Docker", "Kubernetes", "Spring Boot", "Agile"]

            DATA_ENGINEER_SKILL_SET = [x.lower() for x in DATA_ENGINEER_SKILL_SET]
            job_skill_set = []
            for skill in DATA_ENGINEER_SKILL_SET:
                if skill in df_x1["JOB POST"][0]:
                    print(skill)
                    job_skill_set.append(skill.title())
            cv_skill_set = []
            for skill in DATA_ENGINEER_SKILL_SET:
                if skill in df_x1_["JOB POST"][0]:
                    cv_skill_set.append(skill.title())

            gain_skills = list(set(job_skill_set) - set(cv_skill_set))

            col_2.write(f"Empower yourself follow skills:👇")
            for i in gain_skills:
                col_2.write(f"- {i}")

if col_3.button('Course Recommendation to get this job'):

    if job_post_txt == "":
        col_3.write("Please copy-paste your cv text and your job post requirements")

    elif job_post_txt != "":

        d = {'JOB POST': [job_post_txt]}
        df_x = pd.DataFrame(data=d)
        df_x1 = nlp_dooer(df_x)
        model = joblib.load('idolizer_model.pkl')
        label = model.predict(df_x1['JOB POST'])

        if label == 0:
            col_3.write("ROLE: DATA ANALYST")
            col_3.write("Recommended course:")
            col_3.write('https://www.miuul.com/data-analyst-path')
            col_3.write("%10 Indirim kodu 👇 IDOLIZER2022")

        elif label == 2:
            col_3.write("ROLE: DATA SCIENTIST")
            col_3.write("Recommended course:")
            col_3.write('https://www.miuul.com/data-scientist')
            col_3.write("%10 Indirim kodu 👇 IDOLIZER2022")

        elif label == 1:
            col_3.write("ROLE: DATA ENGINEER")
            col_3.write("Recommended course:")
            col_3.write('https://www.miuul.com/data-engineer-path')
            col_3.write("%10 Indirim kodu 👇 IDOLIZER2022")

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
#     page_bg_img = ""'
#      <style>
#      .stApp {
#        background-image: url("data:image/png;base64,%s");
#        background-size: cover;
#      }
#      </style>
#      ""' % bin_str
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
