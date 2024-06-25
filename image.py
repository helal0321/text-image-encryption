print("\n")
from PIL import Image
import numpy as np


def multiplication_cipher(image_array, key):
  
    return (image_array * key) % 256

def encryptImage(image_array, key,path):
    encrypted_array = multiplication_cipher(image_array, key)
    encrypted_image = Image.fromarray(encrypted_array.astype(np.uint8))
    encrypted_image.save(path)
    print("\n encrypted sucessfully")

def decryptImage(image_array, key,path):
    inverse_key = pow(key, -1, 256)
    decrypted_array = multiplication_cipher(image_array, inverse_key)
    decrypted_image = Image.fromarray(decrypted_array.astype(np.uint8))
    decrypted_image.save(path)
    print("\n decrypted sucessfullyss")

image_path=input("enter path of the image you want to encrypt or ecrypt: ")

original_image = Image.open(image_path)

image_array = np.array(original_image)
keyInput=int(input("enter key: "))
if(np.gcd(keyInput, 256) == 1):
   choic=int(input("choose operation enter 1 for encrypt or 2 for decrypt: "))
   if(choic==1):
      encryptImage(image_array,keyInput,image_path)
   elif(choic==2):
      decryptImage(image_array,keyInput,image_path)    
   else:
      print("please enter valid choice") 
else:
   print("invalid key,key must be coprime with 256")      

