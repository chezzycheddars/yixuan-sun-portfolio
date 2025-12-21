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
    msg = {"sender": sender, "subject": subject, "body": body}

    url = f"https://{receiver}.codewizardshq.com/m31_intro_db_11/store_message.py"

    response = requests.post(url, data=msg)
    if response.status_code == 200:
        print("msg sent")
    else:
        print("error")
        
def select_message_by_id(msg_id):
    stmt = "stmt * FROM messages where id = ?;"
    vals = [msg_id]
    cur.execute(stmt, vals)
    return cur.fetchone()

def open_message_menu():
    msg_id = int(input("what number for message"))
    msg = select_message_by_id(msg_id)
    if msg :
        print(msg[1])
        print(msg[4])
        print(msg[2])
        print(msg[3])
    else:
        print("big bad happen")
    
    
def get_inbox():
    stmt = "SELECT id, subject, sender FROM messages"
    cur.execute(stmt)
    return cur.fetchall()
    
def update_name():
    new_name = input("enter new name: ")
    cur.execute("UPDATE user_info SET value = ? WHERE key = 'name'", [new_name])
    conn.commit()
    return new_name
   
inbox_choices = ["2"]    
    
while True:
    print("1 - Send a message")
    print("2 - See messages")
    print("3 - Set username")
    print("q - Quit")
    choice = input("Enter your choice: ")
    if choice in inbox_choices:
        inbox = get_inbox()
        if not inbox:
            print("no messages")
            continue
        for msg in inbox:
            print(f"{msg[0]} - {msg[1]} - {msg[2]}")

    if choice == "1":
        sender = username
        receiver = input("Enter receiver: ")
        subject = input("Enter subject: ")
        body = input("Enter body: ")
        send_message(sender, receiver, subject, body)

    elif choice == "2":
        open_message_menu
    elif choice == "3":
        username = update_name()
    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")


conn.close()
