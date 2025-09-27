import streamlit as st
import sqlite3

# ---------------------------
# Database Functions
# ---------------------------
def init_db():
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS accounts (
            account_number TEXT PRIMARY KEY,
            name TEXT,
            pin TEXT,
            balance REAL
        )
    """)
    conn.commit()
    conn.close()

def create_account_db(account_number, name, pin, balance=0):
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO accounts VALUES (?, ?, ?, ?)", (account_number, name, pin, balance))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_account_db(account_number):
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute("SELECT * FROM accounts WHERE account_number=?", (account_number,))
    row = c.fetchone()
    conn.close()
    return row

def update_balance_db(account_number, new_balance):
    conn = sqlite3.connect("bank.db")
    c = conn.cursor()
    c.execute("UPDATE accounts SET balance=? WHERE account_number=?", (new_balance, account_number))
    conn.commit()
    conn.close()


# ---------------------------
# OOPs Class for BankAccount
# ---------------------------
class BankAccount:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            update_balance_db(self.account_number, self.balance)
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            update_balance_db(self.account_number, self.balance)
            return True
        return False


# ---------------------------
# Streamlit UI
# ---------------------------
st.set_page_config(page_title="Bank Management System", page_icon="🏦", layout="centered")
st.title("🏦 Bank Management System")

# Initialize database
init_db()

menu = ["Create Account", "View Details", "Deposit", "Withdraw"]
choice = st.sidebar.selectbox("Select Option", menu)

# Create Account
if choice == "Create Account":
    st.subheader("Create New Account")
    acc_no = st.text_input("Enter Account Number")
    name = st.text_input("Enter Name")
    pin = st.text_input("Set a 4-digit PIN", type="password")
    balance = st.number_input("Initial Deposit", min_value=0, value=0)

    if st.button("Create"):
        if create_account_db(acc_no, name, pin, balance):
            st.success(f"Account created successfully for {name}")
        else:
            st.error("Account already exists!")

# View Details
elif choice == "View Details":
    st.subheader("View Account Details")
    acc_no = st.text_input("Enter Account Number")
    pin = st.text_input("Enter your PIN", type="password")

    if st.button("View"):
        row = get_account_db(acc_no)
        if row and row[2] == pin:
            acc = BankAccount(*row)
            st.success(f"Account Holder: {acc.name}")
            st.info(f"Balance: ₹ {acc.balance}")
        else:
            st.error("Invalid Account Number or PIN")

# Deposit
elif choice == "Deposit":
    st.subheader("Deposit Money")
    acc_no = st.text_input("Enter Account Number")
    pin = st.text_input("Enter your PIN", type="password")
    amount = st.number_input("Enter amount", min_value=1, value=100)

    if st.button("Deposit"):
        row = get_account_db(acc_no)
        if row and row[2] == pin:
            acc = BankAccount(*row)
            acc.deposit(amount)
            st.success(f"₹{amount} deposited successfully! New Balance: ₹{acc.balance}")
        else:
            st.error("Invalid Account Number or PIN")

# Withdraw
elif choice == "Withdraw":
    st.subheader("Withdraw Money")
    acc_no = st.text_input("Enter Account Number")
    pin = st.text_input("Enter your PIN", type="password")
    amount = st.number_input("Enter amount", min_value=1, value=100)

    if st.button("Withdraw"):
        row = get_account_db(acc_no)
        if row and row[2] == pin:
            acc = BankAccount(*row)
            if acc.withdraw(amount):
                st.success(f"₹{amount} withdrawn successfully! New Balance: ₹{acc.balance}")
            else:
                st.error("Insufficient Balance!")
        else:
            st.error("Invalid Account Number or PIN")



# output terminal:- streamlit run bank_app.py