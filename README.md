# Directory and Subdomain Scanner

## Overview

The **Directory and Subdomain Scanner** is a versatile Python tool designed to facilitate the discovery of subdomains and directories within a given target domain. By leveraging custom or predefined wordlists, this tool enables more focused and efficient scanning. It features a user-friendly menu interface for easy interaction and provides detailed results.

## Features

- **Subdomain Scanning**: Identify subdomains of a specified target domain using either predefined or custom wordlists.
- **Directory Scanning**: Explore directories within discovered subdomains to find hidden resources.
- **Custom Wordlists**: Use your own wordlists for scanning subdomains and directories by specifying file paths.

## Getting Started

### Prerequisites

- Python 3.x
- `requests` library

### Installation

1. **Clone the Repository**

   Begin by cloning the repository to your local machine:

   ```bash
   git clone https://github.com/AbdullahZeynel/Subdomain-Directory-Scanner_Python.git
   cd Subdomain-Directory-Scanner_Python
   ```

2. **Set Up a Virtual Environment (Optional but Recommended)**

   Create and activate a virtual environment to manage dependencies:

   ```bash
   python -m venv myEnv
   source myEnv/bin/activate  # On Windows use `myEnv\Scripts\activate`
   ```

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Prepare Your Wordlists**

   The tool uses two primary wordlists:
   - `subdomains10000.txt`: A list of potential subdomains.
   - `common.txt`: A list of common directories.

   You can use these default wordlists or provide your own by placing them in the same directory as the script or specifying their full paths.

2. **Run the Scanner**

   Execute the script using:

   ```bash
   python subdomain_directory_scanner.py
   ```

3. **Interact with the Menu**

   The script displays a menu with the following options:

   - **1**: Scan a target domain for subdomains and directories.
   - **2**: Customize wordlists (provide paths to your own subdomain and directory wordlists).
   - **3**: Exit the tool.

   Follow the prompts to perform your desired actions.

### Example

Here’s a brief example of using the tool:

1. Choose option **1** from the main menu to start scanning a domain.
2. Enter a target domain, such as `example.com`.
3. The tool will first scan for subdomains using the `subdomains10000.txt` list.
4. Discovered subdomains will then be checked for directories using the `common.txt` list.
5. Results are saved in `founded_subs.txt` (subdomains) and `found_urls.txt` (directories).

### Customization

- **Changing Wordlists**: Choose option **2** from the main menu to provide paths to your custom subdomain and directory wordlists. Ensure the file paths are valid and end with `.txt`.
- **File Path Validity**: The tool verifies that provided paths exist and are text files.

### Contributing

Contributions are welcome! If you have suggestions or improvements, please fork the repository and submit a pull request with your changes.

## Acknowledgements

- The `requests` library for handling HTTP requests.
- GitHub for hosting the repository.
- The creators of the wordlists:
  - [subdomains10000.txt](https://github.com/rbsec/dnscan/blob/master/subdomains-10000.txt)
  - [common.txt](https://github.com/v0re/dirb/blob/master/wordlists/common.txt)
