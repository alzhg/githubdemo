def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(user_inp):
    encoded_str = ''
    for element in user_inp:
        encoded_str += str((int(element) + 3) % 10)
    return encoded_str

user_input = ''

def main():
    while True:
        global user_input
        menu()
        print()
        option = int(input('Please enter an option: '))
        if option == 3:
            break
        elif option == 1:
            user_input = input('Please enter your password to encode: ')
            print('Your password has been encoded and stored!')
            print()
        elif option == 2:
            pwd = encode(user_input)
            print(f'The encoded password is {pwd}, and the original password is {user_input}.')
            print()

if __name__ == "__main__":
    main()