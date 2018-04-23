from WSD2 import WSD
from WeaponsOO import OmniWeaponData
from ArmorsOO import OmniArmorData
import AttacksOO
import Skills
import Items
import random as ra
import Skillcheck as Check
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
			return "and you inflict the status",self.Status
		else:
			return "and you inflict no status at all."

Flame=Element("Flame","Earth","Water","Burning")
Earth=Element("Earth","Wind","Flame","Silence")
Wind=Element("Wind","Lightning","Earth","Clouded")
Lightning=Element("Lightning","Water","Wind","Shocked")
Water=Element("Water","Flame","Lightning","Waterlogged")
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [P]ickpocket!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Reinforced Bone Knife!\n [2] Reinforced Bone Knife!\n ")
		if choice == "1" or choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knife("ReinforcedBoneKnife0","Jango",Flame,1.3,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knife("ReinforcedBoneKnife0","Jango",Flame,1.3,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knife("ReinforcedBoneKnife0","Jango",Flame,1.3,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Knife("ReinforcedBoneKnife0","Jango",Flame,1.3,0,0).TripleCombo
			elif choice == "SU" or choice == "Su" or choice == "su":
				Skills.Surprise("Jango","ReinforcedBoneKnife0","ReinforcedBoneKnife0","Flame","Flame")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n [Sh]uriken!\n [Or]ange Juice!\n [Ha]nd Grenade!\n ")
		if choice == "SH" or choice == "Sh" or choice == "sh":
			Items.Shuriken("Jango")
		elif choice == "OR" or choice == "Or" or choice == "or":
			Items.OrangeJuice("Jango")
		elif choice == "HA" or choice == "Ha" or choice == "ha":
			Items.HandGrenade("Jango")
	elif choice == "P" or choice == "p":
		AttacksOO.Pickpocket("Jango")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Jango",1).Choice
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Ivory Handbow!\n [2] Copper Saber!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Play!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Handbow("NormalIvoryHandbow0","Helm",Water,1,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Handbow("NormalIvoryHandbow0","Helm",Water,1,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Handbow("NormalIvoryHandbow0","Helm",Water,1,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Handbow("NormalIvoryHandbow0","Helm",Water,1,0).TriplePlay
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n [Be]ginner's Parry!\n [Bl]azing Cutlass!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Saber("NormalCopperSaber0","Helm",Water,1.25,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Saber("NormalCopperSaber0","Helm",Water,1.25,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Saber("NormalCopperSaber0","Helm",Water,1.25,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Saber("NormalCopperSaber0","Helm",Water,1.25,0).TripleCombo
			elif choice == "BE" or choice == "Be" or choice == "be":
				AttacksOO.Saber("NormalCopperSaber0","Helm",Water,1.25,0).BeginnersParry
			elif choice == "BL" or choice == "Bl" or choice == "bl":
				AttacksOO.Saber("NormalCopperSaber0","Helm",Flame,1.25,0).BlazingCutlass
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
		if choice == "HE" or choice == "He" or choice == "he":
			Items.HerbalBandage("Helm")
		elif choice == "TO" or choice == "To" or choice == "to":
			Items.TomatoJuice("Helm")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Helm",1).Choice

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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [H]ealing Field!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Ivory Wand!\n [2] Cobalt Battlecannon!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Fi]reball!\n [HR] Healthy Ray!\n [HG] Healthy Glow!\n [EG] Energetic Glow!\n [ER] Energetic Ray!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Wand("NormalIvoryWand0","Roselyn",Flame,1,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Wand("NormalIvoryWand0","Roselyn",Flame,1,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Wand("NormalIvoryWand0","Roselyn",Flame,1,0).HATK
			elif choice == "FI" or choice == "Fi" or choice == "fi":
				AttacksOO.OffenseSpell("NormalIvoryWand0","Roselyn",Flame,1.15,0,0).Fireball
			elif choice == "HR" or choice == "Hr" or choice == "hr":
				Skills.HealthyRay("Roselyn","NormalIvoryWand0")
			elif choice == "HG" or choice == "Hg" or choice == "hg":
				Skills.HealthyGlow("Roselyn","NormalIvoryWand0")
			elif choice == "ER" or choice == "Er" or choice == "er":
				Skills.EnergeticRay("Roselyn","NormalIvoryWand0")
			elif choice == "EG" or choice == "Eg" or choice == "eg":
				Skills.EnergeticGlow("Roselyn","NormalIvoryWand0")
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Battlecannon("NormalCobaltBattlecannon0","Roselyn",Flame,0.5,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Battlecannon("NormalCobaltBattlecannon0","Roselyn",Flame,0.5,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Battlecannon("NormalCobaltBattlecannon0","Roselyn",Flame,0.5,0).HATK
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Roselyn",1).Choice
		
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [Sk]illcheck\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n ")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Brad",1).Choice
		
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n ")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Gilligan",2).Choice

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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n ")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Yule",2).Choice

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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Festive Firwood Mechgun+2!\n ")
		if choice == "1":
			choice=input("[Q]uick!\n [N]ormal!\n [H]ard!\n [Dr]izzle!\n [Bl]itz!\n ")
			if choice == "AT" or choice == "At" or choice == "at":
				Attacks.MechgunManiac("StClips","FestiveWoodMechgun2","Earth")
			elif choice == "DR" or choice == "Dr" or choice == "dr":
				Skills.DrizzleManiac("StClips","FestiveWoodMechgun2","Earth")
			elif choice == "BL" or choice == "Bl" or choice == "bl":
				Skills.BlitzManiac("StClips","FestiveWoodMechgun2","Earth")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("StClips",2).Choice

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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Stony Tungsten Greatsword!\n [2] Tungsten Spear!\n [3] Eye Laser!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [He]avy Stab!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.GreatswordGrinder("StonyTungstenGreatsword0","Reyn",Earth,1.5,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.GreatswordGrinder("StonyTungstenGreatsword0","Reyn",Earth,1.5,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.GreatswordGrinder("StonyTungstenGreatsword0","Reyn",Earth,1.5,0).HATK
			elif choice == "HE" or choice == "He" or choice == "he":
				AttacksOO.GreatswordGrinder("StonyTungstenGreatsword0","Reyn",Earth,1.5,0).HeavyStab
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]ipoint Buster!\n [Cu]two!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Polearm("NormalTungstenPolearm0","Reyn",Lightning,1.35,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Polearm("NormalTungstenPolearm0","Reyn",Lightning,1.35,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Polearm("NormalTungstenPolearm0","Reyn",Lightning,1.35,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Polearm("NormalTungstenPolearm0","Reyn",Lightning,1.35,0).TripointBuster
			elif choice == "CU" or choice == "Cu" or choice == "cu":
				AttacksOO.Polearm("NormalTungstenPolearm0","Reyn",Lightning,1.35,0).Cutwo
		elif choice == "3":
			AttacksOO.Weaponless("Reyn",Lightning,1,0,2).EyeLaser
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Reyn",2).Choice
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
	choice=input("Select something!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n [Sk]illcheck!\n ")
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
	elif choice=="AT" or choice=="At" or choice == "at":
		choice=input("Which weapon?\n [1] Tungsten Saber!\n [2] Silk Glove!\n ")
	elif choice == "I" or choice == "i":
		choice=input("Select an item!\n ")
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		Check.Skillcheck("Lirru",2).Choice