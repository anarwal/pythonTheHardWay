#practice python function imports

def break_words(stuff):
    """This is a python function and will break words for us"""
    words = stuff.split(' ')
    return words

def sort_words(words):
    """This is a python function and will sort words for us"""
    return sorted(words)

def print_first_word(words):
    """This is a python function and will print (pop out) first word for us"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """This is a python function and will print (pop out) last word for us"""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """This is a python function which takes full sentence and return sorted words"""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """This is a python function and will print first and last word of sentence for us"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one"""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

# wordlist = ['this', 'is', 'kingdom', 'of', 'narnia']
# sentence = "welcome to the jungle"
#
# print_first_word(wordlist)
# print_last_word(wordlist)
# print_first_and_last(sentence)
# print_first_and_last_sorted(sentence)