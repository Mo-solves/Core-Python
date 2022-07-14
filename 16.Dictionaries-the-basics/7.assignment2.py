# Define a to_dictionary function that accepts a list of strings
# The function should return a dictionary where the keys are the strings
# and the values are their original index positions in the list


detectives = ['Sherlock Holmes', 'Hercule Poirot', 'Nancy Drew']


def to_dictionary(lists):
    new_dic = {}
    for idx, list in enumerate(lists):
        new_dic[list] = idx
    return new_dic


print(to_dictionary(detectives))

# Define a length_counts function that accepts a list of strings
# The function should return a dictionary where the keys represent
# length and values represent how may string have that length
sa_countries = ['Brazil', 'Venezuela',
                'Argentina', 'Ecuador', 'Bolivia', 'Peru']


def length_counts(lists):
    counts = {}

    for list in lists:
        length = len(list)
        current_count = counts.get(length, 0)
        counts[length] = current_count + 1
    return counts


print(length_counts(sa_countries))
