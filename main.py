with open("unicode.md", "w") as file:
    for index in range(33, 1000000):
        out = '&#' + str(index) + "; = &#38;" + str(index)
        file.write(out)