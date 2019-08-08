from __future__ import print_function
from random import randint
from random import shuffle
from faker import Faker

fake = Faker()

names = ["Arnon Levy", "Kate Levy", "Don Moore", fake.name(), fake.name(), fake.name(), fake.name(), fake.name(), fake.name()]
roles = ["Chairman", "CEO", "VP of Finance", "CTO", "COO", "SVP of Sales", "Managing Director, APAC", "Managing Director, EMEA", "VP of Support"]

print("GuestTek Interactive Entertainment Ltd, the global leader in providing management reorg announcements, is pleased to announce its new team structure.")

# Reorg time!
shuffle(names)

neworg = {key:value for key, value in zip(names, roles)}

# Tell the people what they've won!

for name, pos in neworg.items():
	print(name + " is the new " + pos + ".")

print("GuestTek would like to congratulate the new team and wishes them well in the coming weeks until the next reorg.")

