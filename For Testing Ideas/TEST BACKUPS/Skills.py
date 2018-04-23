from WSD2 import WSD
import random as ra
from WeaponsOO import OmniWeaponData

#Skill Separator Line
def DummyP(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	eLCK=WSD[e].LCK
	ePAR=WSD[e].PAR
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=15
	Hit=15
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)

#Battlecannon Skills
#Tier I
def ConcentratedBlast(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	wPD=OmniWeaponData[Weapon][0]
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	Damage1=round((uSKL*1.5+uABL*0.25-e1TGH-e1PAR)*0.25)
	Damage2=round((uSKL*1.5+uABL*0.25-e2TGH-e2PAR)*0.25)
	Damage3=round((uSKL*1.5+uABL*0.25-e3TGH-e3PAR)*0.25)
	Hit=30-uSKL*0.25-uABL+eEVA-wAC
	ENE=35
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
#Whip Skills
#Tier I
def BurningLash(User,Weapon):
	u=User
	uELM="Fire"
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eEVA=WSD[e].EVA
	eRES=WSD[e].RES
	ePAR=WSD[e].PAR
	eLCK=WSD[e].LCK
	eWT=WSD[e].ArmorWT
	wMD=OmniWeaponData[Weapon][1]
	Damage=(uSTR*0.6+uSPR*0.6+uABL*0.25-eRES-ePAR*1.15)
	CritChance=(100-uLCK*0.5-cBST)
	Hit=50-uAGI-uSTR*0.25+eEVA-wAC
	ENE=10
	SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM)			
def SerpentCoil(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eLCK=WSD[e].LCK
	wPD=OmniWeaponData[Weapon][0]
	ENE=15
	Damage=(uSTR*1.2+uABL*0.25-eTGH-ePAR*1.15)*1.15
	CritChance=(100-uLCK*0.5-cBST)
	Hit=50-uAGI-uSTR*0.25+eEVA-wAC
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

#Flail Skills
def JawbreakerFinisher(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	wPD=OmniWeaponData[Weapon][0]
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSTR=WSD[u].STR
	ENE=10
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage1=uSTR*1.1+uABL*0.25-eTGH*0.75-ePAR
	Damage2=uSTR*1.1+uABL*0.25-eTGH*0.75
	CritChance=(100-uLCK*0.5-cBST)
	Hit=50-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM)

#Any weapon
def EyeLaser(User,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	eLCK=WSD[e].LCK
	ePAR=WSD[e].PAR
	cBST=float(input("User Crit Boost is: "))
	Damage=uSKL*0.65+uABL*0.35-eTGH-ePAR
	Hit=20-uABL*0.75-uSKL*0.25-uLCK+eEVA
	ENE=12
	CritChance=(100-uLCK*0.5-cBST)
	SingleWeaponless(User,ENE,CritChance,Damage,Hit,e,uELM,eELM)

def Pickpocket(User):
	u=User
	uELM=Element
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uSTR=WSD[u].STR
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eAGI=WSD[e].AGI
	eSTR=WSD[e].STR
	cBST=float(input("User Crit Boost is: "))
	CritChance=(100-uLCK*0.5-cBST)
	Proc=(50-uABL+eAGI)
	Struggle=(50-uSTR+eSTR)
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print("CRITICAL!",u,"stole a random item without being noticed!")
		print("---------------")
	else:
		if ra.randint(1,100) >= Proc:
			print("---------------")
			print(u,"quietly stole an item from",e+".")
			print("---------------")
		else:
			if ra.randint(1,100) >= Struggle:
				print("---------------")
				print(u,"won the power struggle and stole an item!")
				print("However,",u,"is now being targeted by,",e+"!")
				print("---------------")
			else:
				print("---------------")
				print(u,"lost the power struggle and did not steal the item successfully...")
				print("At least",e,"isn't targeting you, though.")
				print("---------------")
	
	
def Bodyslam(User,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uLCK=WSD[u].LCK
	uWT=WSD[u].ArmorWT
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eEVA=WSD[e].EVA
	eSTR=WSD[e].STR
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eWT=WSD[e].ArmorWT
	Hit=35-uLCK-eSTR*0.25+eEVA
	ENE=15
	Damage=int(uSTR+uWT-eTGH-ePAR)
	CritChance=(100-uLCK*0.5-cBST)
	SingleWeaponless(User,ENE,CritChance,Damage,Hit,e,uELM,eELM)
	if ra.randint(1,100) >= 50-uWT+eWT:
		print("---------------")
		print(u,"has Stumbled",e+"!")
		print("---------------")
	else:
		print("---------------")
		print(u,"has not Stumbled",e+"!")
		print("---------------")

def BraveLeap(User,Weapon):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	uTGH=WSD[u].TGH
	uRES=WSD[u].RES
	uMAR=WSD[u].MAR
	uPAR=WSD[u].PAR
	uLCK=WSD[u].LCK
	uWT=WSD[u].ArmorWT
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eSTR=WSD[e].STR
	eSPR=WSD[e].SPR
	eSKL=WSD[e].SKL
	eABL=WSD[e].ABL
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	ePAR=WSD[e].PAR
	eLCK=WSD[e].LCK
	CritChance=(100-uLCK*0.5-cBST)
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit!")
		print("Damage Dealt is",(uSTR+uWT-eTGH-ePAR)*2)
		print(e,"is Stumbled! If mounted, they are forced off their steed!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 35-uLCK-uSTR*0.25+eEVA:
			print("---------------")
			print(u,"landed a Direct Hit!")
			print("Damage Dealt is",(uSTR+uWT-eTGH-ePAR))
			print("---------------")
			if ra.randint(1,100) >= 50-uWT:
				print("---------------")
				print(u,"has Stumbled",e+"!")
				print("---------------")
			else:
				print("---------------")
				print(u,"has not Stumbled",e+"!")
				print("---------------")
		else:
			print("---------------")
			print(u,"missed!")
			print("---------------")
#Battlestaff Skills, Tier I
def Golfswing(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage=round(uSTR+uABL*0.25-eTGH-ePAR)*0.5
	CritChance=(100-uLCK*0.5-cBST)
	eWT=WSD[e].WT
	ENE=5
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def PogoPounce(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uWT=WSD[u].WT
	Damage=round(((uSTR+uABL*0.25-eTGH-ePAR)*1.25)+uWT)
	CritChance=(100-uLCK*0.5-cBST)
	ENE=15
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Tier II
def Skullcracker(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uWT=WSD[u].WT
	Damage=round(((uSTR+uABL*0.25-eTGH-ePAR)*1.45)+uWT)
	CritChance=(100-uLCK*0.5-cBST)
	ENE=30
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Tier III
def Crownbuster(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uWT=WSD[u].WT
	Damage=round(((uSTR+uABL*0.25-eTGH-ePAR)*1.65)+uWT)
	CritChance=(100-uLCK*0.5-cBST)
	ENE=45
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Knuckles Skills, Tier I
def OldOneTwo(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=12
	Hit=25-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	Damage=round(max(1,(((uSTR+uABL*0.35-eTGH-ePAR)*2))*0.1),((uSTR+uABL*0.35-eTGH-ePAR)*2))
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

def Roundabout(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSTR+uABL*0.35-eTGH-ePAR)*0.75)
	CritChance=(100-uLCK*0.5-cBST)
	ENE=30
	Status="Stumble"
	eWT=WSD[e].WT
	Chance=round(60-uSTR*0.75+eWT)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
	StatusProcSpecial(User,Status,e,Chance)
#Tier II
def DireImpact(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSTR+uABL*0.35-eTGH-ePAR)*1.3)
	CritChance=(100-uLCK*0.5-cBST)
	ENE=30
	Hit=45-uABL-uSTR*0.25-uLCK+eEVA-wAC
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Tier III
def Sparkatch(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	CritChance=(100-uLCK*0.5-cBST)
	ENE=30
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"caught",e+"'s attack!")
		print("---------------")
	else:
		if ra.randint(1,100) >= Proc:
			print("---------------")
			print(u,"caught",e+"'s attack!")
			print("---------------")
		else:
			print("---------------")
			print(u,"did not catch",e+"'s attack.")
			print("---------------")
#Tier IV
def EruptionSlayer(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSTR*2+uABL*0.35-eTGH-ePAR)*1.5)
	CritChance=(100-uLCK*0.5-cBST)
	ENE=120
	Hit=15-uABL-uSTR*0.25-uLCK+eEVA-wAC
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Claw Skills, Tier I
def Twisterush(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	uSTR=WSD[u].STR
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uABL=WSD[u].ABL
	CritChance=(100-uLCK*0.5-cBST)
	ENE=20
	Hit=35-uLCK-uAGI-uSKL*0.25+eEVA
	Damage=(((uSKL*0.75+uABL*0.25-eTGH-ePAR)*0.4)*4)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

def HeartlessThrustClaw(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	uSTR=WSD[u].STR
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSKL=WSD[u].SKL
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uABL=WSD[u].ABL
	ENE=25
	Hit=45-uAGI-uSKL*0.25-uLCK+eEVA-wAC
	Damage=((uSKL*0.75+uABL*0.25-eTGH-ePAR)*1.45)
	CritChance=(100-uLCK*0.5-cBST)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

def BloodySlashes(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	uSTR=WSD[u].STR
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uSKL=WSD[u].SKL
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=uSKL*0.65+uABL*0.35-eTGH-ePAR
	Damage2=Damage1
	ENE=20
	Hit=15-uAGI-uSKL*0.25-uLCK+eEVA-wAC
	TwoHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Hit,e,wPD,uELM,eELM)
#Claw Skills, Tier II

#Knife Skills
#Tier I
def PinpointStab(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSKL*0.75+uABL*0.25-eTGH-ePAR)*0.75)
	CritChance=(100-uLCK*0.5-cBST)
	Hit=(15-uAGI-uLCK-uSTR*0.25+eEVA)-wAC
	Bypass=50-uLCK+eEVA
	ENE=25
	print("---------------")
	print(u,"spent",ENE,"ENE")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit! Damage dealt is",(Damage-ePAR)*2)
		print("---------------")
	else:
		if ra.randint(1,100) >= (Hit,Bypass):
			print("---------------")
			print(u,"landed a Direct Hit and Bypassed",e+"'s armor!")
			print("Damage dealt is",Damage-ePAR)
			print("---------------")
		else:
			SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def TripleComboKnife(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	CritChance=(100-uLCK*0.5-cBST)
	ENE=10
	Damage1=uSKL*0.75+uABL*0.25-eTGH-ePAR
	Damage2=Damage1
	Damage3=Damage1
	Hit=45-uAGI-uSKL*0.25-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)

def Surprise(User,Weapon1,Weapon2,Element1,Element2):
	u=User
	u1ELM=Element1
	u2ELM=Element2
	uSTR=WSD[u].STR
	w1AC=OmniWeaponData[Weapon1][2]+min(0,(uSTR-OmniWeaponData[Weapon1][3]))
	w2AC=OmniWeaponData[Weapon2][2]+min(0,(uSTR-OmniWeaponData[Weapon2][3]))
	e=input("Target Enemy is: ")
	cBST=float(input("User Crit Boost is: "))
	eELM=WSD[e].Element
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	uAGI=WSD[u].AGI
	eEVA=WSD[e].EVA
	ENE=15
	wPD1=OmniWeaponData[Weapon1][0]
	wPD2=OmniWeaponData[Weapon2][0]
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)*0.75
	Damage2=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)*0.75
	Hit1=30-uAGI-uSKL*0.25-uLCK+eEVA-w1AC
	Hit2=30-uAGI-uSKL*0.25-uLCK+eEVA-w2AC
	DualWeaponTwoHitSingleTargetP(User,wPD1,wPD2,Hit1,Hit2,Damage1,Damage2,ENE,CritChance,e,u1ELM,u2ELM,eELM)
#Tier II
#Tier III
#Tier IV
def CruelSlashKnife(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	uSTR=WSD[u].STR
	uLCK=WSD[u].LCK
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round(uSKL*0.75+uABL*0.25-eTGH-ePAR)*1.5
	Hit=15-uAGI-uLCK-uSTR*0.25+eEVA-wAC
	CritChance=(100-uLCK*0.5-cBST)
	Status="Bleed"
	Chance=0
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
	StatusProcSpecial(User,Status,e,Chance)
#Sharp Knife Skills
#Tier I
def TripleComboSharpKnife(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=(uSKL*0.75+uABL*0.25-eTGH-ePAR)*1.3
	Damage2=Damage1
	Damage3=Damage1
	ENE=10
	Hit=45-uAGI-uSKL*0.25-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
#Saber Skills
#Tier I
def SaberSlap(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	eLCK=WSD[e].LCK
	ePAR=WSD[e].PAR
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	Damage=round((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.5)
	Hit=(20-uAGI*0.5-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC)
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

def TripleComboSaber(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	ENE=20
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=(uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.85
	Damage2=Damage1
	Damage3=Damage1
	Hit=35-uAGI*0.5-uABL*0.5-uSKL*0.125-uSTR*0.125-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
#Single Swords
#Tier I
def BeginnersParry(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uAGI=WSD[u].AGI
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.15)
	Damage2=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.15)
	Proc=85-uLCK-uSKL*0.125-uSTR*0.125-uEVA+eAGI
	Hit=0
	SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM)
def SharpBeginnersParry(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uAGI=WSD[u].AGI
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.15)*1.25
	Damage2=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.15)*1.25
	Proc=85-uLCK-uSKL*0.125-uSTR*0.125-uEVA*1.15+eAGI
	Hit=0
	SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM)

def TripleComboSharpSaber(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	ENE=21
	CritChance=(100-uLCK*0.5-cBST)
	Hit=45-uAGI-uSKL*0.125-uSTR*0.125-uLCK+eEVA-wAC
	Damage1=(((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.85)*1.25)
	Damage2=Damage1
	Damage3=Damage1
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
			
def FuryThrust(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	Hit=45-uAGI*0.5-uSKL*0.125-uSTR*0.125-uABL*0.5-uLCK+eEVA-wAC
	Damage=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.4)
	ENE=10
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

def SkillfulParry(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uAGI=WSD[u].AGI
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.25)
	Damage2=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.25)
	Proc=85-uLCK-uSKL*0.125-uSTR*0.125-uEVA*1.3+eAGI
	Hit=0
	SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM)

def ElegantParry(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uAGI=WSD[u].AGI
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.45)
	Damage2=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.45)
	Proc=85-uLCK-uSKL*0.125-uSTR*0.125-uEVA*1.45+eAGI
	Hit=0
	SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM)

def PerfectParry(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uAGI=WSD[u].AGI
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.6)
	Damage2=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.6)
	Proc=85-uLCK-uSKL*0.125-uSTR*0.125-uEVA*1.6+eAGI
	Hit=0
	SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM)

#Sword Skills: Sword Sharpener + Sword Sighter.
def BeginnersParrySharpSight(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.15)*1.25
	Damage2=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.15)*1.25
	Proc=70-uLCK-uSKL*0.125-uSTR*0.125-uAGI+eEVA
	Hit=0
	SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM)
def TripleComboSwordSharpSight(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	ENE=21
	CritChance=(100-uLCK*0.5-cBST)
	Hit=30-uAGI-uSKL*0.125-uSTR*0.125-uLCK+eEVA-wAC
	Damage1=(((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*0.85)*1.25)
	Damage2=Damage1
	Damage3=Damage1
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
def FuryThrustSharpSight(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uLCK=WSD[u].LCK
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	Hit=30-uAGI*0.5-uSKL*0.125-uSTR*0.125-uABL*0.5-uLCK+eEVA-wAC
	Damage=((uSKL*0.5+uSTR*0.5+uABL*0.25-eTGH-ePAR)*1.65)
	ENE=10
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Greatswords
#Tier I
def HeavyStab(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	ENE=10
	Hit=40-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	Damage=round(uSTR*1.25+uABL*0.25-eTGH-ePAR)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def Sidebuster(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Target Enemy 1 is: ")
	e2=input("Target Enemy 2 is: ")
	e1ELM=WSD[e1].Element
	e1TGH=WSD[e1].TGH
	e1EVA=WSD[e1].EVA
	e1PAR=WSD[e1].PAR
	e1AGI=WSD[e1].AGI
	e2ELM=WSD[e2].Element
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	e2PAR=WSD[e2].PAR
	e2AGI=WSD[e2].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	cBST=float(input("User Crit Boost is: "))
	ENE=20
	Hit1=40-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	Hit2=40-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	Damage1=round(((uSTR*1.25+uABL*0.25-e1TGH-e1PAR))*0.5)
	Damage2=round(((uSTR*1.25+uABL*0.25-e2TGH-e2PAR))*0.5)
	DualTargetP(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wPD,uELM,e1ELM,e2ELM)
	
def ChainsawThrust(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Hit=(75-uLCK-uAGI-wAC+eEVA)
	Damage=(uSTR*1.25+uABL*0.25)
	ENE=30
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

#Tier II
def GreatGust(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e3=input("Enemy 3 is: ")
	e1WT=WSD[e1].WT
	e2WT=WSD[e2].WT
	e3WT=WSD[e3].WT
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wWT=OmniWeaponData[Weapon][3]
	cBST=float(input("User Crit Boost is: "))
	print("---------------")
	print(u,"spent 30 ENE.")
	print("---------------")
	if ra.randint(1,100) >= 50-uSTR*1.25-wWT+e1WT:
		print("---------------")
		print(e1,"was blown away!")
		print("---------------")
	else:
		print("---------------")
		print(e1,"wasn't blown away.")
		print("---------------")
	if ra.randint(1,100) >= 50-uSTR*1.25-wWT+e2WT:
		print("---------------")
		print(e2,"was blown away!")
		print("---------------")
	else:
		print("---------------")
		print(e2,"wasn't blown away.")
		print("---------------")
	if ra.randint(1,100) >= 50-uSTR*1.25-wWT+e3WT:
		print("---------------")
		print(e3,"was blown away!")
		print("---------------")
	else:
		print("---------------")
		print(e3,"wasn't blown away.")
		print("---------------")
#Tier III
def Headcleaver(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	ENE=10
	Hit=40-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	Damage=round(uSTR*1.25+uABL*0.25-eTGH-ePAR)*1.5
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Tier IV
def Grandestine(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	e3=input("Enemy 3 is: ")
	e3ELM=WSD[e3].Element
	e1PAR=WSD[e1].PAR
	e2PAR=WSD[e2].PAR
	e3PAR=WSD[e3].PAR
	e1TGH=WSD[e1].TGH
	e2TGH=WSD[e2].TGH
	e3TGH=WSD[e3].TGH
	e1EVA=WSD[e1].EVA
	e2EVA=WSD[e2].EVA
	e3EVA=WSD[e3].EVA
	uSTR=WSD[u].STR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	ENE=100
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round(((uSTR*1.25+uABL*0.25-e1TGH-e1PAR))*0.33)*2.5
	Damage2=round(((uSTR*1.25+uABL*0.25-e2TGH-e2PAR))*0.33)*2.5
	Damage3=round(((uSTR*1.25+uABL*0.25-e3TGH-e3PAR))*0.33)*2.5
	qHIT1=40-uAGI-uSTR*0.25-uLCK+e1EVA-wAC
	qHIT2=40-uAGI-uSTR*0.25-uLCK+e2EVA-wAC
	qHIT3=40-uAGI-uSTR*0.25-uLCK+e3EVA-wAC
	TripleTargetP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit1,Hit2,Hit3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM)

def CruelCounterGreatsword(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	ENE=60
	CritChance=(100-uLCK*0.5-cBST)
	Hit=40-uAGI-uSTR*0.25-uLCK+eEVA-wAC
	Damage=round(uSTR*1.25+uABL*0.25-eTGH-ePAR)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Greatsword Grinder: Increase damage by 50%
#Tier I
def ChainsawThrustGrinder(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	CritChance=(100-uLCK*0.5-cBST)
	Hit=(75-uLCK-uAGI-wAC+eEVA)
	Damage=((uSTR*1.25+uABL*0.25)*1.5)
	ENE=30
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Polearms
#Tier I
def PolePounce(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	eLCK=WSD[e].LCK
	ePAR=WSD[e].PAR
	uWT=WSD[u].ArmorWT
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	Damage=round((uSKL*0.35+uSTR*0.65+uABL*0.25-eTGH-ePAR)*1.25)+uWT
	Hit=40-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	ENE=15
	CritChance=(100-uLCK*0.5-cBST)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

def TripointBuster(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	CritChance=(100-uLCK*0.5-cBST)
	ENE=12
	Damage1=((uSKL*0.35+uSTR*0.65+uABL*0.25-eTGH-ePAR)*0.25)
	Damage2=Damage1
	Damage3=Damage1
	Hit=40-uAGI*0.75-uABL*0.25-uSKL*0.0875-uSTR*0.1625-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
def Cutwo(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1TGH=WSD[e1].TGH
	e1EVA=WSD[e1].EVA
	e1PAR=WSD[e1].PAR
	e1AGI=e1+"AGI"
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	e2PAR=WSD[e2].PAR
	e2AGI=e2+"AGI"
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage1=(((uSKL*0.35+uSTR*0.65+uABL*0.25-WSD[e1TGH]-WSD[e1PAR])*0.5))
	Damage2=(((uSKL*0.35+uSTR*0.65+uABL*0.25-WSD[e2TGH]-WSD[e2PAR])*0.5))
	Hit1=(30-uAGI*0.75-uABL*0.25-uSKL*0.0875-uSTR*0.1625-uLCK+e1EVA-wAC)
	Hit2=(30-uAGI*0.75-uABL*0.25-uSKL*0.0875-uSTR*0.1625-uLCK+e2EVA-wAC)
	ENE=8
	CritChance=(100-uLCK*0.5-cBST)
	TwoHitterDualP(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wPD,uELM,e1ELM,e2ELM)
#Tier II
#Placeheld

#Tier III
def SixfoldThrust(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	eLCK=WSD[e].LCK
	ePAR=WSD[e].PAR
	uWT=WSD[u].ArmorWT
	cBST=float(input("User Crit Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	Hit=25-uAGI*0.75-uSTR*0.25-uABL*0.25-uLCK+eEVA-wAC
	ENE=40
	CritChance=(100-uLCK*0.5-cBST)
	Damage=round(uSKL*0.35+uSTR*0.65+uABL*0.25-eTGH-ePAR)*0.5
	SixHitterSingleP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

#Polearm Paladin, Damage boost: 35%
#Tier I
def TripointPaladin(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	eAGI=WSD[e].AGI
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	CritChance=(100-uLCK*0.5-cBST)
	ENE=12
	Damage1=((uSKL*0.35+uSTR*0.65+uABL*0.25-eTGH-ePAR)*0.25)*1.35
	Damage2=Damage1
	Damage3=Damage1
	Hit=40-uAGI*0.75-uABL*0.25-uSKL*0.0875-uSTR*0.1625-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)

def CutwoPaladin(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1TGH=WSD[e1].TGH
	e1EVA=WSD[e1].EVA
	e1PAR=WSD[e1].PAR
	e1AGI=e1+"AGI"
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	e2PAR=WSD[e2].PAR
	e2AGI=e2+"AGI"
	uSTR=WSD[u].STR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Damage1=(((uSKL*0.35+uSTR*0.65+uABL*0.25-WSD[e1TGH]-WSD[e1PAR])*0.5)*1.35)
	Damage2=(((uSKL*0.35+uSTR*0.65+uABL*0.25-WSD[e2TGH]-WSD[e2PAR])*0.5)*1.35)
	Hit1=(30-uAGI*0.75-uABL*0.25-uSKL*0.0875-uSTR*0.1625-uLCK+e1EVA-wAC)
	Hit2=(30-uAGI*0.75-uABL*0.25-uSKL*0.0875-uSTR*0.1625-uLCK+e2EVA-wAC)
	ENE=8
	TwoHitterDualP(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wPD,uELM,e1ELM,e2ELM)
#Canes
#Tier I
def Cudgel(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	eEVA=WSD[e].EVA
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Hit=40-uAGI-uSTR*0.125-uSPR*0.125-uLCK+eEVA-wAC
	Damage=((uSTR*0.5+uSPR*0.25+uABL*0.25-eTGH*0.75-eRES*0.25-eMAR)*1.1)
	ENE=10
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def ShatterBlow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	eMAR=WSD[e].MAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Hit=(40-uAGI-uSTR*0.125-uSPR*0.125-uLCK+eEVA-wAC)
	Damage=(((uSTR*0.5+uSPR*0.25+uABL*0.25-eTGH*0.75-eRES*0.25-eMAR)*1.25))
	ENE=25
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Bow Skills
#Tier I
def Longshot(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Hit=(40-uABL-uSTR*0.25-uLCK+eEVA-wAC)
	Damage=((uSTR*0.9+uABL*0.25-eTGH-ePAR))
	ENE=20
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def Clipshot(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Hit=(50-uABL-uSTR*0.25-uLCK+eEVA-wAC)
	Damage=(((uSTR*0.75+uABL*0.25-eTGH-ePAR)*0.75))
	ENE=10
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def Snarrow(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	uAGI=WSD[u].AGI
	Status="Rooted"
	Chance=75
	ENE=15
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	StatusProcSpecial(User,Status,e,Chance)
#Crossbow Skills
#Tier I
def Holepunch(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(75-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH))
	ENE=25
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)

def Needleround(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(30-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH*0.8-ePAR*0.8))
	ENE=20
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Tier II
def Needleshot(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(30-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH*0.65-ePAR*0.8))
	ENE=35
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Tier III
def Rebounder(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(75-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH-ePAR)*0.7)
	ENE=25
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def Boombolt(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(75-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH-ePAR))
	ENE=30
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def Needlebolt(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(30-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH*0.5-ePAR*0.8))
	ENE=35
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Crossbow Corrector
#Tier I
def CorrectHolepunch(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	uSTR=WSD[u].STR
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(55-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH))
	ENE=25
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def CorrectNeedleround(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(10-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH*0.8-ePAR*0.8))
	ENE=20
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def CorrectCrusadeCrusherHolepunch(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	uSTR=WSD[u].STR
	wPD=OmniWeaponData[Weapon][0]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(55-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=(((uSKL*0.75+uABL*0.25-eTGH)*1.15))
	ENE=25
	CritChance=(100-uLCK*0.5-cBST)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def CorrectCrusadeCrusherNeedleround(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	Hit=(10-uABL-uSKL*0.25-uLCK+eEVA-wAC)
	Damage=((uSKL*0.75+uABL*0.25-eTGH*0.8-ePAR*0.55)*1.15)
	ENE=20
	CritChance=(100-uLCK*0.5-cBST)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def DoubleXB(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	CritChance=(100-uLCK*0.5-cBST)
	ENE=30
	Damage1=uSKL*0.75+uABL*0.25-eTGH-ePAR*0.8
	Damage2=Damage1
	Hit=40-uABL-uSKL*0.25-uLCK+eEVA-wAC
	TwoHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Hit,e,wPD,uELM,eELM)
#Handbow Skills
#Tier I
def TriplePlay(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	e2ELM=WSD[e2].Element
	e3=input("Enemy 3 is: ")
	e3ELM=WSD[e3].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1TGH=WSD[e1].TGH
	e1EVA=WSD[e1].EVA
	e1PAR=WSD[e1].PAR
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	e2PAR=WSD[e2].PAR
	e3TGH=WSD[e3].TGH
	e3EVA=WSD[e3].EVA
	e3PAR=WSD[e3].PAR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=15
	Damage1=((uSKL*0.5+uABL*0.25-WSD[e1TGH]-WSD[e1PAR])*0.75)
	Damage2=((uSKL*0.5+uABL*0.25-WSD[e2TGH]-WSD[e2PAR])*0.75)
	Damage3=((uSKL*0.5+uABL*0.25-WSD[e3TGH]-WSD[e3PAR])*0.75)
	Hit1=45-uABL*0.75-uSKL*0.25-uLCK+e1EVA-wAC
	Hit2=45-uABL*0.75-uSKL*0.25-uLCK+e2EVA-wAC
	Hit3=45-uABL*0.75-uSKL*0.25-uLCK+WSD[e3EVA]-wAC
	TripleTargetP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit1,Hit2,Hit3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM)

#Twin Pistol Skills
#Tier I
def ChargeShot(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	ePAR=WSD[e].PAR
	uSKL=WSD[u].SKL
	uLCK=WSD[u].LCK
	uABL=WSD[u].ABL
	CritChance=(100-uLCK*0.5-cBST)
	ENE=12
	Hit=45-uABL-uSKL*0.25-uLCK+eEVA-wAC
	Damage=((uSKL*0.65+uABL*0.35-eTGH-ePAR)*1.5)
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
#Rifle Skills
#Tier I
def PiercingLaser(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	e1PAR=WSD[e1].PAR
	e1TGH=WSD[e1].TGH
	e1EVA=WSD[e1].EVA
	e2PAR=WSD[e2].PAR
	e2TGH=WSD[e2].TGH
	e2EVA=WSD[e2].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=20
	Damage1=uSKL+uABL*0.5-WSD[e1TGH]-WSD[e1PAR]
	Damage2=uSKL+uABL*0.5-WSD[e2TGH]-WSD[e2PAR]
	Hit1=15-uSKL*0.25-uABL+e1EVA-wAC
	Hit2=15-uSKL*0.25-uABL+e2EVA-wAC
	DualTargetP(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wPD,uELM,e1ELM,e2ELM)

#Mechgun Skills
#Tier I
def Drizzle(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round(((uSKL+uABL*0.25-ePAR-eTGH)*0.75)*0.3)
	Damage2=Damage1
	Damage3=Damage1
	ENE=9
	Hit=0-uABL-uSKL*0.25-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
def RubberRounds(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round(((uSKL+uABL*0.25-ePAR-eTGH)*0.3)*0.5)
	Damage2=Damage1
	Damage3=Damage1
	ENE=9
	Hit=0-uABL-uSKL*0.25-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
def DrizzleManiac(User,Weapon,Element):
	u=User
	uELM=Element
	uSTR=WSD[u].STR
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]/2))
	cBST=float(input("User Crit Boost is: "))
	ePAR=WSD[e].PAR
	eTGH=WSD[e].TGH
	eEVA=WSD[e].EVA
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	Damage1=round(((uSKL+uABL*0.25-ePAR-eTGH)*0.75)*0.6)
	Damage2=Damage1
	Damage3=Damage1
	ENE=9
	Hit=0-uABL-uSKL*0.25-uLCK+eEVA-wAC
	ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM)
def BlitzManiac(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=input("Enemy 2 is: ")
	e3=input("Enemy 3 is: ")
	e4=input("Enemy 4 is: ")
	e5=input("Enemy 5 is: ")
	e6=input("Enemy 6 is: ")
	e1EVA=WSD[e1].EVA
	e1TGH=WSD[e1].TGH
	e1PAR=WSD[e1].PAR
	e1ELM=WSD[e1].Element
	e2EVA=WSD[e2].EVA
	e2TGH=WSD[e2].TGH
	e2PAR=WSD[e2].PAR
	e2ELM=WSD[e2].Element
	e3EVA=WSD[e3].EVA
	e3TGH=WSD[e3].TGH
	e3PAR=WSD[e3].PAR
	e3ELM=WSD[e3].Element
	e4EVA=WSD[e4].EVA
	e4TGH=WSD[e4].TGH
	e4PAR=WSD[e4].PAR
	e4ELM=WSD[e4].Element
	e5EVA=WSD[e5].EVA
	e5TGH=WSD[e5].TGH
	e5ELM=WSD[e5].Element
	e5PAR=WSD[e5].PAR
	e6ELM=WSD[e6].Element
	e6EVA=WSD[e6].EVA
	e6TGH=WSD[e6].TGH
	e6PAR=WSD[e6].PAR
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=50
	Damage1=round((uSKL+uABL*0.5-e1PAR-e1TGH)*0.45)
	Damage2=round((uSKL+uABL*0.5-e2PAR-e2TGH)*0.45)
	Damage3=round((uSKL+uABL*0.5-e3PAR-e3TGH)*0.45)
	Damage4=round((uSKL+uABL*0.5-e4PAR-e4TGH)*0.45)
	Damage5=round((uSKL+uABL*0.5-e5PAR-e5TGH)*0.45)
	Damage6=round((uSKL+uABL*0.5-e6PAR-e6TGH)*0.45)
	Hit1=15-uABL-uSKL*0.25-uLCK+e1EVA-wAC
	Hit2=15-uABL-uSKL*0.25-uLCK+e2EVA-wAC
	Hit3=15-uABL-uSKL*0.25-uLCK+e3EVA-wAC
	Hit4=15-uABL-uSKL*0.25-uLCK+e4EVA-wAC
	Hit5=15-uABL-uSKL*0.25-uLCK+e5EVA-wAC
	Hit6=15-uABL-uSKL*0.25-uLCK+e6EVA-wAC
	BlitzBlast(User,ENE,CritChance,Damage1,Damage2,Damage3,Damage4,Damage5,Damage6,Hit1,Hit2,Hit3,Hit4,Hit5,Hit6,e1,e2,e3,e4,e5,e6,wPD,uELM,e1ELM,e2ELM,e3ELM,e4ELM,e5ELM,e6ELM)
def CircleSlider(User,Weapon,Element):
	u=User
	uELM=Element
	e1=input("Enemy 1 is: ")
	e2=e1
	e3=e1
	e4=e1
	e1EVA=WSD[e1].EVA
	e1TGH=WSD[e1].TGH
	e1PAR=WSD[e1].PAR
	e1ELM=WSD[e1].Element
	e2EVA=WSD[e2].EVA
	e2TGH=WSD[e2].TGH
	e2PAR=WSD[e2].PAR
	e2ELM=WSD[e2].Element
	e3EVA=WSD[e3].EVA
	e3TGH=WSD[e3].TGH
	e3PAR=WSD[e3].PAR
	e3ELM=WSD[e3].Element
	e4EVA=WSD[e4].EVA
	e4TGH=WSD[e4].TGH
	e4PAR=WSD[e4].PAR
	e4ELM=WSD[e4].Element
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-(OmniWeaponData[Weapon][3]/2)))
	cBST=float(input("User Crit Boost is: "))
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=50
	Damage1=round((uSKL+uABL*0.5-e1PAR-e1TGH)*0.45)
	Damage2=round((uSKL+uABL*0.5-e2PAR-e2TGH)*0.45)
	Damage3=round((uSKL+uABL*0.5-e3PAR-e3TGH)*0.45)
	Damage4=round((uSKL+uABL*0.5-e4PAR-e4TGH)*0.45)
	Hit1=45-uABL-uSKL*0.25-uLCK+e1EVA-wAC
	Hit2=45-uABL-uSKL*0.25-uLCK+e2EVA-wAC
	Hit3=45-uABL-uSKL*0.25-uLCK+e3EVA-wAC
	Hit4=45-uABL-uSKL*0.25-uLCK+e4EVA-wAC
	QuadrupleTargetP(User,ENE,CritChance,Damage1,Damage2,Damage3,Damage4,Hit1,Hit2,Hit3,Hit4,e1,e2,e3,e4,wPD,uELM,e1ELM,e2ELM,e3ELM)
#Offensive Spells
#Flame: Tier I
def Fireball(User,Weapon):
	u=User
	uELM="Flame"
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eMAR=WSD[e].MAR
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=6
	Hit=35-uABL-uSPR*0.25+eEVA-wAC
	Damage=uSPR*0.75+uABL*0.25-eMAR-eRES
	SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM)

def WovenFireball(User,Weapon):
	u=User
	uELM="Flame"
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	eMAR=WSD[e].MAR
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=6
	Hit=35-uABL-uSPR*0.25+eEVA-wAC
	Damage=(uSPR*0.75+uABL*0.25-eMAR-eRES)*1.15
	SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM)
def FlameBlast(User,Weapon):
	u=User
	uELM="Flame"
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1MAR=WSD[e1].MAR
	e1RES=WSD[e1].RES
	e1EVA=WSD[e1].EVA
	e2MAR=WSD[e2].MAR
	e2RES=WSD[e2].RES
	e2EVA=WSD[e2].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=15
	Damage1=uSPR*0.5+uABL*0.25-e1MAR-e1RES
	Damage2=uSPR*0.5+uABL*0.25-e2MAR-e2RES
	Hit1=30-uABL-uSPR*0.25-uLCK+e1EVA-wAC
	Hit2=30-uABL-uSPR*0.25-uLCK+e2EVA-wAC
	DualTargetM(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wMD,uELM,e1ELM,e2ELM)
	if ra.randint(1,100) >= 60-uLCK+e1RES*0.5:
		print("---------------")
		print(e1,"is Burning! They take damage every turn - 3 turns remaining!")
		print("---------------")
	if ra.randint(1,100) >= 60-uLCK+e2RES*0.5:
		print("---------------")
		print(e2,"is Burning! They take damage every turn - 3 turns remaining!")
		print("---------------")
#Flame: Tier IV
def LavaLaser(User,Weapon):
	u=User
	uELM="Flame"
	uSTR=WSD[u].STR
	uSPR=WSD[u].SPR
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	uAGI=WSD[u].AGI
	uEVA=WSD[u].EVA
	uTGH=WSD[u].TGH
	uRES=WSD[u].RES
	uMAR=WSD[u].MAR
	uPAR=WSD[u].PAR
	uLCK=WSD[u].LCK
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	eSTR=WSD[e].STR
	eSPR=WSD[e].SPR
	eSKL=WSD[e].SKL
	eABL=WSD[e].ABL
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eTGH=WSD[e].TGH
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	ePAR=WSD[e].PAR
	eLCK=WSD[e].LCK
	CritChance=(100-uLCK*0.5-cBST)
	wMD=OmniWeaponData[Weapon][1]
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	ENE=40
	Damage=uSPR*1.5+uABL*0.25-eRES-eMAR
	Hit=30-uLCK-uABL-uSPR*0.25+eEVA
	SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM)
		
#Earth: Tier I
def EarthenHammer(User,Weapon):
	u=User
	uELM="Earth"
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	eMAR=WSD[e].MAR
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=15
	Damage=uSPR*0.75+uABL*0.25-eMAR-eRES
	Hit=35-uABL-uSPR*0.25-uLCK+eEVA-wAC
	SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM)
	if ra.randint(1,100) >= 75-uLCK+eRES*0.5:
		print("---------------")
		print(e,"is Silenced! They cannot use Skills!")
		print("---------------")
#Wind: Tier I
def WindyWhip(User,Weapon):
	u=User
	uELM="Wind"
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	eMAR=WSD[e].MAR
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=15
	Damage=uSPR*0.75+uABL*0.25-eMAR-eRES
	Hit=35-uABL-uSPR*0.25-uLCK+eEVA-wAC
	SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM)
	if ra.randint(1,100) >= 40-uLCK+eRES*0.5:
		print("---------------")
		print(e,"is Clouded! They cannot aggro anyone this turn!")
		print("---------------")
#Lightning: Tier I
def StunBolt(User,Weapon,Element):
	u=User
	uELM="Lightning"
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Boost is: "))
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	eMAR=WSD[e].MAR
	eRES=WSD[e].RES
	eEVA=WSD[e].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=15
	Damage=uSPR*0.75+uABL*0.25-eMAR-eRES
	Hit=35-uABL-uSPR*0.25-uLCK+eEVA-wAC
	SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM)
	if ra.randint(1,100) >= 75-uLCK+eRES*0.5:
		print("---------------")
		print(e,"is Stunned! They cannot use Attacks for 1 turn!")
		print("---------------")
#Water: Tier I
def WaterGrenade(User,Weapon,Element):
	u=User
	uELM="Water"
	e1=input("Enemy 1 is: ")
	e1ELM=WSD[e1].Element
	e2=input("Enemy 2 is: ")
	e2ELM=WSD[e2].Element
	uSTR=WSD[u].STR
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	e1MAR=WSD[e1].MAR
	e1RES=WSD[e1].RES
	e1EVA=WSD[e1].EVA
	e2MAR=WSD[e2].MAR
	e2RES=WSD[e2].RES
	e2EVA=WSD[e2].EVA
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	ENE=15
	Hit1=30-uABL-uSPR*0.25-uLCK+e1EVA-wAC
	Hit2=30-uABL-uSPR*0.25-uLCK+e2EVA-wAC
	Damage1=uSPR*0.5+uABL*0.25-e1MAR-e1RES
	Damage2=uSPR*0.5+uABL*0.25-e2MAR-e2RES
	DualTargetM(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wMD,uELM,e1ELM,e2ELM)

#Support Magic
#Health Restoring: Tier I
def HealthyGlow(User,Weapon):
	u=User
	a1=input("Ally 1 is: ")
	a2=input("Ally 2 is: ")
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	a1HP=WSD[a1].HP
	a2HP=WSD[a2].HP
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(a1,"is Critically healed for", ((uSPR*0.25+uABL*0.25+a1HP*0.1)*2)+wMD)
		print(a2,"is Critically healed for", ((uSPR*0.25+uABL*0.25+a2HP*0.1)*2)+wMD)
		print("---------------")
	else:
		print("---------------")
		print(a1,"is healed for", (uSPR*0.25+uABL*0.25+a1HP*0.15)+wMD)
		print(a2,"is healed for", (uSPR*0.25+uABL*0.25+a2HP*0.15)+wMD)
		print("---------------")
def HealthyRay(User,Weapon):
	u=User
	a=input("Ally is: ")
	aHP=WSD[a].HP
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	cBST=float(input("User Crit Boost is: "))
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	print("---------------")
	print(u,"spent 15 ENE.")
	print(a,"is healed for", (uSPR*0.25+uABL*0.25+aHP*0.3)+wMD*0.25)
	print("---------------")
#Status Curing: Tier I
def RestorativeRay(User,Weapon):
	u=User
	a=input("Ally is: ")
	wMD=OmniWeaponData[Weapon][1]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	aINF=input(u, "is trying to cure", a, "of this status: ")
	cBST=float(input("User Crit Boost is: "))
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= 100-uLCK*0.5-cBST-wMD*0.5:
		print("---------------")
		print(a,"is cured of all negative statuses due to a critical hit!")
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-uLCK-wMD:
			print("---------------")
			print(a,"is cured of", aINF, "!")
			print("---------------")
			
#Monster Skills
#May be learned by players using specific accessories or consuming Monster Meat
#Savage Bite
def SavageBite(User):
	u=User
	uELM=Element
	uAGI=WSD[u].AGI
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Chance Boost is: "))
	uSTR=WSD[u].STR
	eEVA=WSD[e].EVA
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	CritChance=(100-uLCK*0.5-cBST)
	print("---------------")
	print(u,"spent 15 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"landed a Critical Hit against",e,"using Savage Bite!")
		print("Damage dealt is", (uSTR+uABL*0.25-eTGH+ePAR)*2)
		print("---------------")
	else:
		if ra.randint(1,100) >= 75-uLCK-uAGI+eEVA:
			print("---------------")
			print(u,"landed a Direct Hit against",e,"using Savage Bite!")
			print("Damage dealt is", min(10,(uSTR+uABL*0.25-eTGH+ePAR)))
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e)
			print("---------------")
#Vampire Blade
#Use the Weapon field to boost power by naming Sabers or Knives in it.
def VampireBlade(User,Weapon,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Chance Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	eEVA=WSD[e].EVA
	CritChance=(100-uLCK*0.5-cBST)
	Hit=35-uABL+eEVA-wAC
	Damage=(uSPR*1.15+uABL*0.25-eRES-eMAR)
	ENE=25
	SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM)
def HPLeech(User,Weapon):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Chance Boost is: "))
	wPD=OmniWeaponData[Weapon][0]
	uSTR=WSD[u].STR
	wAC=OmniWeaponData[Weapon][2]+min(0,(uSTR-OmniWeaponData[Weapon][3]))
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	eEVA=WSD[e].EVA
	CritChance=(100-uLCK*0.5-cBST)
	print("---------------")
	print(u,"spent 40 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u, "Landed a Critical Hit against", e+"!")
		print("Damage dealt to",e,"is", (uSPR*0.5+uABL*0.5-eRES-eMAR)*2)
		print("Health stolen is", ((uSPR*0.5+uABL*0.5-eRES-eMAR)*2)*0.33)
		print("---------------")
	else:
		if ra.randint(1,100) >=70-uLCK+eEVA-wAC:
			print("---------------")
			print(u, "Landed a Direct Hit against", e+"!")
			print("Damage dealt to",e,"is", (uSPR*0.5+uABL*0.5-eRES-eMAR))
			print("Health stolen is", (uSPR*0.5+uABL*0.5-eRES-eMAR)*0.33)
			print("---------------")
		else:
			print("---------------")
			print(u,"missed",e,"with Health Leech!")
			print("---------------")

def Webshot(User):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Chance Boost is: "))
	uSKL=WSD[u].SKL
	uABL=WSD[u].ABL
	eAGI=WSD[e].AGI
	eEVA=WSD[e].EVA
	eSTR=WSD[e].STR
	eTGH=WSD[e].TGH
	ePAR=WSD[e].PAR
	uLCK=WSD[u].LCK
	CritChance=(100-uLCK*0.5-cBST)
	print("---------------")
	print("Spent 10 ENE.")
	print("---------------")
	if ra.randint(1,100) >= CritChance:
		print("---------------")
		print(u,"scored a Critical Hit! Damage dealt is",(uSKL*0.75+uABL*0.25-eTGH-ePAR)*2)
		print("---------------")
	else:
		if ra.randint(1,100) >= 50-uLCK-uSKL*0.25-uABL+eEVA:
			print("---------------")
			print(u,"scored a Direct Hit! Damage daelt is",())
			print("---------------")
			if ra.randint(1,100) >= 65+eSTR*0.75:
				print("---------------")
				print(e,"is Snared! They cannot change Zones or Dodge until they break free!")
				print("---------------")
			else:
				print("---------------")
				print("Failed to Snare target.")
				print("---------------")
		else:
			print("---------------")
			print(u,"missed",e+"!")
			print("---------------")

def BreathAttack(User,Element):
	u=User
	uELM=Element
	e=input("Target Enemy is: ")
	eELM=WSD[e].Element
	cBST=float(input("User Crit Chance Boost is: "))
	uSPR=WSD[u].SPR
	uABL=WSD[u].ABL
	uLCK=WSD[u].LCK
	eRES=WSD[e].RES
	eMAR=WSD[e].MAR
	eEVA=WSD[e].EVA
	ENE=15
	Hit=35-uLCK-uSPR*0.25+eEVA
	CritChance=(100-uLCK*0.5-cBST)
	Damage=uSPR*0.75+uABL*0.25-eRES-eMAR
	SingleWeaponless(User,ENE,CritChance,Damage,Hit,e,uELM,eELM)
#Definition Separator Line
#Elemental Handling
def QuadrupleTargetP(User,ENE,CritChance,Damage1,Damage2,Damage3,Damage4,Hit1,Hit2,Hit3,Hit4,e1,e2,e3,e4,wPD,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
#Doggo
	if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round((Damage3)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
#Squirrel
	if uELM=="Flame" or uELM=="Fire" and e4ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e4ELM=="Aqua" or e4ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e4ELM=="Flame" or e4ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Earth" and e4ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Earth" and e4ELM=="Fire" or e4ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Earth" and e4ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Wind" and e4ELM=="Lightning" or e4ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Wind" and e4ELM=="Fire" or e4ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Wind" and e4ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e4ELM=="Aqua" or e4ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e4ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e4ELM=="Lightning" or e4ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e4ELM=="Fire" or e4ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e4ELM=="Lightning" or e4ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e4ELM=="Water" or e4ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round((Damage4)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	ProcQuadruple(User,e1,e2,e3,e4,uELM,e1ELM,e2ELM,e3ELM,e4ELM)

def StatusProcSpecial(User,Status,e,Chance):
	u=User
	if ra.randint(1,100) >= Chance:
		print("---------------")
		print(u,"inflicted",Status,"on",e+"!")
		print("---------------")
def SixHitterSingleP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def ProcSingle(User,e,uELM,eELM):
	u=User
	if uELM=="Flame" or uELM=="Fire" and eELM!="Flame" or eELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and eELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and eELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM!="Lightning" or eELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM!="Water" or eELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
def ProcDouble(User,e1,e2,uELM,e1ELM,e2ELM):
	u=User
	if uELM=="Flame" or uELM=="Fire" and e1ELM!="Flame" or e1ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e1ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e1ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM!="Lightning" or e1ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM!="Water" or e1ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Doggo
	if uELM=="Flame" or uELM=="Fire" and e2ELM!="Flame" or e2ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e2ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e2ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM!="Lightning" or e2ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM!="Water" or e2ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
def ProcTriple(User,e1,e2,e3,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	if uELM=="Flame" or uELM=="Fire" and e1ELM!="Flame" or e1ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e1ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e1ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM!="Lightning" or e1ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM!="Water" or e1ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Doggo
	if uELM=="Flame" or uELM=="Fire" and e2ELM!="Flame" or e2ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e2ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e2ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM!="Lightning" or e2ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM!="Water" or e2ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Catto
	if uELM=="Flame" or uELM=="Fire" and e3ELM!="Flame" or e3ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e3ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e3ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM!="Lightning" or e3ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM!="Water" or e3ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
def ProcQuadruple(User,e1,e2,e3,e4,uELM,e1ELM,e2ELM,e3ELM,e4ELM):
	u=User
	if uELM=="Flame" or uELM=="Fire" and e1ELM!="Flame" or e1ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e1ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e1ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM!="Lightning" or e1ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM!="Water" or e1ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e1,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Doggo
	if uELM=="Flame" or uELM=="Fire" and e2ELM!="Flame" or e2ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e2ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e2ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM!="Lightning" or e2ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM!="Water" or e2ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e2,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Catto
	if uELM=="Flame" or uELM=="Fire" and e3ELM!="Flame" or e3ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e3ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e3ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM!="Lightning" or e3ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM!="Water" or e3ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e3,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")
	#Squidward
	if uELM=="Flame" or uELM=="Fire" and e4ELM!="Flame" or e4ELM!="Fire":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e4,"is now Burning! Subtract 5% HP this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Earth" and e4ELM!="Earth":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e4,"is now Silenced! They cannot use Skills this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Wind" and e4ELM!="Wind":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e4,"is now Clouded! They cannot generate aggro this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e4ELM!="Lightning" or e4ELM!="Elec":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e4,"is now Shocked! They cannot use regular Attacks this turn and for 2 Turns after this!")
			print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e4ELM!="Water" or e4ELM!="Aqua":
		if ra.randint(1,100) >= 75:
			print("---------------")
			print(e4,"is now Waterlogged! They cannot use items for this turn and 2 Turns after this!")
			print("---------------")

def DualWeaponTwoHitSingleTargetP(User,wPD1,wPD2,Hit1,Hit2,Damage1,Damage2,ENE,CritChance,e,u1ELM,u2ELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if u1ELM=="Flame" or u1ELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*1.2+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Flame" or u1ELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.8+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Flame" or u1ELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.5+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*1.2+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.8+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.5+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*1.2+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.8+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.5+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Lightning" or u1ELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*1.2+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Lightning" or u1ELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.8+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Lightning" or u1ELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.5+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Water" or u1ELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*1.2+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Water" or u1ELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.8+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u1ELM=="Water" or u1ELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)*0.5+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage1 dealt is",round((Damage1)*2+wPD1))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage1 dealt is",round((Damage1)+wPD1))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
#Doggo
	if u2ELM=="Flame" or u2ELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*1.2+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Flame" or u2ELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.8+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Flame" or u2ELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.5+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*1.2+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.8+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.5+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*1.2+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.8+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.5+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Lightning" or u2ELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*1.2+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Lightning" or u2ELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.8+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Lightning" or u2ELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.5+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Water" or u2ELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*1.2+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Water" or u2ELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.8+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif u2ELM=="Water" or u2ELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)*0.5+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage2 dealt is",round((Damage2)*2+wPD2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage2 dealt is",round((Damage2)+wPD2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def BlitzBlast(User,ENE,CritChance,Damage1,Damage2,Damage3,Damage4,Damage5,Damage6,Hit1,Hit2,Hit3,Hit4,Hit5,Hit6,e1,e2,e3,e4,e5,e6,wPD,uELM,e1ELM,e2ELM,e3ELM,e4ELM,e5ELM,e6ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
#Doggo
	if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round((Damage3)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e4ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e4ELM=="Aqua" or e4ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e4ELM=="Flame" or e4ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Earth" and e4ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Earth" and e4ELM=="Fire" or e4ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Earth" and e4ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Wind" and e4ELM=="Lightning" or e4ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Wind" and e4ELM=="Fire" or e4ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Wind" and e4ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e4ELM=="Aqua" or e4ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e4ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e4ELM=="Lightning" or e4ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e4ELM=="Fire" or e4ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e4ELM=="Lightning" or e4ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e4ELM=="Water" or e4ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round(((Damage4)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e4+"!")
			print("Damage dealt is",round((Damage4)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit4:
				print("---------------")
				print(u,"landed a Direct Hit against",e4+"!")
				print("Damage dealt is",round((Damage4)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e4+"!")
				print("---------------")
#Squirrel
	if uELM=="Flame" or uELM=="Fire" and e5ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e5ELM=="Aqua" or e5ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e5ELM=="Flame" or e5ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Earth" and e5ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Earth" and e5ELM=="Fire" or e5ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Earth" and e5ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Wind" and e5ELM=="Lightning" or e5ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Wind" and e5ELM=="Fire" or e5ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Wind" and e5ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e5ELM=="Aqua" or e5ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e5ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e5ELM=="Lightning" or e5ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e5ELM=="Fire" or e5ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e5ELM=="Lightning" or e5ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e5ELM=="Water" or e5ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round(((Damage5)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e5+"!")
			print("Damage dealt is",round((Damage5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit5:
				print("---------------")
				print(u,"landed a Direct Hit against",e5+"!")
				print("Damage dealt is",round((Damage5)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e5+"!")
				print("---------------")
#Octopus
	if uELM=="Flame" or uELM=="Fire" and e5ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e5ELM=="Aqua" or e5ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e5ELM=="Flame" or e5ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Earth" and e5ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Earth" and e5ELM=="Fire" or e5ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Earth" and e5ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Wind" and e5ELM=="Lightning" or e5ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Wind" and e5ELM=="Fire" or e5ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Wind" and e5ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e5ELM=="Aqua" or e5ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e5ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e5ELM=="Lightning" or e5ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e5ELM=="Fire" or e5ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e5ELM=="Lightning" or e5ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e5ELM=="Water" or e5ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round(((Damage6)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e6+"!")
			print("Damage dealt is",round((Damage6)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit6:
				print("---------------")
				print(u,"landed a Direct Hit against",e6+"!")
				print("Damage dealt is",round((Damage6)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e6+"!")
				print("---------------")

def TripleTargetM(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit1,Hit2,Hit3,e1,e2,e3,wMD,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
#Doggo
	if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round((Damage3)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	ProcTriple(User,e1,e2,e3,uELM,e1ELM,e2ELM,e3ELM)

def TripleTargetP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit1,Hit2,Hit3,e1,e2,e3,wPD,uELM,e1ELM,e2ELM,e3ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
#Doggo
	if uELM=="Flame" or uELM=="Fire" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e3ELM=="Flame" or e3ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Earth" and e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Fire" or e3ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Wind" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Aqua" or e3ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Fire" or e3ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Lightning" or e3ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e3ELM=="Water" or e3ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e3+"!")
			print("Damage dealt is",round((Damage3)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit3:
				print("---------------")
				print(u,"landed a Direct Hit against",e3+"!")
				print("Damage dealt is",round((Damage3)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e3+"!")
				print("---------------")
	ProcTriple(User,e1,e2,e3,uELM,e1ELM,e2ELM,e3ELM)

def DualTargetM(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wMD,uELM,e1ELM,e2ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	ProcDouble(User,e1,e2,uELM,e1ELM,e2ELM)

def DualTargetP(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wPD,uELM,e1ELM,e2ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	ProcDouble(User,e1,e2,uELM,e1ELM,e2ELM)

def SingleTargetConditionalM(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wMD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if ra.randint(1,100) >= Proc:
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round((Damage1)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	else:
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round((Damage2)*2+wMD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)+wMD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	ProcSingle(User,e,uELM,eELM)

def SingleTargetConditionalP(User,ENE,CritChance,Proc,Damage1,Damage2,Hit,e,wPD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if ra.randint(1,100) >= Proc:
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round(((Damage1)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage1 dealt is",round((Damage1)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage1 dealt is",round((Damage1)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	else:
		if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Earth" and eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Wind" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*1.2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*1.2+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.8)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.8+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round(((Damage2)*0.5)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)*0.5+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
		else:
			if ra.randint(1,100) >= CritChance:
				print("---------------")
				print(u, "Landed a Critical Hit against", e+"!")
				print("Damage2 dealt is",round((Damage2)*2+wPD))
				print("---------------")
			else:
				if ra.randint (1,100) >= Hit:
					print("---------------")
					print(u,"landed a Direct Hit against",e+"!")
					print("Damage2 dealt is",round((Damage2)+wPD))
					print("---------------")
				else:
					print("---------------")
					print(u,"missed",e+"!")
					print("---------------")
	ProcSingle(User,e,uELM,eELM)

def ThreeHitterSingleM(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wMD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage1)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage3)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def ThreeHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Damage3,Hit,e,wPD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage3)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage3)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage3)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def TwoHitterSingleP(User,ENE,CritChance,Damage1,Damage2,Hit,e,wPD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def SingleTargetP(User,ENE,CritChance,Damage,Hit,e,wPD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def SingleTargetM(User,ENE,CritChance,Damage,Hit,e,wMD,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2+wMD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)+wMD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def SingleWeaponless(User,ENE,CritChance,Damage,Hit,e,uELM,eELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and eELM=="Flame" or eELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Earth" and eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Fire" or eELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Wind" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Aqua" or eELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Fire" or eELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*1.2)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*1.2))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Lightning" or eELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.8)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.8))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and eELM=="Water" or eELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round(((Damage)*0.5)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)*0.5))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e+"!")
			print("Damage dealt is",round((Damage)*2))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit:
				print("---------------")
				print(u,"landed a Direct Hit against",e+"!")
				print("Damage dealt is",round((Damage)))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e+"!")
				print("---------------")
	ProcSingle(User,e,uELM,eELM)

def TwoHitterDualP(User,ENE,CritChance,Damage1,Damage2,Hit1,Hit2,e1,e2,wPD,uELM,e1ELM,e2ELM):
	u=User
	print("---------------")
	print(u,"spent",ENE,"ENE.")
	print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e1ELM=="Flame" or e1ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Earth" and e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Fire" or e1ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Wind" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Aqua" or e1ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Fire" or e1ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Lightning" or e1ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e1ELM=="Water" or e1ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round(((Damage1)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e1+"!")
			print("Damage dealt is",round((Damage1)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit1:
				print("---------------")
				print(u,"landed a Direct Hit against",e1+"!")
				print("Damage dealt is",round((Damage1)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e1+"!")
				print("---------------")
	if uELM=="Flame" or uELM=="Fire" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Flame" or uELM=="Fire" and e2ELM=="Flame" or e2ELM=="Fire":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Earth" and e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Fire" or e2ELM=="Earth":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Wind" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Aqua" or e2ELM=="Water":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Wind":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Lightning" or uELM=="Elec" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Fire" or e2ELM=="Flame":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*1.2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*1.2+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Lightning" or e2ELM=="Elec":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.8)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.8+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	elif uELM=="Water" or uELM=="Aqua" and e2ELM=="Water" or e2ELM=="Aqua":
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round(((Damage2)*0.5)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)*0.5+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	else:
		if ra.randint(1,100) >= CritChance:
			print("---------------")
			print(u, "Landed a Critical Hit against", e2+"!")
			print("Damage dealt is",round((Damage2)*2+wPD))
			print("---------------")
		else:
			if ra.randint (1,100) >= Hit2:
				print("---------------")
				print(u,"landed a Direct Hit against",e2+"!")
				print("Damage dealt is",round((Damage2)+wPD))
				print("---------------")
			else:
				print("---------------")
				print(u,"missed",e2+"!")
				print("---------------")
	ProcDouble(User,e1,e2,uELM,e1ELM,e2ELM)
