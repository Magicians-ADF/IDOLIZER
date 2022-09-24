import pandas as pd
import numpy as np
import seaborn as sns

# Stop Words
import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords

# TOKENIZER
import textblob
from textblob import TextBlob
nltk.download("punkt")

# lemmatization
from textblob import Word
nltk.download("wordnet")
nltk.download("omw-1.4")

import joblib

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.base import TransformerMixin
from sklearn import metrics
from sklearn.decomposition import TruncatedSVD
from sklearn import ensemble, metrics, model_selection, naive_bayes
from sklearn.pipeline import make_pipeline
import warnings

warnings.filterwarnings("ignore")

# Read data
df = pd.read_excel("job_post_data.xlsx")
df.reset_index(inplace=True, drop=True)


def nlp_dooer(dataframe):
    # dropped numbers
    dataframe["JOB POST"] = dataframe["JOB POST"].str.replace("\d", " ")

    # dropped punctuations
    dataframe["JOB POST"] = dataframe["JOB POST"].str.replace("[^\w\s]", " ")

    dataframe["JOB POST"] = dataframe["JOB POST"].str.replace("\n\n", " ").str.replace("\n", " ")

    # convert to lower case
    dataframe["JOB POST"] = dataframe["JOB POST"].apply(lambda x: " ".join(x.lower() for x in x.split()))

    # dropped stop-words
    sw = stopwords.words("english")
    dataframe["JOB POST"] = dataframe["JOB POST"].apply(lambda x: " ".join(x for x in x.split() if x not in sw))

    # TOKENIZER
    dataframe["JOB POST"] = dataframe["JOB POST"].apply(lambda x: TextBlob(x).words)

    # lemmatization
    dataframe["JOB POST"] = dataframe["JOB POST"].apply(lambda x: " ".join(Word(i).lemmatize() for i in x))

    return dataframe


df = nlp_dooer(df)

encoder = LabelEncoder()
encoder.fit(df['ROL'])
train_y = encoder.transform(df['ROL'])

# 'DATA ANALYST'    --> 0
# 'DATA SCIENTIST'  --> 2
# 'DATA ENGINEER'   --> 1

#
train_tfidf = df['JOB POST'].values.tolist()

# Create a pipeline
model = make_pipeline(TfidfVectorizer(), MultinomialNB(alpha=1))

# Fit the model with training set
model.fit(train_tfidf, train_y)

joblib.dump(model, 'idolizer_model.pkl')


