alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encryption(word, shift_key):
   encrypted_word = " "
   for i in word:
      if i in alphabet:
         position = alphabet.index(i)
         new_position = (position + shift_key) % 26
         encrypted_word += alphabet[new_position]
      else:
         encrypted_word = encrypted_word+i
   print(f"The text after encryption is : {encrypted_word}")

def decryption(word, shift_key):
   decrypted_word = " "
   for i in word:
      if i in alphabet:
         position = alphabet.index(i)
         new_position = (position - shift_key) % 26
         decrypted_word += alphabet[new_position]
      else:
         decrypted_word = decrypted_word+i
   print(f"The text after decryption is : {decrypted_word}")     
end_game = False
while not end_game:
   what_type = input("Type 'encrypt' for encryption 'decrypt' for decryption : ")
   word = input("Enter the word : ").lower()
   shift_key = int(input("Enter the shift key : "))
   if what_type == "encrypt":
      encryption(word,shift_key)
   elif what_type == "decrypt":
        decryption(word,shift_key)
   end = input("Enter 'yes' if you want to continue or enter 'no' to stop : " )
   if end == "yes":
      end_game = False
   else:
      end_game = True
      print("Exiting......")