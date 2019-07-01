from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np

text = [
    "wookie stormtrooper",
    "wookie wookie wookie stormtrooper stormtrooper stormtrooper",
    "harry potter"
]

vect = CountVectorizer()
data = vect.fit_transform(text).todense()

print(vect.get_feature_names())
print(data)

print(pairwise_distances(data, metric='euclidean'))
print(pairwise_distances(data, metric='cosine').round(2))

print(1 - pairwise_distances(data - data.mean(axis=1), metric='cosine'))
print(np.corrcoef(data))
