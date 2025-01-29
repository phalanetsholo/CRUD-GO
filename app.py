from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection
app = Flask(__name__)

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Add Employee Route
@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        First_name = request.form['First_name']
        Last_name = request.form['Fast_name']
        Email = request.form['Email']
        Phone = request.form['Phone']
        Department = request.form['Department']

        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO employees (First_name, Last_name, Email, Phone, Department)'
            'VALUES (%s, %s, %s, %s, %s)',
            (First_name, Last_name, Email, Phone, Department)
        )
        conn.commit()
        cur.close()
        conn.close()
        return redirect(url_for('view_employees'))
    return render_template('add_employee.html')

# View Employees Route
@app.route('/view')
def view_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view_employees.html', employees=employees)

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
