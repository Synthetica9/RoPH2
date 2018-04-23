from WSD import WSD
import TLB
import SLB
import Items
def DummyFoe(DummyFoe):
	u=DummyFoe
	uMHP=u+"MHP"
	uCHP=getattr(WSD[u+"CHP"],'Current')
	uENE=u+"ENE"
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
	choice=input("Select an action type!\n [St]atcheck!\n ")
	if choice == "ST" or choice == "St" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Current Health", (uCHP))
		print("Energy Pool", (WSD[uENE]))
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist:", (WSD[uPAR]))
		print("Magical Resist:", (WSD[uMAR]))
		print("-----------------")

def Sapphiren(Cat):
	u=Cat
	uMHP=u+"MHP"
	uENE=u+"ENE"
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
	choice=input("Select an action type!\n [St]atcheck!\n [T]eeth!\n [Br]eath Attack!\n [Bo]dyslam!\n [Cl]aw Attacks!\n ")
	if choice == "ST" or choice == "St" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Energy Pool", (WSD[uENE]))
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist:", (WSD[uPAR]))
		print("Magical Resist:", (WSD[uMAR]))
		print("-----------------")
	elif choice == "T" or choice == "t":
		SLB.SavageBite("Sapphiren")
	elif choice == "BR" or choice == "Br" or choice == "br":
		SLB.BreathAttack("Sapphiren","Flame")
	elif choice == "BO" or choice == "Bo" or choice == "bo":
		SLB.Bodyslam("Sapphiren")
	elif choice == "CL" or choice == "Cl" or choice == "cl":
		TLB.Claw("Sapphiren","NormalBoneClaw0","Flame")
	elif choice == "SP" or choice == "Sp" or choice == "sp":
		TLB.Polearm("Sapphiren","MasterpiecePlatinumPolearm10","Flame")

def Ogre(Ogre):
	u=Ogre
	uMHP=u+"MHP"
	uENE=u+"ENE"
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
	choice=input("Select an action type!\n [St]atcheck!\n [W]arhammer!\n ")
	if choice == "ST" or choice == "St" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Energy Pool", (WSD[uENE]))
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist:", (WSD[uPAR]))
		print("Magical Resist:", (WSD[uMAR]))
		print("-----------------")
	elif choice == "W" or choice == "w":
		TLB.Warhammer("Ogre","NormalBoneWarhammer0","Earth")
	
def Arachnos(Spider):
	u=Spider
	uMHP=u+"MHP"
	uENE=u+"ENE"
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
	choice=input("Select an action type!\n [St]atcheck!\n [Bi]te!\n [Bo]dyslam!\n [W]eb!\n ")
	if choice == "ST" or choice == "St" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Energy Pool", (WSD[uENE]))
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist:", (WSD[uPAR]))
		print("Magical Resist:", (WSD[uMAR]))
		print("-----------------")
	elif choice == "BI" or choice == "Bi" or choice == "bi":
		SLB.SavageBite("Arachnos")
	elif choice == "BO" or choice == "Bo" or choice == "bo":
		SLB.Bodyslam("Arachnos")
	elif choice == "W" or choice == "w":
		SLB.Webshot("Arachnos")

def Gachum(Gachum):
	u=Gachum
	uMHP=u+"MHP"
	uENE=u+"ENE"
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
	choice=input("Select an action type!\n [St]atcheck!\n [K]nife!\n [S]licer!\n [I]nventory!\n ")
	if choice == "ST" or choice == "St" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Energy Pool", (WSD[uENE]))
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist:", (WSD[uPAR]))
		print("Magical Resist:", (WSD[uMAR]))
		print("-----------------")
	elif choice == "K" or choice == "k":
		TLB.Knife("Gachum","NormalBoneKnife7","Lightning")
	elif choice == "S" or choice == "s":
		TLB.Slicer("Gachum","NormalTinSlicer3","Lightning")
	elif choice == "I" or choice == "i":
		choice=input("Select an Item!\n [G]olden Apple!\n [S]weet Orange!\n [T]hrowing Stars!\n ")
		if choice == "G" or choice == "g":
			Items.GoldenApple("Gachum")
		elif choice == "S" or choice == "s":
			Items.SweetOrange("Gachum")
		elif choice == "T" or choice == "t":
			Items.ThrowingStar("Gachum")
def Gunbo(Gunbo):
	u=Gunbo
	uMHP=u+"MHP"
	uENE=u+"ENE"
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
	choice=input("Select an action type!\n [St]atcheck!\n [T]win Pistols!\n [C]harge Shot!\n [I]nventory!\n ")
	if choice == "ST" or choice == "St" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Energy Pool", (WSD[uENE]))
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist:", (WSD[uPAR]))
		print("Magical Resist:", (WSD[uMAR]))
		print("-----------------")
	elif choice == "T" or choice == "t":
		TLB.Pistol("Gunbo","NormalTungstenTwinPistol2","Aqua")
	elif choice == "C" or choice == "c":
		SLB.ChargeShot("Gunbo","NormalTungstenTwinPistol2")
	elif choice == "I" or choice == "i":
		Items.HandGrenade("Gunbo")
def Robes(Robes):
	u=Robes
	uMHP=u+"MHP"
	uENE=u+"ENE"
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
	choice=input("Select an action type!\n [St]atcheck!\n [B]attlestaff!\n [I]nventory!\n ")
	if choice == "ST" or choice == "St" or choice == "st":
		print("These are the stats for",u,"as they currently stand!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Energy Pool", (WSD[uENE]))
		print("Strength:", (WSD[uSTR]))
		print("Spirit:", (WSD[uSPR]))
		print("Skill:", (WSD[uSKL]))
		print("Ability:", (WSD[uABL]))
		print("Agility:", (WSD[uAGI]))
		print("Evasion:", (WSD[uEVA]))
		print("Toughness:", (WSD[uTGH]))
		print("Resistance:", (WSD[uRES]))
		print("Luck:", (WSD[uLCK]))
		print("Physical Resist:", (WSD[uPAR]))
		print("Magical Resist:", (WSD[uMAR]))
		print("-----------------")
	elif choice == "B" or choice == "b":
		TLB.Staff("Robes","NormalBronzeBattlestaff2","Wind")
	elif choice == "I" or choice == "i":
		choice=input("Select an Item!\n [G]reen Apple!\n [O]range!\n [T]hrowing Stars!\n ")
		if choice == "G" or choice == "g":
			Items.GreenApple("Robes")
		elif choice == "O" or choice == "o":
			Items.SweetOrange("Robes")
		elif choice == "T" or choice == "t":
			Items.ThrowingStar("Robes")

def Skelance(Skelance):
	choice=input("Select an action type!\n [ST] Statcheck!\n [SA] Spear Attacks!\n [SS] Spear Skills!\n ")
	u=Skelance
	uMHP=u+"MHP"
	uENE=u+"ENE"
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
		print("These are Skelance's stats!")
		print("-----------------")
		print("Health Pool", (WSD[uMHP]))
		print("Energy Pool", (WSD[uENE]))
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
		print("-----------------")
	elif choice == "SA" or choice == "sa":
		choice=input("Select a Strength!\n [At]tack!\n ")
		if choice == "AT" or choice == "At" or choice == "at":
			TLB.Polearm("Skelance","NormalBronzePolearm3","Null")
	elif choice == "SS" or choice == "ss":
		choice=input("Select a Skill!\n [TB] Tripoint Buster!\n [CT] Cutwo!\n ")
		if choice == "TB" or choice == "tp" or choice == "TP" or choice == "tb":
			SLB.TripointBuster("Skelance","NormalBronzePolearm3")
		elif choice == "CT" or choice == "ct" or choice == "Cutwo" or choice == "cutwo":
			SLB.Cutwo("Skelance","NormalBronzePolearm3")

def Skelemage(Skelemage):
	u=Skelemage
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
	choice=input("Select an action type!\n [ST] Statcheck!\n [SP] Spells!\n ")
	if choice == "ST" or choice == "st":
		print("These are SkeleMage's stats!")
		print("-----------------")
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
		print("-----------------")
	elif choice == "SP" or choice == "sp" or choice == "Spells" or choice == "spells":
		choice=input("Select a Spell!\n [SB] Stun Bolt!\n [FB] Fire Blast!\n [WG] Water Grenade!\n [EH] Earthen Hammer!\n [WW] Windy Whip!\n ")
		if choice == "SB" or choice == "sb" or choice == "Stun Bolt" or choice == "stun bolt":
			SLB.StunBolt("SkeleMage","NormalCopperRod2")
		elif choice == "FB" or choice == "fb" or choice == "Fire Blast" or choice == "fire blast":
			SLB.FireBlast("SkeleMage","NormalCopperRod2")
		elif choice == "WG" or choice == "wg" or choice == "Water Grenade" or choice == "water grenade":
			SLB.WaterGrenade("SkeleMage","NormalCopperRod2")
		elif choice == "EH" or choice == "eh" or choice == "Earthen Hammer" or choice == "earthen hammer":
			SLB.EarthenHammer("SkeleMage","NormalCopperRod2")
		elif choice == "WW" or choice == "ww" or choice == "Windy Whip" or choice == "windy whip":
			SLB.WindyWhip("SkeleMage","NormalCopperRod2")
def Hellhound(Hellhound):
	choice=input("Select an action type!\n [ST] Statcheck!\n [S] Skills! \n [A] Attacks!\n ")
	u=Hellhound
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
		print("These are the stats for",u,"!")
		print("-----------------")
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
		print("-----------------")
	if choice == "AT" or choice == "At" or choice == "at":
		choice=input("Select an attack!\n [CL] Claws!\n [Te]eth!\n ")
		if choice == "CL" or choice == "cl" or choice == "Claws" or choice == "claws":
			TLB.Claw("Hellhound","NormalBronzeClaw3","Flame")
		elif choice == "Te" or choice == "TE" or choice == "te":
			SLB.SavageBite("Hellhound")
	elif choice == "S" or choice == "s" or choice == "Skills" or choice == "skills":
		choice=input("Select a Skill! \n [FB] Fire Breath!\n [SB] Savage Bite!\n [BS] Bodyslam!\n ")
		if choice == "FB" or choice == "fb":
			SLB.BreathAttack("Hellhound","Flame")
		elif choice == "SB" or choice == "sb":
			SLB.SavageBite("Hellhound")
		elif choice == "BS" or choice == "bs":
			SLB.Bodyslam("Hellhound")			
def Liveflame(Liveflame):
	u=Liveflame
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
	choice = input("Select a thing!\n [S]tat check!\n [BA] Breath Attack!\n [FB] Flame Blast!\n ")
	if choice == "ST" or choice == "st" or choice == "s" or choice == "S":
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
	elif choice == "BA" or choice == "ba":
		SLB.BreathAttack("Livefalme","Flame")
	elif choice == "FB" or choice == "fb":
		SLB.FlameBlast("Liveflame","NormalIvoryRod1")
	elif choice == "BS" or choice == "bs":
		SLB.Bodyslam("Liveflame")
def Jelightning(Jel):
	choice=input("Select an Action!\n [ST] Statcheck!\n ")
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
def Jelflame(Jel):
	choice=input("Select an Action!\n [ST] Statcheck!\n ")
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
	elif choice == "BS" or choice == "bs":
		SLB.Bodyslam("Jelflame")
	elif choice == "BA" or choice == "ba":
		SLB.BreathAttack("Jelflame","Flame")
def Aquajel(Jel):
	choice=input("Select an Action!\n [ST] Statcheck!\n [BS] Bodyslam!\n [WG] Water Grenade!\n ")
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
		SLB.Bodyslam("Aquajel")
	elif choice == "WG" or choice == "wg":
		SLB.WaterGrenade("Aquajel","NormalIvoryWand3")
def Jelearth(Jel):
	choice=input("Select an Action!\n [ST] Statcheck!\n ")
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
def Metajel(Jel):
	choice=input("Select an Action!\n [ST] Statcheck!\n ")
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
		TLB.Bodyslam("Jinglejel")
	elif choice == "WG" or choice == "wg":
		SLB.WaterGrenade("Jinglejel","NormalIvoryWand3")
	elif choice == "SC" or choice == "sc":
		SLB.WaterGrenade("Jinglejel","NormalIvoryRod10")

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
			TLB.BowShotQ("Faerider","CobaltBow2")
		elif choice == "N" or choice == "n":
			TLB.BowShotN("Faerider","CobaltBow2")
		elif choice == "S" or choice == "s":
			TLB.BowShotH("Faerider","CobaltBow2")
		elif choice == "C" or choice == "c":
			SLB.Clipshot("Faerider","CobaltBow2")
		elif choice == "L" or choice == "l":
			SLB.Longshot("Faerider","CobaltBow2")
	elif choice == "FW" or choice == "fw" or choice == "Wand" or choice == "wand":
		choice=input("Select a Wand Action!\n ==ATTACKS==\n [W]eak Ray!\n [N]ormal Ray!\n [S]trong Ray!\n ==SKILLS==\n [W]ater Grenade!\n [F]lame Blast!\n ")
		if choice == "W" or choice == "w":
			TLB.WandRayQ("Faerider","NormalIvoryWand7")
		elif choice == "N" or choice == "n":
			TLB.WandRayN("Faerider","NormalIvoryWand7")
		elif choice == "S" or choice == "s":
			TLB.WandRayH("Faerider","NormalIvoryWand7")
		elif choice == "Flame" or choice == "flame" or choice == "fire" or choice == "Fire":
			SLB.FlameBlast("Faerider","NormalIvoryWand7")
		elif choice == "Water" or choice == "water":
			SLB.WaterGrenade("Faerider","NormalIvoryWand7")
	elif choice == "FC" or choice == "fc":
		choice=input("Select a Cane action!\n [Q]uick Attack!\n [N]ormal Attack!\n [H]ard Attack!\n ")
		if choice == "Q" or choice == "q":
			TLB.CaneWhackQ("Faerider","TungstenCane2")
		elif choice == "N" or choice == "n":
			TLB.CaneWhackN("Faerider","TungstenCane2")
		elif choice == "H" or choice == "h":
			TLB.CaneWhackH("Faerider","TungstenCane2")
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
		TLB.Claw("Norwolf","BoneLeatherClaw2","Aqua")
	elif choice == "BA" or choice == "ba":
		SLB.BreathAttack("Norwolf","Aqua")
	elif choice == "SB" or choice == "sb":
		SLB.SavageBite("Norwolf")
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
		TLB.PistolPacker("Snowgunner","CottonWoodPistol3","Aqua")
	elif choice == "CL" or choice == "cl":
		TLB.Claw("Snowgunner","CottonWoodClaw3","Aqua")
	elif choice == "BA" or choice == "ba":
		SLB.BreathAttack("Snowgunner","Aqua")