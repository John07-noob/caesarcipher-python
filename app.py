#Author : John07-noob
#Date   : Oct 19 2020
def caeser(string, shift):
    cipher = ""
    for char in string:
        if char == " ":
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)
    return cipher

if __name__=='__main__':
    print("Welcome to CaesarCipher")
    user = input("Put text here: ")
    try:
        shift = int(input("Shift key here: "))
        print(f"Result: {caeser(user, shift)}")
    except ValueError:
        print("Sorry. Try again :)")
