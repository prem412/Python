movies = [ "Bahubali", "Inception", "Interstellar", "The Dark Knight" ]
# print(movies[0])
# print(movies[1])
# print(movies[2])
# print(movies[3])
# print(movies[-1])
# print(movies[-2])
# print(movies[-3])
# print(movies[-4])


#Add item
movies.append("Doraemon teen kaabil talwaarbaz")

#Remove item
movies.remove("The Dark Knight")

#change item
movies[0] = "Bahubali 2"

for movie in movies:
    print(movie)



print(len(movies))


movies.insert(2, "Avengers: Endgame")
print(movies)


movies.sort()
print(movies)

movies.reverse()
print(movies)

movies.reverse()
print(movies)







rgb = ("red", "green", "blue")
print(rgb[0])

for color in rgb:
    print(color)