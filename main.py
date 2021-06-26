for files in range(1, 10):
    with open("unicode_"+str(files)+".md", "w") as file:
        for index in range(33, 1000*files):
            out = '&#' + str(index) + "; = &#38;"
            file.write(out)