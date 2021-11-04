from string import printable


def Caesar(text: str, shift: int = 1, key: str = printable):
    new = ""
    text_length = len(text)

    for _ in range(text_length):
        char = text[_]
        location = key.find(char)
        new_location = (location + shift) % 100
        new += key[new_location]
        
    return new


encrypted = Caesar("Hello", 3)
print(encrypted)
