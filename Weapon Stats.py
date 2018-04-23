from WeaponsOO import OmniWeaponData
running = 1
while running == 1:
	Weapon=input("Weapon is: ")
	print("================================")
	print("PDMG is: ", OmniWeaponData[Weapon][0])
	print("MDMG is: ", OmniWeaponData[Weapon][1])
	print("ACC is: ", OmniWeaponData[Weapon][2])
	print("WT is: ", OmniWeaponData[Weapon][3])
	print("Buy Price is: ", OmniWeaponData[Weapon][4])
	print("Sell Price is: ", OmniWeaponData[Weapon][5])
	print("================================")