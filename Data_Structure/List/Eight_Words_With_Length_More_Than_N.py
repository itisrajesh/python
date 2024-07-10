def get_words_longer_than_n(words, n):
    """
    Description: list of words that are longer than n from a given list of words.
    Input: {words: list , n: integer}
    Output: {list : list}
    """
    return [word for word in words if len(word) > n]

if __name__ == "__main__":
    words = ['Python', 'Java', 'C++', 'C#', 'Ruby', 'JavaScript', 'PHP', 'HTML', 'CSS', 'SQL']
    print(get_words_longer_than_n(words, 4))