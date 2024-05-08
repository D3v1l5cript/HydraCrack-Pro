![Screenshot from 2023-12-20 17-29-11](https://github.com/Demonic-cyber/HydraCrack-Pro/assets/92028299/61ae4e63-7c20-4364-9be4-eb2ddd23b2e4)

# HydraCrack-Pro

This tool is a Python-based HydraCrack-Pro using Hydra with additional features like wordlist generation, customizable attacks, and more.

## Features

### 1. Generate Wordlist
- **Description**: Generates wordlists based on the victim's name and keywords.
- **Functionality**:
  - Allows the user to specify the victim's name and keywords.
  - Generates variations of wordlists using combinations of the victim's name and keywords.

### 2. Perform Hydra Attack
- **Description**: Integrates Hydra into the program to perform brute-force attacks.
- **Functionality**:
  - Prompts the user for necessary information such as the target, protocol, usernames, and passwords.
  - Constructs and executes Hydra commands with the provided parameters.

### 3. Crack Wi-Fi Handshake File
- **Description**: Utilizes tools like Aircrack-ng to crack Wi-Fi handshake files.
- **Functionality**:
  - Prompts the user for the path to the handshake file and, optionally, a wordlist.
  - Executes Aircrack-ng with the provided parameters to attempt to crack the Wi-Fi password.

### 4. Crack Hash Using Hashcat
- **Description**: Integrates Hashcat into the program to crack hashes.
- **Functionality**:
  - Prompts the user for the hash type, path to the hash file, and path to the wordlist (if applicable).
  - Constructs and executes Hashcat commands with the provided parameters.

## Usage

1. Clone this repository.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the script: `python HydraCrack-Pro.py`.
4. Follow the on-screen instructions to utilize the tool.

## Requirements

- Python 3.6 or higher
- colorama==0.4.4 (Check `requirements.txt` for more dependencies)

## Commands
`git clone https://github.com/demonic-cyber/HydraCrack-Pro`
`pip install -r requirements.txt`
`python HydraCrack-Pro.py`

## Note
- this tool in under development
- soon new update

## License

This project is licensed under the [MIT License](LICENSE).

# Happy Hacking😈
