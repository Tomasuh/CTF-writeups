f = open("markovhaystack.txt","r")

#Easy doable by finding unique words
unique = []

content = []

for line in f.readlines():
    words = line.split(" ")
    for word in words:
        word = word.rstrip()
        #If word not found numerous times before
        if word not in content:

            #if also not in unique
            if word not in unique:
                unique.append(word)

            #it is in unique but is not uniqe
            else:
                unique.remove(word)
                content.append(word)

print unique
#By grabbing an unique word (in this case "Solution" was one) and locating it in the document the flag was found.