num = 3000
for files in range(1, 10):
    with open("unicode_"+str(num*files)+".html", "w") as file:
        file.write("")
        start = 33
        print(files)
        if files != 1:
            start = num*(files-1) + 1

        line0 = "| "
        line1 = "| "
        line = "| "
        tmpCount = 0
        for index in range(start, num*files):
            if(tmpCount < 10):
                tmpCount += 1
                #if index % 1000 == 0:
                #    out += "\n---\n### "
                line0 += '&#' + str(index) + "; | " 
                line1 += "`&" + str(index) + ";` | "
                line += " --- | "
            else:
                file.write(line0 + "\n" + line + "\n" + line1)
                tmpCount = 0
                line0 = "| "
                line1 = "| "