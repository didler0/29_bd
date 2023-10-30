import pyodbc

class SQL:

    @staticmethod
    def GetClients():
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Client').fetchall()
        return list
    
    @staticmethod
    def GetClientById(id_):
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Client WHERE Id=?',(id_,)).fetchall()
        return list
    
    @staticmethod
    def GetDiscount():
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Discount').fetchall()
        return list
    
    @staticmethod
    def GetDiscountById(id_):
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Discount WHERE Id=?',(id_,)).fetchall()
        return list
    
    @staticmethod
    def GetHotel():
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Hotel').fetchall()
        return list
    
    @staticmethod
    def GetHotelById(id_):
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Hotel WHERE Id=?',(id_,)).fetchall()
        return list
        
    
    @staticmethod
    def GetRoute():
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Route').fetchall()
        return list    
    

    @staticmethod
    def GetRouteById(id_):
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Route WHERE Id=?',(id_,)).fetchall()
        return list
    
    @staticmethod
    def GetTrip():
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Trip').fetchall()
        return list   

    @staticmethod
    def GetTripById(id_):
        connection=pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        list = cursor.execute('SELECT * FROM Trip WHERE Id=?',(id_,)).fetchall()
        return list 
    
    

    @staticmethod
    def DeleteClientById(id_):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Client WHERE Id=?', (id_,))
        #cursor.execute('''UPDATE Client SET id = id - 1 WHERE id > ?''', (id_,))
        connection.commit()

    @staticmethod
    def DeleteDiscountById(id_):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Discount WHERE Id=?', (id_,))
        #cursor.execute('''UPDATE Discount SET id = id - 1 WHERE id > ?''', (id_,))
        connection.commit()

    @staticmethod
    def DeleteHotelById(id_):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Hotel WHERE Id=?', (id_,))
        #cursor.execute('''UPDATE Hotel SET id = id - 1 WHERE id > ?''', (id_,))
        connection.commit()

    @staticmethod
    def DeleteRouteById(id_):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Route WHERE Id=?', (id_,))
        #cursor.execute('''UPDATE Route SET id = id - 1 WHERE id > ?''', (id_,))
        connection.commit()

    @staticmethod
    def DeleteTripById(id_):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute('DELETE FROM Trip WHERE Id=?', (id_,))
        #cursor.execute('''UPDATE Trip SET id = id - 1 WHERE id > ?''', (id_,))
        connection.commit()

    @staticmethod
    def insert_client( phone_number, first_name, last_name, middle_name, address):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO [Client] (PhoneNumber, FirstName, LastName, MiddleName, Address) VALUES (?, ?, ?, ?, ?)", phone_number, first_name, last_name, middle_name, address)
        connection.commit()
        connection.close()
    @staticmethod
    def insert_hotel( phone_number, country, address):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO [Hotel] (HotelPhoneNumber, Country, Address) VALUES (?, ?, ?)", phone_number, country, address)
        connection.commit()
        connection.close()
    @staticmethod
    def insert_route( hotel_class, hotel_id, climate_type):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO [Route] (HotelClass, HotelId, ClimateType) VALUES (?, ?, ?)", hotel_class, hotel_id, climate_type)
        connection.commit()
        connection.close()
    @staticmethod
    def insert_discount( discount_percentage, number_of_tours):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO [Discount] (DiscountPercentage, NumberOfTours) VALUES (?, ?)", discount_percentage, number_of_tours)
        connection.commit()
        connection.close()
    @staticmethod
    def insert_trip( client_id, route_id, departure_date, arrival_date, discount_id, number_of_days):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("INSERT INTO [Trip] (ClientId, RouteId, DepartureDate, ArrivalDate, DiscountId, NumberOfDays) VALUES (?, ?, ?, ?, ?, ?)", client_id, route_id, departure_date, arrival_date, discount_id, number_of_days)
        connection.commit()
        connection.close()    @staticmethod
    def update_client(phone_number, new_first_name, new_last_name, new_middle_name, new_address):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("UPDATE [Client] SET FirstName = ?, LastName = ?, MiddleName = ?, Address = ? WHERE PhoneNumber = ?", new_first_name, new_last_name, new_middle_name, new_address, phone_number)
        connection.commit()
        connection.close()

    @staticmethod
    def update_hotel(hotel_phone_number, new_country, new_address):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("UPDATE [Hotel] SET Country = ?, Address = ? WHERE HotelPhoneNumber = ?", new_country, new_address, hotel_phone_number)
        connection.commit()
        connection.close()
        
    @staticmethod
    def update_route(hotel_id, new_hotel_class, new_climate_type):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("UPDATE [Route] SET HotelClass = ?, ClimateType = ? WHERE HotelId = ?", new_hotel_class, new_climate_type, hotel_id)
        connection.commit()
        connection.close()
    @staticmethod
    def update_discount(discount_id, new_discount_percentage, new_number_of_tours):
       connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
       cursor = connection.cursor()
       cursor.execute("UPDATE [Discount] SET DiscountPercentage = ?, NumberOfTours = ? WHERE DiscountId = ?", new_discount_percentage, new_number_of_tours, discount_id)
       connection.commit()
       connection.close()
    
    
    @staticmethod
    def update_trip(trip_id, new_client_id, new_route_id, new_departure_date, new_arrival_date, new_discount_id, new_number_of_days):
        connection = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER=DIDLERPC\SQLEXPRESS;DATABASE=TravelAgencyDB_zapros;Trusted_Connection=yes;')
        cursor = connection.cursor()
        cursor.execute("UPDATE [Trip] SET ClientId = ?, RouteId = ?, DepartureDate = ?, ArrivalDate = ?, DiscountId = ?, NumberOfDays = ? WHERE TripId = ?", new_client_id, new_route_id, new_departure_date, new_arrival_date, new_discount_id, new_number_of_days, trip_id)
        connection.commit()
        connection.close()
    




    #cursor.execute('''UPDATE change SET id = id - 1 WHERE id > ?''', (key,))
if __name__ == "__main__":
    print(SQL.GetTripById(1))
    



