
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text, shift_number):
    Encrpyted_text=''
    for letter in text:
        new_index=alphabet.index(letter) + shift_number
        new_index %= len(alphabet)
        Encrpyted_text += alphabet[new_index]
    print(f"Your Encrypted text is: {Encrpyted_text}")

# encrypt(text, shift_number)

def decrypt(text, shift_number):
    Decrypted_text=''
    for letter in text:
        new_index=alphabet.index(letter) - shift_number
        new_index %= len(alphabet)
        Decrypted_text += alphabet[new_index]
    print(f"Your Decrypted text is: {Decrypted_text}")

# decrypt(text, shift_number)

print("Welcome to ceaser cipher!")
go_or_not=True
while go_or_not:
    EorD=input("Type 'Encrypt' or 'Decrypt'").lower()
    text=input("Enter the text: ").strip().lower()
    shift_number=int(input("how many letters do you want to shift? "))

    if EorD== 'encrypt':
        encrypt(text, shift_number)
    elif EorD=='decrypt':
        decrypt(text, shift_number)
    else:
        print("choose a right function")

    vari=input("Do you want to continue ciphering? Type 'yes' or 'no'").lower()
    if vari=='yes':
        print("\n" * 20)
        go_or_not=True
    else:
        go_or_not=False

