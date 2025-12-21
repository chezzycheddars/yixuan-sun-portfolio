import sqlite3
import cgi, cgitb
cgitb.enable()

print("Content-Type: text/html")
print()

def get_message():
    message_data = cgi.FieldStorage()
    if (message_data):
        data = {}
        for key in message_data.keys():
            data[key] = message_data[key].value
        return data
    

def insert_message(sender, subject, body):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    stmt = 'INSERT INTO messages (sender, subject, body) VALUES (?, ?, ?)'
    vals = [sender, subject, body]
    cursor.execute(stmt, vals)
    conn.commit()
    conn.close()


msg = get_message()

if msg:
    insert_message(msg["sender"], msg["subject"], msg["body"])
    print("message received")
else:
    print("no message")
