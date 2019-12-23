'''
                           Google Coding Interview Problem
                                  Difficulty:easy
        Given a list of words and two words word1 and word2, return the shortest
        distance between these two words in the list
'''
def check(w1,w2):
    d=n
    wl1=[]
    wl2=[]
    wr1=words.count(w1)
    wr2=words.count(w2)
    for i in range(n):
        if(words[i]==w1):
            wl1.append(i)
            
    
    for i in range(n):

        if(words[i]==w2):
            wl2.append(i)
            
    print(wl1,':',wl2)
    for i in range(wr1):
        for j in range(wr2):
            dnew=abs(wl1[i]-wl2[j])
            if(d>dnew):
                d=dnew
    return d;
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
    d=check(w1,w2)
    print("Shortest distance between them is: ",d)
    print("Do you wanna try again?(y/n)")
    ch=input()
