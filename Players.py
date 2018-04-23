from WSD2 import WSD
from WeaponsOO import OmniWeaponData
from ArmorsOO import OmniArmorData
import AttacksOO
import Skills
import Items
import random as ra
import Skillcheck as Check
import importlib
import Shielding
import HealthBar
import EnergyBar

class Element():
	def __init__(self,Type="None",Advantage="Nada",Disadvantage="Nope",Status="Nothing",Proc=0):
		self.Type=Type
		self.Advantage=Advantage
		self.Disadvantage=Disadvantage
		self.Same=Type
		self.Status=Status
		self.Proc=Proc
	@property
	def StatusProc(self):
		if ra.randint(1,100) >= 100-self.Proc:
			return("and you inflict the status",self.Status)
			print(" ")
		else:
			return("and you inflict no status at all.")
			print(" ")

Flame=Element("Flame","Earth","Water","Burning",25)
Earth=Element("Earth","Wind","Flame","Silence",25)
Wind=Element("Wind","Lightning","Earth","Clouded",25)
Lightning=Element("Lightning","Water","Wind","Shocked",25)
Water=Element("Water","Flame","Lightning","Waterlog",25)

Null=Element("None","Nada","Nope","Nothing",0)

Solar=Element("Solar","Lunar","Time","Flare",33)
Lunar=Element("Lunar","Storm","Solar","Illuminate",10)
Storm=Element("Storm","Void","Lunar","Stormscare",30)
Void=Element("Void","Time","Storm","Voidcall",30)
Time=Element("Time","Solar","Void","Timelock",20)

def Dummy(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tack!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.DummyHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.DummyENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="DummyShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice == "AT" or choice == "At" or choice == "at":
		AttacksOO.Rifle(OmniWeaponData["NormalTungstenRifle0"],"Dummy",Null,1,0,0).HATK
	elif choice == "I" or choice == "i":
		choice=input("Select an Item!\n [P]ick!\n ")
		if choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Dummy")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Dummy"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm

def Jango(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [We]apons!\n [P]ickpocket!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.JangoHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.JangoENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="JangoShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="WE" or choice == "We" or choice=="we":
		choice=input("Which weapon?\n [1] Reinforced Bone Knife!\n [2] Reinforced Bone Knife!\n [3] Tin Slicer!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n [U]nknown Skill!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knife(WSD["Jango"].Weapon1,"Jango",Solar,1.4,0,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knife(WSD["Jango"].Weapon1,"Jango",Solar,1.4,0,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knife(WSD["Jango"].Weapon1,"Jango",Solar,1.4,0,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Knife(WSD["Jango"].Weapon1,"Jango",Solar,1.4,0,0,0).TripleCombo
			elif choice == "U" or choice == "u":
				SkillUsed=eval('AttacksOO.Knife(WSD["Jango"].Weapon1,"Jango",Solar,1.4,0,0,0).'+input("Skillname is: "))
				exec(str(SkillUsed))
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n [U]nknown Skill!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knife(WSD["Jango"].Weapon2,"Jango",Solar,1.4,0,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knife(WSD["Jango"].Weapon2,"Jango",Solar,1.4,0,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knife(WSD["Jango"].Weapon2,"Jango",Solar,1.4,0,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Knife(WSD["Jango"].Weapon2,"Jango",Solar,1.4,0,0,0).TripleCombo
			elif choice == "U" or choice == "u":
				SkillUsed=eval('AttacksOO.Knife(WSD["Jango"].Weapon1,"Jango",Solar,1.4,0,0,0).'+input("Skillname is: "))
				exec(str(SkillUsed))
		elif choice == "3":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Slicer(WSD["Jango"].Weapon3,"Jango",Solar,0.5,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Slicer(WSD["Jango"].Weapon3,"Jango",Solar,0.5,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Slicer(WSD["Jango"].Weapon3,"Jango",Solar,0.5,0,0).HATK
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n [Sh]uriken!\n [Or]ange Juice!\n [P]ick!\n ")
		if choice == "SH" or choice == "Sh" or choice == "sh":
			Items.Shuriken("Jango")
		elif choice == "OR" or choice == "Or" or choice == "or":
			Items.OrangeJuice("Jango")
		elif choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Jango")))
	elif choice == "P" or choice == "p":
		AttacksOO.Pickpocket("Jango")
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Jango"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm

def Helm(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [We]apons!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.HelmHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.HelmENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="HelmShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="WE" or choice=="We" or choice == "we":
		choice=input("Which weapon?\n [1] Copper Saber!\n [2] Ivory Handbow!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n [Be]ginner's Parry!\n [Bl]azing Cutlass!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Saber(WSD["Helm"].Weapon1,"Helm",Storm,1.25,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Saber(WSD["Helm"].Weapon1,"Helm",Storm,1.25,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Saber(WSD["Helm"].Weapon1,"Helm",Storm,1.25,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Saber(WSD["Helm"].Weapon1,"Helm",Storm,1.25,0,0).TripleCombo
			elif choice == "BE" or choice == "Be" or choice == "be":
				AttacksOO.Saber(WSD["Helm"].Weapon1,"Helm",Storm,1.25,0,0).BeginnersParry
			elif choice == "BL" or choice == "Bl" or choice == "bl":
				AttacksOO.Saber(WSD["Helm"].Weapon1,"Helm",Flame,1.25,0,0).BlazingCutlass
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Play!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Handbow(WSD["Helm"].Weapon2,"Helm",Storm,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Handbow(WSD["Helm"].Weapon2,"Helm",Storm,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Handbow(WSD["Helm"].Weapon2,"Helm",Storm,1,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Handbow(WSD["Helm"].Weapon2,"Helm",Storm,1,0,0).TriplePlay
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n [HB] Herbal Bandage!\n [TJ] Tomato Juice!\n [P]ick!\n ")
		if choice == "HB" or choice == "Hb" or choice == "hb":
			Items.HerbalBandage("Helm")
		elif choice == "TJ" or choice == "Tj" or choice == "tj":
			Items.TomatoJuice("Helm")
		elif choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Helm")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Helm"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm

def Roselyn(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [W]eapons!\n [Su]pport Magic!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.RoselynHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.RoselynENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="RoselynShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="WE" or choice=="We" or choice == "we":
		choice=input("Which weapon?\n [1] Ivory Wand!\n [2] Cobalt Battlecannon!\n [3] N/A!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Fi]reball!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Wand(WSD["Roselyn"].Weapon1,"Roselyn",Flame,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Wand(WSD["Roselyn"].Weapon1,"Roselyn",Flame,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Wand(WSD["Roselyn"].Weapon1,"Roselyn",Flame,1,0,0).HATK
			elif choice == "FI" or choice == "Fi" or choice == "fi":
				AttacksOO.OffenseSpell("NormalIvoryWand0","Roselyn",Flame,1.15,0,0,0).Fireball
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Battlecannon(WSD["Roselyn"].Weapon2,"Roselyn",Flame,0.5,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Battlecannon(WSD["Roselyn"].Weapon2,"Roselyn",Flame,0.5,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Battlecannon(WSD["Roselyn"].Weapon2,"Roselyn",Flame,0.5,0,0).HATK
	elif choice == "SU" or choice == "Su" or choice == "su":
		choice=input("Select a Spell!\n [HR] Healthy Ray!\n [HG] Healthy Glow!\n [EG] Energetic Glow!\n [ER] Energetic Ray!\n ")
		if choice == "HR" or choice == "Hr" or choice == "hr":
			AttacksOO.SupportSpell(WSD["Roselyn"].Weapon1,"Roselyn").HealthyRay
		elif choice == "HG" or choice == "Hg" or choice == "hg":
			Skills.HealthyGlow("Roselyn","NormalIvoryWand0")
		elif choice == "ER" or choice == "Er" or choice == "er":
			Skills.EnergeticRay("Roselyn","NormalIvoryWand0")
		elif choice == "EG" or choice == "Eg" or choice == "eg":
			Skills.EnergeticGlow("Roselyn","NormalIvoryWand0")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n [SC] Strawberry Candy!\n [PO] Pearl Ointment!\n [SS] Soothing Salve!\n ")
		if choice == "SC" or choice == "Sc" or choice == "sc":
			Items.StrawberryCandy("Roselyn")
		elif choice == "PO" or choice == "Po" or choice == "po":
			Items.PearlOintment("Roselyn")
		elif choice == "SS" or choice == "Ss" or choice == "ss":
			Items.SoothingSalve("Roselyn")
		elif choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Roselyn")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Roselyn"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm

def Brad(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tack!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.BradHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.BradENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="BradShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Tin Bow!\n [2] Bone Knife!\n ")
		if choice == "1":
			choice=input("Select an Action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [L]ongshot!\n [C]lipshot!\n [A]rrow Item!\n [U]nknown Skill!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Bow(WSD["Brad"].Weapon1,"Brad",Lunar,1.35,25,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Bow(WSD["Brad"].Weapon1,"Brad",Lunar,1.35,25,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Bow(WSD["Brad"].Weapon1,"Brad",Lunar,1.35,25,0).HATK
			elif choice == "L" or choice == "l":
				AttacksOO.Bow(WSD["Brad"].Weapon1,"Brad",Lunar,1.35,25,0).Longshot
			elif choice == "C" or choice == "c":
				AttacksOO.Bow(WSD["Brad"].Weapon1,"Brad",Lunar,1.35,25,0).Clipshot
			elif choice == "A" or choice == "a":
				AttacksOO.Bow(WSD["Brad"].Weapon1,"Brad",Lunar,1.35,25,0).ArrowItem
			elif choice == "U" or choice == "u":
				SkillUsed=eval('AttacksOO.Bow(WSD["Brad"].Weapon1,"Brad",Lunar,1.25,25,0).'+input("Skillname is: "))
				exec(str(SkillUsed))
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
		if choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Brad")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Brad"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm
		
def Gilligan(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tack!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.GilliganHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.GilliganENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="GilliganShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Wood Claw!\n [2] Bone Knuckle!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Bl]oody Slashes!\n [Fu]ry Thrust!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Claw(WSD["Gilligan"].Weapon1,"Gilligan",Wind,1.1,0,20,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Claw(WSD["Gilligan"].Weapon1,"Gilligan",Wind,1.1,0,20,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Claw(WSD["Gilligan"].Weapon1,"Gilligan",Wind,1.1,0,20,0).HATK
			elif choice == "BL" or choice == "Bl" or choice == "bl":
				AttacksOO.Claw(WSD["Gilligan"].Weapon1,"Gilligan",Wind,1.1,0,20,0).BloodySlashes
			elif choice == "FU" or choice == "Fu" or choice == "fu":
				AttacksOO.Claw(WSD["Gilligan"].Weapon1,"Gilligan",Wind,1.1,0,20,0).FuryThrust
			elif choice == "BR" or choice == "br" or choice == "Br":
				AttacksOO.MultiWeapon(WSD["Gilligan"].Weapon1,"Gilligan",Wind,1.1,0,0).BraveLeap
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Fl]icker Jab!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knuckles(WSD["Gilligan"].Weapon2,"Gilligan",Wind,1.1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knuckles(WSD["Gilligan"].Weapon2,"Gilligan",Wind,1.1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knuckles(WSD["Gilligan"].Weapon2,"Gilligan",Wind,1.1,0,0).HATK
			elif choice == "FL" or choice == "Fl" or choice == "fl":
				AttacksOO.Knuckles(WSD["Gilligan"].Weapon2,"Gilligan",Wind,1.1,0,0).FlickerJab
			elif choice == "BR" or choice == "br" or choice == "Br":
				AttacksOO.MultiWeapon(WSD["Gilligan"].Weapon2,"Gilligan",Wind,1.1,0,0).BraveLeap
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
		if choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Gilligan")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Gilligan"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm

def Yule(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttelstats!\n [At]tack!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.YuleHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.YuleENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="YuleShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n ")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
		if choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Yule")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Yule"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm

def StClips(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tack!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.StClipsHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.StClipsENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="StClipsShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Festive Firwood Mechgun+2!\n ")
		if choice == "1":
			choice=input("[Q]uick!\n [N]ormal!\n [H]ard!\n [Dr]izzle!\n [Bl]itz!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.MechgunManiac(WSD["StClips"].Weapon1,"StClips",Earth,1,25,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.MechgunManiac(WSD["StClips"].Weapon1,"StClips",Earth,1,25,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.MechgunManiac(WSD["StClips"].Weapon1,"StClips",Earth,1,25,0).HATK
			elif choice == "DR" or choice == "dr":
				AttacksOO.MechgunManiac(WSD["StClips"].Weapon1,"StClips",Earth,1,25,0).Drizzle
			elif choice == "BL" or choice == "bl":
				AttacksOO.MechgunManiac(WSD["StClips"].Weapon1,"StClips",Earth,1,25,0).Blitz
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
		if choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("StClips")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="StClips"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm

def Reyn(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tack!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.ReynHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.ReynENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="ReynShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Stony Tungsten Greatsword!\n [2] Tungsten Spear!\n [3] Eye Laser!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [He]avy Stab!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.GreatswordGrinder(WSD["Reyn"].Weapon1,"Reyn",Void,1.5,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.GreatswordGrinder(WSD["Reyn"].Weapon1,"Reyn",Void,1.5,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.GreatswordGrinder(WSD["Reyn"].Weapon1,"Reyn",Void,1.5,0,0).HATK
			elif choice == "HE" or choice == "He" or choice == "he":
				AttacksOO.GreatswordGrinder(WSD["Reyn"].Weapon1,"Reyn",Void,1.5,0,0).HeavyStab
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]ipoint Buster!\n [Cu]two!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Polearm(WSD["Reyn"].Weapon2,"Reyn",Solar,1.35,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Polearm(WSD["Reyn"].Weapon2,"Reyn",Solar,1.35,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Polearm(WSD["Reyn"].Weapon2,"Reyn",Solar,1.35,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Polearm(WSD["Reyn"].Weapon2,"Reyn",Solar,1.35,0,0).TripointBuster
			elif choice == "CU" or choice == "Cu" or choice == "cu":
				AttacksOO.Polearm(WSD["Reyn"].Weapon2,"Reyn",Solar,1.35,0,0).Cutwo
			elif choice == "PP" or choice == "Pp" or choice == "pp":
				AttacksOO.Polearm(WSD["Reyn"].Weapon2,"Reyn",Solar,1.35,0,0).PiercingPounce
		elif choice == "3":
			AttacksOO.Weaponless("Reyn",Solar,1,0,2,0).EyeLaser
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n [Ha]nd Grenade!\n [P]ick!\n ")
		if choice == "HA" or choice == "Ha" or choice == "ha":
			Items.HandGrenade("Reyn")
		elif choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Reyn")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Reyn"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm
#Separator Line
def Lirru(Unit):
	u=Unit
	uHP=WSD[Unit].HP
	uENE=WSD[Unit].ENE
	uSTR=WSD[Unit].STR
	uSPR=WSD[Unit].SPR
	uSKL=WSD[Unit].SKL
	uABL=WSD[Unit].ABL
	uAGI=WSD[Unit].AGI
	uEVA=WSD[Unit].EVA
	uTGH=WSD[Unit].TGH
	uRES=WSD[Unit].RES
	uLCK=WSD[Unit].LCK
	uPAR=WSD[Unit].PAR
	uMAR=WSD[Unit].MAR
	uWT=WSD[Unit].ArmorWT
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tack!\n [T]oggle Shield!\n [I]nventory!\n [C]onfirm Actions!\n ")
	if choice=="ST" or choice == "St" or choice == "st":
		print("-----------------")
		print("HP:",uHP)
		print("ENE:",uENE)
		print("STR:",uSTR)
		print("SPR:",uSPR)
		print("SKL:",uSKL)
		print("ABL:",uABL)
		print("AGI:",uAGI)
		print("EVA:",uEVA)
		print("TGH:",uTGH)
		print("RES:",uRES)
		print("LCK:",uLCK)
		print("PAR:",uPAR)
		print("MAR:",uMAR)
		print("WT:",uWT)
		print("-----------------")
	elif choice == "BA" or choice == "Ba" or choice == "ba":
		print("-----------------")
		importlib.reload(HealthBar)
		print("Current HP:",HealthBar.LirruHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.LirruENE)
		print("-----------------")
	elif choice == "T" or choice == "t":
		UserShield="LirruShield"
		importlib.reload(Shielding)
		ShieldPos=getattr(Shielding,UserShield)
		if ShieldPos == "Equipped":
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=NotEquipped",file=f)
		else:
			with open('C:\\Users\\seven\\OneDrive\\Desktop\\RoPH OOP Update\\Shielding.py','a+') as f:
				importlib.reload(Shielding)
				print(UserShield+"=Equipped",file=f)
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Tungsten Saber!\n [2] Blazing Silk Glove!\n ")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n [P]ick!\n ")
		if choice == "P" or choice == "p":
			ItemUsed=eval("Items."+input("Item is: "))
			exec(str(ItemUsed("Lirru")))
	elif choice == "C" or choice == "c":
		choice=input("Select a Type!\n [A]ttackcheck!\n [S]killcheck!\n [I]temcheck!\n ")
		User="Lirru"
		UserLevel=WSD[User].Level
		if choice == "A" or choice == "a":
			Check.Attackcheck(User).Confirm
		elif choice == "S" or choice == "s":
			Check.Skillcheck(User,UserLevel).Choice
		elif choice == "I" or choice == "i":
			Check.Itemcheck(User).Confirm