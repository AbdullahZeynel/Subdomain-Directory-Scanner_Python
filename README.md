# Directory and Subdomain Scanner

## Overview

The **Directory and Subdomain Scanner** is a Python-based tool designed to scan for subdomains and directories of a given target domain. It allows users to use custom wordlists for more targeted scanning and provides an easy-to-use menu interface for interaction.

## Features

- **Subdomain Scanning**: Detect subdomains of a given target domain using predefined or custom wordlists.
- **Directory Scanning**: Check for directories within the discovered subdomains.
- **Custom Wordlists**: Allows users to specify their own wordlists for scanning.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/AbdullahZeynel/Subdomain-Directory-Scanner_Python.git
   cd Subdomain-Directory-Scanner_Python
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   Create and activate a virtual environment:

   ```bash
   python -m venv myEnv
   source myEnv/bin/activate  # On Windows use `myEnv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

   You can create the `requirements.txt` file with the following content:

   ```txt
   requests
   ```

### Usage

1. **Prepare Your Wordlists**

   - **Subdomain Wordlist**: [subdomains-10000.txt](https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt)
   - **Directory Wordlist**: [common.txt](https://github.com/v0re/dirb/blob/master/wordlists/common.txt)

   Download these wordlists or use your own custom files and place them in the same directory as the script or specify the path when using custom wordlists.

2. **Run the Scanner**

   Execute the script:

   ```bash
   python Godfry.SubdomainScanner.py
   ```

3. **Interact with the Menu**

   The script will display a menu with the following options:

   - **1**: Enter a target domain to scan for subdomains and directories.
   - **2**: Use custom wordlists (provide file paths for subdomains and directories).
   - **3**: Exit the tool.

   Follow the prompts to perform scans.

### Example

Here’s a brief example of how to use the tool:

1. Choose option **1** from the main menu to scan a target domain.
2. Enter a domain name, e.g., `example.com`.
3. The script will scan for subdomains using `subdomains-10000.txt` and then check for directories using `common.txt`.
4. Results will be saved in `founded_subs.txt` and `found_urls.txt`.

### Customization

- **Change Wordlists**: Choose option **2** from the main menu to provide paths to your custom subdomain and directory wordlists.
- **File Path Validity**: Ensure that provided file paths are valid and end with `.txt`.

### Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The `requests` library for handling HTTP requests.
- GitHub for hosting the repository.
- The authors of the wordlists:
  - [subdomains-10000.txt](https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt)
  - [common.txt](https://github.com/v0re/dirb/blob/master/wordlists/common.txt)
