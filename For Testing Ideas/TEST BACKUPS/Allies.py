import AttacksOO
import Attacks
import Skills
from WSD2 import WSD
import Items
import random as ra
import importlib
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
Lunar=Element("Lunar","Storm","Solar","Calm",50)
Storm=Element("Storm","Void","Lunar","Stormscare",30)
Void=Element("Void","Time","Storm","Voidcall",30)
Time=Element("Time","Solar","Void","Timelock",20)
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
			AttacksOO.Knife(WSD["Josephine"].Weapon1,"Josephine",Wind,1.3,0,0,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Knife(WSD["Josephine"].Weapon1,"Josephine",Wind,1.3,0,0,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Knife(WSD["Josephine"].Weapon1,"Josephine",Wind,1.3,0,0,0).HATK
	elif choice == "I" or choice == "i":
		choice=input("Use which Item?\n [P]otion!\n [R]ed Apple!\n ")
		if choice == "P" or choice == "p":
			Items.HealthPotion("Josephine")
		elif choice == "R" or choice == "r":
			Items.RedApple("Josephine")
#Numbereds
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
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tack!\n [I]nventory!\n ")
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
		print("Current HP:",HealthBar.OneHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.OneENE)
		print("-----------------")
	if choice == "AT" or choice == "At" or choice == "at":
		choice=input("Select a Weapon!\n [1] Bronze Battlestaff!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [F]our!\n [P]ogo Pounce!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Battlestaff2(WSD["One"].Weapon1,"One",Void,1.3,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Battlestaff2(WSD["One"].Weapon1,"One",Void,1.3,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Battlestaff2(WSD["One"].Weapon1,"One",Void,1.3,0,0).HATK
			elif choice == "F" or choice == "f":
				AttacksOO.Battlestaff2(WSD["One"].Weapon1,"One",Void,1.3,0,0).Four
			elif choice == "P" or choice == "p":
				AttacksOO.Battlestaff2(WSD["One"].Weapon1,"One",Void,1.3,0,0).PogoPounce

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
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Earth,1.25,0,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Earth,1.25,0,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Earth,1.25,0,0).HATK
		elif choice == "D" or choice == "d":
			AttacksOO.Knuckles("NormalBoneKnuckles4","Two",Null,1.25,0,0).DigIn

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
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Earth,1,0,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Earth,1,0,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Earth,1,0,0).HATK
		elif choice == "BU" or choice == "Bu" or choice == "bu":
			AttacksOO.Whip("ReinforcedBronzeWhip10","Four",Flame,1,0,0).BurningLash

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
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [At]tacks!\n [I]nventory!\n ")
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
		print("Current HP:",HealthBar.SixHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.SixENE)
		print("-----------------")
	elif choice == "AT" or choice == "At" or choice == "at":
		choice=input("Select a Weapon!\n [1] Nancy's Flail!\n [2] Cobalt Greatsword!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Ja]wbreaker!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Flail(WSD["Six"].Weapon1,"Six",Flame,1,0,0.15,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Flail(WSD["Six"].Weapon1,"Six",Flame,1,0,0.15,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Flail(WSD["Six"].Weapon1,"Six",Flame,1,0,0.15,0).HATK
			elif choice == "JA" or choice == "Ja" or choice == "ja":
				AttacksOO.Flail(WSD["Six"].Weapon1,"Six",Flame,1,0,0.15,0).Jawbreaker
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Si]debuster!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.GreatswordGrinder(WSD["Six"].Weapon2,"Six",Flame,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.GreatswordGrinder(WSD["Six"].Weapon2,"Six",Flame,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.GreatswordGrinder(WSD["Six"].Weapon2,"Six",Flame,1,0,0).HATK
			elif choice == "SI" or choice == "Si" or choice == "si":
				AttacksOO.GreatswordGrinder(WSD["Six"].Weapon2,"Six",Flame,1,0,0).Sidebuster

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
			AttacksOO.Talis("NormalTinTalis3","Eleven",Lightning,1,0,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Talis("NormalTinTalis3","Eleven",Lightning,1,0,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Talis("NormalTinTalis3","Eleven",Lightning,1,0,0).HATK
		elif choice == "FB" or choice == "Fb" or choice == "fb":
			Skills.OffenseSpell("NormalTinTalis3","Eleven",Flame,1,0,0).FlameBlast
		elif choice == "WG" or choice == "Wg" or choice == "wg":
			AttacksOO.OffenseSpell("NormalTinTalis3","Eleven",Water,1,0,0).WaterGrenade
		elif choice == "SB" or choice == "Sb" or choice == "sb":
			Skills.OffenseSpell("NormalTinTalis3","Eleven",Lightning,1,0,0).StunBolt

def Renfield(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [We]apons!\n [I]nventory!\n ")
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
		print("Current HP:",HealthBar.RenfieldHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.RenfieldENE)
		print("-----------------")
	elif choice == "WE" or choice == "We" or choice == "we":
		choice=input("Select a Weapon!\n [1] Bare Hands!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knuckles(WSD["Renfield"].Weapon1,"Renfield",Solar,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knuckles(WSD["Renfield"].Weapon1,"Renfield",Earth,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knuckles(WSD["Renfield"].Weapon1,"Renfield",Earth,1,0,0).HATK
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
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [We]apons!\n [I]nventory!\n ")
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
		print("Current HP:",HealthBar.ReintaurHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.ReintaurENE)
		print("-----------------")
	elif choice == "WE" or choice == "We" or choice == "we":
		choice=input("Select a Weapon!\n [1] Wooden Crossbow!\n [2] Wooden Warhammer!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Ho]lepunch!\n [Ne]edleround!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Crossbow(WSD["Reintaur"].Weapon1,"Reintaur",Water,1,20,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Crossbow(WSD["Reintaur"].Weapon1,"Reintaur",Water,1,20,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Crossbow(WSD["Reintaur"].Weapon1,"Reintaur",Water,1,20,0,0).HATK
			elif choice == "NE" or choice == "Ne" or choice == "ne":
				AttacksOO.Crossbow(WSD["Reintaur"].Weapon1,"Reintaur",Water,1,20,0,0).Needleround
			elif choice == "HO" or choice == "Ho" or choice == "ho":
				AttacksOO.Crossbow(WSD["Reintaur"].Weapon1,"Reintaur",Water,1,20,0,0).Holepunch
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Warhammer(WSD["Reintaur"].Weapon2,"Reintaur",Water,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Warhammer(WSD["Reintaur"].Weapon2,"Reintaur",Water,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Warhammer(WSD["Reintaur"].Weapon2,"Reintaur",Water,1,0,0).HATK

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
				AttacksOO.Rod("NormalCopperRod0","Wander",Flame,0.5,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Rod("NormalCopperRod0","Wander",Flame,0.5,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Rod("NormalCopperRod0","Wander",Flame,0.5,0,0).HATK
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
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25,0).HATK
		elif choice == "NE" or choice == "Ne" or choice == "ne":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25,0).Needleround
		elif choice == "HO" or choice == "Ho" or choice == "ho":
			AttacksOO.Crossbow("ElectricTinCrossbow2","Janet",Lightning,1.15,20,0.25,0).Holepunch