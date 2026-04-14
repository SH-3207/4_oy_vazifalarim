# class Student:
#     def __init__(self, name: str, student_id: str):
#         self.name = name
#         self.student_id = student_id
#         self.baholar = []  
#         print(f"Yangi talaba yaratildi: {name}, ID: {self.student_id}")

#     def add_grade(self, grade: int):
#         if 0 <= grade <= 100:
#             self.baholar.append(grade)
#             print(f"{grade} bahosi qo'shildi.")
#         else:
#             print(f"(ERROR) {grade} baho 0 va 100 orasida bo'lishi kerak!")

#     def calculate_average(self):
#         if not self.baholar:
#             return 0
#         return sum(self.baholar) / len(self.baholar)

#     def get_status(self):
#         avg = self.calculate_average()
#         if avg >= 90:
#             return "A'lo"
#         elif avg >= 80:
#             return "Yaxshi"
#         elif avg >= 70:
#             return "Qoniqarli"
#         else:
#             return "Qoniqarsiz"

# oquvchi = Student("Shohrux", "SH41072")
# oquvchi.add_grade(85)
# oquvchi.add_grade(95)

# print(f"O'rtacha ball: {oquvchi.calculate_average()}")
# print(f"Status: {oquvchi.get_status()}")

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Employee:
#     def __init__(self, name:str, emp_id:str, hourly_rate:float=15.0 ):
#         self.name=name
#         self.emp=emp_id
#         self.hourly=hourly_rate
#         self.working_hour=[]
    
#     def log_hours(self, hour:int):
#         if 0< hour <24 :
#              self.working_hour.append(hour)
#              return "True"
#         else :
#              return "Folse"
#     def total_hours(self):
#         return sum(self.working_hour)
#     def calculate_salary(self):
#         umumiy_soat=self.total_hours()
#         return float(umumiy_soat*20)
#     def reset_hours(self):
#         self.working_hour.clear()

# employee = Employee("Javlon", "E101", hourly_rate=20.0)
# print(employee.log_hours(8))   	
# print(employee.log_hours(10))  
# print(employee.log_hours(9))   	                            
# print(employee.log_hours(25))  	

# print(employee.total_hours())       	
# print(employee.calculate_salary())  	

# employee.reset_hours()
# print(employee.total_hours())       	
# print(employee.calculate_salary())


# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

class Playlist:
    def __init__(self, owner:str):
        self.owner=owner
        self.tracks=[]
    def add_track(self, title:str , artist:str):
        lst=[]
        lst.append(title)
        lst.append(artist)
        self.tracks.append(tuple(lst))
    def remove_last(self):
        return self.tracks.pop()
    def total_tracks(self):
        return len(self.tracks)
    def unique_tracks(self):
        royxat=[]
        for i in self.tracks:
            if i not in royxat:
                royxat.append(i)
        return royxat
    def search_by_title(self, title:str):
        for ismi , track in self.tracks:
            if title.lower()==ismi.lower():
                return f"Title: {ismi} artist: {track}"
    def filter_by_artist(self, artist:str):
        tanlanganlar=[]
        for ismi , track in self.tracks:
            if track==artist:
                tanlanganlar.append(ismi)
                tanlanganlar.append(track)
        return tanlanganlar

# Masala boyicha tekshirdm 

pl = Playlist("Muhammad")
print(pl.total_tracks()) 

pl.add_track("Yomg'irlar", "Shahzoda")
pl.add_track("Gulim", "Yulduz Usmonova")
pl.add_track("Yomg'irlar", "Shahzoda")
pl.add_track("Xayr edi", "Lola")
pl.add_track("Kel", "Ulug'bek Rahmatullayev")

print(pl.total_tracks()) 

print(pl.unique_tracks())                     

print(pl.remove_last()) 
print(pl.total_tracks()) 

print(pl.search_by_title("Yomg'irlar"))      
print(pl.filter_by_artist("Yulduz Usmonova")) 
