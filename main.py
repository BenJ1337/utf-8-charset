num = 20000
end = 10
for files in range(1, end+1):
    with open("unicode_"+str(num*files)+".md", "w") as file:
        file.write("")
        start = 33
        #print(files)
        if files != 1:
            start = num*(files-1) + 1

        line0 = "| "
        line1 = "| "
        line = "| "
        tmpCount = 1
        table = False
        for index in range(start, num*files+1):
            #print("line: " + str(index))
            if(tmpCount <= 10):
                tmpCount += 1
                line0 += '&#' + str(index) + "; | " 
                line1 += "`&" + str(index) + ";` | "
                if not table :
                    line += " :---: | "
            else:
                file.write(line0 + "\n")
                if not table :
                    table = True
                    file.write(line + "\n")
                file.write(line1 + "\n")
                    
                tmpCount = 2
                line0 = '| &#' + str(index) + "; | " 
                line1 = "| `&" + str(index) + ";` | "
        file.write(line0 + "\n" + line1 + "\n")