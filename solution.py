'''

                           Google Coding Interview Problem
                                  Difficulty:easy
        Given a list of words and two words word1 and word2, return the shortest
        distance between these two words in the list

'''
ch='y'
while(ch=='y'):
    words=[]
    print("How may items you want to add?")
    n=int(input())
    for i in range(n):
        print("Enter word ",i+1," :")
        w=input()
        words.append(w)
    print(words)
    print("Enter two words to know Shortest distance between them:")
    while True:
        print("Enter First Word:")
        w1=input()
        if(w1 in words):
            break
        print("Word not in list!")
        continue
    while True:
        print("Enter Second Word:")
        w2=input()
        if(w2 in words):
            break
        print("Word not in list!")
        continue
    i1=words.index(w1)+1
    i2=words.index(w2)+1
    d=abs(i1-i2)
    print("Shortest distance between them is: ",d)
    print("Do you wanna try again?(y/n)")
    ch=input()
