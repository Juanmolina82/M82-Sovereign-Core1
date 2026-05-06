from flask import Flask, request, jsonify
import datetime
import sqlite3
import os

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('M82_Intel_Vault.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS intel_logs (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp TEXT, news TEXT, impact TEXT)')
    conn.commit()
    conn.close()

@app.route('/agi/v7/inject_intel', methods=['POST'])
def inject_intel():
    data = request.json
    news = data.get('news', 'N/A')
    impact = data.get('impact', 'N/A')
    ts = datetime.datetime.now().isoformat()
    try:
        conn = sqlite3.connect('M82_Intel_Vault.db')
        c = conn.cursor()
        c.execute("INSERT INTO intel_logs (timestamp, news, impact) VALUES (?, ?, ?)", (ts, news, impact))
        conn.commit()
        conn.close()
        return jsonify({"status": "INTEL_SECURED", "db": "ARCHIVED", "timestamp": ts}), 201
    except Exception as e:
        return jsonify({"status": "ERROR", "message": str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(port=8080)
