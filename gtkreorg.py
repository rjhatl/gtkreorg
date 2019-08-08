from random import randint
from random import shuffle
from faker import Faker

fake = Faker()

constants = ["Arnon Levy", "Kate Levy", "Don Moore", fake.name(), fake.name(), fake.name(), fake.name(), fake.name()]
roles = ["Chairman", "CEO", "VP of Finance", "CTO", "COO", "SVP of Sales", "Managing Director, APAC", "Managing Director, EMEA"]

print("GuestTek Interactive Entertainment Ltd, the global leader in providing management reorg announcements, is pleased to announce its new team structure.")

# Reorg time!
shuffle(constants)

neworg = {key:value for key, value in zip(constants, roles)}

# Tell the people what they've won!

for name, pos in neworg.items():
	print(name + " is the new " + pos + ".")

print("GuestTek would like to congratulate the new team and wishes them well in the coming weeks until the next reorg.")

