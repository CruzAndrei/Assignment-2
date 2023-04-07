#BSCPE 1-5/ Cruz, Andrei V./ 04-07-23/ Assignment 2.1
print ("=" * 115)
print ("\n\t\tHello there and welcome! This is a program to decode specific symbols into a character.\n\t\t\t\t\tCome and help me decrypt this texts\n")
print ("=" * 115)
import colorama
from colorama import Fore
colorama.init(autoreset=True)
enter_cont = input('\n\t\t\t\t\t  "Enter to Continue"\n')
print ("=" * 115)

print(Fore.BLUE + "Symbol *".ljust(105,"-") + "Vowel a")
print(Fore.MAGENTA + "Symbol &".ljust(105,"-") + "Vowel e")
print(Fore.BLUE + "Symbol #".ljust(105,"-") + "Vowel i")
print(Fore.MAGENTA + "Symbol +".ljust(105,"-") + "Vowel o")
print(Fore.BLUE + "Symbol !".ljust(105,"-") + "Vowel u")
print ("=" * 115)

#ask user to input their data
import pyfiglet

input_str = input("\nType in your data here: ")
output_str = ""
#inspect each character
for i in range(len(input_str)):
#subtitute symbols into vowels;
#symbol * is for a
    if input_str[i] == "*":
        output_str += "a"
#symbol & is for e
    elif input_str[i] == "&":
        output_str += "e"
#symbol # is for i
    elif input_str[i] == "#":
        output_str += "i"
#symbol + is for o
    elif input_str[i] == "+":
        output_str += "o"
#symbol ! is for u
    elif input_str[i] == "!":
        output_str += "u"        
    else:
        output_str += input_str[i]

print(pyfiglet.figlet_format(output_str, font = "bubble" ))
