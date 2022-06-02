stri = input("Enter string")
stri2 = input("Enter string2: ")
letters=[]
for _ in stri:
    letters.append(_)
for _ in stri2:
    if _ in letters:
        letters.remove(_)
if letters==[]:
    print("Anagram")
else:
    print("Not anagram")