from colorama import Fore, Back, Style, init

init(autoreset=True)

import pymysql

# class MySQL:
#     def  __init__(self):
#         self.connectDB()
#         self.CreateDb()
#         self.CreateCompanyTB()
#     def connectDB(self):
#         self.db = pymysql.connect(
#             host= "localhost",
#             user="root",
#             password="1234"
#         )
#         self.c = self.db.cursor()
#     def CreateDb(self):
#         self.c.execute("Create database if not exists company_db")
#         self.c.execute("USE company_db")
#     def CreateCompanyTB(self):
#         self.c.execute(f'''Create table if not exists company(name varchar(50),
#                  location varchar(50), capital int, employees_count int,
#                  establishedAt int, monthly_expenses int)''')
#     def insertCompany(self, name, location, capital, emp, est, monthly):
#         self.c.execute(f'''insert into company 
#                     values("{name}", "{location}", {capital}, {emp}, {est}, {monthly})''')
#         self.db.commit()
#     def FirstQuary(self):
#         self.c.execute("Select * From company order by name")
#         natija=self.c.fetchall()
#         return natija 
#     def SecondQuary(self):
#         self.c.execute("select * from company order by capital desc")
#         return self.c.fetchall()
#     def ThirdQuary(self):
#         self.c.execute("select * from company order by employees_count limit 1")
#         return self.c.fetchall()
#     def FourthQuary(self):
#         self.c.execute("select * from company where location = 'Toshkent'")
#         return self.c.fetchall()
#     def FifthQuary(self):
#         self.c.execute("select location as Manzil, count(name)as Kompaniyalar from company group by location")
#         return self.c.fetchall()
#     def SixthQuary(self):
#         self.c.execute(" SELECT name AS Company,establishedAt AS Year,(YEAR(CURDATE()) - establishedAt) * 12 * monthly_expenses AS 'Jami Harajat' FROM company")
#         return self.c.fetchall()

# m1 = MySQL()
# # for i in range(5):
# #     m1.insertCompany(input("Name: "), 
# #     input("location: "), int(input("Capital: ")),
# #      int(input("Employees_count: ")), int(input("EstablishedAT: ")), int(input("Monthly: ")))

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 1 Masala rang bilan ishlaganm uchun str qildim ! :
# print(Fore.YELLOW+"_1-Masala: " ,end="\n\n")

# for i in m1.FirstQuary():
#     print(Fore.GREEN+str(i))


# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 2 Masala:
# print(Fore.RED+Style.BRIGHT+" - "*20)
# print(Fore.YELLOW+"_2-Masala: " ,end="\n\n")

# for i in m1.SecondQuary():
#     print(Fore.GREEN+str(i))

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 3 Masala:
# print(Fore.RED+Style.BRIGHT+" - "*20)
# print(Fore.YELLOW+"_3-Masala: " ,end="\n\n")

# for i in m1.ThirdQuary():
#     print(Fore.GREEN+str(i))

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 4 Masala:
# print(Fore.RED+Style.BRIGHT+" - "*20)
# print(Fore.YELLOW+"_4-Masala: " ,end="\n\n")

# for i in m1.FourthQuary():
#     print(Fore.GREEN+str(i))

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 5 Masala:
# print(Fore.RED+Style.BRIGHT+" - "*20)
# print(Fore.YELLOW+"_5-Masala: " ,end="\n\n")

# for i in m1.FifthQuary():
#     print(Fore.GREEN+str(i))

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 6 Masala:
# print(Fore.RED+Style.BRIGHT+" - "*20)
# print(Fore.YELLOW+"_6-Masala: " ,end="\n\n")

# for i in m1.SixthQuary():
#     print(Fore.GREEN+str(i))

# > > > > > > > >  > > > > >  > > > > > > > > > > > > > >  > > > >> > > > >  >>  

# > > > > > > > >  > > > > >  > > > > > > > > > > > > > >  > > > >> > > > >  >>  

# > > > > > > > >  > > > > >  > > > > > > > > > > > > > >  > > > >> > > > >  >>  


for i in range(50):
 print(Fore.GREEN+Style.BRIGHT+">" ,end="")
 print(Fore.RED+Style.BRIGHT+">",end="")

print(Fore.BLUE+ "\n2-Topshirq: ", end="\n\n")

class MySQL1:
    def  __init__(self):
        self.connectDB()
        self.CreateDb()
        self.CreateRestoranTB()
    def connectDB(self):
        self.db = pymysql.connect(
            host= "localhost",
            user="root",
            password="1234"
        )
        self.c = self.db.cursor()
    def CreateDb(self):
        self.c.execute("Create database if not exists restoranlar_db")
        self.c.execute("USE restoranlar_db")
    def CreateRestoranTB(self):
        self.c.execute(f'''Create table if not exists restaran(id int auto_increment primary key,
                       name varchar(100),
                       address varchar(170),
                       maxFoodPrice int,
                       minFoodPrice int,
                       employeesCount int,
                       experience int)''')
    def insertRestaran(self, name, address, maxFoodPrice, minFoodPrice, employeesCount, experience):
        self.c.execute(f'''insert into restaran(name, address, maxFoodPrice, minFoodPrice, 
                       employeesCount, experience) values("{name}", "{address}", {maxFoodPrice}, {minFoodPrice},
                      {employeesCount}, {experience})''')
        self.db.commit()
    def FirstQuary(self):
        self.c.execute("select name as Restoranlar from restaran where name like 'M%r' ")
        return self.c.fetchall()
    
    def SecondQuary(self):
        self.c.execute("select name as Restoranlar, minFoodPrice as Price from restaran order by minFoodPrice limit 3")
        return self.c.fetchall()
    
    def ThirdQuary(self):
        self.c.execute("select name as Restaranlar from restaran order by experience desc limit 4")
        return self.c.fetchall()

m1=MySQL1()

# for i in range(10):
#     m1.insertRestaran(input("Name- "), input("Address- "), int(input("MaxPrice- ")),
#                      int(input("MinPrice- ")),
#                      int(input("employeesCount- ")), int(input("Exeperience- ")) )   

# # 1 Masala rang bilan ishlaganm uchun str qildim ! :

print(Fore.YELLOW+"_1-Masala: " ,end="\n\n")

for i in m1.FirstQuary():
    print(Fore.GREEN+str(i))

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# 2 Masala:
print(Fore.RED+Style.BRIGHT+" - "*20)
print(Fore.YELLOW+"_2-Masala: " ,end="\n\n")

for i in m1.SecondQuary():
    print(Fore.GREEN+str(i))

# # >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# # 3 Masala:
print(Fore.RED+Style.BRIGHT+" - "*20)
print(Fore.YELLOW+"_3-Masala: " ,end="\n\n")

for i in m1.ThirdQuary():
    print(Fore.GREEN+str(i))








