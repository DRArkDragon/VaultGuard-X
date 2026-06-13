# 🔐 VaultGuard-X

<div align="center">

# ☣️ VaultGuard-X

### A Cybersecurity-Themed Password Manager Built with Python

Securely store credentials, generate strong passwords, detect weak passwords, perform breach checks, and audit your vault — all from a hacker-inspired terminal interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Fernet%20Encryption-green?style=for-the-badge)
![Hashing](https://img.shields.io/badge/Master%20Password-bcrypt-red?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</div>

---

## 🚀 Features

* 🔐 **Master Password Authentication** using **bcrypt**
* 🔒 **Encrypted Credential Storage** using **Fernet**
* 👤 Add, View, Search & Delete Credentials
* 🚫 Duplicate Website/Username Protection
* 📊 Password Strength Analyzer
* 🎲 Secure Password Generator
* 🚨 Common Password Breach Scanner
* ⏳ Password Age Audit
* 📈 Security Dashboard & Risk Analysis
* 🎨 Kali Linux / Metasploit Inspired Terminal UI
* 🌍 Cross-Platform Password Input Support
* 📂 Hidden Local Storage for Sensitive Files

---

## 📁 Project Structure

```text
VaultGuard-X/
│── main.py
│── common_passwords.txt
│── README.md
│── requirements.txt
│── LICENSE
│── .gitignore
```

> Runtime files such as the encrypted vault, master password hash, and encryption key are created automatically inside a hidden `.vault_data` directory.

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/VaultGuard-X.git
cd VaultGuard-X
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```

---

## 🛡️ Security Features

* Master passwords are hashed with **bcrypt**.
* Stored credentials are encrypted using **Fernet symmetric encryption**.
* Passwords remain hidden while typing.
* Viewing sensitive credentials requires master password verification.
* Common password database helps identify easily guessable passwords.

---

## 🧰 Built With

* Python 3
* bcrypt
* cryptography (Fernet)
* JSON
* hashlib
* datetime

---

## 📸 Screenshots

### Startup Screen

![Startup](Screenshots/Startup.png)

---

### Main Console

![Menu](Screenshots/Menu.png)

---

### Security Dashboard

![Dashboard](Screenshots/Dashboard.png)

---

## 💡 Future Improvements

* Two-Factor Authentication (2FA)
* Password History Tracking
* Encrypted Vault Export/Import
* Automatic Password Rotation Reminders
* GUI Version
* Cloud Backup & Synchronization

---

## 👨‍💻 Author

**Ankur Chaurasia**

Developed as a cybersecurity-focused portfolio project demonstrating encryption, secure credential management, and password auditing concepts.

🔗 LinkedIn: https://www.linkedin.com/in/ankur-chaurasia-aa8738159/

---

If you found this project useful, feel free to ⭐ the repository and connect with me on LinkedIn.
---

## 📜 License

This project is licensed under the **MIT License**.

Copyright (c) 2026 Ankur Chaurasia

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
