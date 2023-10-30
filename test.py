import tkinter as tk
from tkinter import ttk
import pyodbc

# Create a connection to the database
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DIDLERPC\\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')

# Function to execute SQL queries with filtering and sorting
def execute_query_with_filter_and_sort(table_name, sort_column, sort_order, filter_column, filter_condition, filter_value):
    sql = f"SELECT * FROM {table_name}"
    
    if filter_column and filter_condition and filter_value:
        sql += f" WHERE {filter_column} {filter_condition} '{filter_value}'"

    if sort_column:
        sql += f" ORDER BY {sort_column} {sort_order}"

    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data

# Function to update the table data with sorting and filtering
def update_table(table_name, table, sort_column, sort_order, filter_column, filter_condition, filter_value):
    for row in table.get_children():
        table.delete(row)

    data = execute_query_with_filter_and_sort(table_name, sort_column, sort_order, filter_column, filter_condition, filter_value)

    for row in data:
        table.insert('', 'end', values=[row[i] for i in range(len(row))])

# Create the main window
root = tk.Tk()
root.title("Tabular Form")

# Create tabs for each table
tab_control = ttk.Notebook(root)
tab_client = ttk.Frame(tab_control)
tab_hotel = ttk.Frame(tab_control)
tab_route = ttk.Frame(tab_control)
tab_discount = ttk.Frame(tab_control)
tab_trip = ttk.Frame(tab_control)
tab_control.add(tab_client, text="Table Client")
tab_control.add(tab_hotel, text="Table Hotel")
tab_control.add(tab_route, text="Table Route")
tab_control.add(tab_discount, text="Table Discount")
tab_control.add(tab_trip, text="Table Trip")
tab_control.pack(expand=1, fill="both")

# Create a table for each table
columns_client = ('Id', 'PhoneNumber', 'FirstName', 'LastName', 'MiddleName', 'Address')
table_client = ttk.Treeview(tab_client, columns=columns_client, show='headings')
for col in columns_client:
    table_client.heading(col, text=col)
table_client.pack(fill="both")

columns_hotel = ('Id', 'HotelPhoneNumber', 'Country', 'Address')
table_hotel = ttk.Treeview(tab_hotel, columns=columns_hotel, show='headings')
for col in columns_hotel:
    table_hotel.heading(col, text=col)
table_hotel.pack(fill="both")

columns_route = ('Id', 'HotelClass', 'HotelId', 'ClimateType')
table_route = ttk.Treeview(tab_route, columns=columns_route, show='headings')
for col in columns_route:
    table_route.heading(col, text=col)
table_route.pack(fill="both")

columns_discount = ('Id', 'DiscountPercentage', 'NumberOfTours')
table_discount = ttk.Treeview(tab_discount, columns=columns_discount, show='headings')
for col in columns_discount:
    table_discount.heading(col, text=col)
table_discount.pack(fill="both")

columns_trip = ('Id', 'ClientId', 'RouteId', 'DepartureDate', 'ArrivalDate', 'DiscountId', 'NumberOfDays')
table_trip = ttk.Treeview(tab_trip, columns=columns_trip, show='headings')
for col in columns_trip:
    table_trip.heading(col, text=col)
table_trip.pack(fill="both")

# Add "Update" buttons for each table
btn_update_client = tk.Button(tab_client, text="Update", command=lambda: update_table("Client", table_client, "", "", "", "", ""))
btn_update_client.pack()
btn_update_hotel = tk.Button(tab_hotel, text="Update", command=lambda: update_table("Hotel", table_hotel, "", "", "", "", ""))
btn_update_hotel.pack()
btn_update_route = tk.Button(tab_route, text="Update", command=lambda: update_table("Route", table_route, "", "", "", "", ""))
btn_update_route.pack()
btn_update_discount = tk.Button(tab_discount, text="Update", command=lambda: update_table("Discount", table_discount, "", "", "", "", ""))
btn_update_discount.pack()
btn_update_trip = tk.Button(tab_trip, text="Update", command=lambda: update_table("Trip", table_trip, "", "", "", "", ""))
btn_update_trip.pack()

# Create filter and sorting controls for each table
def create_filter_controls(tab, table_name, table, columns):
    filter_frame = ttk.Frame(tab)
    filter_frame.pack()

    sort_column_entry = tk.Entry(filter_frame)
    sort_column_entry.insert(0, "Id")
    sort_column_entry.pack()
    
    filter_column_combobox = ttk.Combobox(filter_frame, values=columns)
    filter_column_combobox.set(columns[0])
    filter_column_combobox.pack()
    
    filter_condition_combobox = ttk.Combobox(filter_frame, values=["=", ">", "<", ">=", "<=", "LIKE"])
    filter_condition_combobox.set("=")
    filter_condition_combobox.pack()
    
    filter_value_entry = tk.Entry(filter_frame)
    filter_value_entry.pack()
    
    sort_order_combobox = ttk.Combobox(filter_frame, values=["ASC", "DESC"])
    sort_order_combobox.set("ASC")
    sort_order_combobox.pack()

    # Create a button to apply the filter and update the table
    btn_apply_filter = tk.Button(filter_frame, text="Apply Filter", command=lambda: update_table(table_name, table, sort_column_entry.get(), sort_order_combobox.get(), filter_column_combobox.get(), filter_condition_combobox.get(), filter_value_entry.get()))
    btn_apply_filter.pack()

# Define columns for each table
columns_client = ('Id', 'PhoneNumber', 'FirstName', 'LastName', 'MiddleName', 'Address')
columns_hotel = ('Id', 'HotelPhoneNumber', 'Country', 'Address')
columns_route = ('Id', 'HotelClass', 'HotelId', 'ClimateType')
columns_discount = ('Id', 'DiscountPercentage', 'NumberOfTours')
columns_trip = ('Id', 'ClientId', 'RouteId', 'DepartureDate', 'ArrivalDate', 'DiscountId', 'NumberOfDays')

# Create filter and sorting controls for each table
create_filter_controls(tab_client, "Client", table_client, columns_client)
create_filter_controls(tab_hotel, "Hotel", table_hotel, columns_hotel)
create_filter_controls(tab_route, "Route", table_route, columns_route)
create_filter_controls(tab_discount, "Discount", table_discount, columns_discount)
create_filter_controls(tab_trip, "Trip", table_trip, columns_trip)

# Run the main loop
root.mainloop()