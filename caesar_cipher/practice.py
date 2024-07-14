from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(user_text,shift_num):
    enc_word = ""
    for letter in user_text:
        if letter.isalpha():
            shift_index = (alphabet.index(letter) + shift_num)%26
            enc_word+=alphabet[shift_index]
        else:
            enc_word+=letter
    return enc_word
    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

def decrypt(user_text,shift_num):
    decrypt_word = ""
    for letter in user_text:
        if letter.isalpha():
            shift_index = alphabet.index(letter)-shift_num
            if shift_index > 0:
                decrypt_index = shift_index%26
                decrypt_word += alphabet[decrypt_index]
            else: 
                decrypt_index = (shift_index+len(alphabet))%26
                decrypt_word += alphabet[decrypt_index]
        else:
            decrypt_word+=letter
    return decrypt_word

if direction == 'encode':
    enc_word = encrypt(user_text=text,shift_num=shift)
    print(enc_word)
elif direction =='decode':
    dec_word = decrypt(user_text=text,shift_num=shift)
    print(dec_word)