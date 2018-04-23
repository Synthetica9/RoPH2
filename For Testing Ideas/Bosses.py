import Skills
from WSD2 import WSD
import AttacksOO
import random as ra
import importlib

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

def Lumburn(Monster):
	u=Monster
	uHP=WSD[Monster].HP
	uENE=WSD[Monster].ENE
	uSTR=WSD[Monster].STR
	uSPR=WSD[Monster].SPR
	uSKL=WSD[Monster].SKL
	uABL=WSD[Monster].ABL
	uAGI=WSD[Monster].AGI
	uEVA=WSD[Monster].EVA
	uTGH=WSD[Monster].TGH
	uRES=WSD[Monster].RES
	uLCK=WSD[Monster].LCK
	uPAR=WSD[Monster].PAR
	uMAR=WSD[Monster].MAR
	uWT=WSD[Monster].WT
	choice = input("Select a thing!\n [S]tat check!\n [BA] Breath Attack!\n [FB] Flame Blast!\n [F] Fireball!\n ")
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
	elif choice == "BA" or choice == "ba":
		AttacksOO.Weaponless("Lumburn",Flame,1,25,5).BreathAttack
	elif choice == "FB" or choice == "fb":
		AttacksOO.OffenseSpell("NormalIvoryRod2","Lumburn",Flame,1,0).FlameBlast
	elif choice == "BS" or choice == "bs":
		AttacksOO.Weaponless("Lumburn",Flame,1,25,5).Bodyslam
	elif choice == "F" or choice == "f":
		AttacksOO.OffenseSpell("NormalIvoryRod2","Lumburn",Flame,1,0).Fireball