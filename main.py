from typing import Optional, Tuple, Union
import db_adapter
import customtkinter
import tkinter
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("dark-blue")





class App(customtkinter.CTk):
    WIDTH = 820
    HEIGHT = 380
    def __init__(self):
        super().__init__()
        self.title("bd29_nakhimov")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable(False,False)


        self.grid_columnconfigure(1, weight=0)
        self.grid_rowconfigure(0, weight=0)

        self.frame_left = customtkinter.CTkFrame(master=self,corner_radius=6,border_color='dodgerBlue',border_width=2)
        self.frame_left.grid(row=0, column=0,padx=20,pady=20)

        self.BtnClient=customtkinter.CTkButton(master=self.frame_left,text="Таблица Client",command=lambda:self.OutputData(1))
        self.BtnClient.grid(row=0,column=0,padx=40,pady=10,sticky="nwe")
        self.BtnDiscount=customtkinter.CTkButton(master=self.frame_left,text="Таблица Discount",command=lambda:self.OutputData(2))
        self.BtnDiscount.grid(row=1,column=0,padx=40,pady=10,sticky="nwe")
        self.BtnHotel=customtkinter.CTkButton(master=self.frame_left,text="Таблица Hotel",command=lambda:self.OutputData(3))
        self.BtnHotel.grid(row=2,column=0,padx=40,pady=10,sticky="nwe")
        self.BtnRoute=customtkinter.CTkButton(master=self.frame_left,text="Таблица Route",command=lambda:self.OutputData(4))
        self.BtnRoute.grid(row=3,column=0,padx=40,pady=10,sticky="nwe")
        self.BtnTrip=customtkinter.CTkButton(master=self.frame_left,text="Таблица Trip",command=lambda:self.OutputData(5))
        self.BtnTrip.grid(row=4,column=0,padx=40,pady=10,sticky="nwe")

        self.frame_right = customtkinter.CTkFrame(master=self,corner_radius=6,height=340,width=720)
        self.frame_right.grid(row=0, column=2,padx=20,pady=20)
        

        
    def kostyl(self):
        self.qwe=customtkinter.CTkLabel(master=self.frame_right,text='',width=40)
        self.qwe.grid(row=0,column=0,padx=10,pady=10)
        self.qwe=customtkinter.CTkLabel(master=self.frame_right,text='',width=40)
        self.qwe.grid(row=0,column=1,padx=10,pady=10)    
        self.qwe=customtkinter.CTkLabel(master=self.frame_right,text='',width=40)
        self.qwe.grid(row=0,column=2,padx=10,pady=10) 
        self.qwe=customtkinter.CTkLabel(master=self.frame_right,text='',width=40)
        self.qwe.grid(row=0,column=3,padx=10,pady=10)           

    def OutputData(self,val):
        match val:
            case 1:
                
                self.frame_right.destroy()
                self.frame_right = customtkinter.CTkScrollableFrame(master=self,corner_radius=6,height=340,width=480)
                self.frame_right.grid(row=0, column=2,padx=20,pady=20)
                self.ComBobChVal=customtkinter.CTkComboBox(master=self.frame_right,values=[" "])
                self.ComBobChVal.grid(row=1,column=0,pady=40,padx=10)    

                self.LoadDat=customtkinter.CTkButton(master=self.frame_right,text="Загрузить данные",command=lambda:self.LoadData(1))
                self.LoadDat.grid(row=1,column=1,pady=10,padx=10)

                self.Clear=customtkinter.CTkButton(master=self.frame_right,text="Отчистка",command=lambda:self.Clearr(1))
                self.Clear.grid(row=1,column=2,pady=10,padx=10)
                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Номер телефона")
                self.label.grid(row=2,column=0,pady=10,padx=10)
                self.PhoneNumb=customtkinter.CTkEntry(master=self.frame_right)
                self.PhoneNumb.grid(row=2,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Имя")
                self.label.grid(row=3,column=0,pady=10,padx=10)
                self.FirstName=customtkinter.CTkEntry(master=self.frame_right)
                self.FirstName.grid(row=3,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Фамилия")
                self.label.grid(row=4,column=0,pady=10,padx=10)
                self.LastName=customtkinter.CTkEntry(master=self.frame_right)
                self.LastName.grid(row=4,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Отчество")
                self.label.grid(row=5,column=0,pady=10,padx=10)
                self.MiddleName=customtkinter.CTkEntry(master=self.frame_right)
                self.MiddleName.grid(row=5,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Адрес")
                self.label.grid(row=6,column=0,pady=10,padx=10)
                self.Adress=customtkinter.CTkEntry(master=self.frame_right)
                self.Adress.grid(row=6,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.AddData=customtkinter.CTkButton(master=self.frame_right,text="Добавить",command=lambda:self.AdddData(1))
                self.AddData.grid(row=7,column=0,pady=10,padx=10)
                self.UpdateData=customtkinter.CTkButton(master=self.frame_right,text="Сохранить",command=lambda:self.UpdateDatap(1))
                self.UpdateData.grid(row=7,column=1,pady=10,padx=10)
                self.DelData=customtkinter.CTkButton(master=self.frame_right,text="Удалить",command=lambda:self.DellData(1))
                self.DelData.grid(row=7,column=2,pady=10,padx=10)

                ToComboBoxOne = db_adapter.SQL.GetClients()
                list = []
                for kurs in ToComboBoxOne:
                    list.append(str(kurs[0])+' '+kurs[3])
                self.ComBobChVal.configure(values = list)

                self.update()
            case 2:
                self.frame_right.destroy()
                self.frame_right = customtkinter.CTkScrollableFrame(master=self,corner_radius=6,height=340,width=480)
                self.frame_right.grid(row=0, column=2,padx=20,pady=20)
                self.ComBobChVal=customtkinter.CTkComboBox(master=self.frame_right,values=[" "])
                self.ComBobChVal.grid(row=1,column=0,pady=40,padx=10)    

                self.LoadDat=customtkinter.CTkButton(master=self.frame_right,text="Загрузить данные",command=lambda:self.LoadData(2))
                self.LoadDat.grid(row=1,column=1,pady=10,padx=10)

                self.Clear=customtkinter.CTkButton(master=self.frame_right,text="Отчистка",command=lambda:self.Clearr(2))
                self.Clear.grid(row=1,column=2,pady=10,padx=10)
                ##self.label=customtkinter.CTkLabel(master=self.frame_right,text="Id")
                ##self.label.grid(row=2,column=0,pady=10,padx=10)
                ##self.IdClient=customtkinter.CTkEntry(master=self.frame_right)
                ##self.IdClient.grid(row=2,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Процент скидки")
                self.label.grid(row=3,column=0,pady=10,padx=10)
                self.PercentOfDiscount=customtkinter.CTkEntry(master=self.frame_right)
                self.PercentOfDiscount.grid(row=3,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Кол-во туров")
                self.label.grid(row=4,column=0,pady=10,padx=10)
                self.NumberOfTours=customtkinter.CTkEntry(master=self.frame_right)
                self.NumberOfTours.grid(row=4,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.AddData=customtkinter.CTkButton(master=self.frame_right,text="Добавить",command=lambda:self.AdddData(2))
                self.AddData.grid(row=5,column=0,pady=10,padx=10)
                self.UpdateData=customtkinter.CTkButton(master=self.frame_right,text="Сохранить",command=lambda:self.UpdateDatap(2))
                self.UpdateData.grid(row=5,column=1,pady=10,padx=10)
                self.DelData=customtkinter.CTkButton(master=self.frame_right,text="Удалить",command=lambda:self.DellData(2))
                self.DelData.grid(row=5,column=2,pady=10,padx=10)

                ToComboBoxOne = db_adapter.SQL.GetDiscount()
                list = []
                for kurs in ToComboBoxOne:
                    list.append(str(kurs[0]))
                self.ComBobChVal.configure(values = list)

                self.update()
            case 3:
                self.frame_right.destroy()
                self.frame_right = customtkinter.CTkScrollableFrame(master=self,corner_radius=6,height=340,width=480)
                self.frame_right.grid(row=0, column=2,padx=20,pady=20)
                self.ComBobChVal=customtkinter.CTkComboBox(master=self.frame_right,values=[" "])
                self.ComBobChVal.grid(row=1,column=0,pady=40,padx=10)    

                self.LoadDat=customtkinter.CTkButton(master=self.frame_right,text="Загрузить данные",command=lambda:self.LoadData(3))
                self.LoadDat.grid(row=1,column=1,pady=10,padx=10)

                self.Clear=customtkinter.CTkButton(master=self.frame_right,text="Отчистка",command=lambda:self.Clearr(3))
                self.Clear.grid(row=1,column=2,pady=10,padx=10)

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="id")
                self.label.grid(row=2,column=0,pady=10,padx=10)
                self.HotelId=customtkinter.CTkEntry(master=self.frame_right)
                self.HotelId.grid(row=2,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Номер телефона")
                self.label.grid(row=3,column=0,pady=10,padx=10)
                self.HotelPhoneNumb=customtkinter.CTkEntry(master=self.frame_right)
                self.HotelPhoneNumb.grid(row=3,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Страна")
                self.label.grid(row=4,column=0,pady=10,padx=10)
                self.Country=customtkinter.CTkEntry(master=self.frame_right)
                self.Country.grid(row=4,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Адрес")
                self.label.grid(row=5,column=0,pady=10,padx=10)
                self.HotelAdress=customtkinter.CTkEntry(master=self.frame_right)
                self.HotelAdress.grid(row=5,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')   
                
                self.AddData=customtkinter.CTkButton(master=self.frame_right,text="Добавить",command=lambda:self.AdddData(3))
                self.AddData.grid(row=6,column=0,pady=10,padx=10)
                self.UpdateData=customtkinter.CTkButton(master=self.frame_right,text="Сохранить",command=lambda:self.UpdateDatap(3))
                self.UpdateData.grid(row=6,column=1,pady=10,padx=10)
                self.DelData=customtkinter.CTkButton(master=self.frame_right,text="Удалить",command=lambda:self.DellData(3))
                self.DelData.grid(row=6,column=2,pady=10,padx=10)


                ToComboBoxOne = db_adapter.SQL.GetHotel()
                list = []
                for kurs in ToComboBoxOne:
                    list.append(str(kurs[0]))
                self.ComBobChVal.configure(values = list)

                self.update()
            case 4:
                self.frame_right.destroy()
                self.frame_right = customtkinter.CTkScrollableFrame(master=self,corner_radius=6,height=340,width=480)
                self.frame_right.grid(row=0, column=2,padx=20,pady=20)
                self.ComBobChVal=customtkinter.CTkComboBox(master=self.frame_right,values=[" "])
                self.ComBobChVal.grid(row=1,column=0,pady=40,padx=10)    

                self.LoadDat=customtkinter.CTkButton(master=self.frame_right,text="Загрузить данные",command=lambda:self.LoadData(4))
                self.LoadDat.grid(row=1,column=1,pady=10,padx=10)

                self.Clear=customtkinter.CTkButton(master=self.frame_right,text="Отчистка",command=lambda:self.Clearr(4))
                self.Clear.grid(row=1,column=2,pady=10,padx=10)


                self.label=customtkinter.CTkLabel(master=self.frame_right,text="id")
                self.label.grid(row=2,column=0,pady=10,padx=10)
                self.HotelIdd=customtkinter.CTkEntry(master=self.frame_right)
                self.HotelIdd.grid(row=2,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Класс отеля")
                self.label.grid(row=3,column=0,pady=10,padx=10)
                self.ClassOfHotel=customtkinter.CTkEntry(master=self.frame_right)
                self.ClassOfHotel.grid(row=3,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="id отеля")
                self.label.grid(row=4,column=0,pady=10,padx=10)
                self.HotelId=customtkinter.CTkEntry(master=self.frame_right)
                self.HotelId.grid(row=4,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Тип климата")
                self.label.grid(row=5,column=0,pady=10,padx=10)
                self.TypeOfClimate=customtkinter.CTkEntry(master=self.frame_right)
                self.TypeOfClimate.grid(row=5,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.label=customtkinter.CTkLabel(master=self.frame_right,text="Стоимость")
                self.label.grid(row=6,column=0,pady=10,padx=10)
                self.Price=customtkinter.CTkEntry(master=self.frame_right)
                self.Price.grid(row=6,column=1,pady=10,padx=10,columnspan=2,sticky='nwe')

                self.AddData=customtkinter.CTkButton(master=self.frame_right,text="Добавить",command=lambda:self.AdddData(4))
                self.AddData.grid(row=7,column=0,pady=10,padx=10)
                self.UpdateData=customtkinter.CTkButton(master=self.frame_right,text="Сохранить",command=lambda:self.UpdateDatap(4))
                self.UpdateData.grid(row=7,column=1,pady=10,padx=10)
                self.DelData=customtkinter.CTkButton(master=self.frame_right,text="Удалить",command=lambda:self.DellData(4))
                self.DelData.grid(row=7,column=2,pady=10,padx=10)

                ToComboBoxOne = db_adapter.SQL.GetRoute()
                list = []
                for kurs in ToComboBoxOne:
                    list.append(str(kurs[0]))
                self.ComBobChVal.configure(values = list)

                self.update()
            case 5:
                self.frame_right.destroy()
                self.frame_right = customtkinter.CTkScrollableFrame(master=self,corner_radius=6,height=340,width=480)
                self.frame_right.grid(row=0, column=2,padx=20,pady=20)
                self.ComBobChVal=customtkinter.CTkComboBox(master=self.frame_right,values=[" "])
                self.ComBobChVal.grid(row=1,column=0,pady=40,padx=10)    

                self.LoadDat=customtkinter.CTkButton(master=self.frame_right,text="Загрузить данные",command=lambda:self.LoadData(5))
                self.LoadDat.grid(row=1,column=1,pady=10,padx=10)

                self.Clear=customtkinter.CTkButton(master=self.frame_right,text="Отчистка",command=lambda:self.Clearr(5))
                self.Clear.grid(row=1,column=2,pady=10,padx=10)

                                # Поле id
                self.label_id = customtkinter.CTkLabel(master=self.frame_right, text="id")
                self.label_id.grid(row=2, column=0, pady=10, padx=10)
                self.id = customtkinter.CTkEntry(master=self.frame_right)
                self.id.grid(row=2, column=1, pady=10, padx=10, columnspan=2,sticky='nwe')

                # Поле ClientId
                self.label_ClientId = customtkinter.CTkLabel(master=self.frame_right, text="id клиента")
                self.label_ClientId.grid(row=3, column=0, pady=10, padx=10)
                self.ClientId = customtkinter.CTkEntry(master=self.frame_right)
                self.ClientId.grid(row=3, column=1, pady=10, padx=10, columnspan=2,sticky='nwe')

                # Поле RouteId
                self.label_RouteId = customtkinter.CTkLabel(master=self.frame_right, text="Ид марщрут")
                self.label_RouteId.grid(row=4, column=0, pady=10, padx=10)
                self.RouteId = customtkinter.CTkEntry(master=self.frame_right)
                self.RouteId.grid(row=4, column=1, pady=10, padx=10, columnspan=2,sticky='nwe')

                # Поле DepartureDate
                self.label_DepartureDate = customtkinter.CTkLabel(master=self.frame_right, text="Дата отъезда")
                self.label_DepartureDate.grid(row=5, column=0, pady=10, padx=10)
                self.DepartureDate = customtkinter.CTkEntry(master=self.frame_right)
                self.DepartureDate.grid(row=5, column=1, pady=10, padx=10, columnspan=2,sticky='nwe')

                # Поле ArrivalDate
                self.label_ArrivalDate = customtkinter.CTkLabel(master=self.frame_right, text="Дата прибытия")
                self.label_ArrivalDate.grid(row=6, column=0, pady=10, padx=10)
                self.ArrivalDate = customtkinter.CTkEntry(master=self.frame_right)
                self.ArrivalDate.grid(row=6, column=1, pady=10, padx=10, columnspan=2,sticky='nwe')

                # Поле DiscountId
                self.label_DiscountId = customtkinter.CTkLabel(master=self.frame_right, text="Ид скидки")
                self.label_DiscountId.grid(row=7, column=0, pady=10, padx=10)
                self.DiscountId = customtkinter.CTkEntry(master=self.frame_right)
                self.DiscountId.grid(row=7, column=1, pady=10, padx=10, columnspan=2,sticky='nwe')

                # Поле NumberOfDays
                self.label_NumberOfDays = customtkinter.CTkLabel(master=self.frame_right, text="Кол-во дней")
                self.label_NumberOfDays.grid(row=8, column=0, pady=10, padx=10)
                self.NumberOfDays = customtkinter.CTkEntry(master=self.frame_right)
                self.NumberOfDays.grid(row=8, column=1, pady=10, padx=10, columnspan=2,sticky='nwe')

                self.AddData=customtkinter.CTkButton(master=self.frame_right,text="Добавить",command=lambda:self.AdddData(5))
                self.AddData.grid(row=9,column=0,pady=10,padx=10)
                self.UpdateData=customtkinter.CTkButton(master=self.frame_right,text="Сохранить",command=lambda:self.UpdateDatap(5))
                self.UpdateData.grid(row=9,column=1,pady=10,padx=10)
                self.DelData=customtkinter.CTkButton(master=self.frame_right,text="Удалить",command=lambda:self.DellData(5))
                self.DelData.grid(row=9,column=2,pady=10,padx=10)


                ToComboBoxOne = db_adapter.SQL.GetTrip()
                list = []
                for kurs in ToComboBoxOne:
                    list.append(str(kurs[0]))
                self.ComBobChVal.configure(values = list)
                
                self.update()



    def LoadData(self,val):

        match val:
            case 1:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetClientById(key)
                self.PhoneNumb .delete(0, tkinter.END)
                self.FirstName .delete(0, tkinter.END)
                self.LastName  .delete(0, tkinter.END)
                self.MiddleName.delete(0, tkinter.END)
                self.Adress    .delete(0, tkinter.END)

                self.PhoneNumb.insert(0,str(data[0][1]))
                self.FirstName.insert(0,str(data[0][2]))
                self.LastName.insert(0,str(data[0][3]))
                self.MiddleName.insert(0,str(data[0][4]))
                self.Adress.insert(0,str(data[0][5]))
                
                
            case 2:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetDiscountById(key)
                ##self.IdClient .delete(0, tkinter.END)
                self.PercentOfDiscount .delete(0, tkinter.END)
                self.NumberOfTours  .delete(0, tkinter.END)


                ##self.IdClient.insert(0,str(data[0][0]))
                self.PercentOfDiscount.insert(0,str(data[0][1]))
                self.NumberOfTours.insert(0,str(data[0][2]))
                
            case 3:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetHotelById(key)
                self.HotelId .delete(0, tkinter.END)
                self.HotelPhoneNumb .delete(0, tkinter.END)
                self.Country  .delete(0, tkinter.END)
                self.HotelAdress.delete(0, tkinter.END)


                self.HotelId.insert(0,str(data[0][0]))
                self.HotelPhoneNumb.insert(0,str(data[0][1]))
                self.Country.insert(0,str(data[0][2]))
                self.HotelAdress.insert(0,str(data[0][3]))

            case 4:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetRouteById(key)
                self.HotelIdd .delete(0, tkinter.END)
                self.ClassOfHotel .delete(0, tkinter.END)
                self.HotelId  .delete(0, tkinter.END)
                self.TypeOfClimate.delete(0, tkinter.END)
                self.Price    .delete(0, tkinter.END)

                self.HotelIdd.insert(0,str(data[0][0]))
                self.ClassOfHotel.insert(0,str(data[0][1]))
                self.HotelId.insert(0,str(data[0][2]))
                self.TypeOfClimate.insert(0,str(data[0][3]))
                self.Price.insert(0,str(data[0][4]))               
            case 5:
                 key=self.ComBobChVal.get()
                 key=key.split(' ')
                 key=key[0]
                 print(key)
                 data=[ ]
                 data=db_adapter.SQL.GetTripById(key)
                 self.id .delete(0, tkinter.END)
                 self.ClientId .delete(0, tkinter.END)
                 self.RouteId  .delete(0, tkinter.END)
                 self.DepartureDate.delete(0, tkinter.END)
                 self.ArrivalDate    .delete(0, tkinter.END)
                 self.DiscountId    .delete(0, tkinter.END)
                 self.NumberOfDays    .delete(0, tkinter.END)

                 self.id.insert(0,str(data[0][0]))
                 self.ClientId.insert(0,str(data[0][1]))
                 self.RouteId.insert(0,str(data[0][2]))
                 self.DepartureDate.insert(0,str(data[0][3]))
                 self.ArrivalDate.insert(0,str(data[0][4]))
                 self.DiscountId.insert(0,str(data[0][5]))  
                 self.NumberOfDays.insert(0,str(data[0][6]))       
        


    def DellData(self,key):           
        val=self.ComBobChVal.get()
        val=val.split(' ')
        val=val[0]
        
        match key:
            case 1:
                db_adapter.SQL.DeleteClientById(val)
                print("ura")
                self.OutputData(1)
            case 2:
                db_adapter.SQL.DeleteDiscountById(val)
                print("ura")
                self.OutputData(2)
            case 3:
                db_adapter.SQL.DeleteHotelById(val)
                print("ura")
                self.OutputData(3)
            case 4:
                db_adapter.SQL.DeleteRouteById(val)
                print("ura")
                self.OutputData(4)
            case 5:
                db_adapter.SQL.DeleteTripById(val)
                print("ura")
                self.OutputData(5)
                
    def AdddData(self,key):
        val=self.ComBobChVal.get()
        val=val.split(' ')
        val=val[0]

        match key:
            case 1:
                ph=self.PhoneNumb.get()
                fl=self.FirstName.get()
                ln=self.LastName.get()
                mn=self.MiddleName.get()
                adr=self.Adress.get()

                db_adapter.SQL.insert_client(ph,fl,ln,mn,adr)
                print("ura")
                self.OutputData(1)
            case 2:

                percofdesc=self.PercentOfDiscount.get()
                numboftour=self.NumberOfTours.get()

                db_adapter.SQL.insert_discount(percofdesc,numboftour)
                print("ura")
                self.OutputData(2)
            case 3:
                hotID=self.HotelId.get()
                hotphone=self.HotelPhoneNumb.get()
                countr=self.Country.get()
                hoteladr=self.HotelAdress.get()
                
                db_adapter.SQL.insert_hotel(hotphone,countr,hoteladr)
                print("ura")
                self.OutputData(3)
            case 4:
                hotelID=self.HotelIdd
                clasOFH=self.ClassOfHotel.get()
                HootID=self.HotelId.get()
                TypeOf=self.TypeOfClimate.get()
                Pri=self.Price.get()      
                
                db_adapter.SQL.insert_route(hotelID,clasOFH,HootID,TypeOf,Pri)
                print("ura")
                self.OutputData(4)
            case 5:
                idd=self.id.get() 
                cliID=self.ClientId.get() 
                routeId=self.RouteId.get() 
                departDate=self.DepartureDate.get() 
                arrivalDate=self.ArrivalDate.get() 
                discountId=self.DiscountId.get() 
                numbofDay=self.NumberOfDays  .get()               

                db_adapter.SQL.insert_trip(cliID,routeId,departDate,arrivalDate,discountId,numbofDay)
                print("ura")
                self.OutputData(5)
    def UpdateDatap(self,key):
        val=self.ComBobChVal.get()
        val=val.split(' ')
        val=val[0]
#1
        match key:
            case 1:
                ph=self.PhoneNumb.get()
                fl=self.FirstName.get()
                ln=self.LastName.get()
                mn=self.MiddleName.get()
                adr=self.Adress.get()

                db_adapter.SQL.update_client(val, ph, fl, ln, mn, adr)
                print("ura")
                self.OutputData(1)
            case 2:
                percofdesc=self.PercentOfDiscount.get()
                numboftour=self.NumberOfTours.get()
                db_adapter.SQL.update_discount(val, percofdesc, numboftour)
                print("ura")
                self.OutputData(2)
            case 3:
                hotphone=self.HotelPhoneNumb.get()
                countr=self.Country.get()
                hoteladr=self.HotelAdress.get()
                db_adapter.SQL.update_hotel_by_id(val,hotphone,countr,hoteladr)
                print("ura")
                self.OutputData(3)
            case 4:

                clasOFH=self.ClassOfHotel.get()
                HootID=self.HotelId.get()
                TypeOf=self.TypeOfClimate.get()
                Pri=self.Price.get()      
                db_adapter.SQL.update_route_by_id(val,clasOFH,HootID,TypeOf,Pri)
                print("ura")
                self.OutputData(4)
            case 5:
                idd=self.id.get() 
                cliID=self.ClientId.get() 
                routeId=self.RouteId.get() 
                departDate=self.DepartureDate.get() 
                arrivalDate=self.ArrivalDate.get() 
                discountId=self.DiscountId.get() 
                numbofDay=self.NumberOfDays  .get()               
                db_adapter.SQL.update_trip(val,cliID,routeId,departDate,arrivalDate,discountId,numbofDay)
                print("ura")
                self.OutputData(5)

    def Clearr(self,val):
        match val:
            case 1:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetClientById(key)
                self.PhoneNumb .delete(0, tkinter.END)
                self.FirstName .delete(0, tkinter.END)
                self.LastName  .delete(0, tkinter.END)
                self.MiddleName.delete(0, tkinter.END)
                self.Adress    .delete(0, tkinter.END)
               
            
            
            case 2:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetDiscountById(key)
                self.IdClient .delete(0, tkinter.END)
                self.PercentOfDiscount .delete(0, tkinter.END)
                self.NumberOfTours  .delete(0, tkinter.END)
                

            case 3:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetHotelById(key)
                self.HotelId .delete(0, tkinter.END)
                self.HotelPhoneNumb .delete(0, tkinter.END)
                self.Country  .delete(0, tkinter.END)
                self.HotelAdress.delete(0, tkinter.END)
                
            case 4:
                key=self.ComBobChVal.get()
                key=key.split(' ')
                key=key[0]
                print(key)
                data=[ ]
                data=db_adapter.SQL.GetRouteById(key)
                self.HotelIdd .delete(0, tkinter.END)
                self.ClassOfHotel .delete(0, tkinter.END)
                self.HotelId  .delete(0, tkinter.END)
                self.TypeOfClimate.delete(0, tkinter.END)
                self.Price    .delete(0, tkinter.END)
                 
            case 5:
                 key=self.ComBobChVal.get()
                 key=key.split(' ')
                 key=key[0]
                 print(key)
                 data=[ ]
                 data=db_adapter.SQL.GetTripById(key)
                 self.id .delete(0, tkinter.END)
                 self.ClientId .delete(0, tkinter.END)
                 self.RouteId  .delete(0, tkinter.END)
                 self.DepartureDate.delete(0, tkinter.END)
                 self.ArrivalDate    .delete(0, tkinter.END)
                 self.DiscountId    .delete(0, tkinter.END)
                 self.NumberOfDays    .delete(0, tkinter.END)
                 
        
            
         
        
    


if __name__ == "__main__":
    app = App()
    app.mainloop()