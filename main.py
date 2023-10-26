"""
Name: Dustin Nguyen % Yegor
Class: COP3502c
Section:22282
Description: A simple encoder and decorder program using git hub to collaborate with my partner
"""
def encode(password):
    #Creates an empty string to store the encoded password
    encoded = ""
    for i in password:
        #Adds 3 to each of the elements
        if i == '7' or i == '8' or i == '9':
            special = {
                '7': '0', '8': '1', '9': '2'
            }
            encoded += special[i]

        else:
            encoded += str(int(i) + 3)
    return encoded
def decode(password):
    return decoded
def main():
    encoded_password = 0
    run = True
    while run:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)

            print("Your password has been encoded and stored!")
        elif user_option ==2:
            password = int(input("Please enter your password to encode: "))
            decode(encoded_password)
        elif user_option == 3:
            run = False

if __name__ == "__main__":
    main()