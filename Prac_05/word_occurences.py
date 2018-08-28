mywords={}
text=input("text: ")
words=text.split()
for word in words:
    number=mywords.get(word,0)
    mywords[word]=number+1
words=list(mywords.keys())
words.sort()
max_length=max(len(word) for word in words)
for word in words:
    print("{:{}} : {}".format(word, max_length, mywords[word]))