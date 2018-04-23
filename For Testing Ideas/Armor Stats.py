from ArmorsOO import OmniArmorData
running = 1
while running == 1:
	Armor=input("Armor Piece is: ")
	print("================================")
	print("PDEF is: ", OmniArmorData[Armor][0])
	print("MDEF is: ", OmniArmorData[Armor][1])
	print("WT is: ", OmniArmorData[Armor][2])
	print("Buy Price is: ", OmniArmorData[Armor][3])
	print("Sell Price is: ", OmniArmorData[Armor][4])
	print("================================")