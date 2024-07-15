import psycopg2
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        dbname='calendar_app',
        user='law',
        password='password',
        host='localhost',
        port='5432'
    )
    return conn

@app.route('/api/events', methods=['GET'])
def get_events():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT id, title, date FROM events;')
    events = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)