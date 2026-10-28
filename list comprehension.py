mylist=[2,5,3,8]
print("first list:",mylist)
newlist=[number**2 for number in mylist]
print("new list:",newlist)
#vowel
word = input("Enter a word: ")
vowels = ['a', 'e', 'i', 'o', 'u']
lis = []

for x in word:
    if x in vowels and x not in lis:
        lis.append(x)

print("Vowels present in the given word:", lis)

