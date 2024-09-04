import requests
import os

main_menu = """
==========================================
      Directory and Subdomain Scanner
==========================================

Please choose an option:

1. Enter a target domain to scan.
2. Use custom wordlists (provide file paths).
3. Exit.

Note: You can use your own wordlists for both 
subdomain and directory scanning by providing 
the file paths.

==========================================
"""

customization_menu = """
==========================================
       Wordlist Customization Menu
==========================================

Please choose an option:

1. Change subdomain wordlist.
2. Change directories wordlist.
3. Back to main menu.

Note: Provide the full file path for your 
custom wordlists.

==========================================
"""
global wordlist
wordlist = 'subdomains10000.txt'
global directoryList
directoryList = 'common.txt'
#____________________________________________________________________________

def clearScreen():
    # Check if the system is Windows or Linux/macOS and clear the screen accordingly
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For Linux/macOS
        os.system('clear')
#____________________________________________________________________________

def check_path_validity(file_path):
    # Check if the provided path exists and ends with .txt
    if os.path.exists(file_path) and file_path.endswith('.txt'):
        return True
    else:
        return False
#____________________________________________________________________________

def scan_subdomains(target_domain):
    foundSubdomains = []

    with open(wordlist,'r') as file1:
        for subdomain in file1:
            subdomain = subdomain.strip()
            url = f"http://{subdomain}.{target_domain}"

            try:
                requests.get(url)

            except requests.exceptions.RequestException:
                print("pass")
                pass

            else:
                print(f"[+] Found: {url}")
                foundSubdomains.append(url)

        print('\n\nSubdomain scan completed.')

        with open('founded_subs.txt','w') as file2:
            for subdomain in foundSubdomains:
                file2.write(subdomain)
                file2.write('\n')

    return foundSubdomains
#____________________________________________________________________________

def scan_directories():
    found_urls = []

    with open('founded_subs.txt', 'r') as foundURL:
        for subdomain_url in foundURL:
            subdomain_url = subdomain_url.strip()  
            
            with open(directoryList, 'r') as directories:
                for directory in directories:
                    directory = directory.strip()  
                    url = f"{subdomain_url}/{directory}"

                    try:
                        response = requests.get(url)
                        if response.ok:  # Checks if status_code is between 200 and 399
                            print(f"[+] Found directory: {url}")
                            found_urls.append(url)
                    except requests.exceptions.RequestException as e:
                        print("pass")
                        pass
                
            print(f"\n{subdomain_url} directory scan completed.")

    with open('found_urls.txt', 'w') as file2:
        for url in found_urls:
            file2.write(f"{url}\n")

    print('\nFound URLs:')
    print(found_urls)
#____________________________________________________________________________

def main():
    clearScreen()
    print(main_menu)
    userInput = input("\n\nYour Choice:").strip()

    if userInput == '1':
        clearScreen()
        target_domain = input("Please enter your target domain:")
        print('\n\n')
        FoundAddresses = scan_subdomains(target_domain)
        print('\n\nFound Addresses:')

        for address in FoundAddresses:
            print(address)

        input("\nPlease press ENTER to continue with directory scanning.")

        FoundUrl = scan_directories()
        print('\n\nFound Urls:')

        for url in FoundUrl:
            print(url)

    elif userInput == '2':
        while True:
            clearScreen()
            print(customization_menu)
            userInput2 = input("\n\nYour Choice:")

            if userInput2 in ['1', '2']:
                clearScreen()
                targetPath = 'Subdomain' if userInput2 == '1' else 'Directory'
                file_path = input(f'Please enter the full path to your {targetPath} .txt file:').strip()
                
                if check_path_validity(file_path):
                    if userInput2 == '1':
                        wordlist = file_path
                    else:
                        directoryList = file_path
                    print("The path is valid. Proceeding...")
                    input('Please press ENTER.')
                else:
                    print("Error: The path is invalid or the file is not a .txt. Please try again.")
                    input('Please press ENTER.')
                    continue
            else:
                if userInput2 != '3':
                    input('Invalid input. Please press ENTER to return to Main Menu.')
                main()
    elif userInput == '3':
        exit()
    else:
        input('Invalid input. Please press ENTER to return to Main Menu.')
        main()
#____________________________________________________________________________

if __name__ == "__main__":
    main()
