# Instructions for Setting Up the Vinted Bot

## Prerequisites
1. **Python**: Make sure you have Python installed on your machine.
2. **Dependencies**: The script requires some Python libraries such as `webbrowser`, `time`, `os`, and `json`. These are generally available by default with Python.

## Setup Steps

1. **Clone the Repository**:
   - Use the following command to clone the repository:
     ```bash
     git clone https://github.com/ClementG91/Bot-Vinted.git
     ```

2. **Prepare the `urls.json` File**:
   - Create a file named `urls.json` in the project folder and insert the URLs you want to open. The format should be:
     ```json
     {
       "urls": [ "link1", "link2", "link3", "link4", "link5", "link6" ]
     }
     ```
   - Ensure this file is in the same directory as the `main.py` script.

3. **Configure the Browser**:
   - The script will open URLs in your default browser. Make sure this browser is properly installed and configured on your machine.

4. **Modify Browser Closure**:
   - To close the browser at the end of the script execution, modify the line in the code that says:
     ```python
     os.system("taskkill /im brave.exe /f")
     ```
   - Replace `brave.exe` with the executable name of your browser (for example, `chrome.exe` for Google Chrome, `firefox.exe` for Mozilla Firefox, etc.).

5. **Run the Script**:
   - Open a terminal and navigate to the project folder.
   - Execute the script with the command:
     ```bash
     python main.py
     ```

## How the Script Works
- The script opens a new tab for each URL listed in `urls.json`.
- If a URL fails to open, an error message will be displayed.
- After execution, the browser process will be closed using the `taskkill` command for better memory management.

## Disclaimer
Please note that the use of this script may be against the terms of service of Vinted. Its use is at your own risk.
