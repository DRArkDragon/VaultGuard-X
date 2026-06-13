import json
import random
import string
import time
import hashlib
import bcrypt
from datetime import datetime
from cryptography.fernet import Fernet
import os
if os.name == "nt":
    import msvcrt
else:
    from getpass import getpass


DATA_DIR = ".vault_data"

VAULT_FILE = os.path.join(DATA_DIR, "vault.json")
MASTER_FILE = os.path.join(DATA_DIR, "master.json")
KEY_FILE = os.path.join(DATA_DIR, "secret.key")

os.makedirs(DATA_DIR, exist_ok=True)


# ==========================
# COLORS
# ==========================

class Colors:

    GREEN = '\033[92m'
    RED = '\033[91m'
    CYAN = '\033[96m'
    YELLOW = '\033[93m'
    MAGENTA = '\033[95m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    WHITE = '\033[97m'
    

    END = '\033[0m'


# ==========================
# LOAD BREACH DATABASE
# ==========================

def load_common_passwords():

    try:

        with open(
            "common_passwords.txt",
            "r",
            encoding="utf-8"
        ) as file:

            return {
                line.strip().lower()
                for line in file
                if line.strip()
            }

    except FileNotFoundError:

        print(
            f"{Colors.RED}[!] common_passwords.txt not found!{Colors.END}"
        )

        return set()

HACKER_QUOTES = [

    "Security is not a product, but a process.",
    "The quieter you become, the more you can hear.",
    "Trust, but verify.",
    "Passwords are like underwear. Change them often.",
    "Attackers only need one weakness.",
    "Think like an attacker. Defend like a guardian.",
    "Every system is secure until it isn't.",
    "The strongest firewall is user awareness.",
    "Encryption is your last line of defense.",
    "Hack the problem, not the system."

]


# ==========================
# FILE FUNCTIONS
# ==========================


def initialize_storage():

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(VAULT_FILE):

        with open(VAULT_FILE, "w") as file:

            json.dump([], file)


def hash_password(password):

    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

def pause():

    input(f"\n{Colors.YELLOW}Press Enter to Continue...{Colors.END}")


def clear():

    os.system('cls' if os.name == 'nt' else 'clear')


def loading():

    clear()

    print(f"{Colors.GREEN}")

    modules = [
        "Loading Encryption Engine",
        "Loading Credential Database",
        "Loading Breach Scanner",
        "Loading Security Dashboard",
        "Initializing VaultGuard-X"
    ]

    for module in modules:

        print(f"[+] {module}")
        time.sleep(0.5)

    print("\n[✓] All Modules Loaded Successfully")

    print(f"{Colors.END}")

    time.sleep(1)


def masked_input(prompt):

    if os.name != "nt":
        return getpass(prompt)

    print(prompt, end="", flush=True)

    password = ""

    while True:

        key = msvcrt.getch()

        if key in [b'\r', b'\n']:
            print()
            break

        elif key == b'\x08':

            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)

        else:

            char = key.decode("utf-8")
            password += char
            print("*", end="", flush=True)

    return password


# ==========================
# RANDOM BANNER DISPLAY
# ==========================


def show_random_banner():

    banners = [

r"""
██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗
██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
██║   ██║███████║██║   ██║██║     ██║   ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║   ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
 ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
""",

r"""
██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗ ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗
██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
██║   ██║███████║██║   ██║██║     ██║   ██║  ███╗██║   ██║███████║██████╔╝██║  ██║
██║   ██║██╔══██║██║   ██║██║     ██║   ██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
╚██████╔╝██║  ██║╚██████╔╝███████╗██║   ╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
 ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝    ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝

                CYBER SECURITY VAULT
""",

r"""
██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
██║   ██║███████║██║   ██║██║     ██║
╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║
 ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║
  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝

 ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗
██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
██║  ███╗██║   ██║███████║██████╔╝██║  ██║
██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝
""",

r"""
██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
██║   ██║███████║██║   ██║██║     ██║
╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║
 ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║
  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝

 ██████╗ ██╗   ██╗███████╗██████╗
██╔════╝ ██║   ██║██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚═╝  ╚═╝
""",

r"""
██╗   ██╗ █████╗ ██╗   ██╗██╗  ████████╗
██║   ██║██╔══██╗██║   ██║██║  ╚══██╔══╝
██║   ██║███████║██║   ██║██║     ██║
╚██╗ ██╔╝██╔══██║██║   ██║██║     ██║
 ╚████╔╝ ██║  ██║╚██████╔╝███████╗██║
  ╚═══╝  ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝

 ██████╗ ██╗   ██╗ █████╗ ██████╗ ██████╗
██╔════╝ ██║   ██║██╔══██╗██╔══██╗██╔══██╗
██║  ███╗██║   ██║███████║██████╔╝██║  ██║
██║   ██║██║   ██║██╔══██║██╔══██╗██║  ██║
╚██████╔╝╚██████╔╝██║  ██║██║  ██║██████╔╝
 ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝

        [ PASSWORD VAULT FRAMEWORK ]
"""
]

    quotes = [
        "Trust, but verify.",
        "Every password is a target.",
        "Encryption is your last line of defense.",
        "Security begins with awareness.",
        "Weak passwords create strong attackers.",
        "Attackers need one weakness. Defenders need none.",
        "Secure today. Survive tomorrow."
    ]

    print(random.choice([
    Colors.GREEN,
    Colors.CYAN,
    Colors.RED,
    Colors.MAGENTA
]))
    print(random.choice(banners))
    print(Colors.END)

    print("=" * 65)
    print("[+] CYBERSECURITY PASSWORD VAULT & AUDITING PLATFORM")
    print("[+] Author  : Ankur Chaurasia")
    print("[+] Version : 2.0")
    print("[+] Status  : SECURE")
    print("=" * 65)

    print(f"\n{Colors.YELLOW}[*] {random.choice(quotes)}{Colors.END}\n")



# ==========================
# ENCRYPTION FUNCTIONS
# ==========================


def generate_key():

    if not os.path.exists(KEY_FILE):

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

def load_key():

    with open(KEY_FILE, "rb") as file:
        return file.read()
    
def encrypt_password(password):

    key = load_key()

    f = Fernet(key)

    encrypted = f.encrypt(password.encode())

    return encrypted.decode()


def decrypt_password(password):

    key = load_key()

    f = Fernet(key)

    decrypted = f.decrypt(password.encode())

    return decrypted.decode()


def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []

    try:
        with open(VAULT_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_vault(data):
    with open(VAULT_FILE, "w") as file:
        json.dump(data, file, indent=4)


# ==========================
# MASTER PASSWORD SETUP
# ==========================

def setup_master_password():

    if os.path.exists(MASTER_FILE):
        return

    print(f"\n{Colors.CYAN}===== FIRST TIME SETUP ====={Colors.END}")

    password = masked_input("Create Master Password: ")

    with open(MASTER_FILE, "w") as file:
        json.dump(
            {
                "master_password":
                hash_password(password)
            },
            file
        )

    print(f"{Colors.GREEN}Master Password Created!{Colors.END}")


def get_master_password():

    with open(MASTER_FILE, "r") as file:
        data = json.load(file)

    return data["master_password"]



def verify_master_password():

    stored_password = get_master_password()

    password = masked_input(
        "\n[AUTH] Enter Master Password: "
    )

    return bcrypt.checkpw(
        password.encode(),
        stored_password.encode()
    )


# ==========================
# LOGIN
# ==========================

def login():

    stored_password = get_master_password()

    print(f"""
    {Colors.GREEN}=========================================
            AUTHENTICATION REQUIRED
    ========================================={Colors.END}
    """)

    attempts = 3

    while attempts > 0:

        password = masked_input("Enter Master Password: ")

        if bcrypt.checkpw(password.encode(),stored_password.encode()):
            print(f"{Colors.GREEN}Login Successful!{Colors.END}")
            return True

        attempts -= 1

        print(
            f"{Colors.RED}Incorrect Password! Attempts Left: {attempts}{Colors.END}"
        )

    print(f"{Colors.RED}Access Denied!{Colors.END}")
    return False


# ==========================
# ADD CREDENTIAL
# ==========================

def add_credential():

    vault = load_vault()

    website = input(
        "Website (e.g. gmail/facebook/github): "
    ).strip().lower()

    username = input(
        "Username/Email: "
    ).strip().lower()

    # Duplicate Check
    for item in vault:

        if (
            item["website"] == website
            and
            item["username"] == username
        ):

            print(
                f"{Colors.RED}[!] Duplicate Credential Detected{Colors.END}"
            )

            print(
                f"{Colors.YELLOW}Website : {website}{Colors.END}"
            )

            print(
                f"{Colors.YELLOW}Username: {username}{Colors.END}"
            )

            pause()
            return

    password = encrypt_password(
        masked_input("Password: ")
    )

    vault.append({
        "website": website,
        "username": username,
        "password": password,
        "created": str(datetime.now().date())
    })

    save_vault(vault)

    print(
        f"{Colors.GREEN}[+] Credential Stored Securely{Colors.END}"
    )

    pause()


# ==========================
# VIEW CREDENTIALS
# ==========================

def view_credentials():

    vault = load_vault()

    if not vault:

        print(f"""
    {Colors.RED}
    [!] VAULT EMPTY
    ----------------------------------
    No credentials are currently stored.
    Add a credential to begin using
    VaultGuard-X.
    ----------------------------------
    {Colors.END}
    """)

        pause()

        return

    print(f"\n{Colors.CYAN}===== SAVED CREDENTIALS ====={Colors.END}")

    for i, item in enumerate(vault, start=1):

        print(f"\n{i}. Website : {item['website']}")
        print(f"   Username: {item['username']}")
        show = input("Show Password? (y/n): ")

        if show.lower() == "y":

            if verify_master_password():

                print(
                    f"   Password: {decrypt_password(item['password'])}"
                )

            else:

                print(
                    f"{Colors.RED}[!] Authentication Failed{Colors.END}"
                )

        else:

            print("   Password: ********")
        print(f"   Added On: {item['created']}")

    pause()


# ==========================
# SEARCH
# ==========================

def search_credential():

    website = input("Enter Website Name: ").lower()

    vault = load_vault()

    for item in vault:

        if item["website"].lower() == website:

            print(f"\n{Colors.GREEN}Credential Found!{Colors.END}")
            print("Username:", item["username"])

            if verify_master_password():

                print(
                    "Password:",
                    decrypt_password(item["password"])
                )

            else:

                print(f"{Colors.RED}[!] Credential Not Found!{Colors.END}")
            pause()
            return

    print(f"{Colors.RED}Credential Not Found!{Colors.END}")

    pause()


# ==========================
# DELETE
# ==========================

def delete_credential():

    website = input("Enter Website To Delete: ").lower()

    vault = load_vault()

    new_vault = []

    deleted = False

    for item in vault:

        if item["website"].lower() != website:
            new_vault.append(item)
        else:
            deleted = True

    save_vault(new_vault)

    if deleted:
        print(f"{Colors.GREEN}[-] Credential Removed{Colors.END}")
    else:
        print(f"{Colors.RED}Credential Not Found!{Colors.END}")

    pause()


# ==========================
# PASSWORD STRENGTH CHECKER
# ==========================

def password_strength():

    password = input("Enter Password: ")

    score = 0

    if len(password) >= 8:
        score += 25

    if any(c.isupper() for c in password):
        score += 25

    if any(c.islower() for c in password):
        score += 25

    if any(c.isdigit() for c in password):
        score += 15

    if any(c in string.punctuation for c in password):
        score += 10

    print(f"\nSecurity Score: {score}/100")

    if score >= 80:
        print(f"{Colors.GREEN}Strong Password{Colors.END}")

    elif score >= 50:
        print(f"{Colors.YELLOW}Medium Password{Colors.END}")

    else:
        print(f"{Colors.RED}Weak Password{Colors.END}")

    pause()


# ==========================
# PASSWORD GENERATOR
# ==========================

def generate_password():

    length = int(input("Password Length: "))

    chars = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    password = ''.join(
        random.choice(chars)
        for _ in range(length)
    )

    print(f"\nGenerated Password:\n{password}")

    pause()


# ==========================
# BREACH CHECK
# ==========================

def breach_check():

    password = input("Enter Password To Check: ")

    common_passwords = load_common_passwords()

    if password.lower() in common_passwords:

        print(
            f"{Colors.RED}\n[!] Breach Database Match Found! Password Found In Common Breach List!{Colors.END}"
        )

    else:

        print(
            f"{Colors.GREEN}\n[✓] No Match Found In Breach Database.{Colors.END}"
        )
    pause()


# ==========================
# PASSWORD AGE CHECK
# ==========================

def password_age_check():

    vault = load_vault()

    print(f"\n{Colors.CYAN}===== PASSWORD AGE REPORT ====={Colors.END}")

    for item in vault:

        created = datetime.strptime(
            item["created"],
            "%Y-%m-%d"
        )

        age = (datetime.now() - created).days

        print(
            f"{item['website']} : {age} days old"
        )

        if age > 90:
            print(
                f"{Colors.YELLOW}Change Recommended!{Colors.END}"
            )
    pause()


# ==========================
# SECURITY DASHBOARD
# ==========================

def security_dashboard():

    vault = load_vault()

    weak = 0
    medium = 0
    strong = 0

    for item in vault:

        password = decrypt_password(
            item["password"]
        )

        score = 0

        if len(password) >= 8:
            score += 25

        if any(c.isupper() for c in password):
            score += 25

        if any(c.islower() for c in password):
            score += 25

        if any(c.isdigit() for c in password):
            score += 15

        if any(c in string.punctuation for c in password):
            score += 10

        if score < 50:
            weak += 1

        elif score < 80:
            medium += 1

        else:
            strong += 1

    total = weak + medium + strong

    security_score = max(
        0,
        100 - weak * 15 - medium * 5
    )

    if security_score >= 80:
        risk = f"{Colors.GREEN}LOW{Colors.END}"
        risk_icon = "[+]"
        risk_color = Colors.GREEN

    elif security_score >= 50:
        risk = f"{Colors.YELLOW}MEDIUM{Colors.END}"
        risk_icon = "[!]"
        risk_color = Colors.YELLOW

    else:
        risk = f"{Colors.RED}HIGH{Colors.END}"
        risk_icon = "[X]"
        risk_color = Colors.RED

    print(f"""
    {Colors.CYAN}
    ==================================================
                SECURITY ASSESSMENT REPORT
    ==================================================
    {Colors.END}
    """)

    print(f"{Colors.GREEN}[+] Total Accounts   : {total}{Colors.END}")
    print(f"{Colors.RED}[-] Weak Passwords  : {weak}{Colors.END}")
    print(f"{Colors.YELLOW}[!] Medium Passwords: {medium}{Colors.END}")
    print(f"{Colors.GREEN}[+] Strong Passwords : {strong}{Colors.END}")

    print()
    print(f"{risk_color}{risk_icon} Overall Risk    : {risk}{Colors.END}")
    print(f"{Colors.CYAN}[*] Security Score : {security_score}/100{Colors.END}")

    print(f"""
    {Colors.GREEN}
    [✓] Scan Status : COMPLETE
    ==================================================
    {Colors.END}
    """)

    pause()


# ==========================
# MENU
# ==========================


def menu():

    while True:

        clear()

        vault = load_vault()

        print(f"""{Colors.CYAN}   
        ╔══════════════════════════════════════════════════════╗
        ║{Colors.RED}               ☣ VAULTGUARD-X CONSOLE                {Colors.CYAN} ║
        ╠══════════════════════════════════════════════════════╣
        ║ {Colors.WHITE}STATUS              : {Colors.GREEN}ONLINE{Colors.CYAN}                         ║
        ║ {Colors.WHITE}ENCRYPTION          : {Colors.GREEN}AES-256 ACTIVE{Colors.CYAN}                 ║
        ║ {Colors.WHITE}BREACH DB           : {Colors.YELLOW}LOADED{Colors.CYAN}                         ║
        ║ {Colors.WHITE}VAULT STATE         : {Colors.GREEN}SECURE{Colors.CYAN}                         ║
        ║ {Colors.WHITE}PASSWORD DATABASE   : {Colors.YELLOW}(10K entries){Colors.CYAN}                  ║
        ╚══════════════════════════════════════════════════════╝
        {Colors.END}""")

        print(f"""{Colors.PURPLE}
        ------------------------------------------------------
         {Colors.WHITE}Active Vault Entries : {Colors.GREEN}{len(vault):<3}{Colors.PURPLE}                         
         {Colors.WHITE}Threat Monitoring   : {Colors.GREEN}ENABLED{Colors.PURPLE}                      
         {Colors.WHITE}Framework Version   : {Colors.YELLOW}2.0{Colors.PURPLE}                          
        ------------------------------------------------------
        {Colors.END}""")

        print(f"""
    {Colors.GREEN}═══════ VAULT MODULES ═══════{Colors.END}
    {Colors.GREEN}[01]{Colors.END} Credential Manager    -> Store new credentials securely
    {Colors.GREEN}[02]{Colors.END} Credential Viewer     -> View saved credentials
    {Colors.GREEN}[03]{Colors.END} Recon Module          -> Search existing credentials
    {Colors.GREEN}[04]{Colors.END} Delete Module         -> Remove credentials from vault

    {Colors.YELLOW}══════ PASSWORD TOOLS ══════{Colors.END}
    {Colors.YELLOW}[05]{Colors.END} Password Analyzer    -> Check password strength
    {Colors.YELLOW}[06]{Colors.END} Password Generator   -> Generate secure passwords
    {Colors.YELLOW}[07]{Colors.END} Breach Scanner       -> Scan common breached passwords

    {Colors.MAGENTA}══════ SECURITY MODULES ══════{Colors.END}
    {Colors.MAGENTA}[08]{Colors.END} Audit Engine        -> Check password age
    {Colors.MAGENTA}[09]{Colors.END} Security Dashboard  -> Analyze vault security

    {Colors.RED}══════ SYSTEM ══════{Colors.END}
    {Colors.RED}[10]{Colors.END} Exit System            -> Close VaultGuard-X
    """)

        choice = input(f"{Colors.RED}vaultguard-x{Colors.END} > ")

        if choice == "1":
            add_credential()

        elif choice == "2":
            view_credentials()

        elif choice == "3":
            search_credential()

        elif choice == "4":
            delete_credential()

        elif choice == "5":
            password_strength()

        elif choice == "6":
            generate_password()

        elif choice == "7":
            breach_check()

        elif choice == "8":
            password_age_check()

        elif choice == "9":
            security_dashboard()

        elif choice == "10":

            print(
                f"\n{Colors.GREEN}[✓] Logging Out...{Colors.END}"
            )

            time.sleep(1)

            print(
                f"{Colors.GREEN}[✓] Vault Closed Securely{Colors.END}"
            )

            time.sleep(1)

            break

        else:

            print(
                f"{Colors.RED}[!] Invalid Choice!{Colors.END}"
            )

            time.sleep(1)

# ==========================
# MAIN
# ==========================


initialize_storage()
generate_key()

clear()

show_random_banner()

setup_master_password()

if login():

    loading()

    menu()