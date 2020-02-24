words=[]
count=int(input('How many: '))
five_count=0
for i in range(count):
    word=input('Enter your word: ')
    words.append(word)
    if len(word)==5:
        five_count+=1

print(words)
print(five_count,'have 5 alphabets.')