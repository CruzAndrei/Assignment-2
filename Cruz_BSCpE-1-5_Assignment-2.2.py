#BSCPE 1-5/ Cruz, Andrei V./ 04-07-23/ Assignment 2.2

print ("-" * 115)
print ("\n\t\tHello there and welcome to a program that uses Vigenère Cipher to Ciphertext a text!!\n\t\t\tCome and help me decrypt this texts and find out its true meaning!!\n")
print ("-" * 115)
enter_cont = input('\n\t\t\t\t\t\t"Enter to Continue"\n')
print ("-" * 115)
import colorama
from colorama import Fore
colorama.init(autoreset=True)
name = "Vigenère Cipher"
print(Fore.LIGHTGREEN_EX + name.center(115,"="))

import string
#alphabet characters uppercase and lowercase
alph_char = string.ascii_uppercase + string.ascii_lowercase
#message and key
def encrypt (text, key):
    text_alph_char = [alph_char.find(i) for i in text]
    key_alp_char= [alph_char.find(i) for i in key]
#key
    key_length = len(key)
#message
    text_length = len(text)

    cipher_text = ""
#joined together with its corresponding value (0-25)
    for n in range (text_length) :
        letter = (text_alph_char[n] + key_alp_char[n % key_length]) % len(alph_char)
        cipher_text += alph_char[letter]

    return cipher_text
#ciphertext
def decrypt(cipher, key):

    cipher_alph_char = [alph_char.find(i) for i in cipher]
    key_alph_char = [alph_char.find(i) for i in key]
#encrypted
    key_length = len(key)
#alphabet value
    cipher_length = len(cipher)

    plain_text = ""

    for n in range(cipher_length):
        letter = (cipher_alph_char[n] - key_alph_char[n % key_length]) % len(alph_char)
        plain_text += alph_char[letter]
#the encrypted or the joined values of message and key are subtracted from the alphabet value        
    return plain_text

if __name__ == "__main__":

    text = input ("Message: ")
    key = input ("Key: ")

    cipher = encrypt(text,key)
    plaintext = decrypt(cipher,key)

import time
import pyfiglet
print ("=" * 115,"\n")
print (Fore.GREEN + pyfiglet.figlet_format("Message: " + text, font = 'digital'),'\n')
time.sleep(3)
print (Fore.WHITE + pyfiglet.figlet_format("Key: " + key, font = 'digital'),'\n')
time.sleep(3)
print (Fore.BLUE + pyfiglet.figlet_format("Ciphertext: " + cipher, font = 'digital'),'\n')
time.sleep(3)
print (Fore.MAGENTA + pyfiglet.figlet_format("Message: " + plaintext, font = 'digital'),'\n')


