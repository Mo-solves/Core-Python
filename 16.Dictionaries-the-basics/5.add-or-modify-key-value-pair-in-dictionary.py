from ctypes.wintypes import WORD


sports_team_rosters = {
    'New England Patriots': ['Tom Brady', 'Rob Gronkowski', 'Julian'],
    'New York Giants': ['Eli Manning', 'Odell Beckam']
}

# print(sports_team_rosters['Pittsburgh Steelers'])
sports_team_rosters['Pittsburgh Steelers'] = [
    'Ben Roethlisberger', 'Antonio Brown']

# print(sports_team_rosters['Pittsburgh Steelers'])
# print(sports_team_rosters)

sports_team_rosters['New York Giants'] = ['Eli Manning']

# Create an empty dictionary
video_game_options = {}
video_game_options = dict()

video_game_options['subtitles'] = True
video_game_options['difficult'] = 'Medium'
video_game_options['volume'] = 7
print(video_game_options)

video_game_options['difficult'] = 'Hard'
video_game_options['subtitles'] = False
video_game_options['Volume'] = 10
print(video_game_options)


# Dynamic references
words = ['danger', 'beware', 'danger']


def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


print(count_words(words))
