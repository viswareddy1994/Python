from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(user_text, shift_num, dir):
        caesar_word = ""
        if dir == "decode":
            shift_num = -shift_num
        for char in user_text:
            if char.isalpha():
                shift_index = (alphabet.index(char) + shift_num)%26
                caesar_word += alphabet[shift_index]
            else:
                caesar_word += char
        return caesar_word
flag = 'yes'
while flag=='yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    # Calling Caeser Function
    caesar_word = caesar(user_text=text, shift_num=shift, dir=direction)
    print(f"Here is the {direction}d result: {caesar_word}")
    flag = input("Type 'yes' if you want to go again. Otherwise type 'no': ")
    if flag =='no':
        print("Goodbye!")

        
