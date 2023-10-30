from flask import Flask, render_template, request
import pyodbc

app = Flask(__name__)

# Database connection settings
db_connection = pyodbc.connect(
    f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;'
)

# Define a route to select and display data from a table
@app.route('/display_table', methods=['GET', 'POST'])
def display_table():
    cursor = db_connection.cursor()

    if request.method == 'POST':
        table_name = request.form['table_name']
        cursor.execute(f'SELECT * FROM {table_name}')
        data = cursor.fetchall()
        column_names = [column[0] for column in cursor.description]
        return render_template('display_data.html', data=data, column_names=column_names)

    return render_template('select_table.html')

if __name__ == '__main__':
    app.run(debug=True)
