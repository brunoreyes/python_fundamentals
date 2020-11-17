import timeit


text = "what have the romans ever done for us"

def comp_capitals():
    capitals = [char.upper() for char in text]
    print (capitals)

    # Using map
def map_capitals():
    map_capitals = list(map(str.upper, text))
    print(map_capitals)

def comp_words():
    words = [word.upper() for word in text.split(' ')]
    print(words)

    # Using map
def map_words():
    map_words = list(map(str.upper, text.split(' ')))
    print(map_capitals)


if __name__ == '__main__':
    print(comp_capitals())
    print(map_capitals())
    print(comp_words())
    print(map_words())

    print(timeit.timeit(comp_capitals, number=10000))
    print(timeit.timeit(map_capitals, number=10000))
    print(timeit.timeit(comp_words, number=10000))
    print(timeit.timeit(map_words, number=10000))