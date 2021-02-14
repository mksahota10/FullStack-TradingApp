import sqlite3, config
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index(): 
    connection = sqlite3.connect('app.db')  
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    cursor.execute("""
    SELECT id, symbol, name FROM stock
""")

    rows = cursor.fetchall()
    return {"Title": "Dashboard", "stocks": rows}