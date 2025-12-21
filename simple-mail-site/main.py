#!/usr/bin/env python3
import requests
import sqlite3

conn = sqlite3.connect("app.db")
conn.row_factory = sqlite3.Row
cur = conn.cursor()

cur.execute(
    """
    CREATE TABLE IF NOT EXISTS messages (
        id INTEGER PRIMARY KEY,
        sender TEXT,
        subject TEXT,
        body TEXT,
        timestamp TEXT DEFAULT CURRENT_TIMESTAMP
    )
"""
)

cur.execute("""
    CREATE TABLE IF NOT EXISTS user_info (
        id INTEGER PRIMARY KEY,
        key TEXT UNIQUE,
        value TEXT
    );
""")
cur.execute("""SELECT * FROM user_info WHERE key = 'name'""")
result = cur.fetchone()
if result:
    username = result["value"]
    print(f"Welcome, {username}")
else: 
    username = input("enter name: ")
    cur.execute("""INSERT INTO user_info (key, value) VALUES ('name', ?)""", [username])
    conn.commit()


conn.commit()


def send_message(sender, receiver, subject, body):
    """Send a message to the receiver. The receiver argument can be:
    - a hostname like 'alice' (posts to https://{receiver}.codewizardshq.com/...)
    - the special word 'local' to post to http://localhost:8000/cgi-bin/store_message.py
    - or a full URL (starting with http:// or https://)
    """
    msg = {"sender": sender, "subject": subject, "body": body}

    # determine target URL
    if receiver.startswith("http://") or receiver.startswith("https://"):
        url = receiver
    elif receiver.lower() == 'local':
        url = "http://localhost:8000/cgi-bin/store_message.py"
    else:
        url = f"https://{receiver}.codewizardshq.com/m31_intro_db_11/store_message.py"

    try:
        response = requests.post(url, data=msg, timeout=10)
        if response.status_code == 200:
            print("Message sent.")
        else:
            print(f"Error sending message: HTTP {response.status_code}")
            # print response text for easier debugging (first 500 chars)
            print(response.text[:500])
    except requests.RequestException as e:
        print("Request failed:", e)
        print("Tried URL:", url)
        return False
    return True
        
def select_message_by_id(msg_id):
    stmt = "SELECT * FROM messages WHERE id = ?;"
    vals = [msg_id]
    cur.execute(stmt, vals)
    return cur.fetchone()

def open_message_menu():
    try:
        msg_id = int(input("Enter message number to open (or 0 to cancel): "))
    except ValueError:
        print("Invalid number")
        return
    if msg_id == 0:
        return
    msg = select_message_by_id(msg_id)
    if msg:
        print("--- MESSAGE ---")
        print("ID:", msg["id"])
        print("From:", msg["sender"])
        print("Received:", msg["timestamp"])
        print("Subject:", msg["subject"])
        print("Body:\n", msg["body"])
        print("---------------")
    else:
        print("Message not found.")
    
    
def get_inbox():
    stmt = "SELECT id, subject, sender FROM messages"
    cur.execute(stmt)
    return cur.fetchall()
    
def update_name():
    new_name = input("enter new name: ")
    cur.execute("UPDATE user_info SET value = ? WHERE key = 'name'", [new_name])
    conn.commit()
    return new_name
   
while True:
    print("\n--- Simple Mail ---")
    print("1 - Send a message")
    print("2 - See messages (list)")
    print("3 - Open a message by number")
    print("4 - Set username")
    print("q - Quit")
    choice = input("Enter your choice: ")

    if choice == "1":
        sender = username
        receiver = input("Enter receiver (hostname, 'local', or full URL): ")
        subject = input("Enter subject: ")
        body = input("Enter body: ")
        send_message(sender, receiver, subject, body)

    elif choice == "2":
        inbox = get_inbox()
        if not inbox:
            print("no messages")
            continue
        for msg in inbox:
            print(f"{msg[0]} - {msg[1]} - {msg[2]}")

    elif choice == "3":
        open_message_menu()

    elif choice == "4":
        username = update_name()

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


conn.close()

