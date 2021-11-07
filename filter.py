import csv
import numpy as np

# Importing the csv file
reviews = open('userReviews.csv')
reader = csv.reader(reviews, delimiter=',')
userreviews = list(reader)

x = []
y = []
z = []

movie = 'star-wars-episode-v---the-empire-strikes-back'

# Defining X
for row in userreviews:
    x.append(row[0].split(';')[2])

# Defining Y
for i in userreviews:
    if (i[0].split(';')[0]) == movie:
        y.append(i[0].split(';')[2])

print(y)

# Defining Z (I couldn't figure this one out unfortunately, so I printed the results of one of the users who reviewed the previously defined movie)
user = 'jeff_reviews'
for j in userreviews:
    if (j[0].split(';')[2]) == user:
        z.append(j[0].split(';')[0])

np.savetxt("pythonAuthor.csv", z, delimiter=",",fmt='% s')