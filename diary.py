from datetime import datetime
import os

# ── file helpers ──────────────────────────────────────────────────────────────
DIARY_FILE = "diary.txt"
USER_FILE  = "user.txt"

def init_files():
    for fname in [DIARY_FILE, USER_FILE]:
        if not os.path.exists(fname):
            open(fname, "w").close()

init_files()


# ── date utilities ────────────────────────────────────────────────────────────
def input_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:                         # BUG FIX: bare except → except ValueError
            print("Invalid format. Please use YYYY-MM-DD.")

def getdate():
    return datetime.now().strftime("%Y-%m-%d")


# ── diary functions ───────────────────────────────────────────────────────────
def addentry():
    date  = getdate()
    # BUG FIX: check if an entry already exists for today
    with open(DIARY_FILE, "r") as f:
        for line in f:
            if line.startswith(date):
                print(f"An entry for {date} already exists. Use 'Edit Entry' to modify it.")
                return
    entry = input("Enter your diary entry: ")
    with open(DIARY_FILE, "a") as f:
        f.write(date + ": " + entry + "\n")
    print("Entry added successfully!")

def viewentry():                                   # BUG FIX: date was required arg with no prompt
    date  = input_date()
    found = False
    with open(DIARY_FILE) as f:
        for line in f:
            if line.startswith(date):
                print(line.strip())
                found = True
    if not found:
        print(f"No entry found for {date}.")

def viewallentries():
    with open(DIARY_FILE) as f:
        lines = f.readlines()
    if not lines:
        print("No entries yet.")
        return
    print("\n── All Diary Entries ──")
    for line in lines:
        print(line.strip())

def delentry():
    date = input_date()
    with open(DIARY_FILE, "r") as f:
        lines = f.readlines()
    new_lines = [line for line in lines if not line.startswith(date)]
    if len(new_lines) == len(lines):               # BUG FIX: notify if nothing was deleted
        print(f"No entry found for {date}.")
        return
    with open(DIARY_FILE, "w") as f:
        f.writelines(new_lines)
    print(f"Entry for {date} deleted successfully!")

def editentry():
    date      = input_date()
    with open(DIARY_FILE, "r") as f:
        lines = f.readlines()
    found = any(line.startswith(date) for line in lines)
    if not found:                                  # BUG FIX: notify if entry doesn't exist
        print(f"No entry found for {date}.")
        return
    new_entry = input("Enter new entry: ")
    with open(DIARY_FILE, "w") as f:
        for line in lines:
            if line.startswith(date):
                f.write(date + ": " + new_entry + "\n")
            else:
                f.write(line)
    print("Entry updated successfully!")

def searchentry():                                 # ADDED: search by keyword
    keyword = input("Enter keyword to search: ").lower()
    with open(DIARY_FILE) as f:
        lines = f.readlines()
    results = [line.strip() for line in lines if keyword in line.lower()]
    if results:
        print(f"\nFound {len(results)} entry/entries:")
        for r in results:
            print(" ", r)
    else:
        print("No entries found with that keyword.")


# ── auth functions ────────────────────────────────────────────────────────────
def signup():
    username = input("Enter username: ").strip()
    if not username:
        print("Username cannot be empty.")
        return False
    # BUG FIX: check for duplicate usernames
    with open(USER_FILE, "r") as f:
        for line in f:
            if line.strip().startswith(username + " : "):
                print("Username already exists. Please choose another.")
                return False
    pwd = input("Enter password: ").strip()
    if not pwd:                                    # BUG FIX: disallow empty password
        print("Password cannot be empty.")
        return False
    with open(USER_FILE, "a") as f:
        f.write(username + " : " + pwd + "\n")
    print("Signup successful!")
    return True

def signin():
    username = input("Enter username: ").strip()
    pwd      = input("Enter password: ").strip()
    with open(USER_FILE, "r") as f:
        for line in f:
            parts = line.strip().split(" : ")
            if len(parts) == 2:                    # BUG FIX: guard against malformed lines
                u, p = parts
                if u == username and p == pwd:
                    print(f"Login successful! Welcome, {username}.")
                    return username                # BUG FIX: return username instead of True
    print("Invalid credentials. Please try again.")
    return None


# ── diary menu (shown after login) ───────────────────────────────────────────
def diary_menu(username):
    while True:
        print(f"\n===== 📓 Dear Diary — {username} =====")
        print("1. Add Today's Entry")
        print("2. View Entry by Date")
        print("3. View All Entries")
        print("4. Edit Entry")
        print("5. Delete Entry")
        print("6. Search Entries")
        print("7. Logout")

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            addentry()
        elif choice == "2":
            viewentry()
        elif choice == "3":
            viewallentries()
        elif choice == "4":
            editentry()
        elif choice == "5":
            delentry()
        elif choice == "6":
            searchentry()
        elif choice == "7":
            print("Logged out. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1–7.")


# ── entry point ───────────────────────────────────────────────────────────────
def main():
    while True:
        print("\n====== 📒 Personal Diary App ======")
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            signup()
        elif choice == "2":
            username = signin()
            if username:                           # BUG FIX: signin now returns username or None
                diary_menu(username)
        elif choice == "3":
            print("Goodbye!")
            break                                  # BUG FIX: was missing; loop never exited
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()
