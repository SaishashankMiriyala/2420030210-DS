#euclidean distance and similarity
"""import numpy as np
from scipy.spatial import distance
pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])
euclidean_dist = distance.euclidean(pointA, pointB)
print("Euclidean Distance:", euclidean_dist)
similarity_euclidean = 1 / (1 + euclidean_dist)
print("Euclidean Similarity:", similarity_euclidean)"""

#for manhattan distance
"""import numpy as np
from scipy.spatial import distance
pointA = np.array([2, 4, 6, 8])
pointB = np.array([5, 1, 9, 7])
manhattan_dist = distance.cityblock(pointA, pointB)
print("Manhattan Distance:", manhattan_dist)
similarity_manhattan = 1 / (1 + manhattan_dist)
print("Manhattan Similarity:", similarity_manhattan)"""

#Minkowski Distance with p=3
"""import numpy as np
from scipy.spatial import distance
pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])
minkowski_dist_p3 = distance.minkowski(pointA, pointB, p=3)
print("Minkowski Distance (p=3):", minkowski_dist_p3)
similarity_minkowski= 1 / (1 + minkowski_dist_p3)
print("Minkowski Similarity (p=3):", similarity_minkowski)"""

#Minkowski Distance with p=1
"""import numpy as np
from scipy.spatial import distance
pointA = np.array([2, 4, 6, 8])
pointB = np.array([5, 1, 9, 7])
minkowski_dist_p3 = distance.minkowski(pointA, pointB, p=1)
print("Minkowski Distance (p=1):", minkowski_dist_p3)
similarity_minkowski= 1 / (1 + minkowski_dist_p3)
print("Minkowski Similarity (p=1):", similarity_minkowski)"""

#All in one
"""import numpy as np
from scipy.spatial import distance
pointA = np.array([2, 4, 6])
pointB = np.array([5, 1, 9])
euclidean_dist = distance.euclidean(pointA, pointB)
print("Euclidean Distance:", euclidean_dist)
similarity_euclidean = 1 / (1 + euclidean_dist)
print("Euclidean Similarity:", similarity_euclidean)

manhattan_dist = distance.cityblock(pointA, pointB)
print("Manhattan Distance:", manhattan_dist)
similarity_manhattan = 1 / (1 + manhattan_dist)
print("Manhattan Similarity:", similarity_manhattan)

minkowski_dist_p3 = distance.minkowski(pointA, pointB, p=1)
print("Minkowski Distance (p=1):", minkowski_dist_p3)
similarity_minkowski= 1 / (1 + minkowski_dist_p3)
print("Minkowski Similarity (p=1):", similarity_minkowski)

minkowski_dist_p3 = distance.minkowski(pointA, pointB, p=3)
print("Minkowski Distance (p=3):", minkowski_dist_p3)
similarity_minkowski= 1 / (1 + minkowski_dist_p3)
print("Minkowski Similarity (p=3):", similarity_minkowski)"""

