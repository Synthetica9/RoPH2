import TLB
import SLB
from WSD import WSD
import Items

#Other Units
def Josephine(Josephine):
	u=Josephine
	choice=input("Select an Action!\n [ST] Statcheck!\n [K]nife!\n [I]nventory!\n ")
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
		TLB.SharpKnife("Josephine","IronKnife10","Wind")
	elif choice == "I" or choice == "i":
		choice=input("Use which Item?\n [P]otion!\n [R]ed Apple!\n ")
		if choice == "P" or choice == "p":
			Items.HealthPotion("Josephine")
		elif choice == "R" or choice == "r":
			Items.RedApple("Josephine")
#Numbereds
def Four(Four):
	u=Four
	choice=input("Select an Action!\n [ST] Statcheck!\n [FW] The Fourth Whip!\n ")
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
	elif choice == "FW" or choice == "fw":
		choice=input("Select a Whip Action!\n [At]tacks!\n [Sk]ills!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.Whip("Four","ReinforcedBronzeWhip10")
		elif choice == "Sk" or choice == "SK" or choice == "sk":
			choice=input("Select a Skill!\n [Bu]rning Lash!\n [Se]rpent's Coil!\n ")
			if choice == "BU" or choice == "bu" or choice == "Bu":
				SLB.BurningLash("Four","ReinforcedBronzeWhip10")
			elif choice == "Se" or choice == "se" or choice == "SE":
				SLB.SerpentCoil("Four","ReinforcedBronzeWhip10")
def One(One):
	u=One
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
	choice = input("Select something!\n [ST] Statcheck!\n ")
	if choice == "ST" or choice == "st":
		print("These are",u+"'s stats, so far!")
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
def Six(Six):
	u=Six
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
	choice = input("Select something!\n [ST] Statcheck!\n [FL] Flail Actions!\n ")
	if choice == "ST" or choice == "st":
		print("These are Six's stats, so far!")
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
	elif choice == "FL" or choice == "fl":
		choice = input("Select a thing!\n [A] Attack!\n [S] Skill!\n ")
		if choice == "At" or choice == "at" or choice == "AT":
			TLB.SixthFlail("Six","NormalCobaltFlail10")
		elif choice == "SK" or choice == "sk" or choice == "Sk":
			choice=input("Select a Skill!\n [Fu]ry Twirl!\n [Ja]wbreaker!\n ")
			if choice == "fu" or choice == "FU" or choice == "Fu":
				SLB.FuryTwirlFinisher("Six","NormalCobaltFlail10")
			elif choice == "JA" or choice == "Ja" or choice == "ja":
				SLB.JawbreakerFinisher("Six","NormalCobaltFlail10")
def Eleven(Eleven):
	u = Eleven
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
	choice = input("Select something!\n [ST] Statcheck!\n [WL] Weapons list!\n")
	if choice == "ST" or choice == "st":
		print("These are Eleven's stats, so far!")
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
	elif choice == "WL" or choice == "wl" or choice == "Weapons List" or choice == "weapons list":
		choice = input("Select a weapon!\n [TT] Tin Talis, for Throwing!\n ")
		if choice == "TT" or choice == "tt":
			choice = input("[At]tacks!\n ==SKILLS==\n [FB] Flame Blast!\n [WG] Water Grenade!\n [SB] Stun Bolt!\n ")
			if choice == "AT" or choice == "At" or choice == "at":
				TLB.TalisToss("Eleven","NormalTinTalis3")
			elif choice == "FB" or choice == "fb" or choice == "Fire Blast" or choice == "fire blast":
				SLB.FireBlast("Eleven","NormalTinTalis3")
			elif choice == "WG" or choice == "wg" or choice == "Water Grenade" or choice == "water grenade":
				SLB.WaterGrenade("Eleven","NormalTinTalis3")
			elif choice == "SB" or choice == "sb":
				SLB.StunBolt("Eleven","NormalTinTalis3")
def Twins(Two):
	u=Two
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
	choice = input("Select something!\n [ST] Statcheck!\n [K]nuckles!\n ")
	if choice == "ST" or choice == "st":
		print("These are the stats for the Twin Suppliers, currently!")
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
	elif choice == "AT" or choice == "At" or choice == "at":
		TLB.BareKnuckles("Two","BoneLeatherKnuckles4")
				
def Reintaur(Reintaur):
	choice=input("Select an Action!\n [ST] Statcheck!\n [WC] Wooden Crossbow!\n ")
	u=Reintaur
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
	elif choice == "WC" or choice == "wc":
		choice=input("Select a Crossbow Action!\n [At]tacks!\n [Ho]olepunch, Corrected!\n [Ne]edleround, Corrected!\n ")
		if choice == "AT" or choice == "At" or choice == "at":
			TLB.CrossbowCorrecter("Reintaur","CottonWoodCrossbow5")
		elif choice == "HO" or choice == "ho" or choice == "Ho":
			SLB.CorrectHolepunch("Reintaur","CottonWoodCrossbow5")
		elif choice == "Ne" or choice == "ne" or choice == "NE":
			SLB.CorrectNeedleround("Reintaur","CottonWoodCrossbow5")

def Wander(Wander):
	u=Wander
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
	choice = input("Select something!\n [ST] Statcheck!\n [SM] Support Magic!\n [At]tacks!\n ")
	if choice == "ST" or choice == "st":
		print("These are Wander's stats, so far!")
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
	elif choice == "At" or choice == "at" or choice == "AT":
		TLB.RodShot("Wander","CopperRod0")
	elif choice == "SM" or choice == "sm":
		choice=input("Select a Support Spell!\n [HR] Healthy Ray!\n [HG] Healthy Glow!\n [RR] Restorative Ray!\n ")
		if choice == "HR" or choice == "hr":
			SLB.HealthyRay("Wander","CopperRod0")
		elif choice == "hg" or choice == "HG":
			SLB.HealthyGlow("Wander","CopperRod0")
		elif choice == "RR" or choice == "rr":
			SLB.RestorativeRay("Wander","CopperRod0")

def Janet(Janet):
	u = Janet
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
	choice = input("Select something!\n [ST] Statcheck!\n [XB] Electric Tin Crossbow+2!\n ")
	if choice == "ST" or choice == "st":
		print("These are Janet's stats, so far!")
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
	elif choice == "XB" or choice == "xb" or choice == "Crossbow" or choice == "crossbow" or choice == "Xbow" or choice == "xbow":
		choice = input("Select an Action!\n [At]tack!\n [HP] Holepunch!\n [NR] Needleround!\n ")
		if choice == "AT" or choice == "At" or choice == "at":
			TLB.CrushingCrossbowCorrectionCrusader("Janet","ElectricTinCrossbow2","Lightning")
		elif choice == "NR" or choice == "nr" or choice == "Needleround" or choice == "needleround":
			SLB.CorrectCrusadeCrusherNeedleround("Janet","ElectricTinCrossbow2")
		elif choice == "HP" or choice == "hp" or choice == "Holepunch" or choice == "holepunch":
			SLB.CorrectCrusadeCrusherHolepunch("Janet","ElectricTinCrossbow2")