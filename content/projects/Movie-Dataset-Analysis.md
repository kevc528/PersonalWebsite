# Movie Dataset Analysis
> A movie recommender and analysis using The Movies Dataset on Kaggle

---
**Source Code**

<https://github.com/kevc528/MovieDatasetAnalysis>

**Data Set**

<https://www.kaggle.com/rounakbanik/the-movies-dataset>

---

![Movies](/content/images/movies.jpg)

## About
This project was my final project for CIS545, which is a big datat analytics class I took freshman spring. For 
the project we had to analyze and model a large dataset. I decided to analyze The Movies Dataset and build a 
movie recommendation system.

I’ve always found it amazing how websites like Netflix, Spotify, and Amazon are able to provide recommendations 
to customers. Recommendation systems are widely used today and very important for so many companies, making them 
a very popular application of data science.

## Development
For my analysis, I programmed using a Jupyer Notebook. My code used various data science packages like pandas, 
pandasql, numpy, scikit-learn, matplotlib, seaborn, etc. My approach to this project was first to gather insights 
about movies and ratings by analyzing dataset. I wanted to see which features actually impacted how a movie was 
reviewed to determine what people look for in a movie.

Then after finding factors that cause people to like or dislike movies, I moved on to modeling and building the 
movie recommender. I actually built two models, taking different approaches for recommending movies. The first 
approach was a unsupervised model where someone would input a movie they liked to get back similar movies. This 
used Principal Component Analysis (PCA) to reduce dimensionality and then K Nearest Neighbors to recommend movies 
that are the "nearest neighbors". The second approach was a supervised model where someone would input a user and 
a movie title and get back "Like" or "Not Like" based on previous reviews. This used scaling, PCA, and Logistic Regression with L1 regulartization to fit a sigmoid function deciding the boundary between "Like" and 
"Not Like". 

Deeper analysis of methods and my final reflection are included in the Jupyter Notebook in the source code.