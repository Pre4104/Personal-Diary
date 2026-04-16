# Personal Diary App

A command-line personal diary application built with **Python**. Supports user signup/login and lets each user add, view, edit, delete, and search diary entries — all stored locally in text files.

---

## Features

- User signup and sign-in with credential validation
- Add a diary entry for today (one entry per day)
- View an entry by a specific date
- View all entries at once
- Edit an existing entry by date
- Delete an entry by date
- Search all entries by keyword

---

## Project Structure

```
personal-diary-app/
├── diary.py        ← main program
├── diary.txt       ← auto-created; stores diary entries
├── user.txt        ← auto-created; stores user credentials
└── README.md
```

> `diary.txt` and `user.txt` are created automatically on first run.

---

## How to Run

### Requirements
- Python 3.x (no external libraries needed)

### Steps

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/personal-diary-app.git

# Navigate into the folder
cd personal-diary-app

# Run the program
python diary.py
```

---

## Usage

### On first run — Sign Up
```
====== Personal Diary App ======
1. Sign Up
2. Sign In
3. Exit
Enter your choice: 1
Enter username: prerana
Enter password: mypassword
Signup successful!
```

### After signing in — Diary Menu
```
===== Dear Diary — prerana =====
1. Add Today's Entry
2. View Entry by Date
3. View All Entries
4. Edit Entry
5. Delete Entry
6. Search Entries
7. Logout
```

---

## Data Storage

- `user.txt` — stores usernames and passwords as `username : password` (one per line)
- `diary.txt` — stores entries as `YYYY-MM-DD: entry text` (one per line)

> Note: Passwords are stored in plain text. This project is for educational/personal use only. Do not use real passwords.

---

## Technologies Used

- **Language:** Python 3.x
- **Libraries:** `datetime`, `os` (both built-in)

---

## Author

**B S Lakshmi Prerana**
Kendriya Vidyalaya AFS Yelahanka, Bengaluru – 560063
