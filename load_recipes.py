import json

from LDA_text_model import LDAtext
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

from text_utils import striphtml, remove_words

with open('recipes.json', 'r') as fp:
    recipes = json.load(fp)

recipes = recipes['recipes']

summary = [
    striphtml(recipes[k]['summary']).replace('spoonacular', '')
    for k in range(len(recipes))
]

summary = remove_words(['score', 'recipe', 'take', 'things', 'serving'],
                       summary)

# LDA
a = LDAtext()

a.train(summary, number_of_topics=2, number_of_passes=30, number_of_workers=4)

print(a.topics())

# KMeans clustering with TF-IDF weights
tfidf_vectorizer = TfidfVectorizer()
tfidf = tfidf_vectorizer.fit_transform(summary)
kmeans = KMeans(n_clusters=2)
kmeans.fit(tfidf)
