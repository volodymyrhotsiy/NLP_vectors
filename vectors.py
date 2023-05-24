import numpy as np
from scipy.spatial.distance import cosine

def distance(w1, w2):
    return cosine(w1, w2)

def closest_words(embedding):
    distances = {
        w: distance(embedding, words[w])
        for w in words
    }
    return sorted(distances, key=lambda w: distances[w])[:10]

def closest_word(embedding):
    return closest_words(embedding)[0]

with open("words.txt", encoding="utf-8") as f:
    words = dict()
    for i in range(50000):
        row = next(f).split()
        word = row[0]
        vector = np.array([float(x) for x in row[1:]])
        words[word] = vector

print(closest_word(words["king"] - words["man"] + words["woman"]))
print(closest_word(words["paris"] - words["france"] + words["england"]))
print(closest_word(words["teacher"] - words["school"] + words["hospital"]))