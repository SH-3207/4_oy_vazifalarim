from colorama import Fore, Back, Style, init
import time
import sys
import random

init(autoreset=True)

class MenuItem:
    def __init__(self, nomi, turi):
        self.nomi = nomi
        self.turi = turi
        self.miqdor = 6
        
    def serve(self, soni):
        if self.miqdor >= soni:
            text = f"- {self.nomi} uchun buyurtma qabul qilindi: "
            for i in text:
                sys.stdout.write(Fore.YELLOW + i)
                sys.stdout.flush()
                time.sleep(0.04)
            self.miqdor -= soni
            print()
            
            matn = "- Tayyorlanmoqda..."
            for i in matn:
                sys.stdout.write(Fore.MAGENTA + i)
                sys.stdout.flush()
                time.sleep(0.05)
            
            print(Fore.GREEN + Style.BRIGHT + f"\n✅ {soni} ta {self.nomi} tayyor! Yoqimli ishtaha!")
            time.sleep(0.5)
            
        elif self.miqdor <= 0:
            print(Fore.RED + Style.BRIGHT + f"\n❌ Mahsulot tugadi! Ombor to'ldirilmoqda...")
            self.restock()
        else:
            print(Fore.RED + f"⚠️ Kechirasiz, atigi {self.miqdor} ta {self.nomi} qolgan.")
            time.sleep(0.5)

    def restock(self):
        if self.turi.lower() == "ichimlik":
            self.miqdor = 20
        elif self.turi.lower() == "shirinlik":
            self.miqdor = 10
        print(Fore.CYAN + f"🔄 Ombor to'ldirildi! Yangi miqdor: {self.miqdor}")

class Customer:
    def __init__(self, name, balance, item_obj):
        self.name = name
        self.__balance = balance
        self.item = item_obj
        self.total_bought = 0
        
        self.variants = {
            "kichik": 10,
            "o'rta": 20,
            "katta": 30,
            "": 0 
        }

    def buy(self):
        size = random.choice(list(self.variants.keys()))
        price = self.variants[size]

        print(Fore.BLUE + Style.BRIGHT + f"\n👤 {self.name} buyurtma bermoqchi: " + Fore.WHITE + f"'{size}'")

        if size == "":
            print(Fore.LIGHTBLACK_EX + f"🤷 {self.name} fikridan qaytdi.")
            return True

        if self.__balance >= price:
            if self.item.miqdor > 0:
                self.item.serve(1)
                self.__balance -= price
                self.total_bought += 1
                print(Fore.CYAN + f"💰 Natija: {self.name} {size} oldi. Hamyonda: {self.__balance} qoldi.")
                return True
            else:
                self.item.serve(1) 
                return True
        else:
            print(Fore.RED + Back.WHITE + f"🛑 {self.name}ning puli yetmadi! (Balans: {self.__balance})")
            return False



print(Fore.MAGENTA + Style.BRIGHT + "_"*45)
print(Fore.CYAN + Style.BRIGHT + "   ☕ KAFE VA MIJOZLAR SIMULYATSIYASI 🍰")
print(Fore.MAGENTA + Style.BRIGHT + "_"*45 + "\n")

nom = input(Fore.LIGHTYELLOW_EX + "Sotiladigan mahsulot nomi (masalan, Kofe): ")
tur = input(Fore.LIGHTYELLOW_EX + "Turi (ichimlik/shirinlik): ")
mahsulot = MenuItem(nomi=nom, turi=tur)


mijozlar = []
try:
    sanoq_input = input(Fore.LIGHTBLUE_EX + "\nNechta mijoz ishtirok etadi? ")
    sanoq = int(sanoq_input)
    
    for i in range(sanoq):
        print(Fore.WHITE + f"\n--- {i+1}-mijoz ma'lumotlari ---")
        ismini = input(Fore.YELLOW + f"Ismi: ")
        balans = int(input(Fore.YELLOW + f"Balansi (pul miqdori): "))
        mijozlar.append(Customer(ismini, balans, mahsulot))
except ValueError:
    print(Fore.RED + "\n❌ Xato kiritish! Dastur 2 ta standart mijoz bilan davom etadi.")
    mijozlar = [Customer("Ali", 100, mahsulot), Customer("Vali", 100, mahsulot)]

print(Fore.GREEN + Style.BRIGHT + "\n🚀 Simulyatsiya boshlanmoqda...")
time.sleep(1)

barcha_mijozlar = mijozlar.copy()

while len(mijozlar) > 0:
    faol_mijoz = random.choice(mijozlar)
    yashayaptimi = faol_mijoz.buy()
    
    if not yashayaptimi:
        print(Fore.RED + Style.BRIGHT + f"\n❕ {faol_mijoz.name} hamyoni bo'shadi va kafeni tark etdi.")
        mijozlar.remove(faol_mijoz)
    
    if len(mijozlar) > 0:
        davom = input(Fore.BLACK + Back.CYAN + "\n[Enter] - Davom etish | (exit) - Tugatish: ")
        if davom.lower() == "exit":
            print(Fore.RED + "\nSimulyatsiya foydalanuvchi tomonidan to'xtatildi.")
            break
    time.sleep(0.3)

print("\n" + Fore.GREEN + "="*45)
print(Fore.WHITE + Back.GREEN + Style.BRIGHT + "           YAKUNIY STATISTIKA            ")
print(Fore.GREEN + "="*45)

for m in barcha_mijozlar:
    rang = Fore.LIGHTGREEN_EX if m.total_bought > 0 else Fore.LIGHTRED_EX
    print(rang + f"● {m.name:10} | Xaridlar soni: {m.total_bought} ta")

golib = max(barcha_mijozlar, key=lambda x: x.total_bought)
if golib.total_bought > 0:
    print(Fore.YELLOW + Style.BRIGHT + f"\n🏆 ENG FAOL MIJOZ: {golib.name}!")
else:
    print(Fore.RED + "\nHech kim xarid qila olmadi.")

print(Fore.GREEN + "="*45)