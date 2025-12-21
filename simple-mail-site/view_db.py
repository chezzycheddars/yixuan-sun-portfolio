#!/usr/bin/env python3
import cgitb
import sqlite3
import html

cgitb.enable()

print("Content-Type: text/html; charset=utf-8")
print()

print('''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>DB Viewer</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=Manrope&family=Rubik&display=swap');
  
body {
    text-align: center;
    font-family: 'Manrope', sans-serif;
}

table{
    font-size: 16px;
    table-layout: fixed;
    margin: 30px;
    background-color: #2a3333;
}

p{
    display: inline-block;
    padding: 1% 1%;
    font-size: 18px;
    margin: auto 60px;
    background-color: #181717;
    border: white 1px dashed;
    text-align: initial;
}

div{
    background: rgba(46, 46, 46, 0.9);
    margin: 3% 15%;
    border: grey 1px solid;
    color: #ffff;
    border-radius:3px;
    display: flex;
    flex-direction: column;
    gap: 12px;
}

td, th{
    padding:18px;
    border-radius: 3px;
    color:white;
    text-align:center;
}

th{
    background-color: #1e1e1e;
    color: #ffffff;
}

td{
    background-color: #262626;
    color: #ffffff;
}

h4{
    margin: 0;
    margin-bottom: 34px;
}

body{
    background-image:url('bg.jpg');
    background-repeat: no-repeat;
    background-size: cover;
}
</style>
</head>
<body>
''')

def show_data(rows, cols):
    print("<table><tbody>")

    print("<tr>")
    for heading in cols:
        print("<th>", html.escape(str(heading)) ,"</th>")
    print("</tr>")

    if not rows:
        print("<tr>")
        print(f"<td colspan='{len(cols)}'>no rows in table</td>")
        print("</tr>")
    else:
        for row in rows:
            print("<tr>")
            for data in row:
                print("<td>", html.escape(str(data)), "</td>")
            print("</tr>")
    print("</tbody></table>")

connection = sqlite3.connect('app.db')
connection.row_factory = sqlite3.Row
try:
    print("<div>")

    sql = connection.cursor()
    stmt = """
        SELECT name FROM sqlite_schema
        WHERE 
            type ='table' AND 
            name NOT LIKE 'sqlite_%';
    """
    tables = sql.execute(stmt).fetchall()

    if not tables:
        print("<h1>No tables in database</h1>") 
    for table in tables:
        tablename = table[0]
        print(f"<h1>{html.escape(tablename)}</h1>")
        cols = sql.execute(f'select name from pragma_table_info("{tablename}")').fetchall()
        cols = [col[0] for col in cols]
        rows = sql.execute(f"SELECT * FROM {tablename}").fetchall()
        show_data(rows, cols)

    print("</div>")
finally:
    connection.close()

print('\n</body>\n</html>')
