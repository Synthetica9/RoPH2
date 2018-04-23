import TLB
import SLB
from WSD import WSD
def Jelloween(Jelloween):
	u = Jelloween
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uLCK=u+"LCK"
	choice = input("Select a thing!\n [ST]Statcheck!\n [BS] Bodyslam!\n [EH] Earthen Hammer!\n ")
	if choice == "ST" or choice == "st":
		print("These are Jelloween's stats, so far!")
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
		print("-----------------")
	if choice == "BS" or choice == "bs" or choice == "Bodyslam" or choice == "bodyslam":
		TLB.Bodyslam("Jelloween")
	elif choice == "EH" or choice == "eh" or choice == "Earthen Hammer" or choice == "earthen hammer":
		SLB.EarthenHammer("Jelloween","NormalIvoryWand3")
def Dracula(Dracula):
	u = Dracula
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uLCK=u+"LCK"
	choice = input("Select a thing!\n [ST]Statcheck!\n [At]tack!\n [VB] Vampire Blade!\n [HP] Health Leech!\n [SB] Savage Bite!\n ")
	if choice == "ST" or choice == "st":
		print("These are Dracula's stats, so far!")
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
		print("-----------------")
	elif choice == "VB" or choice == "vb" or choice == "Vampire Blade" or choice == "vampire blade":
		SLB.VampireBlade("Dracula","NormalTungstenSword2")
	elif choice == "HP" or choice == "hp" or choice == "Health Leech" or choice == "HP Leech" or choice == "health leech" or choice == "hp leech":
		SLB.HPLeech("Dracula","NormalGoldRod3")
	elif choice == "AT" or choice == "At" or choice == "at":
		TLB.Claw("Dracula","NormalCobaltClaw2","Null")
	elif choice == "SB" or choice == "sb" or choice == "Sb":
		TLB.SavageBite("Dracula")

def Lumburn(Lumburn):
	u=Lumburn
	uSTR=u+"STR"
	uSPR=u+"SPR"
	uSKL=u+"SKL"
	uABL=u+"ABL"
	uAGI=u+"AGI"
	uEVA=u+"EVA"
	uTGH=u+"TGH"
	uRES=u+"RES"
	uLCK=u+"LCK"
	choice = input("Select a thing!\n [S]tat check!\n [BA] Breath Attack!\n [FB] Flame Blast!\n [F] Fireball!\n ")
	if choice == "S" or choice == "s" or choice == "ST" or choice == "st":
		print("These are the stats for",u,"so far!")
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
		print("-----------------")
	elif choice == "BA" or choice == "ba":
		SLB.BreathAttack("Lumburn","Flame")
	elif choice == "FB" or choice == "fb":
		SLB.FlameBlast("Lumburn","NormalIvoryRod1")
	elif choice == "BS" or choice == "bs":
		SLB.Bodyslam("Lumburn")
	elif choice == "F" or choice == "f":
		SLB.Fireball("Lumburn","NormalIvoryRod1")