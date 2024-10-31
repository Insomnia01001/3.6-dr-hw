import math 
import random
from datetime import datetime
# son  =int(input("enter number: "))
# print(pow(son,3))



# Input1= [1, 2, 3, 4, 5, 6, 7, 8]
# for i in Input1: 
#     a =random.choice(Input1)
#     print(a,end=" ")


# a  =datetime.now()
# for i in range(1,1000):
#     print(i)
# b= datetime.now()
# natja = b-a
# print(natja)
def print_calendar(month):
    months = {
        1: ("January", 31),
        2: ("February", 28),  # Yilni hisobga olmaymiz
        3: ("March", 31),
        4: ("April", 30),
        5: ("May", 31),
        6: ("June", 30),
        7: ("July", 31),
        8: ("August", 31),
        9: ("September", 30),
        10: ("October", 31),
        11: ("November", 30),
        12: ("December", 31),
    }
    
    if month in months:
        month_name, days = months[month]
        print(f"{month_name} Mon Tue Wed Thu Fri Sat Sun")
        
        # Kalendarni chop etamiz
        day = 1
        week_days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        current_day_index = 0
        
        # Birinchi haftani to'ldirish
        while day <= days:
            if current_day_index < len(week_days):
                print(f"{day:2}", end=' ')
                current_day_index += 1
                day += 1
            else:
                print()
                current_day_index = 0
        
        # Qolgan kunlarni chop etamiz
        while day <= days:
            print(f"{day:2}", end=' ')
            current_day_index += 1
            day += 1
            if current_day_index == 7:
                print()
                current_day_index = 0
        print()  # Oxirgi qatordan keyin yangi qatorda tugatamiz
    else:
        print("Iltimos, 1-12 oralig'ida son kiriting.")

# Foydalanuvchidan kiritishni so'raymiz
try:
    user_input = int(input("1-12 oralig'ida son kiriting: "))
    print_calendar(user_input)
except ValueError:
    print("Iltimos, raqam kiriting.")
