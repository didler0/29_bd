import tkinter as tk
from tkinter import ttk
import pyodbc

# Создаем подключение к базе данных
connection = pyodbc.connect('DRIVER={SQL Server};SERVER=DIDLERPC\\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')

# Функция для выполнения SQL-запросов с условиями сортировки и фильтрации
def execute_query_with_filter(table_name, sort_column, filter_column, filter_condition, filter_value):
    sql = f"SELECT * FROM {table_name}"
    
    if filter_column and filter_condition and filter_value:
        sql += f" WHERE {filter_column} {filter_condition} '{filter_value}'"
    
    if sort_column:
        sql += f" ORDER BY {sort_column}"
    
    cursor = connection.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data

# Функция для обновления данных в таблице с учетом сортировки и фильтрации
def update_table(table_name, table, sort_column, filter_column, filter_condition, filter_value):
    for row in table.get_children():
        table.delete(row)
    
    data = execute_query_with_filter(table_name, sort_column, filter_column, filter_condition, filter_value)
    
    for row in data:
        table.insert('', 'end', values=[row[i] for i in range(len(row))])

# Создание главного окна
root = tk.Tk()
root.title("Табличная форма")

# Создание вкладок для каждой таблицы
tab_control = ttk.Notebook(root)
tab_client = ttk.Frame(tab_control)
tab_hotel = ttk.Frame(tab_control)
tab_route = ttk.Frame(tab_control)
tab_discount = ttk.Frame(tab_control)
tab_trip = ttk.Frame(tab_control)
tab_control.add(tab_client, text="Таблица Client")
tab_control.add(tab_hotel, text="Таблица Hotel")
tab_control.add(tab_route, text="Таблица Route")
tab_control.add(tab_discount, text="Таблица Discount")
tab_control.add(tab_trip, text="Таблица Trip")
tab_control.pack(expand=1, fill="both")

# Создание таблицы для каждой таблицы
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

# Добавьте кнопки "Обновить" для каждой таблицы
btn_update_client = tk.Button(tab_client, text="Обновить", command=lambda: update_table("Client", table_client, "", "", "", ""))
btn_update_client.pack()
btn_update_hotel = tk.Button(tab_hotel, text="Обновить", command=lambda: update_table("Hotel", table_hotel, "", "", "", ""))
btn_update_hotel.pack()
btn_update_route = tk.Button(tab_route, text="Обновить", command=lambda: update_table("Route", table_route, "", "", "", ""))
btn_update_route.pack()
btn_update_discount = tk.Button(tab_discount, text="Обновить", command=lambda: update_table("Discount", table_discount, "", "", "", ""))
btn_update_discount.pack()
btn_update_trip = tk.Button(tab_trip, text="Обновить", command=lambda: update_table("Trip", table_trip, "", "", "", ""))
btn_update_trip.pack()

# Создайте элементы управления Entry и Combobox для каждой таблицы, а также кнопки для выполнения операций
def create_filter_controls(tab, table_name, table):
    filter_frame = ttk.Frame(tab)
    filter_frame.pack()

    sort_column_entry = tk.Entry(filter_frame)
    sort_column_entry.insert(0, "Id")
    sort_column_entry.pack()
    filter_column_entry = tk.Entry(filter_frame)
    filter_column_entry.pack()
    filter_condition_combobox = ttk.Combobox(filter_frame, values=["=", ">", "<", ">=", "<=", "LIKE"])
    filter_condition_combobox.set("=")
    filter_condition_combobox.pack()
    filter_value_entry = tk.Entry(filter_frame)
    filter_value_entry.pack()
    
    # Создайте кнопку для применения фильтра и обновления таблицы
    btn_apply_filter = tk.Button(filter_frame, text="Применить фильтр", command=lambda: update_table(table_name, table, sort_column_entry.get(), filter_column_entry.get(), filter_condition_combobox.get(), filter_value_entry.get()))
    btn_apply_filter.pack()

# Создайте элементы управления для каждой таблицы
create_filter_controls(tab_client, "Client", table_client)
create_filter_controls(tab_hotel, "Hotel", table_hotel)
create_filter_controls(tab_route, "Route", table_route)
create_filter_controls(tab_discount, "Discount", table_discount)
create_filter_controls(tab_trip, "Trip", table_trip)

# Запуск главного цикла
root.mainloop()