def favorite_movies():
    movies = []
    print('Enter your Five favorite Movies')
    for movie in range(1, 6):
        favorite = input(f'{movie}: ')
        movies.append(favorite)
    return movies


def print_favorite(movies):
    print('Your favorite movies are: ')
    for idx, movie in enumerate(movies):
        print(f'{idx + 1}: {movie}')

def choose():
    movies = []
    flag = True
    while flag != False:
        print("Option 1: Enter your favorite movies: ")
        print("Option 2: print your movies")
        print('Option 3: Exit')
        option = input()
        if option == '1':
           movies = favorite_movies()
        elif option == '2':
            if len(movies) == 0:
                print('Your list is empty')
            else:
                print_favorite(movies)
        elif option == '3':
            flag = False
            break


choose()
