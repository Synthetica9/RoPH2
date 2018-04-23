from WSD import WSD
from Weapons import OmniWeapData
from Armors import OmniArmorData
import TLB
import SLB


def Helm(Helm):
	u=Helm
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
	choice = input("Select something!\n [ST] Statcheck!\n [CS] Copper Saber!\n [IH] Ivory Handbow!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		choice=input("Select one!\n [P]layer!\n [E]quipment!\n ")
		if choice == "P" or choice == "p":
			print("These are the stats of",u,"so far!")
			print("-----------------")
			print("Health Pool:",(WSD[uMHP]))
			print("Energy Pool:",(WSD[uENE]))
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
		elif choice == "E" or choice == "e":
			choice=input("Which items stats are we checking?\n [CS] Copper Saber!\n [IH] Ivory Handbow!\n [WS] Wood Shield!\n ")
			if choice == "CS" or choice == "Cs" or choice == "cs":
				print("-----------------")
				print(OmniWeapData["NormalCopperSaber0"][6])
				print("Physical Damage is", OmniWeapData["NormalCopperSaber0"][0])
				print("Magical Damage is", OmniWeapData["NormalCopperSaber0"][1])
				print("Weapon Accuracy is", OmniWeapData["NormalCopperSaber0"][2])
				print("Weapon Weight is", OmniWeapData["NormalCopperSaber0"][3])
				print("Can be sold for", OmniWeapData["NormalCopperSaber0"][5])
				print("-----------------")
			elif choice == "IH" or choice == "Ih" or choice == "ih" or choice == "HB" or choice == "Hb" or choice == "hb":
				print("-----------------")
				print(OmniWeapData["NormalIvoryHandbow0"][6])
				print("Physical Damage is", OmniWeapData["NormalIvoryHandbow0"][0])
				print("Magical Damage is", OmniWeapData["NormalIvoryHandbow0"][1])
				print("Weapon Accuracy is", OmniWeapData["NormalIvoryHandbow0"][2])
				print("Weapon Weight is", OmniWeapData["NormalIvoryHandbow0"][3])
				print("Can be sold for", OmniWeapData["NormalIvoryHandbow0"][5])
				print("-----------------")
			elif choice == "WS" or choice == "Ws" or choice == "ws":
				print("-----------------")
				print("Physical Resist is", OmniArmorData["NormalWoodSmallshield0"][0])
				print("Magical Resist is", OmniArmorData["NormalWoodSmallshield0"][1])
				print("Weight is", OmniArmorData["NormalWoodSmallshield0"][2])
				print("Can be sold for", OmniArmorData["NormalWoodSmallshield0"][4])
				print("-----------------")
	elif choice == "CS" or choice == "Cs" or choice == "cs":
		choice=input("Attacks or Skills?\n [A]ttacks!\n [S]kills!\n ")
		if choice == "A" or choice == "a":
			TLB.SharpSaber("Helm","NormalCopperSaber0","Aqua")
		elif choice == "S" or choice == "s":
			choice=input("Select a Skill!\n [A]rmistice!\n [T]riple Combo: Sword!\n [B]egginer's Parry!\n ")
			if choice == "A" or choice == "a":
				print("You lower your weapon and offer a truce.")
			elif choice == "T" or choice == "t":
				SLB.SharpTripleComboSword("Helm","NormalCopperSaber0")
			elif choice == "B" or choice == "b":
				SLB.SharpBeginnersParry("Helm","NormalCopperSaber0")
	elif choice == "IH" or choice == "Ih" or choice == "ih" or choice == "HB" or choice == "Hb" or choice == "hb":
		choice=input("Attacks or Skills?\n [A]ttacks!\n [S]kills!\n ")
		if choice == "A" or choice == "a":
			TLB.Handbow("Helm","NormalIvoryHandbow0","Aqua")
		elif choice == "S" or choice == "s":
			SLB.TriplePlay("Helm","NormalIvoryHandbow0")

def Roselyn(Roselyn):
	u=Roselyn
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
	choice = input("Select something!\n [ST] Statcheck!\n [IW] Ivory Wand!\n [BC] Battlecannon!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		choice=input("Select one!\n [P]layer!\n [E]quipment!\n ")
		if choice == "P" or choice == "p":
			print("These are the stats of",u,"so far!")
			print("-----------------")
			print("Health Pool:",(WSD[uMHP]))
			print("Energy Pool:",(WSD[uENE]))
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
		elif choice == "E" or choice == "e":
			choice=input("Which items stats are we checking?\n [IW] Ivory Wand?\n [BC] Battlecannon?\n [BS] Bronze Shield?\n [AS] Armor Set?\n ")
			if choice == "IW" or choice == "iw":
				print("-----------------")
				print(OmniWeapData["NormalIvoryWand0"][6])
				print("Physical Damage is", OmniWeapData["NormalIvoryWand0"][0])
				print("Magical Damage is", OmniWeapData["NormalIvoryWand0"][1])
				print("Weapon Accuracy is", OmniWeapData["NormalIvoryWand0"][2])
				print("Weapon Weight is", OmniWeapData["NormalIvoryWand0"][3])
				print("Can be sold for", OmniWeapData["NormalIvoryWand0"][5])
				print("-----------------")
			elif choice == "BC" or choice == "bc":
				print("-----------------")
				print(OmniWeapData["NormalCobaltBattlecannon0"][6])
				print("Physical Damage is", OmniWeapData["NormalCobaltBattlecannon0"][0])
				print("Magical Damage is", OmniWeapData["NormalCobaltBattlecannon0"][1])
				print("Weapon Accuracy is", OmniWeapData["NormalCobaltBattlecannon0"][2])
				print("Weapon Weight is", OmniWeapData["NormalCobaltBattlecannon0"][3])
				print("Can be sold for", OmniWeapData["NormalCobaltBattlecannon0"][5])
				print("-----------------")
			elif choice == "BS" or choice == "bs":
				print("-----------------")
				print("Physical Resist is", OmniArmorData["NormalBronzeSmallshield0"][0])
				print("Magical Resist is", OmniArmorData["NormalBronzeSmallshield0"][1])
				print("Weight is", OmniArmorData["NormalBronzeSmallshield0"][2])
				print("Can be sold for", OmniArmorData["NormalBronzeSmallshield0"][4])
				print("-----------------")
	elif choice == "IW" or choice == "iw":
		choice=input("Select your Action!\n [At]tacks!\n [Sk]ills!\n ")
		if choice == "AT" or choice == "at" or choice == "At":
			TLB.WandRay("Roselyn","IvoryWand0","Flame")
		elif choice == "SK" or choice == "Sk" or choice == "sk":
			choice=input("Select a Skill!\n [FB] Flame Blast!\n [FI] Fireball!\n ")
			if choice == "FB" or choice == "Fb" or choice == "fb":
				SLB.FlameBlast("Roselyn","IvoryWand0")
			elif choice == "FI" or choice == "Fi" or choice == "fi":
				SLB.Fireball("Roselyn","IvoryWand0")
	elif choice == "BC" or choice == "bc":
		TLB.UnlearnedBattlecannon("Roselyn","NormalCobaltBattlecannon0","Flame")

def Brad(Brad):
	u=Brad
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
	choice = input("Select something!\n [ST] Statcheck!\n [BB] Bronze Bow!\n [BK] Bone Knife!\n [T] Teeth!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		choice=input("Select one!\n [P]layer!\n [E]quipment!\n ")
		if choice == "P" or choice == "p":
			print("These are the stats of",u,"so far!")
			print("-----------------")
			print("Health Pool:",(WSD[uMHP]))
			print("Energy Pool:",(WSD[uENE]))
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
		elif choice == "E" or choice == "e":
			choice=input("Which items stats are we checking?\n [BB] Bronze Bow!\n [BK] Bone Knife!\n [SS] Steel Shield!\n [AS] Armor Set!\n ")
			if choice == "bb" or choice == "BB":
				print("-----------------")
				print(OmniWeapData["NormalBronzeBow0"][6])
				print("Physical Damage is", OmniWeapData["NormalBronzeBow0"][0])
				print("Magical Damage is", OmniWeapData["NormalBronzeBow0"][1])
				print("Weapon Accuracy is", OmniWeapData["NormalBronzeBow0"][2])
				print("Weapon Weight is", OmniWeapData["NormalBronzeBow0"][3])
				print("Can be sold for", OmniWeapData["NormalBronzeBow0"][5])
				print("-----------------")
			elif choice == "BK" or choice == "bk":
				print("-----------------")
				print(OmniWeapData["NormalBoneKnife0"][6])
				print("Physical Damage is", OmniWeapData["NormalBoneKnife0"][0])
				print("Magical Damage is", OmniWeapData["NormalBoneKnife0"][1])
				print("Weapon Accuracy is", OmniWeapData["NormalBoneKnife0"][2])
				print("Weapon Weight is", OmniWeapData["NormalBoneKnife0"][3])
				print("Can be sold for", OmniWeapData["NormalBoneKnife0"][5])
				print("-----------------")
			elif choice == "SS" or choice == "ss":
				print("-----------------")
				print("Physical Resist is", OmniArmorData["NormalSteelSmallshield0"][0])
				print("Magical Resist is", OmniArmorData["NormalSteelSmallshield0"][1])
				print("Weight is", OmniArmorData["NormalSteelSmallshield0"][2])
				print("Can be sold for", OmniArmorData["NormalSteelSmallshield0"][4])
				print("-----------------")
			elif choice == "AS" or choice == "as":
				print("-----------------")
				print(OmniArmorData["NormalBronzeHead0"][5])
				print("Headgear Physical Resist is", OmniArmorData["NormalBronzeHead0"][0])
				print("Headgear Magical Resist is", OmniArmorData["NormalBronzeHead0"][1])
				print("Headgear Weight is", OmniArmorData["NormalBronzeHead0"][2])
				print("Headgear can be sold for", OmniArmorData["NormalBronzeHead0"][4])
				print("-----------------")
				print(OmniArmorData["NormalBronzeTorso0"][5])
				print("Torsogear Physical Resist is", OmniArmorData["NormalBronzeTorso0"][0])
				print("Torsogear Magical Resist is", OmniArmorData["NormalBronzeTorso0"][1])
				print("Torsogear Weight is", OmniArmorData["NormalBronzeTorso0"][2])
				print("Torsogear can be sold for", OmniArmorData["NormalBronzeTorso0"][4])
				print("-----------------")
				print(OmniArmorData["NormalBronzeArms0"][5])
				print("Armwear Physical Resist is", OmniArmorData["NormalBronzeArms0"][0])
				print("Armwear Magical Resist is", OmniArmorData["NormalBronzeArms0"][1])
				print("Armwear Weight is", OmniArmorData["NormalBronzeArms0"][2])
				print("Armwear can be sold for", OmniArmorData["NormalBronzeArms0"][4])
				print("-----------------")
				print(OmniArmorData["NormalBronzeLegs0"][5])
				print("Legwear Physical Resist is", OmniArmorData["NormalBronzeLegs0"][0])
				print("Legwear Magical Resist is", OmniArmorData["NormalBronzeLegs0"][1])
				print("Legwear Weight is", OmniArmorData["NormalBronzeLegs0"][2])
				print("Legwear can be sold for", OmniArmorData["NormalBronzeLegs0"][4])
				print("-----------------")
				print(OmniArmorData["NormalBronzeFeet0"][5])
				print("Footwear Physical Resist is", OmniArmorData["NormalBronzeFeet0"][0])
				print("Footwear Magical Resist is", OmniArmorData["NormalBronzeFeet0"][1])
				print("Footwear Weight is", OmniArmorData["NormalBronzeFeet0"][2])
				print("Footwear can be sold for", OmniArmorData["NormalBronzeFeet0"][4])
				print("-----------------")
	elif choice == "BB" or choice == "bb":
		choice=input("Select an action!\n [At]tacks!\n [Lo]ngshot!\n [Cl]ipshot!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.BraveBowHunter("Brad","NormalBronzeBow0","Flame")
		elif choice == "LO" or choice == "lo" or choice == "Lo":
			SLB.Longshot("Brad","NormalBronzeBow0","Flame")
		elif choice == "CL" or choice == "cl" or choice == "Cl":
			SLB.Clipshot("Brad","NormalBronzeBow0")
	elif choice == "BK" or choice == "bk":
		choice=input("Select an action!\n [At]tacks!\n [Tr]iple Combo!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.Knife("Brad","NormalBoneKnife0","Flame")
		elif choice == "TR" or choice == "tr" or choice == "Tr":
			SLB.TripleComboKnife("Brad","NormalBoneKnife0")
	elif choice == "T" or choice == "t" or choice == "teeth" or choice == "Teeth":
		SLB.SavageBite("Brad")
	else:
		print("-----------------")
		print("Please select a valid option.")
		print("-----------------")

def Gilligan(Gilligan):
	u=Gilligan
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
	choice = input("Select something!\n [ST] Statcheck!\n [WC] Wooden Claw!\n [BK] Bone Knuckles!\n [BL] Brave Leap!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		print("These are the stats of",u,"so far!")
		print("-----------------")
		print("Health Pool:",(WSD[uMHP]))
		print("Energy Pool:",(WSD[uENE]))
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
	elif choice == "WC" or choice == "wc":
		choice=input("Select an attack type!\n [At]tacks!\n [Sk]ills!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.ClawClash("Gilligan","NormalWoodClaw0","Wind")
		elif choice == "SK" or choice == "sk" or choice == "Sk":
			choice=input("Select a Skill!\n [BS] Bloody Slashes!\n [FT] Fury Thrust!\n [TR] Twisterush!\n ")
			if choice == "BS" or choice == "bs":
				SLB.BloodySlashes("Gilligan","NormalWoodClaw0")
			elif choice == "FT" or choice == "ft":
				SLB.FuryThrust("Gilligan","NormalWoodClaw0")
			elif choice == "TR" or choice == "tr":
				SLB.Twisterush("Gilligan","NormalWoodClaw0")
	elif choice == "BK" or choice == "bk":
		TLB.Knuckles("Gilligan","NormalBoneKnuckle0","Wind")
	elif choice == "BL" or choice == "bl":
		SLB.BraveLeap("Gilligan","NormalWoodClaw0")

def Yule(Yule):
	u=Yule
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
	choice = input("Select something!\n [ST] Statcheck!\n [TY] Tungsten YoYo!\n [GM] Gold Mic!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		print("These are the stats of",u,"so far!")
		print("-----------------")
		print("Health Pool:",(WSD[uMHP]))
		print("Energy Pool:",(WSD[uENE]))
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
	elif choice == "TY" or choice == "ty":
		choice = input("Select an action!\n [At]tacks!\n [Bu]rning Lash!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.Whip("Yule","NormalTungstenYoyo0","Aqua")
		elif choice == "Bu" or choice == "bu" or choice == "BU":
			SLB.BurningLash("Yule","NormalTungstenYoyo0")
	elif choice == "GM" or choice == "gm":
		choice = input("Select an action!\n [At]tacks!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.Mic("Yule","NormalGoldMic0","Aqua")

def StClips(StClips):
	u=StClips
	uSTR=u+"STR"
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
	choice = input("Select something!\n [ST] Statcheck!\n [FM] Festive Firwood Mechgun!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		print("These are the stats of",u,"so far!")
		print("-----------------")
		print("Health Pool:",(WSD[uMHP]))
		print("Energy Pool:",(WSD[uENE]))
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
	elif choice == "FM" or choice == "fm":
		choice = input("Select an action!\n [At]tacks!\n [D]rizzle!\n [B]litz!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.MechgunManiac("StClips","FestiveWoodMechgun2","Null")
		elif choice == "d" or choice == "D":
			SLB.DrizzleManiac("StClips","FestiveWoodMechgun2","Null")
		elif choice == "b" or choice == "B":
			SLB.BlitzManiac("StClips","FestiveWoodMechgun2","Null")
def Reyn(Reyn):
	u=Reyn
	uSTR=u+"STR"
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
	choice = input("Select something!\n [ST] Statcheck!\n [TG] Icy Tungsten Greatsword!\n [TP] Tungsten Polearm!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		choice=input("Select one!\n [P]layer!\n [E]quipment!\n ")
		if choice == "P" or choice == "p":
			print("These are the stats of",u,"so far!")
			print("-----------------")
			print("Health Pool:",(WSD[uMHP]))
			print("Energy Pool:",(WSD[uENE]))
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
		elif choice == "E" or choice == "e":
			choice=input("Select a Weapon to check!\n [TP] Tungsten Polearm!\n [TG] Icy Tungsten Greatsword!\n [AS] Armor Set!\n ")
			if choice == "TP" or choice == "tp":
				print("-----------------")
				print("Physical Damage is", OmniWeapData["NormalTungstenPolearm0"][0])
				print("Magical Damage is", OmniWeapData["NormalTungstenPolearm0"][1])
				print("Weapon Accuracy is", OmniWeapData["NormalTungstenPolearm0"][2])
				print("Weapon Weight is", OmniWeapData["NormalTungstenPolearm0"][3])
				print("-----------------")
			elif choice == "TG" or choice == "tg":
				print("-----------------")
				print("Physical Damage is", OmniWeapData["ElectricTungstenGreatsword0"][0])
				print("Magical Damage is", OmniWeapData["ElectricTungstenGreatsword0"][1])
				print("Weapon Accuracy is", OmniWeapData["ElectricTungstenGreatsword0"][2])
				print("Weapon Weight is", OmniWeapData["ElectricTungstenGreatsword0"][3])
				print("-----------------")
			elif choice == "AS" or choice == "as":
				print("-----------------")
				print("Headgear Physical Resist is", OmniArmorData["NormalTungstenHead0"][0])
				print("Headgear Magical Resist is", OmniArmorData["NormalTungstenHead0"][1])
				print("Headgear Weight is", OmniArmorData["NormalTungstenHead0"][2])
				print("Headgear can be sold for", OmniArmorData["NormalTungstenHead0"][4])
				print("-----------------")
				print("Torsogear Physical Resist is", OmniArmorData["NormalTungstenTorso0"][0])
				print("Torsogear Magical Resist is", OmniArmorData["NormalTungstenTorso0"][1])
				print("Torsogear Weight is", OmniArmorData["NormalTungstenTorso0"][2])
				print("Torsogear can be sold for", OmniArmorData["NormalTungstenTorso0"][4])
				print("-----------------")
				print("Armwear Physical Resist is", OmniArmorData["NormalTungstenArms0"][0])
				print("Armwear Magical Resist is", OmniArmorData["NormalTungstenArms0"][1])
				print("Armwear Weight is", OmniArmorData["NormalTungstenArms0"][2])
				print("Armwear can be sold for", OmniArmorData["NormalTungstenArms0"][4])
				print("-----------------")
				print("Legwear Physical Resist is", OmniArmorData["NormalTungstenLegs0"][0])
				print("Legwear Magical Resist is", OmniArmorData["NormalTungstenLegs0"][1])
				print("Legwear Weight is", OmniArmorData["NormalTungstenLegs0"][2])
				print("Legwear can be sold for", OmniArmorData["NormalTungstenLegs0"][4])
				print("-----------------")
				print("Footwear Physical Resist is", OmniArmorData["NormalTungstenFeet0"][0])
				print("Footwear Magical Resist is", OmniArmorData["NormalTungstenFeet0"][1])
				print("Footwear Weight is", OmniArmorData["NormalTungstenFeet0"][2])
				print("Footwear can be sold for", OmniArmorData["NormalTungstenFeet0"][4])
				print("-----------------")
				print("Physical Resist is", OmniArmorData["NormalTungstenMediumshield0"][0])
				print("Magical Resist is", OmniArmorData["NormalTungstenMediumshield0"][1])
				print("Weight is", OmniArmorData["NormalTungstenMediumshield0"][2])
				print("Can be sold for", OmniArmorData["NormalTungstenMediumshield0"][4])
				print("-----------------")
	elif choice == "TG" or choice == "tg":
		choice = input("Select an action!\n [At]tacks!\n [Gr]inding Chainsaw Thrust!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.GreatswordGrinder("Reyn","IcyTungstenGreatsword0","Aqua")
		elif choice == "Gr" or choice == "gr" or choice == "GR":
			SLB.ChainsawThrustGrinder("Reyn","ElectricTungstenGreatsword0")
	elif choice == "TP" or choice == "tp":
		choice=input("Select an attack!\n [A]ttacks!\n [S]kills!\n ")
		if choice == "A" or choice == "a":
			TLB.PolearmPaladin("Reyn","NormalTungstenPolearm0","Lightning")
		elif choice == "S" or choice == "s":
			choice = input("Select a Skill!\n [C]utwo!\n [T]ripoint Buster!\n ")
			if choice == "C" or choice == "c":
				SLB.CutwoPaladin("Reyn","NormalTungstenPolearm0")
			elif choice == "T" or choice == "t":
				SLB.TripointPaladin("Reyn","NormalTungstenPolearm0")
def Lirru(Lirru):
	u=Lirru
	uSTR=u+"STR"
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
	choice = input("Select something!\n [ST] Statcheck!\n [SW] Sword Actions!\n [BS] Bodyslam!\n [GL] Glove Actions!\n [I] Inventory!\n ")
	if choice == "ST" or choice == "st":
		print("These are the stats of",u,"so far!")
		print("-----------------")
		print("Health Pool:",(WSD[uMHP]))
		print("Energy Pool:",(WSD[uENE]))
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
	elif choice == "BS" or choice == "bs":
		SLB.Bodyslam("Lirru")
	elif choice == "SW" or choice == "sw":
		choice=input("Select an action type!\n [At]tack!\n [Sk]ills!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.SharpSwordSighter("Lirru","NormalTungstenSword0","Flame")
		elif choice == "Sk" or choice == "sk" or choice == "SK":
			choice=input("Select a Skill!\n [TC] Triple Combo!\n [BP] Beginner's Parry!\n [FT] Fury Thrust!\n ")
			if choice == "TC" or choice == "tc":
				SLB.TripleComboSwordSharpSight("Lirru","NormalTungstenSword0")
			elif choice == "BP" or choice == "bp":
				SLB.BeginnersParrySharpSight("Lirru","NormalTungstenSword0")
			elif choice == "FT" or choice == "ft":
				SLB.FuryThrustSharpSight("Lirru","NormalTungstenSword0")
#===================OLD UNITS===================#
def Chambellan(Chambellan):
	u=Chambellan
	uSTR=u+"STR"
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
	choice = input("Select something!\n [ST] Statcheck!\n [WL] Weapons List!\n")
	if choice == "ST" or choice == "st":
		print("These are Chambellan's stats so far!")
		print("-----------------")
		print("Health Pool:",(WSD[uMHP]))
		print("Energy Pool:",(WSD[uENE]))
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
	elif choice == "WL" or choice == "wl":
		choice = input("Select a Weapon to use!\n [GC] Gold Cane!\n [IW] Ivory Wand!\n ")
		if choice == "GC" or choice == "gc":
			choice = input("Select an Action!\n [Q] Quick!\n [N] Normal!\n [H] Hard!\n [HG] Healthy Glow!\n [HR] Healthy Ray!\n [RR] Restorative Ray!\n [CL] Cudgel!\n [SB] Shatter Blow!\n ")
			if choice == "Q" or choice == "q":
				TLB.CaneCrushQ("Chambellan","NormalGoldCane0")
			elif choice == "N" or choice == "n":
				TLB.CaneCrushN("Chambellan","NormalGoldCane0")
			elif choice == "H" or choice == "h":
				TLB.CaneCrushH("Chambellan","NormalGoldCane0")
			elif choice == "HG" or choice == "hg":
				SLB.HealthyGlow("Chambellan","NormalGoldCane0")
			elif choice == "HR" or choice == "hr":
				SLB.HealthyRay("Chambellan","NormalGoldCane0")
			elif choice == "RR" or choice == "rr":
				SLB.RestorativeRay("Chambellan","NormalGoldCane0")
			elif choice == "CL" or choice == "cl" or choice == "Cudgel" or choice == "cudgel":
				SLB.Cudgel("Chambellan","NormalGoldCane0")
			elif choice == "SB" or choice == "sb" or choice == "Shatter Blow" or choice == "shatter blow":
				SLB.ShatterBlow("Chambellan","NormalGoldCane0")
		elif choice == "IW" or choice == "iw":
			choice = input("Select an action!\n [W] Weak Magic Blast!\n [S] Split Magic Blast!\n [N] Normal Magic Blast!\n [HG] Healthy Glow!\n [HR] Healthy Ray!\n [RR] Restorative Ray!\n ")
			if choice == "W" or choice == "w" or choice == "Weak" or choice == "weak":
				TLB.MagicBlastW("Chambellan","NormalIvoryWand0")
			elif choice == "S" or choice == "s" or choice == "Split" or choice == "split":
				TLB.MagicBlastS("Chambellan","NormalIvoryWand0")
			elif choice == "N" or choice == "n" or choice == "Normal" or choice == "normal":
				TLB.MagicBlastN("Chambellan","NormalIvoryWand0")
			elif choice == "F" or choice == "f" or choice == "Focused" or choice == "focused":
				TLB.MagicBlastF("Chambellan","NormalIvoryWand0")
			elif choice == "HG" or choice == "hg":
				SLB.HealthyGlow("Chambellan","NormalIvoryWand0")
			elif choice == "HR" or choice == "hr":
				SLB.HealthyRay("Chambellan","NormalIvoryWand0")
			elif choice == "RR" or choice == "rr":
				SLB.RestorativeRay("Chambellan","NormalIvoryWand0")
def AHLoriana(AHLoriana):
	u = AHLoriana
	uSTR=u+"STR"
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
	choice = input("Select something!\n [ST] Statcheck!\n [WL] Weapons List!\n")
	if choice == "ST" or choice == "st":
		print("These are Loriana's stats, so far!")
		print("-----------------")
		print("Health Pool:",(WSD[uMHP]))
		print("Energy Pool:",(WSD[uENE]))
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
	elif choice == "WL" or choice == "wl":
		choice = input("Select a Weapon!\n [IW] Ivory Wand!\n [GR] Gold Rod!\n ")
		if choice == "IW" or choice == "iw" or choice == "Ivory Wand" or choice == "ivory wand":
			choice = input("Select an action!\n [W] Weak Magic Blast!\n [S] Split Magic Blast!\n [N] Normal Magic Blast!\n [FB] Flame Blast!\n [WW] Windy Whip!\n ")
			if choice == "W" or choice == "w" or choice == "Weak" or choice == "weak":
				TLB.MagicBlastW("Loriana","NormalIvoryWand0")
			elif choice == "S" or choice == "s" or choice == "Split" or choice == "split":
				TLB.MagicBlastS("Loriana","NormalIvoryWand0")
			elif choice == "N" or choice == "n" or choice == "Normal" or choice == "normal":
				TLB.MagicBlastN("Loriana","NormalIvoryWand0")
			if choice == "WW" or choice == "ww" or choice == "Windy Whip" or choice == "windy whip":
				SLB.WindyWhip("Loriana","NormalIvoryWand0")
			elif choice == "FB" or choice == "fb" or choice == "Flame Blast" or choice == "flame blast":
				SLB.FlameBlast("Loriana","NormalIvoryWand0")
		elif choice == "GR" or choice == "gr" or choice == "Gold Rod" or choice == "Golden Rod" or choice == "gold rod" or choice == "golden rod":
			choice = input("Select an action!\n [W] Weak Magic Blast!\n [S] Split Magic Blast!\n [N] Normal Magic Blast!\n [FB] Flame Blast!\n [WW] Windy Whip!\n ")
			if choice == "W" or choice == "w" or choice == "Weak" or choice == "weak":
				TLB.MagicBlastW("Loriana","NormalGoldRod0")
			elif choice == "S" or choice == "s" or choice == "Split" or choice == "split":
				TLB.MagicBlastS("Loriana","NormalGoldRod0")
			elif choice == "N" or choice == "n" or choice == "Normal" or choice == "normal":
				TLB.MagicBlastN("Loriana","NormalGoldRod0")
			if choice == "WW" or choice == "ww" or choice == "Windy Whip" or choice == "windy whip":
				SLB.WindyWhip("Loriana","NormalGoldRod0")
			elif choice == "FB" or choice == "fb" or choice == "Flame Blast" or choice == "flame blast":
				SLB.FlameBlast("Loriana","NormalGoldRod0")