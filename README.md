# README

## Calculator Application

### Description
This is a simple GUI-based calculator application built using Python's `tkinter` library. It supports basic arithmetic operations such as addition, subtraction, multiplication, and division.

### Features
- Responsive GUI with buttons for digits (0-9) and basic operations (+, -, *, /).
- Ability to evaluate arithmetic expressions entered directly or using the provided buttons.
- Clear button (`CE`) to reset the input field.
- Error handling for invalid expressions.

### How to Run
1. Install Python 3.x if not already installed.
2. Save the `Calculator` code into a Python file (e.g., `calculator.py`).
3. Run the application using:
   ```bash
   python calculator.py
   ```
4. The calculator window will appear with buttons for interacting.

---

## Random Password Generator

### Description
A GUI-based application to manage passwords for different websites. It features:
- A random password generator.
- Functionality to save website credentials (website name, email/username, password) into a SQLite database.
- Search functionality to find saved credentials.

### Features
- **Generate Password:** Creates a random 8-character password with numbers, special characters, and letters.
- **Save Credentials:** Stores website, email/username, and password in a SQLite database.
- **Search Website:** Retrieves and displays stored credentials for a given website.
- User-friendly GUI.

### How to Run
1. Install Python 3.x and the `sqlite3` module (pre-installed with Python).
2. Save the `Generate Random Password` code into a Python file (e.g., `password_manager.py`).
3. Place an image file named `image.png` in the same directory as the script (for the GUI logo).
4. Run the application using:
   ```bash
   python password_manager.py
   ```
5. The application window will appear, allowing you to generate, save, and search for passwords.

### Notes
- Ensure that the file `image.png` exists in the script's directory; otherwise, remove the image-related code for it to run without the image.
- The application creates a SQLite database (`database.db`) in the same directory to store credentials.

---

## Dependencies
Both applications rely only on Python's built-in libraries:
- `tkinter` for GUI development.
- `sqlite3` for database management (for the password generator).

No additional installations are needed.
