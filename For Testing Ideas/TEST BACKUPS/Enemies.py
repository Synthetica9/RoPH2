from WSD2 import WSD
import Attacks
import Skills
import Items
import AttacksOO
import random as ra
import Skillcheck as Check
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

def DummyFoe(Monster):
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
	uWT=WSD[Monster].ArmorWT
	choice=input("Select an action type!\n [St]atcheck!\n ")
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

def Sapphiren(Monster):
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
	uWT=WSD[Monster].ArmorWT
	choice=input("Select an action type!\n [St]atcheck!\n [Sa]vage Bite!\n [Br]eath Attack!\n [Cl]aw Attacks!\n ")
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
	elif choice == "SA" or choice == "Sa" or choice == "sa":
		AttacksOO.Weaponless("Sapphiren",Flame,1,0,0).SavageBite
	elif choice == "BR" or choice == "Br" or choice == "br":
		AttacksOO.Weaponless("Sapphiren",Flame,1,0,0).BreathAttack
	elif choice == "BO" or choice == "Bo" or choice == "bo":
		AttacksOO.Weaponless("Sapphiren",Flame,1,0,0).Bodyslam
	elif choice == "CL" or choice == "Cl" or choice == "cl":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Claw("NormalBoneClaw0","Sapphiren",Flame,1,0,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Claw("NormalBoneClaw0","Sapphiren",Flame,1,0,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Claw("NormalBoneClaw0","Sapphiren",Flame,1,0,0).HATK

def Ogre(Monster):
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
	uWT=WSD[Monster].ArmorWT
	choice=input("Select an action type!\n [St]atcheck!\n [W]arhammer!\n ")
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
	elif choice == "W" or choice == "w":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Warhammer("NormalBoneWarhammer0","Ogre",Earth,1,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Warhammer("NormalBoneWarhammer0","Ogre",Earth,1,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Warhammer("NormalBoneWarhammer0","Ogre",Earth,1,0).HATK

def Arachnos(Monster):
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
	uWT=WSD[Monster].ArmorWT
	choice=input("Select an action type!\n [St]atcheck!\n [Sa]vage Bite!\n [We]bshot!\n [Bo]dyslam!\n ")
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
	elif choice == "SA" or choice == "Sa" or choice == "sa":
		AttacksOO.Weaponless("Arachnos",Wind,1,0,0).SavageBite
	elif choice == "BO" or choice == "Bo" or choice == "bo":
		AttacksOO.Weaponless("Arachnos",Wind,1,0,0).Bodyslam
	elif choice == "W" or choice == "w":
		AttacksOO.Weaponless("Arachnos",Wind,1,0,0).WebShot

def Gachum(Unit):
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
	choice=input("Select an action type!\n [St]atcheck!\n [At]tack!\n [I]nventory!\n ")
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
		choice=input("Which weapon?\n [1] Bone Knife!\n [2] Tin Slicer!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knife("NormalBoneKnife7","Gachum",Lightning,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knife("NormalBoneKnife7","Gachum",Lightning,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knife("NormalBoneKnife7","Gachum",Lightning,1,0,0).HATK
			elif choice == "PI" or choice == "Pi" or choice == "pi":
				AttacksOO.Knife("NormalBoneKnife7","Gachum",Lightning,1,0,0).PinpointStab
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Slicer("NormalTinSlicer3","Gachum",Lightning,1,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Slicer("NormalTinSlicer3","Gachum",Lightning,1,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Slicer("NormalTinSlicer3","Gachum",Lightning,1,0).HATK
	elif choice == "I" or choice == "i":
		choice=input("Select an Item!\n [G]olden Apple!\n [S]weet Orange!\n [T]hrowing Stars!\n ")
		if choice == "G" or choice == "g":
			Items.GoldenApple("Gachum")
		elif choice == "S" or choice == "s":
			Items.SweetOrange("Gachum")
		elif choice == "T" or choice == "t":
			Items.ThrowingStar("Gachum")
def Gunbo(Unit):
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
	choice=input("Select an action type!\n [St]atcheck!\n [T]win Pistols!\n [I]nventory!\n ")
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
	elif choice == "T" or choice == "t":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [C]harge Shot!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Pistols("NormalTungstenTwinPistol10","Gunbo",Water,1,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Pistols("NormalTungstenTwinPistol10","Gunbo",Water,1,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Pistols("NormalTungstenTwinPistol10","Gunbo",Water,1,0).HATK
		elif choice == "C" or choice == "c":
			AttacksOO.Pistols("NormalTungstenTwinPistol10","Gunbo",Water,1,0).ChargeShot
	elif choice == "I" or choice == "i":
		Items.HandGrenade("Gunbo")
def Robes(Unit):
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
	choice=input("Select an action type!\n [St]atcheck!\n [B]attlestaff!\n [I]nventory!\n ")
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
	elif choice == "B" or choice == "b":
		choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
		if choice == "Q" or choice == "q":
			AttacksOO.Battlestaff("NormalBronzeBattlestaff2","Robes",Wind,1,0).QATK
		elif choice == "N" or choice == "n":
			AttacksOO.Battlestaff("NormalBronzeBattlestaff2","Robes",Wind,1,0).NATK
		elif choice == "H" or choice == "h":
			AttacksOO.Battlestaff("NormalBronzeBattlestaff2","Robes",Wind,1,0).HATK
	elif choice == "I" or choice == "i":
		choice=input("Select an Item!\n [G]reen Apple!\n [O]range!\n [T]hrowing Stars!\n ")
		if choice == "G" or choice == "g":
			Items.GreenApple("Robes")
		elif choice == "O" or choice == "o":
			Items.SweetOrange("Robes")
		elif choice == "T" or choice == "t":
			Items.ThrowingStar("Robes")

def Skelemage(Monster,Element):
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
	choice=input("Select an action type!\n [St]atcheck!\n [Sp]ells!\n ")
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
	elif choice == "SP" or choice == "Sp" or choice == "sp":
		choice=input("Select a Spell!\n [SB] Stun Bolt!\n [FB] Fire Blast!\n [WG] Water Grenade!\n [EH] Earthen Hammer!\n [WW] Windy Whip!\n ")
		if choice == "SB" or choice == "sb" or choice == "Sb":
			AttacksOO.OffenseSpell("NormalCopperRod2","Skelemage",Lightning,1,0,0).StunBolt
		elif choice == "FB" or choice == "fb" or choice == "Fb":
			AttacksOO.OffenseSpell("NormalCopperRod2","Skelemage",Flame,1,0,0).FlameBlast
		elif choice == "WG" or choice == "wg" or choice == "Wg":
			AttacksOO.OffenseSpell("NormalCopperRod2","Skelemage",Water,1,0,0).WaterGrenade
		elif choice == "EH" or choice == "eh" or choice == "Eh":
			AttacksOO.OffenseSpell("NormalCopperRod2","Skelemage",Water,1,0,0).EarthenHammer
		elif choice == "WW" or choice == "ww" or choice == "Ww":
			AttacksOO.OffenseSpell("NormalCopperRod2","Skelemage",Water,1,0,0).WindyWhip

def Hellhound(Monster):
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
	uWT=WSD[Monster].ArmorWT
	choice=input("Select an action type!\n [St]atcheck!\n [At]tacks!\n [Sk]ills!")
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
	if choice == "AT" or choice == "At" or choice == "at":
		choice=input("Select an attack!\n [CL] Claws!\n [Te]eth!\n ")
		if choice == "CL" or choice == "cl" or choice == "Claws" or choice == "claws":
			Attacks.Claw("Hellhound","NormalBronzeClaw3","Flame")
		elif choice == "Te" or choice == "TE" or choice == "te":
			AttacksOO.Weaponless("Hellhound",Flame,1,0,0).SavageBite
	elif choice == "SK" or choice == "Sk" or choice == "sk":
		choice=input("Select a Skill! \n [FB] Fire Breath!\n [SB] Savage Bite!\n [BS] Bodyslam!\n ")
		if choice == "FB" or choice == "fb":
			Skills.BreathAttack("Hellhound","Flame")
		elif choice == "SB" or choice == "sb":
			Skills.SavageBite("Hellhound")
		elif choice == "BS" or choice == "bs":
			Skills.Bodyslam("Hellhound")			
def Liveflame(Monster):
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
	uWT=WSD[Monster].ArmorWT
	choice=input("Select an action type!\n [St]atcheck!\n [Br]eath Attack!\n [Fl]ameblast!\n [Bo]dyslam!\n ")
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
	elif choice == "BR" or choice == "br" or choice == "Br":
		Skills.BreathAttack("Liveflame","Flame")
	elif choice == "FL" or choice == "fl" or choice == "Fl":
		Skills.FlameBlast("Liveflame","NormalIvoryRod1")
	elif choice == "BO" or choice == "bo" or choice == "Bo":
		Skills.Bodyslam("Liveflame")
def Jel(Monster,Element):
	u=Monster
	uELM=Element
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
	uWT=WSD[Monster].ArmorWT
	choice=input("Select an action type!\n [St]atcheck!\n [Bo]dyslam!\n [Br]eathattack!\n ")
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
	elif choice == "BO" or choice == "Bo" or choice == "bo":
		Skills.Bodyslam(Monster,Element)
	elif choice == "BR"or choice == "Br" or choice == "br":
		Skills.BreathAttack(Monster,Element)
#@#==WINTERTIME FOES==#@#
def Jinglejel(Jel):
	choice=input("Select an Action!\n [ST] Statcheck!\n [BS] Bodyslam!\n [WG] Water Grenade!\n [SC] Snowball Cannon!\n ")
	u=Jel
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uLCK=u+"LCK"
	uPAR=u+"PAR"
	uMAR=u+"MAR"
	if choice == "ST" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("\n-----------------")
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist: ",(WSD[uPAR]))
		print("Magical Resist: ",(WSD[uMAR]))
		print("-----------------\n")
	if choice == "BS" or choice == "bs" or choice == "Bodyslam" or choice == "bodyslam":
		Attacks.Bodyslam("Jinglejel")
	elif choice == "WG" or choice == "wg":
		Skills.WaterGrenade("Jinglejel","NormalIvoryWand3")
	elif choice == "SC" or choice == "sc":
		Skills.WaterGrenade("Jinglejel","NormalIvoryRod10")

#Faerider: a four-armed, winged foe who rides a mount in to battle.
def Faerider(Fae):
	choice=input("Select an Action!\n [ST] Statcheck!\n [FB] Faewood Bow!\n [FW] Faewood Wand!\n [FC] Faewood Cane!\n ")
	u=Fae
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uLCK=u+"LCK"
	uPAR=u+"PAR"
	uMAR=u+"MAR"
	if choice == "ST" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("\n-----------------")
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist: ",(WSD[uPAR]))
		print("Magical Resist: ",(WSD[uMAR]))
		print("PAR:", (WSD[uPAR]))
		print("MAR:", (WSD[uMAR]))
		print("-----------------\n")
	elif choice == "FB" or choice == "fb" or choice == "Bow" or choice == "bow":
		choice=input("Select a Bow Action!\n ==ATTACKS==\n [W]eak!\n [N]ormal!\n [S]trong!\n ==SKILLS==\n [L]ongshot!\n [C]lipshot!\n ")
		if choice == "W" or choice == "w":
			Attacks.BowShotQ("Faerider","CobaltBow2")
		elif choice == "N" or choice == "n":
			Attacks.BowShotN("Faerider","CobaltBow2")
		elif choice == "S" or choice == "s":
			Attacks.BowShotH("Faerider","CobaltBow2")
		elif choice == "C" or choice == "c":
			Skills.Clipshot("Faerider","CobaltBow2")
		elif choice == "L" or choice == "l":
			Skills.Longshot("Faerider","CobaltBow2")
	elif choice == "FW" or choice == "fw" or choice == "Wand" or choice == "wand":
		choice=input("Select a Wand Action!\n ==ATTACKS==\n [W]eak Ray!\n [N]ormal Ray!\n [S]trong Ray!\n ==SKILLS==\n [W]ater Grenade!\n [F]lame Blast!\n ")
		if choice == "W" or choice == "w":
			Attacks.WandRayQ("Faerider","NormalIvoryWand7")
		elif choice == "N" or choice == "n":
			Attacks.WandRayN("Faerider","NormalIvoryWand7")
		elif choice == "S" or choice == "s":
			Attacks.WandRayH("Faerider","NormalIvoryWand7")
		elif choice == "Flame" or choice == "flame" or choice == "fire" or choice == "Fire":
			Skills.FlameBlast("Faerider","NormalIvoryWand7")
		elif choice == "Water" or choice == "water":
			Skills.WaterGrenade("Faerider","NormalIvoryWand7")
	elif choice == "FC" or choice == "fc":
		choice=input("Select a Cane action!\n [Q]uick Attack!\n [N]ormal Attack!\n [H]ard Attack!\n ")
		if choice == "Q" or choice == "q":
			Attacks.CaneWhackQ("Faerider","TungstenCane2")
		elif choice == "N" or choice == "n":
			Attacks.CaneWhackN("Faerider","TungstenCane2")
		elif choice == "H" or choice == "h":
			Attacks.CaneWhackH("Faerider","TungstenCane2")
def Norwolf(Norwolf):
	choice=input("Select an Action!\n [ST] Statcheck!\n [FC] Frost Claws!\n [BA] Breath Attack!\n [SB] Savage Bite!\n ")
	u=Norwolf
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uLCK=u+"LCK"
	uPAR=u+"PAR"
	uMAR=u+"MAR"
	if choice == "ST" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("\n-----------------")
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist: ",(WSD[uPAR]))
		print("Magical Resist: ",(WSD[uMAR]))
		print("-----------------\n")
	elif choice == "FC" or choice == "fc":
		Attacks.Claw("Norwolf","BoneLeatherClaw2","Aqua")
	elif choice == "BA" or choice == "ba":
		Skills.BreathAttack("Norwolf","Aqua")
	elif choice == "SB" or choice == "sb":
		Skills.SavageBite("Norwolf")
def Snowgunner(Snowman):
	choice = input("Select an Action!\n [ST] Statcheck!\n [PB] Pistol Blaster!\n [CL] Claw Attacks!\n [BA] Breath Attack!\n ")
	u=Snowman
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uLCK=u+"LCK"
	uPAR=u+"PAR"
	uMAR=u+"MAR"
	if choice == "ST" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("\n-----------------")
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist: ",(WSD[uPAR]))
		print("Magical Resist: ",(WSD[uMAR]))
		print("-----------------\n")
	elif choice == "PB" or choice == "pb":
		Attacks.PistolPacker("Snowgunner","CottonWoodPistol3","Aqua")
	elif choice == "CL" or choice == "cl":
		Attacks.Claw("Snowgunner","CottonWoodClaw3","Aqua")
	elif choice == "BA" or choice == "ba":
		Skills.BreathAttack("Snowgunner","Aqua")
#seperator line
def Todd(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [We]apons!\n ")
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
		print("Current HP:",HealthBar.ToddHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.ToddENE)
		print("-----------------")
	elif choice == "WE" or choice == "we":
		choice=input("Select a Weapon!\n [1] Steel Twin Pistols!\n [2] Steel Knife!\n [3] Steel Knife!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [C]harge Shot!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Pistols(WSD["Todd"].Weapon1,"Todd",Lunar,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Pistols(WSD["Todd"].Weapon1,"Todd",Lunar,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Pistols(WSD["Todd"].Weapon1,"Todd",Lunar,1,0,0).HATK
			elif choice == "C" or choice == "c":
				AttacksOO.Pistols(WSD["Todd"].Weapon1,"Todd",Lunar,1,0,0).ChargeShot
		elif choice == "2":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knife(WSD["Todd"].Weapon2,"Todd",Lunar,1,0,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knife(WSD["Todd"].Weapon2,"Todd",Lunar,1,0,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knife(WSD["Todd"].Weapon2,"Todd",Lunar,1,0,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Knife(WSD["Todd"].Weapon2,"Todd",Lunar,1,0,0,0).TripleCombo
			elif choice == "SU" or choice == "Su" or choice == "su":
				AttacksOO.Knife(WSD["Todd"].Weapon2,"Todd",Lunar,1,0,0,0).Surprise
		elif choice == "3":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Knife(WSD["Todd"].Weapon3,"Todd",Lunar,1,0,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Knife(WSD["Todd"].Weapon3,"Todd",Lunar,1,0,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Knife(WSD["Todd"].Weapon3,"Todd",Lunar,1,0,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Knife(WSD["Todd"].Weapon3,"Todd",Lunar,1,0,0,0).TripleCombo
			elif choice == "SU" or choice == "Su" or choice == "su":
				AttacksOO.Knife(WSD["Todd"].Weapon3,"Todd",Lunar,1,0,0,0).Surprise
def Freak(Unit):
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
		print("Current HP:",HealthBar.FreakHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.FreakENE)
		print("-----------------")
	elif choice == "WE" or choice == "we":
		choice=input("Select a Weapon!\n [1] Magenium Wand!\n ")
		if choice == "1":
			choice=input("Select an Action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [H]althy [R]ay!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Wand(WSD["Freak"].Weapon1,"Freak",Void,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Wand(WSD["Freak"].Weapon1,"Freak",Void,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Wand(WSD["Freak"].Weapon1,"Freak",Void,1,0,0).HATK
			elif choice == "HR" or choice == "Hr" or choice == "hr":
				AttacksOO.SupportSpell(WSD["Freak"].Weapon1,"Freak").HealthyRay

def Marshal(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [We]apons!\n ")
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
		print("Current HP:",HealthBar.MarshalHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.MarshalENE)
		print("-----------------")
	elif choice == "WE" or choice == "we":
		choice = input("Select a Weapon!\n [1] Steel Battlecannon!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Battlecannon(WSD["Marshal"].Weapon1,"Marshal",Solar,0.5,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Battlecannon(WSD["Marshal"].Weapon1,"Marshal",Solar,0.5,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Battlecannon(WSD["Marshal"].Weapon1,"Marshal",Solar,0.5,0,0).HATK

def Higgins(Unit):
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
	choice=input("Select something!\n [St]atcheck!\n [Ba]ttlestats!\n [We]apons!\n [T]oggle Shield!\n [C]onfirm Actions!\n ")
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
		print("Current HP:",HealthBar.HigginsHP)
		importlib.reload(EnergyBar)
		print("Current ENE:",EnergyBar.HigginsENE)
		print("-----------------")
	elif choice == "WE" or choice == "we":
		choice = input("Select a Weapon!\n [1] Steel Saber!\n [2] Ivory Cane!\n ")
		if choice == "1":
			choice=input("Select an action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [Tr]iple Combo!\n [Be]ginner's Parry!\n [Bl]azing Cutlass!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Saber(WSD["Higgins"].Weapon1,"Higgins",Earth,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Saber(WSD["Higgins"].Weapon1,"Higgins",Earth,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Saber(WSD["Higgins"].Weapon1,"Higgins",Earth,1,0,0).HATK
			elif choice == "TR" or choice == "Tr" or choice == "tr":
				AttacksOO.Saber(WSD["Higgins"].Weapon1,"Higgins",Earth,1,0,0).TripleCombo
			elif choice == "BE" or choice == "Be" or choice == "be":
				AttacksOO.Saber(WSD["Higgins"].Weapon1,"Higgins",Earth,1,0,0).BeginnersParry
			elif choice == "BL" or choice == "Bl" or choice == "bl":
				AttacksOO.Saber(WSD["Higgins"].Weapon1,"Higgins",Flame,1,0,0).BlazingCutlass
		elif choice == "2":
			choice=input("Select an Action!\n [Q]uick!\n [N]ormal!\n [H]ard!\n [HR] Healthy Ray!\n ")
			if choice == "Q" or choice == "q":
				AttacksOO.Cane(WSD["Higgins"].Weapon2,"Higgins",Earth,1,0,0).QATK
			elif choice == "N" or choice == "n":
				AttacksOO.Cane(WSD["Higgins"].Weapon2,"Higgins",Earth,1,0,0).NATK
			elif choice == "H" or choice == "h":
				AttacksOO.Cane(WSD["Higgins"].Weapon2,"Higgins",Earth,1,0,0).HATK
			elif choice == "HR" or choice == "Hr" or choice == "hr":
				AttacksOO.SupportSpell(WSD["Higgins"].Weapon2,"Higgins").HealthyRay