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
    n = sorted(s.split())
    print(n)
 
else:
    print("Wrong choice")
