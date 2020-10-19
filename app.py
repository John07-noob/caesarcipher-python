#Author : John07-noob
#Date   : Oct 19 2020
abc = ['a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',    #1
        'a','b','c','d','e','f','g','h','i','j',
            'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',]   #2

def caesar(user, shift):
    try:
        for i in user:
            for lists in abc:
                char = i
                shift = shift
                if char == lists: #abc
                    found_char = abc.index(char)
                    result = abc[found_char+shift]
                    print(result)
    except IndexError:
        print("Sorry. Try again :)")

print("Welcome to CaesarCipher")
user = input("Put text here: ")
try:
    shift = int(input("Shift key here: "))
    caesar(user, shift)
except ValueError:
    print("Sorry. Try again :)")