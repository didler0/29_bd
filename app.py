from flask import Flask, render_template
import pyodbc

app = Flask(__name__)

# Database connection settings
db_connection = pyodbc.connect(
    f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;'
)

# Define a route to display data from multiple tables
@app.route('/display_data')
def display_data():
    cursor = db_connection.cursor()

    # Fetch data from the "Client" table
    cursor.execute('SELECT * FROM Client')
    clients_data = cursor.fetchall()
    clients_column_names = [column[0] for column in cursor.description]

    # Fetch data from the "Hotel" table
    cursor.execute('SELECT * FROM Hotel')
    hotels_data = cursor.fetchall()
    hotels_column_names = [column[0] for column in cursor.description]

    # Fetch data from the "Route" table
    cursor.execute('SELECT * FROM Route')
    routes_data = cursor.fetchall()
    routes_column_names = [column[0] for column in cursor.description]

    # Fetch data from the "Discount" table
    cursor.execute('SELECT * FROM Discount')
    discounts_data = cursor.fetchall()
    discounts_column_names = [column[0] for column in cursor.description]

    # Fetch data from the "Trip" table
    cursor.execute('SELECT * FROM Trip')
    trips_data = cursor.fetchall()
    trips_column_names = [column[0] for column in cursor.description]

    return render_template('display_data.html',
        clients_data=clients_data, clients_column_names=clients_column_names,
        hotels_data=hotels_data, hotels_column_names=hotels_column_names,
        routes_data=routes_data, routes_column_names=routes_column_names,
        discounts_data=discounts_data, discounts_column_names=discounts_column_names,
        trips_data=trips_data, trips_column_names=trips_column_names
    )

if __name__ == '__main__':
    app.run(debug=True)