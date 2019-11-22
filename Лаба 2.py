from collections import Counter
s= input("Enter your text:")
choice= input('Enter your choice(1,2):')
if choice== "1" :
    d={}
    for i in s :
         if i.isalpha():
             d[i] = d.get(i,0)+1

    for i in sorted(d):
        print(i,"=",d[i])
elif choice=="2":
    word_list = []
    for word in s.split():
        clear_word = ""
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()
        word_list.append(clear_word)

    print("Words:",Counter(word_list))
else:
    print("Wrong choice")