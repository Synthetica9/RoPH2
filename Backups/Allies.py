import AttacksOO
import Attacks
import Skills
from WSD2 import WSD
import Items
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
			
Flame=Element("Flame","Earth","Water","Burning")
Earth=Element("Earth","Wind","Flame","Silence")
Wind=Element("Wind","Lightning","Earth","Clouded")
Lightning=Element("Lightning","Water","Wind","Shocked")
Water=Element("Water","Flame","Lightning","Waterlogged")
#Other Units
def Josephine(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [K]nife!\n [I]nventory!\n ")
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
	elif choice == "K" or choice == "k":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Knife("NormalIronKnife10","Josephine",Wind,1.3,0,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Knife("NormalIronKnife10","Josephine",Wind,1.3,0,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Knife("NormalIronKnife10","Josephine",Wind,1.3,0,0).HATK
	elif choice == "I" or choice == "i":
		choice=input("Use which Item?\n [P]otion!\n [R]ed Apple!\n ")
		if choice == "P" or choice == "p":
			Items.HealthPotion("Josephine")
		elif choice == "R" or choice == "r":
			Items.RedApple("Josephine")
#Numbereds
def Four(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [FW] The Fourth Whip!\n [I]nventory!\n ")
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
	elif choice == "FW" or choice == "fw":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Bu]rning Lash!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Earth,1,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Earth,1,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Earth,1,0).HATK
		elif choice == "BU" or choice == "Bu" or choice == "bu":
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Flame,1,0).BurningLash
def One(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n ")
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
def Six(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [At]tacks!\n [I]nventory!\n ")
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
	elif choice == "AT" or choice == "At" or choice == "at":
		choice=input("Select a Weapon!\n [1] Nancy's Flail!\n [2] Cobalt Greatsword!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Ja]wbreaker!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Flail("NormalCobaltFlail10","Six",Flame,1,0,0.15).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Flail("NormalCobaltFlail10","Six",Flame,1,0,0.15).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Flail("NormalCobaltFlail10","Six",Flame,1,0,0.15).HATK
			elif choice == "JA" or choice == "Ja" or choice == "ja":
				AttacksOO.Flail("NormalCobaltFlail10","Six",Flame,1,0,0.15).Jawbreaker
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Si]debuster!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.GreatswordGrinder("NormalCobaltGreatsword3","Six",Flame,1,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.GreatswordGrinder("NormalCobaltGreatsword3","Six",Flame,1,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.GreatswordGrinder("NormalCobaltGreatsword3","Six",Flame,1,0).HATK
			elif choice == "SI" or choice == "Si" or choice == "si":
				AttacksOO.GreatswordGrinder("NormalCobaltGreatsword3","Six",Flame,1,0).Sidebuster

def Eleven(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [TT] Tin Talis!\n [I]nventory!\n ")
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
	if choice == "TT" or choice == "tt":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ==SKILLS==\n [FB] Flame Blast!\n [WG] Water Grenade!\n [SB] Stun Bolt!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Talis("NormalTinTalis3","Eleven",Lightning,1,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Talis("NormalTinTalis3","Eleven",Lightning,1,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Talis("NormalTinTalis3","Eleven",Lightning,1,0).HATK
		elif choice == "FB" or choice == "Fb" or choice == "fb":
			Skills.OffenseSpell("NormalTinTalis3","Eleven",Flame,1,0).FlameBlast
		elif choice == "WG" or choice == "Wg" or choice == "wg":
			AttacksOO.OffenseSpell("NormalTinTalis3","Eleven",Water,1,0).WaterGrenade
		elif choice == "SB" or choice == "Sb" or choice == "sb":
			Skills.OffenseSpell("NormalTinTalis3","Eleven",Lightning,1,0).StunBolt
def Twins(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n ")
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
	elif choice == "AT" or choice == "At" or choice == "at":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [D]ig In!")
		if choice == "Q" or choice == "q":
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Earth,1.25,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Earth,1.25,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Earth,1.25,0).HATK
		elif choice == "D" or choice == "d":
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Null,1.25,0).DigIn
	
def Reintaur(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [WC] Wooden Crossbow!\n [I]nventory!\n ")
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
	elif choice == "WC" or choice == "Wc" or choice == "wc":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Ho]lepunch!\n [Ne]edleround!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Crossbow("NormalWoodCrossbow5","Reintaur",Water,1,20,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Crossbow("NormalWoodCrossbow5","Reintaur",Water,1,20,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Crossbow("NormalWoodCrossbow5","Reintaur",Water,1,20,0).HATK
		elif choice == "NE" or choice == "Ne" or choice == "ne":
			AttacksOO.Crossbow("NormalWoodCrossbow5","Reintaur",Water,1,20,0).Needleround
		elif choice == "HE" or choice == "He" or choice == "he":
			AttacksOO.Crossbow("NormalWoodCrossbow5","Reintaur",Water,1,20,0).Holepunch

def Wander(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [Su]pport Magic!\n [I]nventory!\n ")
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
	elif choice == "At" or choice == "at" or choice == "AT":
		choice=input("Which weapon?\n [1] Copper Rod!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Rod("NormalCopperRod0","Wander",Flame,0.5,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Rod("NormalCopperRod0","Wander",Flame,0.5,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Rod("NormalCopperRod0","Wander",Flame,0.5,0).HATK
	elif choice == "SU" or choice == "Su" or choice == "su":
		choice=input("Select a Support Spell!\n [HR] Healthy Ray!\n [HG] Healthy Glow!\n [RR] torative Ray!\n ")
		if choice == "HR" or choice == "Hr" or choice == "hr":
			AttacksOO.SupportSpell("NormalCopperRod0","Wander").HealthyRay
		elif choice == "HG" or choice == "Hg" or choice == "hg":
			AttacksOO.SupportSpell("NormalCopperRod0","Wander").HealthyGlow
		elif choice == "RR" or choice == "Rr" or choice == "rr":
			Skills.RestorativeRay("Wander","NormalCopperRod0")

def Janet(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n ")
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
	elif choice == "AT" or choice == "At" or choice == "at":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Ho]lepunch!\n [Ne]edleround!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25).HATK
		elif choice == "NE" or choice == "Ne" or choice == "ne":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25).Needleround
		elif choice == "HO" or choice == "Ho" or choice == "ho":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25).Holepunch