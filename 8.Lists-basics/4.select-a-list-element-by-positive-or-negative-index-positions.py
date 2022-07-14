from traceback import print_stack


web_browser = ["Chrome", 'Firefox', 'Safari', 'Opera', "Edge"]

print(web_browser[0])
print(web_browser[1])
print(web_browser[4])

# print(web_browser[10])

print(web_browser[2][3])

presidents = ['Washington', 'Adams', 'Jefferson']

print(presidents[-1])
print(presidents[-2])
print(presidents[-3])

favorite_movies = []

count = 5

while count > 0:
    movie = input("Enter your 5 favorite Movie: ")
    favorite_movies.append(movie)
    count -= 1

print(favorite_movies)
