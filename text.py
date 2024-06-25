print("\n")
import numpy as np
alphabets="abcdefghijklmnopqrstuvwxyz"
def encrypt_text(plainText,key):
            
                cipherText=''
                for i in plainText :
                    if(i.isalpha()):
                        cipherCharacterIndex=(alphabets.index(i)*key)%26
                        cipherText+=alphabets[cipherCharacterIndex]
                    else:
                            cipherText+=i    
                return cipherText
                  
def decrypt_text(cipherText,key):
        
            keyInverse = pow(key, -1, 26)
            plainText=''
            for i in cipherText :
                    if(i.isalpha()):
                        plainTextCharacterIndex=(alphabets.index(i)*keyInverse)%26
                        plainText+=alphabets[plainTextCharacterIndex]
                    else:
                            plainText+=i    
            return plainText

def process_file(file_path, key, mode):

        with open(file_path, 'r') as file:
            text = file.read()
            loweredText=text.lower()
            processed_text = encrypt_text(loweredText, key) if mode == 'encrypt' else decrypt_text(loweredText, key)
        
        with open(file_path, 'w') as file:
            file.write(processed_text)
        print(f"file {mode}ed sucessfully")

choic=input("please enter your choic, encrypt or decrypt the text: ")
if(choic=="encrypt"):
        file_path=input("please enter the file path to encrypt: ")
        key=int(input("please enter the key: "))
        if(np.gcd(key,26)==1):
            process_file(file_path,key,choic)
        else:
                print("enter a valid key")    
elif(choic=="decrypt"):
        file_path=input("please enter the file path to decrypt: ")
        key=int(input("please enter the key: "))
        if(np.gcd(key,26)==1):
            process_file(file_path,key,choic)
        else:
               print("enter a valid key")    
else:
        print("please enter a valid choic")                