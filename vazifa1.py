# class kitob:
#     def __init__(self, nomi, mualifi, narxi, nashryoti ):
#         self.nomi=nomi
#         self.mualifi=mualifi
#         self.narxi=narxi
#         self.nashryoti=nashryoti
#     def chiqarish(self):
#         print(f"Nomi: {self.nomi}, Nashriyot: {self.nashryoti}, Narxi: {self.narxi}")
 
 
# kitoblar = [
#     kitob("O'tkan kunlar", "A.Qodiriy", 50000, "Akademnashr"),
#     kitob("Sariq devni minib", "X.To'xtaboyev", 40000, "G'afur G'ulom"),
#     kitob("Yulduzli tunlar", "P.Qodirov", 65000, "Hilol"),
#     kitob("Daftar hoshiyasidagi bitiklar", "O'.Hoshimov", 35000, "Sharq"),
#     kitob("Shaytanat", "T.Malik", 80000, "Adolat")
# ]

# print("Nashriyoti 'A' dan 'H' gacha bo'lgan kitoblar:")
# for k in kitoblar:
#     birinchi_harf = k.nashryoti[0].upper()
#     if 'A' <= birinchi_harf <= 'H':
#         k.chiqarish()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# class Kompyuter:
#     def __init__(self, nomi, rami, narxi, protsessori):
#         self.nomi = nomi
#         self.rami = rami
#         self.narxi = narxi
#         self.protsessori = protsessori

#     def chiqarish(self):
#         print(f"Model: {self.nomi}, RAM: {self.rami}GB, Narxi: {self.narxi}")

# komplar = [
#     Kompyuter("HP Victus", 16, 800, "i5"),
#     Kompyuter("Acer Aspire", 8, 500, "i3"),
#     Kompyuter("MacBook Air", 8, 1000, "M1"),
#     Kompyuter("Asus Rog", 32, 1500, "i9")
# ]

# print("\nRAMi 4 dan katta va 16 dan kichik kompyuterlar:")
# for comp in komplar:
#     if 4 < comp.rami < 16:
#         comp.chiqarish()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


# class User:
#     def __init__(self, ism, foydalanuvchi_ismi, email, yosh=None, shahar=None):
#         self.ism = ism
#         self.username = foydalanuvchi_ismi
#         self.email = email
#         self.yosh = yosh
#         self.shahar = shahar

#     def get_info(self):
#         """Foydalanuvchi haqida ma'lumotni chiroyli ko'rinishda chiqarish"""
#         info = (f"Foydalanuvchi: {self.username}, ismi: {self.ism}, "
#                 f"email: {self.email}")
#         if self.yosh:
#             info += f", yoshi: {self.yosh}da"
#         if self.shahar:
#             info += f", shahri: {self.shahar}"
#         return info

#     def get_email(self):
#         """Faqat foydalanuvchi emailini qaytarish"""
#         return f"{self.ism}ning emaili: {self.email}"


# user1 = User("Alijon Valiyev", "alijon1994", "alijon1994@gmail.com")
# user2 = User("Jasur Olimov", "jasur_pro", "jolimov@outlook.com", 28, "Buxoro")

# print(user1.get_info())
# print(user2.get_info())
# print(user1.get_email())



