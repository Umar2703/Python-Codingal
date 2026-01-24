def match_words(words):
    count =0
    list =[]
    for word in words:
        if len(word)>1 and word[0] == word[-1]:
            count=count+1
            list.append(word)
    print("list of words with first and last character same",list)
    return count
count = match_words(["ABC","ccdc","xsx","dps","sos"])
print("number of words having first and last character same is",count)