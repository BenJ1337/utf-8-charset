for files in range(1, 10):
    with open("unicode_"+str(10000*files)+".md", "w") as file:
        file.write("## ")
        start = 33
        print(files)
        if files != 1:
            start = 10000*(files-1) + 1
        for index in range(start, 10000*files):
            out = ""
            if index % 1000:
                out += "\n---\n"
            out += '&#' + str(index) + "; `&#38;" + str(index) + ";`  "
            file.write(out)