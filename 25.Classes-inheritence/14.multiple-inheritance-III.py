class FilmMaker():
    def give_interview(self):
        print('I love making movies')


class Director(FilmMaker):
    pass


class Screenwriter(FilmMaker):
    def give_interview(self):
        print('I love writing scripts!')


class JackOfAllTrades(Director, Screenwriter):
    pass


stallone = JackOfAllTrades()
stallone.give_interview()

print(JackOfAllTrades.mro())
