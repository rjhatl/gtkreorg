from __future__ import print_function
from random import randint
from random import shuffle
from datetime import date
from faker import Faker


fake = Faker()
today = str(date.today())

names = ["Arnon Levy", "Kate Levy", "Don Moore", fake.name(
), fake.name(), fake.name(), fake.name(), fake.name(), fake.name(),
    fake.name()]
roles = ["Chairman", "CEO", "VP of Finance", "CTO", "COO", "SVP of Sales",
    "Managing Director, APAC", "Managing Director, EMEA", "VP of Support",
    "Secretary of Balloon Doggies"]

print("")
print("Breaking news report!")
print("")
print("")
print("\033[1m" + "GuestTek Appoints New Management Team" + "\033[0m")
print("")
print("\033[1m" + "Calgary, Alberta - " + today + "\033[0m  " +
"GuestTek Interactive Entertainment Ltd, the \n\
 global leader in providing management reorg announcements, is pleased to \n\
 announce its new senior management team:\n ")

# Reorg time!
shuffle(names)

neworg = {key: value for key, value in zip(names, roles)}

# Tell the people what they've won!
for name, pos in neworg.items():
    print("\033[1m" + name + "\033[0m" + " is the new " + pos + ".")

# Who do the balloon doggies demand as their leader?
secbd = list(neworg.keys())[-1]

print("")
print(f" {secbd}, the new Secretary of Balloon Doggies, said they are very\n\
 pleased to serve in this new role, and are very humbled that the\n\
 balloon doggies demanded it so vocally.")
print("")
print(" GuestTek would like to congratulate the new team and wishes them well\n\
 in the coming weeks leading up to the next reorg. We would also like to\n\
 thank the previous employees who held these roles and wish them the best\n\
 of luck in their new endeavors, or worst case, we'll see them back here\n\
 again in a future reorg.")
