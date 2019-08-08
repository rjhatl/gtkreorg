from __future__ import print_function
from random import randint
from random import shuffle
from datetime import date
from faker import Faker

fake = Faker()
today = str(date.today())

names = ["Arnon Levy", "Kate Levy", "Don Moore", fake.name(
), fake.name(), fake.name(), fake.name(), fake.name(), fake.name()]
roles = ["Chairman", "CEO", "VP of Finance", "CTO", "COO", "SVP of Sales",
         "Managing Director, APAC", "Managing Director, EMEA", "VP of Support"]

print("")
print("Breaking news report!")
print("")
print("")
print("\033[1m" + "GuestTek Appoints New Management Team" + "\033[0m")
print("")
print("\033[1m" + "Calgary, Alberta - " + today + "\033[0m  " +
"GuestTek Interactive Entertainment Ltd, the global leader in providing \
management reorg announcements, is pleased to announce its new team \
structure effective immediately: ")
print("")

# Reorg time!
shuffle(names)

neworg = {key: value for key, value in zip(names, roles)}

# Tell the people what they've won!

for name, pos in neworg.items():
    print("\033[1m" + name + "\033[0m" + " is the new " + pos + ".")

print("")
print("GuestTek would like to congratulate the new team and wishes \
them well in the coming weeks until the next reorg. We would also \
like to thank the previous employees who held these roles and \
wish them the best of luck in their new endeavors, or worst case, \
we'll see them back here again in a future reorg.")
