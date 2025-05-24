def text_to_binary(text):
    return ' '.join(format(ord(char), '08b') for char in text)

def binary_to_text(binary):
    try:
        chars = binary.split()
        return ''.join(chr(int(b, 2)) for b in chars)
    except ValueError:
        return "Invalid binary input."

while True:
    print("\nBinary Converter Menu:")
    print("1. Convert Text to Binary")
    print("2. Convert Binary to Text")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        user_input = input("Enter text to convert to binary: ")
        print("Binary Output:", text_to_binary(user_input))

    elif choice == '2':
        user_input = input("Enter binary (space-separated 8-bit values): ")
        print("Text Output:", binary_to_text(user_input))

    elif choice == '3':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")
