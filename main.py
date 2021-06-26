for files in range(1, 10):
    with open("unicode_"+str(files)+".md", "w") as file:
        start = 33
        if files != 1:
            start = 10000*files + 1
        for index in range(33, 10000*files):
            out = '&#' + str(index) + "; = &#38;" + str(index)
            file.write(out)