#!/usr/bin/env python3
import sqlite3
import cgi, cgitb
import html
cgitb.enable()

print("Content-Type: text/html; charset=utf-8")
print()

def get_message():
    message_data = cgi.FieldStorage()
    if message_data:
        data = {}
        for key in message_data.keys():
            data[key] = message_data[key].value
        return data
    return None
    
def insert_message(sender, subject, body):
    max_len = 2000
    sender = sender[:max_len]
    subject = subject[:max_len]
    body = body[:max_len]

    conn = sqlite3.connect('app.db')
    try:
        cursor = conn.cursor()
        stmt = 'INSERT INTO messages (sender, subject, body) VALUES (?, ?, ?)'
        vals = [sender, subject, body]
        cursor.execute(stmt, vals)
        conn.commit()
    finally:
        conn.close()

msg = get_message()

if msg:
    sender = msg.get("sender", "").strip()
    subject = msg.get("subject", "").strip()
    body = msg.get("body", "").strip()
    if sender and body:
        insert_message(sender, subject, body)
        print("message received")
    else:
        print("missing fields: sender and body are required")
else:
    print("no message")
