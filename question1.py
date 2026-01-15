
def countLetters(anyText: str, anyLetter: str) -> int:

    counter = 0
    for i in anyText:
        if i == anyLetter:
            counter += 1
    return counter
print (countLetters("hello, 1"))
       
