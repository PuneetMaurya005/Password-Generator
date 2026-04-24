# 🔐 Secure Password Generator

A simple yet powerful command-line password generator built with Python. It uses the `secrets` module for cryptographically secure password generation and automatically copies the result to your clipboard using `pyperclip`.

---

## ✨ Features

- ✅ Cryptographically secure using Python's `secrets` module
- ✅ Customizable password length
- ✅ Optional symbol support (`@#$%^&*`)
- ✅ Generate multiple passwords at once
- ✅ Guarantees at least one uppercase, lowercase, digit, and symbol
- ✅ Auto-copies password(s) to clipboard

---
## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/secure-password-generator.git
   cd secure-password-generator
   ```

2. **Install dependencies**
   ```bash
   pip install pyperclip
   ```

---

## 🛠️ Usage

```bash
python passgen.py
```

**Sample interaction:**

```
=== Secure Password Generator ===

Password length (default 16): 20
Include symbols? (y/n, default y): y
How many passwords? (default 1): 2

Generated Password(s):
----------------------------------------
1. Gk#7Xp^mN2@qLvT9wZa
2. A$3jYn&8*dWc@eKuP6bF

All passwords copied to clipboard!
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `pyperclip` | Copies generated password(s) to clipboard |

Install via:
```bash
pip install pyperclip

---

## 🔒 Security Notes

- Every generated password is guaranteed to contain:
  - At least one **uppercase** letter
  - At least one **lowercase** letter
  - At least one **digit**
  - At least one **symbol** (if enabled)

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

Made with ❤️ using Python
