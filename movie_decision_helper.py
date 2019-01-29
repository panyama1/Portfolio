# Uses several parameters such as IMDB Score and Genres to compute recommendations

#import packages

%matplotlib inline
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

from wordcloud import WordCloud, STOPWORDS
import warnings
warnings.filterwarnings("ignore")

#read data file
data = pd.read_csv('../input/movie_metadata.csv')

pd.set_option('display.max_columns',None)
data.head()

data.tail(3)

data.shape

data.describe()

data.info(verbose=False)  # check what kind of data are

#Check how many values are null in each column
data[data.columns[:]].isnull().sum()

data[data['imdb_score']>7.5].shape[0]

plt.rcParams['figure.figsize']=(18,9)

data_groupby_ratings = data.groupby(['imdb_score'])['movie_title'].count()
data_groupby_ratings.plot()

data_groupby_duration = data.groupby(['duration'])['movie_title'].count()
data_groupby_duration.plot()

data[data['duration'] <= 100].shape[0]

data[data['duration'] >= 180].shape[0]

# use a visualization to detect whether there is a relationship between duration and star rating
data.boxplot(column='duration', by='imdb_score');

# visualize the relationship between content rating and duration
data.boxplot(column='duration', by='content_rating')

data['language'].unique()

sns.set(style="darkgrid")
plt.figure(figsize = (12, 6))
sns.countplot(x="language", data = data)
ax = plt.xticks(rotation=90)

sns.set(style="darkgrid")
sns.countplot(x="color", data = data)

# plot title year vs gross
data_groupby_gross = data.groupby(['title_year'])['gross'].count()
data_groupby_gross.plot()

#ploting buget vs title_year
data_groupby_gross = data.groupby(['title_year'])['budget'].count()
data_groupby_gross.plot()

data[data['language'] == 'English'].shape[0] # number of english movies

