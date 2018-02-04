""" Split a sentence into a list.
    Replace given word with * of as many letters as original word.
    Add words from list back to string.
"""     


def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result



print(censor("this hack is a wack hack",'hack'))
