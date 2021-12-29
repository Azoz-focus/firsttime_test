import os
import time

b= True

def quiz():
    c= True
    while c==True:
        print("how are you? ")
        alhamdllilah=input()
        if alhamdllilah == "alhamdulillah":
            c=False
            time.sleep(2)
            print("you are clever!")
            time.sleep(5)
            quit()
        else:
            print("try again!")
            print("\n")
            time.sleep(2)
            os.system('cls')

while b==True:
    print("hello whats your name? ")
    sync= input()
    if sync == 'sceptic':
        b=False
        quiz()
    else:
        print("try again!")
        print("\n")
        time.sleep(2)
        os.system('cls')

