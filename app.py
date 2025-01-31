from flask import Flask, render_template, request, redirect, url_for
from database import get_db_connection
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/add', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        First_name = request.form['First_name']
        Last_name = request.form['Last_name']
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


@app.route('/view')
def view_employees():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM employees;')
    employees = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('view_employees.html', employees=employees)


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_employee(id):
    conn = get_db_connection()
    cur = conn.cursor()
    if request.method == 'POST':
        first_name = request.form['First_name']
        last_name = request.form['Last_name']
        email = request.form['Email']
        phone = request.form['Phone']
        department = request.form['Department']

        cur.execute(
            'UPDATE employees SET First_name = %s, Last_name = %s, Email = %s, Phone = %s, Department = %s'
            'WHERE id = %s',
            (first_name, last_name, email, phone, department, id)
        )
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('view_employees'))
    
    cur.execute('SELECT * FROM employees WHERE id = %s', (id,))
    employee = cur.fetchone()
    cur.close()
    conn.close()
    return render_template('update_employee.html', employee=employee)


if __name__ == '__main__':
    app.run(debug=True)
