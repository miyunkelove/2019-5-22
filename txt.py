def collect():
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if len(word) > 20:
            print(word)

def has_no_e():
    fin = open('words.txt')
    count = 0
    number = 0
    for line in fin:
        number = number + 1
        word = line.strip()
        if 'e' in word:
            count = count + 1
        else:
            print(word)
    print((number - count) / number * 100, '%')

has_no_e()
#collect()