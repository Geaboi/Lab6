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
        #Determines the special cases by using a dictionary and adding it
        if i == '7' or i == '8' or i == '9':
            special = {
                '7': '0', '8': '1', '9': '2'
            }
            encoded += special[i]

        else:
            # Converts i to integer and adds 3 to it
            encoded += str(int(i) + 3)
    return encoded

def decode(password):
    password_list = []
    decoded_list = []
    for i in password:
        password_list.append(int(i))
    for i in range(0, len(password_list)):
        if 3 <= password_list[i]:
            decoded_list.append(str(password_list[i] - 3))
        elif 0 <= password_list[i] <= 2:
            decode_var = (password_list[i] - 3) + 10
            decoded_list.append(str(decode_var))
    decode_string = ''.join(decoded_list)
    return decode_string

def main():
    encoded_password = 0
    run = True
    while run:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        #Checks the users options and runs it through if statements
        user_option = int(input("Please enter an option: "))
        if user_option == 1:
            #Asks the user for input and sends it to the encoder function
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)

            print("Your password has been encoded and stored!")
        elif user_option ==2:
            print(f"The encoded password is {encoded_password}, and the original password is {decode(encoded_password)}.")
        elif user_option == 3:
            run = False

if __name__ == "__main__":
    main()