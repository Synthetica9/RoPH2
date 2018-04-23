from WSD2 import WSD
from WSD2 import Unit
from WeaponsOO import OmniWeaponData
from ArmorsOO import OmniArmorData
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
Null=Element("None","Nada","Nope","Nothing")

#Flame=Element("Flame","Earth","Water","Burning")
#Earth=Element("Earth","Lightning","Flame","Silence")
#Lightning=Element("Lightning","Water","Earth","Shocked")
#Water=Element("Water","Flame","Lightning","Waterlogged")

#Solar=Element("Solar","Shadow","Lunar","???")
#Shadow=Element("Shadow",

class Equipment():
	def __init__(self,Unit):
		self.Unit=Unit
		self.Stats=Unit.Stats

class MultiWeapon():
	def __init__(self,Weapon,Unit,Element,DMod,HMod):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.DMod=DMod
		self.HMod=HMod
		self.PMod=PMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def BraveLeap(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		hit=round(35-HMod-(self.Unit.LCK-self.Unit.STR*0.25-self.ATA*0.5)+(WSD[Target].EVA))
		damage=round((self.Unit.STR+self.Unit.WT*1.25)*DMod+self.PDMG-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"


class Weaponless():
	def __init__(self,Unit,Element,DMod,HMod,PMod):
		self.Unit=WSD[Unit]
		self.Element=Element
		self.DMod=DMod
		self.HMod=HMod
		self.PMod=PMod
		self.Name=Unit
	@property
	def WebShot(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		hit=round(50-HMod-self.Unit.LCK-self.Unit.SKL*0.25-self.Unit.ABL+WSD[Target].EVA)
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SKL*0.75+self.Unit.ABL*0.25)-(WSD[Target].PDEF))
		def SnareProc(Target,PMod):
			if ra.randint(1,100) >= 65-PMod+WSD[Target].STR*0.75:
				print("You Snared",Target+"!")
			else:
				print("You didn't Snare",Target+"...")
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print("Additionally,",Target,"is Snared!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
					SnareProc(Target,PMod)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print("Additionally,",Target,"is Snared!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
					SnareProc(Target,PMod)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
				print("Additionally,",Target,"is Snared!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
					SnareProc(Target,PMod)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
				print("Additionally,",Target,"is Snared!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
					SnareProc(Target,PMod)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def SavageBite(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round(PMod*5+self.Unit.STR*0.35+self.Unit.ABL*0.15-WSD[Target].PDEF)
		hit=round(60-self.Unit.LCK-self.Unit.AGI+WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def BreathAttack(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((PMod*5+self.Unit.SPR*0.35+self.Unit.ABL*0.15)-(WSD[Target].MDEF))
		hit=round((35-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Pickpocket(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		PMod=self.PMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		proc=(50-self.Unit.ABL+WSD[Target].AGI-PMod)
		struggle=(50-self.Unit.STR+WSD[Target].STR)
		print("================================")
		if ra.randint(1,100) >= crit:
			print("CRITICAL!",u,"stole a random item without being noticed!")
		else:
			if ra.randint(1,100) >= proc:
				print(u,"quietly stole an item from",e+".")
			else:
				if ra.randint(1,100) >= struggle:
					print(u,"won the power struggle and stole an item!")
					print("However,",u,"is now being targeted by",e+"!")
				else:
					print(u,"lost the power struggle and did not steal the item successfully...")
					print("At least",e,"isn't targeting you, though.")
		print("================================")
		return "================================"
	@property
	def Bodyslam(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		hit=round(35-HMod-(self.Unit.LCK-self.Unit.STR*0.25)+(WSD[Target].EVA))
		damage=round((self.Unit.STR+self.Unit.WT)*DMod-(WSD[Target].PDEF)+PMod*5)
		crit=(100-self.Unit.LCK*0.5-cBST)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def EyeLaser(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		hit=round(20-HMod-(self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25)+(WSD[Target].EVA))
		damage=round(PMod*5+(self.Unit.SKL+self.Unit.ABL*0.35)*DMod-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"

class Weapon():
	def __init__(self,Weapon,Unit,Equipment):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Equipment=Equipment
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]

class Flail():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0,BMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.BMod=BMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def Jawbreaker(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		BMod=self.BMod
		damage=round((self.Unit.STR*1.1+self.Unit.ABL*0.25)-(WSD[Target].TGH-WSD[Target].PAR*0.15))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=round(50-HMod-self.Unit.LCK-self.Unit.AGI*0.65-self.Unit.STR*0.35+WSD[Target].EVA-self.ATA)
		print("================================")
		print(self.Name,"has spent 25 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		BMod=self.BMod
		damage=round((self.Unit.STR*1.1+self.Unit.ABL*0.25)-(WSD[Target].TGH*(0.9-BMod)-WSD[Target].PAR))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=round(35-HMod-self.Unit.LCK-self.Unit.AGI*0.65-self.Unit.STR*0.35+WSD[Target].EVA-self.ATA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		BMod=self.BMod
		damage=round((self.Unit.STR*1.1+self.Unit.ABL*0.25)-(WSD[Target].TGH*(0.8-BMod)-WSD[Target].PAR))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=round(50-HMod-self.Unit.LCK-self.Unit.AGI*0.65-self.Unit.STR*0.35+WSD[Target].EVA-self.ATA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		BMod=self.BMod
		damage=round((self.Unit.STR*1.1+self.Unit.ABL*0.25)-(WSD[Target].TGH*(0.7-BMod)-WSD[Target].PAR))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=round(65-HMod-self.Unit.LCK-self.Unit.AGI*0.65-self.Unit.STR*0.35+WSD[Target].EVA-self.ATA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"

class Warhammer():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*1.33+self.Unit.ABL*0.25)*DMod)-(WSD[Target].PDEF))
		hit=round((40-HMod-self.Unit.AGI*0.5-self.Unit.STR*0.25-self.ATA)+(WSD[Target].EVA))
		crit=(100-self.Unit.LCK*0.5-cBST)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*1.33+self.Unit.ABL*0.25)*1.25*DMod)-(WSD[Target].PDEF))
		hit=round((55-HMod-self.Unit.AGI*0.5-self.Unit.STR*0.25-self.ATA)+(WSD[Target].EVA))
		crit=(100-self.Unit.LCK*0.5-cBST)
		print("================================")
		print(self.Name,"has spent 24 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*1.33+self.Unit.ABL*0.25)*1.5*DMod)-(WSD[Target].PDEF))
		hit=round((70-HMod-self.Unit.AGI*0.5-self.Unit.STR*0.25-self.ATA)+(WSD[Target].EVA))
		crit=(100-self.Unit.LCK*0.5-cBST)
		print("================================")
		print(self.Name,"has spent 36 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"

class Saber():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL*0.25+self.PDMG)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(20-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 5 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL*0.25*self.DMod)+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL*0.25+self.PDMG)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(50-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def FuryThrust(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL*0.25)*1.4)*self.DMod)+self.PDMG)-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(65-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def BeginnersParry(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL*0.25+self.PDMG)*1.15)-(WSD[Target].PDEF)
		damage2=((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL*0.25+self.PDMG)*0.15)-(WSD[Target].PDEF)
		Hit=0
		Proc=(75-self.Unit.LCK-self.Unit.SKL*0.15-self.Unit.STR*0.15-self.Unit.EVA+WSD[Target].AGI)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= Proc:
					print("Damage dealt to",Target,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= Proc:
					print("Damage dealt to",Target,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("Damage dealt to",Target,"is", round(damage2*0.8), self.Element.StatusProc)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= Proc:
					print("Damage dealt to",Target,"is", round(damage1*0.5))
				else:
					print("Damage dealt to",Target,"is", round(damage2*0.5))
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is",round(damage1*2))
			else:
				if ra.randint(1,100) >= Proc:
					print("Damage dealt to",Target,"is", round(damage1))
				else:
					print("Damage dealt to",Target,"is", round(damage2))
		print("================================")
		return "================================"
	@property
	def TripleCombo(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round(((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL+self.PDMG*0.25)*0.85)-(WSD[Target1].PDEF))
		damage2=round(((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL+self.PDMG*0.25)*0.85)-(WSD[Target2].PDEF))
		damage3=round(((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL+self.PDMG*0.25)*0.85)-(WSD[Target3].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(35-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA)
		hit2=(35-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA)
		hit3=(35-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def SaberSlap(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SKL*0.5+self.Unit.ABL*0.25*self.DMod)+self.PDMG)-(WSD[Target].PDEF)*0.5)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI*0.5-self.Unit.SKL*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect, AND your target is Dazed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
					print(self.DazeProc(Target))
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect, AND your target is Dazed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc,self.DazeProc(Target))
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2),"and your target is Dazed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5),self.DazeProc(Target))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect, AND your target is Dazed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage,self.DazeProc(Target))
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def DazeProc(self,Target):
		Chance=(60-self.Unit.LCK-self.Unit.STR*0.25+WSD[Target].TGH*1.25)
		if ra.randint(1,100) >= Chance:
			print("Target is Dazed.")
		else:
			print('Target is not Dazed.')
	@property
	def BlazingCutlass(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR*0.5+self.Unit.SPR*0.5+self.Unit.ABL*0.25)*self.DMod+self.MDMG)-(WSD[Target].MDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI*0.5-self.Unit.SPR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Saber("NormalUnobtaniumSaber0","Dummy",Null,1,0)
SharpSaber=Saber("NormalUnobtaniumSaber0","Dummy",Null,1.25,0)
SightedSaber=Saber("NormalUnobtaniumSaber0","Dummy",Null,1,15)
SharpSightSaber=Saber("NormalUnobtaniumSaber0","Dummy",Null,1.25,15)
UnlearnedSaber=Saber("NormalUnobtaniumSaber0","Dummy",Null,0.5,0)

class Whip():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def BurningLash(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.6+self.Unit.SPR*0.6+self.Unit.ABL*0.15)*1)*self.DMod+self.MDMG)-(WSD[Target].MDEF*1.15)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.4)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF*1.15)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(25-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.4)*1)*self.DMod+self.PDMG)-(WSD[Target].PDEF*1.15)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 6 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.4)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF*1.15)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(45-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Whip("NormalUnobtaniumWhip0","Dummy",Null,1,0)

class Polearm():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def TripointBuster(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage1)
				else:
					print("You missed", Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage1)
				else:
					print("You missed", Target)
		#Doggos
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage1*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage1)
				else:
					print("You missed", Target)
		if self.Unit.STR >= WSD[Target].WT:
			print(Target,"is sent back 1 Zone!")
		else:
			print(Target,"stays in current Zone.")
		print("================================")
		return "================================"
	@property
	def Cutwo(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF))
		damage2=round((((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(30-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA)
		hit2=(30-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 8 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2)
				else:
					print("You missed",Target2)
	@property
	def PowerSlide(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		damage=round(((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def PiercingPounce(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG+self.Unit.WT)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(25-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def SixfoldThrust(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		hit2=(0-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		hit3=(0-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		hit4=(0-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		hit5=(0-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		hit6=(0-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 40 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(25-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 8 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*self.DMod)+self.PDMG-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		damage=round(((self.Unit.SKL*0.35+self.Unit.STR*0.65+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(55-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.ABL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		print("================================")
		print(self.Name,"has spent 16 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Polearm("NormalUnobtaniumPolearm0","Dummy",Null,1,0)
UnlearnedPolearm=Polearm("NormalUnobtaniumPolearm0","Dummy",Null,0.5,0)
PolearmPaladin=Polearm("NormalUnobtaniumPolearm0","Dummy",Null,1.35,0)
PolearmPractitioner=Polearm("NormalUnobtaniumPolearm0","Dummy",Null,1,30)
PaladinPractitioner=Polearm("NormalUnobtaniumPolearm0","Dummy",Null,1.35,30)
class Knife():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0,ProcMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
		self.ProcMod=ProcMod
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def BleedProc(self):
		if ra.randint(1,100) >= 70-self.ProcMod:
			return("You inflict Bleed!")
		else:
			return("You didn't inflict Bleed this time.")
	@property
	def CruelSlash(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1.5)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		print("================================")
		print(self.Name,"has spent 60 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2), "and your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5), self.BleedProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print(("Damage dealt to",Target,"is",damage), self.BleedProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Surprise(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		damage1=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PAR)
		damage2=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PAR)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-15-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		hit2=(0-15-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage1*1.2), self.Element.StatusProc, self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage1*0.8), self.Element.StatusProc, self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage1*0.5)*2)), "and your target is bleeding!"
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage1*0.5)), self.BleedProc
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is",damage1), self.BleedProc
				else:
					print("You missed",Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc, self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*0.8), self.Element.StatusProc, self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage2*0.5)*2)), "and your target is bleeding!"
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*0.5)), self.BleedProc
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is",damage2), self.BleedProc
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def PinpointStab(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		damage1=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PAR)
		damage2=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		Bypass=50-self.Unit.LCK+WSD[Target].EVA
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if ra.randint(1,100) >= Bypass:
			if eELM==Advantage: 
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is", round(damage1*1.2), self.Element.StatusProc, self.BleedProc)
					else:
						print("You missed",Target)
			elif eELM==Disadvantage:
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is", round(damage1*0.8), self.Element.StatusProc, self.BleedProc)
					else:
						print("You missed",Target)
			elif eELM==Same:
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round((damage1*0.5)*2)), "and your target is bleeding!"
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is", round(damage1*0.5)), self.BleedProc
					else:
						print("You missed",Target)
			else:
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is",damage1), self.BleedProc
					else:
						print("You missed",Target)
		else:
			if eELM==Advantage: 
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc, self.BleedProc)
					else:
						print("You missed",Target)
			elif eELM==Disadvantage:
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is", round(damage2*0.8), self.Element.StatusProc, self.BleedProc)
					else:
						print("You missed",Target)
			elif eELM==Same:
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round((damage2*0.5)*2)), "and your target is bleeding!"
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is", round(damage2*0.5)), self.BleedProc
					else:
						print("You missed",Target)
			else:
				if ra.randint(1,100) >= crit:
					print("Critical! Damage dealt to",Target,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
				else:
					if ra.randint(1,100) >= hit:
						print("Damage dealt to",Target,"is",damage2), self.BleedProc
					else:
						print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def TripleCombo(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.85)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.85)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.85)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(0-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(0-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND is Bleeding!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND is Bleeding!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2),"and your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
					print(self.BleedProc)
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1, self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND Bleed as well!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2),"and you inflicted Bleed as well!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2, self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed", Target2)
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND you inflicted Bleed!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND you inflicted Bleed!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2),"AND your target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
					print(self.BleedProc)
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "AND Bleeding status effects!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3, self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 2 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2)), "and your target is bleeding!"
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
					print(self.BleedProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		print("================================")
		print(self.Name,"has spent 5 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2)), "and your target is bleeding!"
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
					print(self.BleedProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		hit=(30-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2)), "and your target is bleeding!"
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
					print(self.BleedProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is bleeding!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
					print(self.BleedProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Knife("NormalUnobtaniumKnife0","Dummy",Null,1,0)
SharpKnife=Knife("NormalUnobtaniumKnife0","Dummy",Null,1.3,0,0)
SerratedKnife=Knife("NormalUnobtaniumKnife0","Dummy",Null,1,0,30)
SightedKnife=Knife("NormalUnobtaniumKnife0","Dummy",Null,1,30,0)
SharpSerratedKnife=Knife("NormalUnobtaniumKnife0","Dummy",Null,1.3,0,30)
SharpSerratedSightedKnife=Knife("NormalUnobtaniumKnife0","Dummy",Null,1.3,0,0)
UnlearnedKnife=Knife("NormalUnobtaniumKnife0","Dummy",Null,0.5,0,0)

class Knuckles():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def OldOneTwo(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=min(1,round((self.Unit.STR+self.Unit.ABL*0.35)*self.DMod+self.PDMG)-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(25-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		hit2=(25-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is",damage)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.35)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 0 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR+self.Unit.ABL*0.35)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.35)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 8 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def DigIn(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.35)*1.4)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Roundabout(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR+self.Unit.ABL*0.35)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect! Your target is also Stumbled!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, "and your target is also Stumbled!")
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect and your target is also Stumbled!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, "and your target is also Stumbled!")
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2),"and your target is also Stumbled!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5),"and your target is also Stumbled!")
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect and your target is also Stumbled!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage,"and your target is also Stumbled!")
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def DireImpact(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.35)*1.55)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def EruptionSlayer(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*2+self.Unit.ABL*0.35)*1.5)*self.DMod+self.PDMG)-(WSD[Target].PDEF)*1.5
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 120 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Knuckles("NormalUnobtaniumKnuckles0","Dummy",Null,1,0)
BareknuckleBoxer=Knuckles("NormalUnobtaniumKnuckles0","Dummy",Null,1.25,0)
BareknuckleBullseye=Knuckles("NormalUnobtaniumKnuckles0","Dummy",Null,1,25)
BareknuckleBullseyeBoxer=Knuckles("NormalUnobtaniumKnuckles0","Dummy",Null,1.25,25)
UnlearnedKnuckles=Knuckles("NormalUnobtaniumKnuckles0","Dummy",Null,0.5,0)

class Battlestaff():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def PogoPounce(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG+self.Unit.WT)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(50-HMod-self.Unit.STR*0.75-self.Unit.WT*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Skullcracker(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.25)*1.45)*self.DMod+self.PDMG+self.Unit.WT)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.STR*0.75-self.Unit.WT*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Crownbuster(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.25)*1.65)*self.DMod+self.PDMG+self.Unit.WT)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.STR*0.75-self.Unit.WT*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Four(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target].PDEF)*0.5
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 5 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		damage=round((self.Unit.STR+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(50-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 8 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(65-HMod-self.Unit.AGI*0.75-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Battlestaff("NormalUnobtaniumBattlestaff0","Dummy",Null,1,0)
BattlestaffBaser=Battlestaff("NormalUnobtaniumBattlestaff0","Dummy",Null,1.3,0)
BattlestaffBrandisher=Battlestaff("NormalUnobtaniumBattlestaff0","Dummy",Null,1,20)
BattlestaffBrandishBasher=Battlestaff("NormalUnobtaniumBattlestaff0","Dummy",Null,1.3,20)
UnlearnedBattlestaff=Battlestaff("NormalUnobtaniumBattlestaff0","Dummy",Null,0.5,0)

class Claw():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0,ProcMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
		self.ProcMod=ProcMod
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def DisarmProc(self):
		if ra.randint(1,100) >= 70-self.ProcMod:
			return "You Disarm your opponent!"
		else:
			return "You didn't disarm them this time."
	@property
	def Twisterush(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.4)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HeartlessThrust(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1.45)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(45-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 25 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2), "and your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5), self.DisarmProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.DisarmProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def BloodySlashes(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(95-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2), "and your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5), self.DisarmProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.DisarmProc)
				else:
					print("You missed",Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2), "and your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5), self.DisarmProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.DisarmProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 3 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2), "and your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5), self.DisarmProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.DisarmProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 6 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2), "and your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5), self.DisarmProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.DisarmProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(45-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 9 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect AND target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc, self.DisarmProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2), "and your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5), self.DisarmProc)
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect AND your target is Disarmed!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.DisarmProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Claw("NormalUnobtaniumClaw0","Dummy",Null,1,0,0)
ClawCutter=Claw("NormalUnobtaniumClaw0","Dummy",Null,1.3,0,0)
ClawCalibrator=Claw("NormalUnobtaniumClaw0","Dummy",Null,1,20,0)
ClawClasher=Claw("NormalUnobtaniumClaw0","Dummy",Null,1,0,20)
ClawClashCalibrator=Claw("NormalUnobtaniumClaw0","Dummy",Null,1,20,20)
ClawCutCalibrator=Claw("NormalUnobtaniumClaw0","Dummy",Null,1.3,20,0)
ClawCutClasher=Claw("NormalUnobtaniumClaw0","Dummy",Null,1.3,0,20)
CutClashCalibrator=Claw("NormalUnobtaniumClaw0","Dummy",Null,1.3,20,20)
UnlearnedClaw=Claw("NormalUnobtaniumClaw0","Dummy",Null,0.5,0,0)

class Bow():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def Snarrow(self):
		Target=input("Target is: ")
		HMod=self.HMod
		Hit=(50-HMod-self.Unit.LCK+WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if ra.randint >= Hit:
			print("You rooted",Target,"so they can't move for 2 turns!")
		else:
			print("You missed.")
		print("================================")
		return "================================"
	@property
	def Clipshot(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)*0.33)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(10-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Longshot(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(20-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.75+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(50-HMod-self.Unit.ABL-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 18 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Bow("NormalUnobtaniumBow0","Dummy",Null,1,0)
BowBraver=Bow("NormalUnobtaniumBow0","Dummy",Null,1.25,0)
BowHunter=Bow("NormalUnobtaniumBow0","Dummy",Null,1,25)
BraveBowHunter=Bow("NormalUnobtaniumBow0","Dummy",Null,1.25,25)
UnlearnedBow=Bow("NormalUnobtaniumBow0","Dummy",Null,0.5,0)

class Crossbow():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0,PMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
		self.PMod=PMod
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def Boombolt(self):
		Target=input("Target is: ")
		uELM=self.Element
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		cBST=float(input("User Crit Boost is: "))
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*self.DMod)+self.PDMG)-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=round((40-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Rebounder(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*self.DMod)*0.7+self.PDMG)-(WSD[Target].TGH-WSD[Target].PAR*(0.8-PMod)))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def InjectionRound(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target].TGH*0.25-WSD[Target].PAR))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(70-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 75 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Needlebolt(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target].TGH*0.5-WSD[Target].PAR))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(70-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 50 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Needleshot(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target].TGH*0.65-WSD[Target].PAR))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(70-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 35 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Needleround(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target].TGH*0.8-WSD[Target].PAR))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(70-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Holepunch(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target].TGH))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(70-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 25 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].TGH-WSD[Target].PAR*(0.9-PMod)))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round(((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].TGH-WSD[Target].PAR*(0.8-PMod)))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		PMod=self.PMod
		damage=round((((self.Unit.SKL*0.75+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].TGH-WSD[Target].PAR*(0.7-PMod)))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(50-HMod-self.Unit.ABL-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1,0)
Crusader=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1.15,0,0)
CrusadeCrusher=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1.15,0,0.25)
Corrector=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1,20,0)
Crusher=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1,0,0.25)
CorrectCrusher=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1,20,0.25)
CorrectCrusader=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1.15,20,0)
CorrectCrusadeCrusher=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,1.15,20,0.25)
UnlearnedCrossbow=Crossbow("NormalUnobtaniumCrossbow0","Dummy",Null,0.5,0,0)

class Handbow():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.5+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.ABL*0.75-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 7 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL*0.5+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.ABL*0.75-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL*0.5+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(45-HMod-self.Unit.ABL*0.75-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 13 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def TriplePlay(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL*0.5+self.Unit.ABL*0.25)*0.85)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL*0.5+self.Unit.ABL*0.25)*0.85)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.SKL*0.5+self.Unit.ABL*0.25)*0.85)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(15-HMod-self.Unit.ABL*0.75-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA)
		hit2=(15-HMod-self.Unit.ABL*0.75-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA)
		hit3=(15-HMod-self.Unit.ABL*0.75-self.Unit.SKL*0.25-self.Unit.LCK-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 9 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
#Default=Handbow("NormalUnobtaniumHandbow0","Dummy",Null,1,0)
HandbowHarmer=Handbow("NormalUnobtaniumHandbow0","Dummy",Null,1.2,0)
UnlearnedHandbow=Handbow("NormalUnobtaniumHandbow0","Dummy",Null,0.5,0)

class Rifle():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def Headshot(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL+self.Unit.ABL*0.5)*4)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(70-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent",round(self.Unit.ENE*0.4),"ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def PlasmaShell(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=damage=round(((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PAR*1.25-WSD[Target1].TGH)
		damage2=damage=round(((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PAR*1.25-WSD[Target2].TGH)
		damage3=damage=round(((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PAR*1.25-WSD[Target3].TGH)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-25-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA)
		hit2=(0-25-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA)
		hit3=(0-25-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def DispersionBlast(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL+self.Unit.ABL*0.5)*self.DMod+self.PDMG)-(WSD[Target].PAR*1.5)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-25-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def PiercingLaser(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod

		damage1=round(((self.Unit.SKL+self.Unit.ABL*0.5)*self.DMod)*0.75+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL+self.Unit.ABL*0.5)*self.DMod)*0.75+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(15-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA)
		hit2=(15-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-50-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL+self.Unit.ABL*0.5)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-25-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL+self.Unit.ABL*0.5)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-HMod-self.Unit.ABL*0.5-self.Unit.SKL*0.5-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 45 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Rifle("NormalUnobtaniumRifle0","Dummy",Null,1,0)
ScopedSight=Rifle("NormalUnobtaniumRifle0","Dummy",Null,1,30)
RifleGrip=Rifle("NormalUnobtaniumRifle0","Dummy",Null,1.3,0)
ScopedGrip=Rifle("NormalUnobtaniumRifle0","Dummy",Null,1.3,30)

class Talis():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.ABL*0.25+self.Unit.SPR*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-HMod-self.Unit.ABL*0.75-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR*0.5+self.Unit.ABL*0.25+self.Unit.SPR*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(20-HMod-self.Unit.ABL*0.75-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 8 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.ABL*0.25+self.Unit.SPR*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.ABL*0.75-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Talis("NormalUnobtaniumTalis0","Dummy",Null,1,0)
UnlearnedTalis=Talis("NormalUnobtaniumTalis0","Dummy",Null,0.5,0)
TalisTosser=Talis("NormalUnobtaniumTalis0","Dummy",Null,1.2,0)
TalisTargeter=Talis("NormalUnobtaniumTalis0","Dummy",Null,1,25)
TargetTosser=Talis("NormalUnobtaniumTalis0","Dummy",Null,1.2,25)

class Cane():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def WeakHealT1(self):
		Target1=input("Ally 1 is: ")
		Target2=input("Ally 2 is: ")
		Target3=input("Ally 3 is: ")
		Health1=round((((self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Target1].HP*0.1)*0.5)+self.MDMG))
		Health2=round((((self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Target2].HP*0.1)*0.5)+self.MDMG))
		Health3=round((((self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Target3].HP*0.1)*0.5)+self.MDMG))
		print("================================")
		print(self.Name,"has spent 5 ENE.")
		print(Target1,"heals for",heal1)
		print(Target2,"heals for",heal2)
		print(Target3,"heals for",heal3)
		print("================================")
		return "================================"
	@property
	def MidHealT1(self):
		Target1=input("Ally 1 is: ")
		Target2=input("Ally 2 is: ")
		Health1=round((((self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Target1].HP*0.1)*1)+self.MDMG))
		Health2=round((((self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Target2].HP*0.1)*1)+self.MDMG))
		print("================================")
		print(self.Name,"has spent 5 ENE.")
		print(Target1,"heals for",heal1)
		print(Target2,"heals for",heal2)
		print("================================")
		return "================================"
	@property
	def StrongHealT1(self):
		Target1=input("Ally 1 is: ")
		Health1=round((((self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Target1].HP*0.1)*1.5)+self.MDMG))
		print("================================")
		print(self.Name,"has spent 5 ENE.")
		print(Target1,"heals for",heal1)
		print("================================")
		return "================================"
	@property
	def Morningstar(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SPR*0.25+self.Unit.ABL*0.25)*1.4)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(15-HMod-self.Unit.AGI-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Mace(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SPR*0.25+self.Unit.ABL*0.25)*1.3)*self.DMod)+self.PDMG-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(25-HMod-self.Unit.AGI-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Club(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SPR*0.25+self.Unit.ABL*0.25)*1.2)*self.DMod)+self.PDMG-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.AGI-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Cudgel(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SPR*0.25+self.Unit.ABL*0.25)*1.1)*self.DMod)+self.PDMG-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(45-HMod-self.Unit.AGI-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SPR*0.25+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.AGI-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 1 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.STR*0.5+self.Unit.SPR*0.25+self.Unit.ABL*0.25)*self.DMod)+self.PDMG-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(55-HMod-self.Unit.AGI-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 4 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*0.5+self.Unit.SPR*0.25+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(70-HMod-self.Unit.AGI-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 7 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Cane("NormalUnobtaniumCane0","Dummy",Null,1,0)
UnlearnedCane=Cane("NormalUnobtaniumCane0","Dummy",Null,0.5,0)
CaneCrusher=Cane("NormalUnobtaniumCane0","Dummy",Null,1.3,0)
CaneCorrector=Cane("NormalUnobtaniumCane0","Dummy",Null,1,15)
CrushingCaneCorrector=Cane("NormalUnobtaniumCane0","Dummy",Null,1.3,15)

class Wand():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*0.75)*self.DMod+self.MDMG)-(WSD[Target].MDEF*0.8))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*self.DMod+self.MDMG)-(WSD[Target].MDEF*0.8))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-15-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*1.25)*self.DMod+self.MDMG)-(WSD[Target].MDEF*0.8))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(0-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Wand("NormalUnobtaniumWand0","Dummy",Null,1,0)
WandWarrior=Wand("NormalUnobtaniumWand0","Dummy",Null,1.3,0)
WandCorrector=Wand("NormalUnobtaniumWand0","Dummy",Null,1,30)
CorrectWandWarrior=Wand("NormalUnobtaniumWand0","Dummy",Null,1.3,30)
UnlearnedWand=Wand("NormalUnobtaniumWand0","Dummy",Null,0.5,0)
	
class OffenseSpell():
	def __init__(self,Weapon,Unit,Element,DMod,HMod,EMod):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Name=Unit
		self.HMod=HMod
		self.DMod=DMod
		self.EMod=EMod
	@property
	def StatusProc(self):
		if ra.randint(1,100) >= 75-self.EMod:
			return "and you inflict the status",self.Element.Status
		else:
			return "and you inflict no status at all."
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def FunnelFury(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR*1.35+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((35-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 40 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def WindyWhirl(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*0.35+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*0.35+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target2].MDEF))
		damage3=round((self.Unit.SPR*0.35+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target3].MDEF))
		hit1=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA))
		hit2=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA))
		hit3=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target3].EVA))
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		if e3ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*1.2), self.StatusProc)
				else:
					print("You missed",Target3)
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.StatusProc)
				else:
					print("You missed",Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed",Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is",damage3, self.StatusProc)
				else:
					print("You missed",Target3)
		print("================================")
		return "================================"
	@property
	def WindyEdge(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR*0.65+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((40-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def DizzyDisc(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR+self.Unit.ABL*0.25)*0.5*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((10-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the Dizzy status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.DizzyProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the Dizzy status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.DizzyProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the Dizzy status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.DizzyProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def DizzyProc(self):
		if ra.randint(1,100) >= 45:
			return "and you inflict the status Dizzy."
		else:
			return "and you inflict no status at all."
	@property
	def GaiaHammer(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*1.15+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*1.15+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target2].MDEF))
		damage3=round((self.Unit.SPR*1.15+self.Unit.ABL*0.35)*DMod+self.MDMG-(WSD[Target3].MDEF))
		hit1=round((25-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target1].EVA))
		hit2=round((25-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target2].EVA))
		hit3=round((25-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target3].EVA))
		print("================================")
		print(self.Name,"has spent 0 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print(("Damage dealt to",self.Name,"is",damage1*1.2)*2)
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
					print("Damage dealt to",self.Name,"is",damage1*1.2)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print(("Damage dealt to",self.Name,"is",damage1*0.8)*2)
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
					print("Damage dealt to",self.Name,"is",damage1*0.8)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
				print(("Damage dealt to",self.Name,"is",damage1*0.5)*2)
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
					print("Damage dealt to",self.Name,"is",damage1*0.5)
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
					print("Damage dealt to",self.Name,"is",damage1)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print(("Damage dealt to",self.Name,"is",damage2*1.2)*2)
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
					print("Damage dealt to",self.Name,"is",damage2*1.2)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print(("Damage dealt to",self.Name,"is",damage2*0.8)*2)
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
					print("Damage dealt to",self.Name,"is",damage2*0.8)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
				print(("Damage dealt to",self.Name,"is",damage2*0.5)*2)
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
					print(("Damage dealt to",self.Name,"is",damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
				print("Damage dealt to",self.Name,"is",damage2*2)
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
					print("Damage dealt to",self.Name,"is",damage2)
				else:
					print("You missed",Target2)
		if e3ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print(("Damage dealt to",self.Name,"is",damage3*1.2)*2)
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*1.2), self.StatusProc)
					print(("Damage dealt to",self.Name,"is",damage3*1.2))
				else:
					print("You missed",Target3)
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
				print(("Damage dealt to",self.Name,"is",damage3*0.8)*2)
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.StatusProc)
					print(("Damage dealt to",self.Name,"is",damage3*0.8))
				else:
					print("You missed",Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
				print(("Damage dealt to",self.Name,"is",damage3*0.5)*2)
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
					print(("Damage dealt to",self.Name,"is",damage3*0.5))
				else:
					print("You missed",Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
				print("Damage dealt to",self.Name,"is",damage3*2)
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is",damage3, self.StatusProc)
					print("Damage dealt to",self.Name,"is",damage3)
				else:
					print("You missed",Target3)
		print("================================")
		return "================================"
	@property
	def ShockwaveSplitter(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR+self.Unit.ABL*0.25)*0.66*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR+self.Unit.ABL*0.25)*0.66*DMod+self.MDMG-(WSD[Target2].MDEF))
		hit1=round((40-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target1].EVA))
		hit2=round((40-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target2].EVA))
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		print("================================")
		return "================================"
	@property
	def PoisonProc(self):
		if ra.randint(1,100) >= 33:
			return "and you inflict the status Poison."
		else:
			return "and you inflict no status at all."
	@property
	def PoisonVines(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR+self.Unit.ABL*0.25)*0.5*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((45-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the Poison status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.PoisonProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the Poison status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.PoisonProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the Poison status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.PoisonProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def RazorLeaves(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR+self.Unit.ABL*0.25)*0.7*DMod+self.MDMG-(WSD[Target].MDEF))
		hit1=round((45-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target].EVA))
		hit2=round((45-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target].EVA))
		hit3=round((45-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
	@property
	def BurningSoul(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*1.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*1.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target2].MDEF))
		damage3=round((self.Unit.SPR*1.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target3].MDEF))
		hit1=round((25-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target1].EVA))
		hit2=round((25-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target2].EVA))
		hit3=round((25-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target3].EVA))
		print("================================")
		print(self.Name,"has spent 40 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		if e3ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*1.2), self.StatusProc)
				else:
					print("You missed",Target3)
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.StatusProc)
				else:
					print("You missed",Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed",Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is",damage3, self.StatusProc)
				else:
					print("You missed",Target3)
		print("================================")
		return "================================"
	@property
	def CrescentBurner(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		Target4=input("Target 4 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		e4ELM=WSD[Target4].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		EMod=self.EMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR+self.Unit.ABL*0.25)*DMod-(WSD[Target1].MDEF)*0.33)
		damage2=round((self.Unit.SPR+self.Unit.ABL*0.25)*DMod-(WSD[Target2].MDEF)*0.33)
		damage3=round((self.Unit.SPR+self.Unit.ABL*0.25)*DMod-(WSD[Target3].MDEF)*0.33)
		damage4=round((self.Unit.SPR+self.Unit.ABL*0.25)*DMod-(WSD[Target4].MDEF)*0.33)
		hit1=round((35-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target1].EVA))
		hit2=round((35-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target2].EVA))
		hit3=round((35-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target3].EVA))
		hit4=round((35-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target4].EVA))
		print("================================")
		print(self.Name,"has spent 40 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		if e3ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*1.2), self.StatusProc)
				else:
					print("You missed",Target3)
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.StatusProc)
				else:
					print("You missed",Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed",Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is",damage3, self.StatusProc)
				else:
					print("You missed",Target3)
		if e4ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage4*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage4*1.2), self.StatusProc)
				else:
					print("You missed",Target4)
		elif e4ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage4*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage4*0.8), self.StatusProc)
				else:
					print("You missed",Target4)
		elif e4ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage4*0.5)*2))
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage4*0.5))
				else:
					print("You missed",Target4)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round(damage4*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is",damage4, self.StatusProc)
				else:
					print("You missed",Target4)
		print("================================")
		return "================================"
	@property
	def Firebolt(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target].MDEF*0.85))
		hit=round((45-HMod-self.Unit.LCK-self.Unit.SPR*0.25)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 25 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def StunBolt(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((40-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def Fireball(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((40-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def IceKnife(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((40-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def EarthenHammer(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((40-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def WindyWhip(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage=round((self.Unit.SPR*0.5+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target].MDEF))
		hit=round((40-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA))
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def DoubleZap(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target2].MDEF))
		hit1=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA))
		hit2=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA))
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		print("================================")
		return "================================"
	@property
	def FlameBlast(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target2].MDEF))
		hit1=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA))
		hit2=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA))
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		print("================================")
		return "================================"
	@property
	def WaterGrenade(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target2].MDEF))
		hit1=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA))
		hit2=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA))
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		print("================================")
		return "================================"
	@property
	def StoneFrag(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target2].MDEF))
		hit1=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA))
		hit2=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA))
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		print("================================")
		return "================================"
	@property
	def WindyWhirl(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		crit=(100-self.Unit.LCK*0.5-cBST)
		damage1=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target1].MDEF))
		damage2=round((self.Unit.SPR*0.25+self.Unit.ABL*0.25)*DMod+self.MDMG-(WSD[Target2].MDEF))
		hit1=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target1].EVA))
		hit2=round((30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target2].EVA))
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.StatusProc)
				else:
					print("You missed",Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed",Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is",damage1, self.StatusProc)
				else:
					print("You missed",Target1)
		if e2ELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*1.2), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.StatusProc)
				else:
					print("You missed",Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed",Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is",damage2, self.StatusProc)
				else:
					print("You missed",Target2)
		print("================================")
		return "================================"

class SupportSpell():
	def __init__(self,Weapon,Unit):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Name=Unit
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def HealthyGlow(self):
		Ally1=input("Ally 1 is: ")
		Ally2=input("Ally 2 is: ")
		Heal1=round(self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Ally1].HP*0.1+self.MDMG)
		Heal2=round(self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Ally2].HP*0.1+self.MDMG)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		print(Ally1,"is healed for",Heal1)
		print(Ally2,"is healed for",Heal2)
		print("================================")
		return "================================"
	@property
	def HealthyRay(self):
		Ally=input("Ally is: ")
		Heal=round(self.Unit.SPR*0.25+self.Unit.ABL*0.25+WSD[Ally].HP*0.25+self.MDMG)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		print(Ally,"is healed for",Heal)
		print("================================")
		return "================================"
		
class Rod():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def QATK(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SPR*1.25+self.Unit.ABL*0.25)*0.75)*self.DMod+self.MDMG)-(WSD[Target].MDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(30-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SPR*1.25+self.Unit.ABL*0.25)*self.DMod+self.MDMG)-(WSD[Target].MDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(45-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SPR*1.25+self.Unit.ABL*0.25)*1.25)*self.DMod+self.MDMG)-(WSD[Target].MDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(60-HMod-self.Unit.ABL-self.Unit.SPR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 25 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
#Default=Rod("NormalUnobtaniumRod0","Dummy",Null,1,0)
RodLoyalist=Rod("NormalUnobtaniumRod0","Dummy",Null,1.3,0)
RodReticule=Rod("NormalUnobtaniumRod0","Dummy",Null,1,30)
LoyalReticule=Rod("NormalUnobtaniumRod0","Dummy",Null,1.3,30)

class Slicer():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def QATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.STR*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.STR*0.75+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 8 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((self.Unit.STR*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((self.Unit.STR*0.75+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(10-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(10-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.STR*0.75+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.STR*0.75+self.Unit.ABL*0.25)*1.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 16 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
#Default=Slicer("NormalUnobtaniumSlicer0","Dummy",Null,1,0)
UnlearnedSlicer=Slicer("NormalUnobtaniumSlicer0","Dummy",Null,0.5,0)
SlicerSlasher=Slicer("NormalUnobtaniumSlicer0","Dummy",Null,1.25,0)
SlicerSighter=Slicer("NormalUnobtaniumSlicer0","Dummy",Null,1,25)
SightedSlicerSlasher=Slicer("NormalUnobtaniumSlicer0","Dummy",Null,1.25,25)

class Pistols():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def BladeBlast(self):
		Target1=input("Target 1 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		crit=(100-self.Unit.LCK*0.5-cBST)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*1)*self.DMod+self.PDMG)-(WSD[Target1].PDEF*0.85)
		hit1=(30-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		print("================================")
		print(self.Name,"has spent 28 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
	@property
	def ChargeShot(self):
		Target1=input("Target 1 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		crit=(100-self.Unit.LCK*0.5-cBST)
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*1.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		hit1=(45-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		print("================================")
		print(self.Name,"has spent 24 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
	@property
	def QATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(0-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 8 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(15-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(15-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 12 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*1.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL*0.65+self.Unit.ABL*0.35)*1.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(30-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(30-HMod-self.Unit.ABL*0.75-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 16 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
#Default=Pistols("NormalUnobtaniumTwinPistol0","Dummy",Null,1,0)
PistolPacker=Pistols("NormalUnobtaniumTwinPistol0","Dummy",Null,1.25,0)
PistolPinpoint=Pistols("NormalUnobtaniumTwinPistol0","Dummy",Null,1,30)
PinpointPacker=Pistols("NormalUnobtaniumTwinPistol0","Dummy",Null,1.25,30)

class Greatsword():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def Grandestine(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*2.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*2.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*2.5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 100 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def Headcleaver(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25*self.DMod)*1.5+self.PDMG)-(WSD[Target].PDEF*0.85))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(60-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 42 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def GreatGust(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		Proc1=(50-self.Unit.STR*1.25-self.WT+WSD[Target1].WT)
		Proc2=(50-self.Unit.STR*1.25-self.WT+WSD[Target2].WT)
		Proc3=(50-self.Unit.STR*1.25-self.WT+WSD[Target3].WT)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if ra.randint(1,100) >= Proc1:
			print(Target1,"was blown away.")
		else:
			print(Target1,"wasn't blown away.")
		if ra.randint(1,100) >= Proc2:
			print(Target2,"was blown away.")
		else:
			print(Target2,"wasn't blown away.")
		if ra.randint(1,100) >= Proc3:
			print(Target3,"was blown away.")
		else:
			print(Target3,"wasn't blown away.")
		print("================================")
		return "================================"
	@property
	def Sidebuster(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def HeavyStab(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25*self.DMod)+self.PDMG)-(WSD[Target].PDEF*0.85))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(40-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(40-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(40-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 9 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*1.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*1.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.33)*1.25)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(60-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(60-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(60-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 21 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"

#Default=Greatsword("NormalUnobtaniumGreatsword0","Dummy",Null,1,0)
GreatswordGutter=Greatsword("NormalUnobtaniumGreatsword0","Dummy",Null,1.5,0)
GreatswordGuide=Greatsword("NormalUnobtaniumGreatsword0","Dummy",Null,1,35)
GutterGuide=Greatsword("NormalUnobtaniumGreatsword0","Dummy",Null,1.5,35)
class GreatswordGrinder():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def Grandestine(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*2.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*2.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*2.5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 100 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def Headcleaver(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25*self.DMod)*1.5+self.PDMG)-(WSD[Target].PDEF*0.85))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(60-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 42 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def GreatGust(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		Proc1=(50-self.Unit.STR*1.25-self.WT+WSD[Target1].WT)
		Proc2=(50-self.Unit.STR*1.25-self.WT+WSD[Target2].WT)
		Proc3=(50-self.Unit.STR*1.25-self.WT+WSD[Target3].WT)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if ra.randint(1,100) >= Proc1:
			print(Target1,"was blown away.")
		else:
			print(Target1,"wasn't blown away.")
		if ra.randint(1,100) >= Proc2:
			print(Target2,"was blown away.")
		else:
			print(Target2,"wasn't blown away.")
		if ra.randint(1,100) >= Proc3:
			print(Target3,"was blown away.")
		else:
			print(Target3,"wasn't blown away.")
		print("================================")
		return "================================"
	@property
	def Sidebuster(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def HeavyStab(self):
		Target=input("Target is: ")
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25*self.DMod)+self.PDMG)-(WSD[Target].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(40-HMod-self.Unit.AGI-self.Unit.STR*0.25-self.Unit.LCK-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed",Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed",Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is",damage, self.Element.StatusProc)
				else:
					print("You missed",Target)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(40-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(40-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(40-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 9 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(50-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*1.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*1.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.STR*1.25+self.Unit.ABL*0.25)*0.67)*1.25)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(60-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(60-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(60-HMod-self.Unit.AGI-self.Unit.LCK-self.Unit.STR*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 21 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
#Default=GreatswordGrinder("NormalUnobtaniumGreatsword0","Dummy",Null,1,0)
GrindingGreatswordGutter=GreatswordGrinder("NormalUnobtaniumGreatsword0","Dummy",Null,1.5,0)
GrindingGreatswordGuide=GreatswordGrinder("NormalUnobtaniumGreatsword0","Dummy",Null,1,35)
GrindingGutterGuide=GreatswordGrinder("NormalUnobtaniumGreatsword0","Dummy",Null,1.5,35)

class Mechgun():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def SneakShooter(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round((self.Unit.SKL+self.Unit.ABL*0.25)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 35 ENE.")
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		#Doggos
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		print("================================")
		return "================================"
	@property
	def Unload(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		LVL=input("User level is: ")
		eELM=WSD[Target1].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL+self.Unit.ABL*0.25)+LVL*10)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		hit=0
		print("================================")
		print(self.Name,"has spent",self.Unit.ENE,"ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		print("================================")
		return "================================"
	@property
	def Bulletstorm(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		Target4=input("Target 4 is: ")
		Target5=input("Target 5 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		e4ELM=WSD[Target4].Element
		e5ELM=WSD[Target5].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		damage4=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*5)*self.DMod+self.PDMG)-(WSD[Target4].PDEF)
		damage5=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*5)*self.DMod+self.PDMG)-(WSD[Target5].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		hit4=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target4].EVA)
		hit5=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target5].EVA)
		print("================================")
		print(self.Name,"has spent 40 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		#Megaman
		if e4ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.5))
				else:
					print("You missed", Target4)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", damage1)
				else:
					print("You missed", Target4)
		if e5ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e5ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target5)
		elif e5ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.5))
				else:
					print("You missed", Target5)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", damage2)
				else:
					print("You missed", Target5)
	@property
	def HeavyRain(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*4)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*4)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*4)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def Downpour(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*4)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*4)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def Blitz(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		Target4=input("Target 4 is: ")
		Target5=input("Target 5 is: ")
		Target6=input("Target 6 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		e4ELM=WSD[Target4].Element
		e5ELM=WSD[Target5].Element
		e6ELM=WSD[Target6].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.45)*self.DMod+self.PDMG)-(WSD[Target1].PDEF))
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.45)*self.DMod+self.PDMG)-(WSD[Target2].PDEF))
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.45)*self.DMod+self.PDMG)-(WSD[Target3].PDEF))
		damage4=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.45)*self.DMod+self.PDMG)-(WSD[Target4].PDEF))
		damage5=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.45)*self.DMod+self.PDMG)-(WSD[Target5].PDEF))
		damage6=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.45)*self.DMod+self.PDMG)-(WSD[Target6].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		hit4=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target4].EVA)
		hit5=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target5].EVA)
		hit6=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target6].EVA)
		print("================================")
		print(self.Name,"has spent 54 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		#Megaman
		if e4ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.5))
				else:
					print("You missed", Target4)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", damage1)
				else:
					print("You missed", Target4)
		if e5ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e5ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target5)
		elif e5ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.5))
				else:
					print("You missed", Target5)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", damage2)
				else:
					print("You missed", Target5)
		#Doggos
		if e6ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e6ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target6,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target6)
		elif e6ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target6,"is", round(damage3*0.5))
				else:
					print("You missed", Target6)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target6,"is", damage3)
				else:
					print("You missed", Target6)
		print("================================")
		return "================================"
	@property
	def CircleSlider(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 27 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def RubberRounds(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		print("Deduct damage from enemy ENE!")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def Drizzle(self):
		Target1=input("Target 1 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*3)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		print("================================")
		print(self.Name,"has spent 10 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.3)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 3 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.SKL+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 6 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.7)*1.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.7)*1.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.7)*1.25)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 9 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
#Default=Mechgun("NormalUnobtaniumMechgun0","Dummy",Null,1,0)
MechgunMarker=Mechgun("NormalUnobtaniumMechgun0","Dummy",Null,1,25)
MechgunMalice=Mechgun("NormalUnobtaniumMechgun0","Dummy",Null,1.25,0)
MaliceMarker=Mechgun("NormalUnobtaniumMechgun0","Dummy",Null,1.25,25)
class MechgunManiac():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def Unload(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		LVL=input("User level is: ")
		eELM=WSD[Target1].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL+self.Unit.ABL*0.25)+LVL*10)*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		hit=0
		print("================================")
		print(self.Name,"has spent",self.Unit.ENE,"ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		print("================================")
		return "================================"
	@property
	def SneakShooter(self):
		Target=input("Target is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		eELM=WSD[Target1].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage=round(((self.Unit.SKL+self.Unit.ABL*0.25))*self.DMod+self.PDMG)-(WSD[Target].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target].EVA)
		print("================================")
		print(self.Name,"has spent 35 ENE.")
		if eELM==Advantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		#Doggos
		if eELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif eELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target)
		elif eELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round((damage*0.5)*2))
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", round(damage*0.5))
				else:
					print("You missed", Target)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target,"is", round(damage*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit:
					print("Damage dealt to",Target,"is", damage)
				else:
					print("You missed", Target)
		print("================================")
		return "================================"
	@property
	def Bulletstorm(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		Target4=input("Target 4 is: ")
		Target5=input("Target 5 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		e4ELM=WSD[Target4].Element
		e5ELM=WSD[Target5].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		damage4=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*5)*self.DMod+self.PDMG)-(WSD[Target4].PDEF)
		damage5=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*5)*self.DMod+self.PDMG)-(WSD[Target5].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		hit4=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target4].EVA)
		hit5=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target5].EVA)
		print("================================")
		print(self.Name,"has spent 40 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		#Megaman
		if e4ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.5))
				else:
					print("You missed", Target4)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", damage1)
				else:
					print("You missed", Target4)
		if e5ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e5ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target5)
		elif e5ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.5))
				else:
					print("You missed", Target5)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", damage2)
				else:
					print("You missed", Target5)
	@property
	def HeavyRain(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*4)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*4)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*4)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 30 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def Downpour(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*4)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*4)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		print("================================")
		return "================================"
	@property
	def Blitz(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		Target4=input("Target 4 is: ")
		Target5=input("Target 5 is: ")
		Target6=input("Target 6 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		e4ELM=WSD[Target4].Element
		e5ELM=WSD[Target5].Element
		e6ELM=WSD[Target6].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF))
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF))
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PDEF))
		damage4=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target4].PDEF))
		damage5=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target5].PDEF))
		damage6=round((((self.Unit.SKL+self.Unit.ABL*0.5)*0.75)*self.DMod+self.PDMG)-(WSD[Target6].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		hit4=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target4].EVA)
		hit5=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target5].EVA)
		hit6=(15-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target6].EVA)
		print("================================")
		print(self.Name,"has spent 54 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		#Megaman
		if e4ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target4)
		elif e4ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", round(damage1*0.5))
				else:
					print("You missed", Target4)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target4,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit4:
					print("Damage dealt to",Target4,"is", damage1)
				else:
					print("You missed", Target4)
		if e5ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e5ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target5)
		elif e5ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", round(damage2*0.5))
				else:
					print("You missed", Target5)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target5,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit5:
					print("Damage dealt to",Target5,"is", damage2)
				else:
					print("You missed", Target5)
		#Doggos
		if e6ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e6ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target6,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target6)
		elif e6ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target6,"is", round(damage3*0.5))
				else:
					print("You missed", Target6)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target6,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit6:
					print("Damage dealt to",Target6,"is", damage3)
				else:
					print("You missed", Target6)
		print("================================")
		return "================================"
	@property
	def CircleSlider(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 27 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def RubberRounds(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(0-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 20 ENE.")
		print("Deduct damage from enemy ENE!")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def Drizzle(self):
		Target1=input("Target 1 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*3)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		print("================================")
		print(self.Name,"has spent 9 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.75)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.75)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*0.6)*0.75)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(20-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 3 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round(((self.Unit.SKL+self.Unit.ABL*0.25)*0.8)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL+self.Unit.ABL*0.25)*0.8)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.SKL+self.Unit.ABL*0.25)*0.8)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(35-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target1=input("Target 1 is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round((((self.Unit.SKL+self.Unit.ABL*0.25)*1)*1.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round((((self.Unit.SKL+self.Unit.ABL*0.25)*1)*1.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round((((self.Unit.SKL+self.Unit.ABL*0.25)*1)*1.25)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 21 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
#Default=MechgunManiac("NormalUnobtaniumMechgun0","Dummy",Null,1,0)
ManicMechgunMarker=MechgunManiac("NormalUnobtaniumMechgun0","Dummy",Null,1,25)
ManicMechgunMalice=MechgunManiac("NormalUnobtaniumMechgun0","Dummy",Null,1.25,0)
ManicMaliceMarker=MechgunManiac("NormalUnobtaniumMechgun0","Dummy",Null,1.25,25)

class Battlecannon():
	def __init__(self,Weapon,Unit,Element,DMod=1,HMod=0):
		self.Weapon=OmniWeaponData[Weapon]
		self.Unit=WSD[Unit]
		self.Element=Element
		self.Advantage=Element.Advantage
		self.Disadvantage=Element.Disadvantage
		self.Same=Element.Same
		self.DMod=DMod
		self.HMod=HMod
		self.Name=Unit
	@property
	def PDMG(self):
		return self.Weapon[0]
	@property
	def MDMG(self):
		return self.Weapon[1]
	@property
	def ATA(self):
		return self.Weapon[2]+min(0,(self.Unit.STR-self.Weapon[3]))
	@property
	def WT(self):
		return self.Weapon[3]
	@property
	def Buy(self):
		return self.Weapon[4]
	@property
	def Sell(self):
		return self.Weapon[5]
	@property
	def ConcentratedBlast(self):
		Target1=input("Target is: ")
		Target2=Target1
		Target3=Target1
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round((((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.25)*self.DMod+self.PDMG)-(WSD[Target1].PDEF))
		damage2=round((((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.25)*self.DMod+self.PDMG)-(WSD[Target2].PDEF))
		damage3=round((((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.25)*self.DMod+self.PDMG)-(WSD[Target3].PDEF))
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(30-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(30-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(30-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 35 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def QATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod
		damage1=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.33)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.33)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.33)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(30-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(30-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(30-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 15 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def NATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*0.5)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(40-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(40-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(40-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 25 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"
	@property
	def HATK(self):
		Target1=input("Target 1 is: ")
		Target2=input("Target 2 is: ")
		Target3=input("Target 3 is: ")
		uELM=self.Element
		cBST=float(input("User Crit Boost is: "))
		e1ELM=WSD[Target1].Element
		e2ELM=WSD[Target2].Element
		e3ELM=WSD[Target3].Element
		Advantage=self.Element.Advantage
		Disadvantage=self.Element.Disadvantage
		Same=self.Element.Same
		HMod=self.HMod
		DMod=self.DMod


		damage1=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target1].PDEF)
		damage2=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target2].PDEF)
		damage3=round(((self.Unit.SKL*1.5+self.Unit.ABL*0.25)*1)*self.DMod+self.PDMG)-(WSD[Target3].PDEF)
		crit=(100-self.Unit.LCK*0.5-cBST)
		hit1=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target1].EVA)
		hit2=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target2].EVA)
		hit3=(50-HMod-self.Unit.ABL-self.Unit.LCK-self.Unit.SKL*0.25-self.ATA)+(WSD[Target3].EVA)
		print("================================")
		print(self.Name,"has spent 35 ENE.")
		if e1ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*1.2), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target1)
		elif e1ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round((damage1*0.5)*2))
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", round(damage1*0.5))
				else:
					print("You missed", Target1)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target1,"is", round(damage1*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit1:
					print("Damage dealt to",Target1,"is", damage1)
				else:
					print("You missed", Target1)
		if e2ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target,"is", round(damage2*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e2ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target2)
		elif e2ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round((damage2*0.5)*2))
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", round(damage2*0.5))
				else:
					print("You missed", Target2)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target2,"is", round(damage2*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit2:
					print("Damage dealt to",Target2,"is", damage2)
				else:
					print("You missed", Target2)
		#Doggos
		if e3ELM==Advantage: 
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*1.2)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target,"is", round(damage3*1.2), self.Element.StatusProc)
				else:
					print("You missed.")
		elif e3ELM==Disadvantage:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.8)*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.8), self.Element.StatusProc)
				else:
					print("You missed", Target3)
		elif e3ELM==Same:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round((damage3*0.5)*2))
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", round(damage3*0.5))
				else:
					print("You missed", Target3)
		else:
			if ra.randint(1,100) >= crit:
				print("Critical! Damage dealt to",Target3,"is", round(damage3*2), "and you inflicted the", self.Element.Status, "status effect!")
			else:
				if ra.randint(1,100) >= hit3:
					print("Damage dealt to",Target3,"is", damage3)
				else:
					print("You missed", Target3)
		print("================================")
		return "================================"

#Default=Battlecannon("NormalUnobtaniumBattlecannon0","Dummy",Null,1,0)