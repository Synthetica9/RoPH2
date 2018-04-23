import Attacks
import Skills
from WSD2 import WSD
import AttacksOO
import random as ra

class Element():
	def __init__(self,Type="None",Advantage="Nada",Disadvantage="Nope",Status="Nothing"):
		self.Type=Type
		self.Advantage=Advantage
		self.Disadvantage=Disadvantage
		self.Same=Type
		self.Status=Status
	@property
	def StatusProc(self):
		if ra.randint(1,100) >= 75:
			return("and you inflict the status",self.Status)
			print(" ")
		else:
			return("and you inflict no status at all.")
			print(" ")

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