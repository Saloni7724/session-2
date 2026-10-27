# Task 3

ratings = [5, 4, 4, 3, 5, 4, 2, 4]

mode = max(set(ratings), key=ratings.count)

print("Ratings:", ratings)
print("Most common rating:", mode)