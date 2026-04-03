class flashcard:
    def __init__(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __dtr__(self):
        return self.word +"("+ self.meaning+ ")"
flash = []
print("welcome to fashcard application")
while(True):
    word=input("enter the name you want to add to flashcard:")
    meaning=input("enter the meaning of the word:")
    flash.append(flashcard(word,meaning))
    option=int(input("enter 0, if u want another flashcard enter 1:"))
    if option:
        break
print("Your flashcards:")
for i in flash:
    print(">",i) 