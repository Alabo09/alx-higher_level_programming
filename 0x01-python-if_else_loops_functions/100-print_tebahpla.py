#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 != 0:
        i = i - 32
    print("{}".format(chr(i)), end="")





vi 101-remove_char_at.py

#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    i = 0
    for c in str:
        if i != n:
            new += c
        i += 1
    return new
