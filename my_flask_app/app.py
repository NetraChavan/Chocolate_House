from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


def init_db():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()

    
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                        id INTEGER PRIMARY KEY,
                        flavor_name TEXT,
                        description TEXT,
                        availability TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredient_inventory (
                        id INTEGER PRIMARY KEY,
                        ingredient_name TEXT,
                        quantity REAL,
                        unit TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                        id INTEGER PRIMARY KEY,
                        customer_name TEXT,
                        flavor_suggestion TEXT,
                        allergy_concern TEXT)''')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add_flavor', methods=['POST'])
def add_flavor():
    flavor_name = request.form['flavor_name']
    description = request.form['description']
    availability = request.form['availability']
    
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO seasonal_flavors (flavor_name, description, availability) VALUES (?, ?, ?)",
                   (flavor_name, description, availability))
    conn.commit()
    conn.close()

    return redirect(url_for('view_flavors'))

@app.route('/view_flavors')
def view_flavors():
    conn = sqlite3.connect("chocolate_house.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM seasonal_flavors")
    flavors = cursor.fetchall()
    conn.close()

    return render_template('view_flavors.html', flavors=flavors)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
