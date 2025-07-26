print('Caesar Cipher / Decryption Program')

while True:
    print('\n1. Encrypt')
    print('2. Decrypt')
    print('3. Exit')

    choice = input('Enter your choice: (1-2-3) ')

    if choice == '1':
        text = input('Enter the text to encrypt: ')
        shift = int(input('Enter the shift amount: '))

        encrypted_text = ""

        for char in text:
            if char.isalpha():
                shifted = shift % 26
                base = ord('a') if char.islower() else ord('A')
                encrypted_char = chr((ord(char) - base + shifted) % 26 + base)
                encrypted_text += encrypted_char
            else:
                encrypted_text += char

        print(f"Encrypted text: {encrypted_text}")

    elif choice == '2':
        text = input('Enter the text to decrypt: ')
        shift = int(input('Enter the shift amount: '))

        decrypted_text = ""

        for char in text:
            if char.isalpha():
                shifted = -shift % 26
                base = ord('a') if char.islower() else ord('A')
                decrypted_char = chr((ord(char) - base + shifted) % 26 + base)
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        print(f"Decrypted text: {decrypted_text}")

    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid input, please enter 1, 2, or 3.")
        break
