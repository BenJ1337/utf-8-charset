with open("unicode.md", "w") as file:
    for index in range(33, 10000):
        out = '&#' + str(index) + "; "
        file.write(out)