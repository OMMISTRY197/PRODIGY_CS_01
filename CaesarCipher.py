def caesar_encrypt(text, step):
    result = []
    for char in text:
        if char.isupper():
            result.append(chr((ord(char) - ord('A') + step) % 26 + ord('A')))
        elif char.islower():
            result.append(chr((ord(char) - ord('a') + step) % 26 + ord('a')))
        else:
            result.append(char)
    return ''.join(result)

def caesar_decrypt(text, step):
    return caesar_encrypt(text, -step)

def main():
    while True:
        action = input("Do you want to encrypt or decrypt the text? (e/d): ").strip().lower()
        
        if action not in ('e', 'd'):
            print("Invalid option. Please choose 'e' for encrypt or 'd' for decrypt.")
            continue
        
        text = input("Enter Text: ")
        step = int(input("Enter Steps: "))
        
        if action == 'e':
            result = caesar_encrypt(text, step)
            print("Encrypted Text:", result)
        else:
            result = caesar_decrypt(text, step)
            print("Decrypted Text:", result)
        
        continue_choice = input("Do you want to continue? (y/n): ").strip().lower()
        if continue_choice != 'y':
            print("Exiting the Program")
            break

if __name__ == "__main__":
    main()