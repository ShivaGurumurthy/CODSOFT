import random
import string

def generate_password(length=8):
    if length <= 4:
        raise ValueError("The entered password does not match the criteria... Please enter a new one...")
    
    print('''Choose from the following list of options to generate your password:
          1.) Letters
          2.) Numbers
          3.) Special Symbols
          4.) Exit Python Password Generator...''')
    
    characterList = ""
    
    while True:
        choice = int(input("Pick a number: "))
        if choice == 1:
            characterList += string.ascii_letters
        elif choice == 2:
            characterList += string.digits
        elif choice == 3:
            characterList += string.punctuation
        elif choice == 4:
            break
        else:
            print("You've entered an invalid option... Please try again...")
    

    if not characterList:
        print("No character sets selected. Exiting.")
        return

    password = []
    
    for i in range(length):
        randomchar = random.choice(characterList)
        password.append(randomchar)
    
    
    print("Your password is: " + ''.join(password))


try:
    password_length = int(input("Enter the password length: "))
    generate_password(password_length)
except ValueError as ve:
    print(ve)
