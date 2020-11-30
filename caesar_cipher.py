def caesar(alphabet):
    text = [words for words in input("Text: ").split()]
    shift = int(input("Shift: "))
    route = input("Route(l/r): ")

    def get_char(char, alphabet_, shift_):
        if char.isalpha():
            i = 0
            if char.isupper():
                i = 1
            if route == 'r':
                return alphabet_[i][(alphabet_[i].index(char) + shift_) % len(alphabet_[0])]
            else:
                return alphabet_[i][(alphabet_[i].index(char) - shift_) % len(alphabet_[0])]
        return char
    for words in text:
        shift = 0
        for ch in words:
            if ch.isalpha():
                shift += 1
        shifted = "".join([get_char(char, alphabet, shift) for char in words])
        print(shifted, end=' ')

def english_alphabet():
   return "".join([chr(char) for char in range(ord("a"), ord("z") + 1)])

caesar([english_alphabet(), english_alphabet().upper()])
