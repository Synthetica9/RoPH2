from ArmorsOO import OmniArmorData
from WeaponsOO import OmniWeaponData
from DressingRoomOO import OmniUnitData
from MonsterFactoryOO import OmniMonsterData
import random as ra
#import HealthBar
#import EnergyBar
import Shielding
import importlib
from Accessories import ACC
from Accessories import Accessory
from Accessories import Wiggles
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
Lunar=Element("Lunar","Storm","Solar","Illuminate",10)
Storm=Element("Storm","Void","Lunar","Stormscare",30)
Void=Element("Void","Time","Storm","Voidcall",30)
Time=Element("Time","Solar","Void","Timelock",20)
class DummyTrait():
	def __init__(self,HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0):
		self.HP=HP
		self.ENE=ENE
		self.STR=STR
		self.SPR=SPR
		self.SKL=SKL
		self.ABL=ABL
		self.AGI=AGI
		self.EVA=EVA
		self.TGH=TGH
		self.RES=RES
		self.LCK=LCK
	@property
	def HPPlus(self):
		return 0
	@property
	def HPMinus(self):
		return 0
	@property
	def ENEPlus(self):
		return 0
	@property
	def ENEMinus(self):
		return 0
	@property
	def STRPlus(self):
		return 0
	@property
	def STRMinus(self):
		return 0
	@property
	def SPRPlus(self):
		return 0
	@property
	def SPRMinus(self):
		return 0
	@property
	def SKLPlus(self):
		return 0
	@property
	def SKLMinus(self):
		return 0
	@property
	def ABLPlus(self):
		return 0
	@property
	def ABLMinus(self):
		return 0
	@property
	def AGIPlus(self):
		return 0
	@property
	def AGIMinus(self):
		return 0
	@property
	def EVAPlus(self):
		return 0
	@property
	def EVAMinus(self):
		return 0
	@property
	def TGHPlus(self):
		return 0
	@property
	def TGHMinus(self):
		return 0
	@property
	def RESPlus(self):
		return 0
	@property
	def RESMinus(self):
		return 0
	@property
	def LCKPlus(self):
		return 0
	@property
	def LCKMinus(self):
		return 0
	def __str__(self):
		return(
		f"""These are your stats.\n HP: {self.HP} \n ENE: {self.ENE} \n STR: {self.STR} \n SPR: {self.SPR} \n SKL: {self.SKL} \n ABL: {self.ABL} \n AGI: {self.AGI} \n EVA: {self.EVA} \n TGH: {self.TGH} \n RES: {self.RES} \n LCK: {self.LCK}""")

class Stats(object):
	def __init__(self,HP=0,ENE=0,STR=0,SPR=0,SKL=0,ABL=0,AGI=0,EVA=0,TGH=0,RES=0,LCK=0):
		self.HP=HP
		self.ENE=ENE
		self.STR=STR
		self.SPR=SPR
		self.SKL=SKL
		self.ABL=ABL
		self.AGI=AGI
		self.EVA=EVA
		self.TGH=TGH
		self.RES=RES
		self.LCK=LCK
	def __str__(self):
		return(
		f"""These are your stats.\n HP: {self.HP} \n ENE: {self.ENE} \n STR: {self.STR} \n SPR: {self.SPR} \n SKL: {self.SKL} \n ABL: {self.ABL} \n AGI: {self.AGI} \n EVA: {self.EVA} \n TGH: {self.TGH} \n RES: {self.RES} \n LCK: {self.LCK}""")

class ArmorSet():
	def __init__(self,Head=OmniArmorData["NormalUnobtaniumHead0"],Torso=OmniArmorData["NormalUnobtaniumTorso0"],Arms=OmniArmorData["NormalUnobtaniumArms0"],Legs=OmniArmorData["NormalUnobtaniumLegs0"],Feet=OmniArmorData["NormalUnobtaniumFeet0"]):
		self.Head=Head
		self.Torso=Torso
		self.Arms=Arms
		self.Legs=Legs
		self.Feet=Feet

class Equipment():
	def __init__(self,Unit):
		self.Unit=Unit
		self.Stats=Unit.Stats
	@property
	def Check(self):
		return self.Stats[0]

class Weapon(Equipment):
	def __init__(self,WeaponData=OmniWeaponData["NormalUnobtaniumSaber0"]):
		self.WeaponData=WeaponData
		self.Equipment=Equipment
	@property
	def PDMG(self):
		return self.WeaponData[0]
	@property
	def MDMG(self):
		return self.WeaponData[1]
	@property
	def ATA(self):
		return self.WeaponData[2]
	@property
	def WT(self):
		return self.WeaponData[3]
	@property
	def Buy(self):
		return self.WeaponData[4]
	@property
	def Sell(self):
		return self.WeaponData[5]

class Shield():
	def __init__(self,ShieldData=OmniArmorData["NormalUnobtaniumMediumShield0"]):
		self.ShieldData=ShieldData
	@property
	def PAR(self):
		return (self.ShieldData[0])
	@property
	def MAR(self):
		return (self.ShieldData[1])
	@property
	def WT(self):
		return (self.ShieldData[2])
	@property
	def Buy(self):
		return (self.ShieldData[3])
	@property
	def Sell(self):
		return (self.ShieldData[4])

class Foe():
	def __init__(self,Name="None",Element="Null",Stats=OmniMonsterData["NormalNormalDummy1"],ArmorSet=ArmorSet(),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=Shield()):
		self.Name=Name
		self.Element=Element
		self.Stats=Stats
		self.ArmorSet=ArmorSet
		self.Weapon1=Weapon1
		self.Weapon2=Weapon2
		self.Weapon3=Weapon3
		self.Shield=Shield
	@property
	def HP(self):
		return round(self.Stats[0])
	@property
	def ENE(self):
		return round(self.Stats[1])
	@property
	def STR(self):
		return round(self.Stats[2])
	@property
	def SPR(self):
		return round(self.Stats[3])
	@property
	def SKL(self):
		return round(self.Stats[4])
	@property
	def ABL(self):
		return round(self.Stats[5])
	@property
	def AGI(self):
		return round(self.Stats[6])
	@property
	def EVA(self):
		return round(self.Stats[7])+min(0,self.EffectiveWT)
	@property
	def TGH(self):
		return round(self.Stats[8])
	@property
	def RES(self):
		return round(self.Stats[9])
	@property
	def LCK(self):
		return round(self.Stats[10])
	@property
	def PAR(self):
		UserShield=self.Name+"Shield"
		ShieldPos=getattr(Shielding,UserShield)
		importlib.reload(Shielding)
		if ShieldPos == "Equipped":
			return self.ArmorSet[0][0]+self.ArmorSet[1][0]+self.ArmorSet[2][0]+self.ArmorSet[3][0]+self.ArmorSet[4][0]+self.Shield[0]
		else:
			return self.ArmorSet[0][0]+self.ArmorSet[1][0]+self.ArmorSet[2][0]+self.ArmorSet[3][0]+self.ArmorSet[4][0]
	@property
	def MAR(self):
		UserShield=self.Name+"Shield"
		ShieldPos=getattr(Shielding,UserShield)
		importlib.reload(Shielding)
		if ShieldPos == "Equipped":
			return self.ArmorSet[0][1]+self.ArmorSet[1][1]+self.ArmorSet[2][1]+self.ArmorSet[3][1]+self.ArmorSet[4][1]+self.Shield[1]
		else:
			return self.ArmorSet[0][1]+self.ArmorSet[1][1]+self.ArmorSet[2][1]+self.ArmorSet[3][1]+self.ArmorSet[4][1]
	@property
	def ArmorWT(self):
		return self.ArmorSet[0][2]+self.ArmorSet[1][2]+self.ArmorSet[2][2]+self.ArmorSet[3][2]+self.ArmorSet[4][2]
	@property
	def WT(self):
		return self.ArmorWT+self.Stats[11]
	@property
	def EffectiveWT(self):
		return round(min(0,self.STR-self.ArmorWT))
	@property
	def PDEF(self):
		return round(self.PAR+self.TGH)
	@property
	def MDEF(self):
		return round(self.MAR+self.RES)
	def __str__(self):
		return(
		f"""These are your stats, {self.Name}.\n HP: {self.HP} \n ENE: {self.ENE} \n STR: {self.STR} \n SPR: {self.SPR} \n SKL: {self.SKL} \n ABL: {self.ABL} \n AGI: {self.AGI} \n EVA: {self.EVA} \n TGH: {self.TGH} \n RES: {self.RES} \n LCK: {self.LCK} \n PAR: {self.PAR} \n MAR: {self.MAR} \n Weight: {self.WT}""")
#Placeheld
class Unit(object):
	def __init__(self,Name="None",Level=1,Element="Null",Stats="DummyDummyClassDU",ArmorSet=(),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=Shield(),Trait1=DummyTrait(),Trait2=DummyTrait(),Trait3=DummyTrait(),Trait4=DummyTrait(),Trait5=DummyTrait(),Accessory1=Accessory(),Accessory2=Accessory(),Accessory3=Accessory(),Accessory4=Accessory()):
		self.Name=Name
		self.Level=Level
		self.Element=Element
		self.Stats=OmniUnitData[Stats+str(self.Level)]
		self.ArmorSet=ArmorSet
		self.Weapon1=Weapon1
		self.Weapon2=Weapon2
		self.Weapon3=Weapon3
		self.Shield=Shield
		self.Trait1=Trait1
		self.Trait2=Trait2
		self.Trait3=Trait3
		self.Trait4=Trait4
		self.Trait5=Trait5
		self.Accessory1=Accessory1
		self.Accessory2=Accessory2
		self.Accessory3=Accessory3
		self.Accessory4=Accessory4
	@property
	def LVL(self):
		return int(self.Level)
	@property
	def HP(self):
		return round(self.Stats[0]+self.Trait1.HPPlus+self.Trait1.HPMinus+self.Trait2.HPPlus+self.Trait2.HPMinus+self.Trait3.HPPlus+self.Trait3.HPMinus+self.Trait4.HPPlus+self.Trait4.HPMinus+self.Trait5.HPPlus+self.Trait5.HPMinus+self.Accessory1.HPPlus+self.Accessory1.HPMinus+self.Accessory2.HPPlus+self.Accessory2.HPMinus+self.Accessory3.HPPlus+self.Accessory3.HPMinus+self.Accessory4.HPPlus+self.Accessory4.HPMinus)
	@property
	def ENE(self):
		return round(self.Stats[1]+self.Trait1.ENEPlus+self.Trait1.ENEMinus+self.Trait2.ENEPlus+self.Trait2.ENEMinus+self.Trait3.ENEPlus+self.Trait3.ENEMinus+self.Trait4.ENEPlus+self.Trait4.ENEMinus+self.Trait5.ENEPlus+self.Trait5.ENEMinus+self.Accessory1.ENEPlus+self.Accessory1.ENEMinus+self.Accessory2.ENEPlus+self.Accessory2.ENEMinus+self.Accessory3.ENEPlus+self.Accessory3.ENEMinus+self.Accessory4.ENEPlus+self.Accessory4.ENEMinus)
	@property
	def STR(self):
		return round(self.Stats[2]+self.Trait1.STRPlus+self.Trait1.STRMinus+self.Trait2.STRPlus+self.Trait2.STRMinus+self.Trait3.STRPlus+self.Trait3.STRMinus+self.Trait4.STRPlus+self.Trait4.STRMinus+self.Trait5.STRPlus+self.Trait5.STRMinus+self.Accessory1.STRPlus+self.Accessory1.STRMinus+self.Accessory2.STRPlus+self.Accessory2.STRMinus+self.Accessory3.STRPlus+self.Accessory3.STRMinus+self.Accessory4.STRPlus+self.Accessory4.STRMinus)
	@property
	def SPR(self):
		return round(self.Stats[3]+self.Trait1.SPRPlus+self.Trait1.SPRMinus+self.Trait2.SPRPlus+self.Trait2.SPRMinus+self.Trait3.SPRPlus+self.Trait3.SPRMinus+self.Trait4.SPRPlus+self.Trait4.SPRMinus+self.Trait5.SPRPlus+self.Trait5.SPRMinus+self.Accessory1.SPRPlus+self.Accessory1.SPRMinus+self.Accessory2.SPRPlus+self.Accessory2.SPRMinus+self.Accessory3.SPRPlus+self.Accessory3.SPRMinus+self.Accessory4.SPRPlus+self.Accessory4.SPRMinus)
	@property
	def SKL(self):
		return round(self.Stats[4]+self.Trait1.SKLPlus+self.Trait1.SKLMinus+self.Trait2.SKLPlus+self.Trait2.SKLMinus+self.Trait3.SKLPlus+self.Trait3.SKLMinus+self.Trait4.SKLPlus+self.Trait4.SKLMinus+self.Trait5.SKLPlus+self.Trait5.SKLMinus+self.Accessory1.SKLPlus+self.Accessory1.SKLMinus+self.Accessory2.SKLPlus+self.Accessory2.SKLMinus+self.Accessory3.SKLPlus+self.Accessory3.SKLMinus+self.Accessory4.SKLPlus+self.Accessory4.SKLMinus)
	@property
	def ABL(self):
		return round(self.Stats[5]+self.Trait1.ABLPlus+self.Trait1.ABLMinus+self.Trait2.ABLPlus+self.Trait2.ABLMinus+self.Trait3.ABLPlus+self.Trait3.ABLMinus+self.Trait4.ABLPlus+self.Trait4.ABLMinus+self.Trait5.ABLPlus+self.Trait5.ABLMinus+self.Accessory1.ABLPlus+self.Accessory1.ABLMinus+self.Accessory2.ABLPlus+self.Accessory2.ABLMinus+self.Accessory3.ABLPlus+self.Accessory3.ABLMinus+self.Accessory4.ABLPlus+self.Accessory4.ABLMinus)
	@property
	def AGI(self):
		return round(self.Stats[6]+self.Trait1.AGIPlus+self.Trait1.AGIMinus+self.Trait2.AGIPlus+self.Trait2.AGIMinus+self.Trait3.AGIPlus+self.Trait3.AGIMinus+self.Trait4.AGIPlus+self.Trait4.AGIMinus+self.Trait5.AGIPlus+self.Trait5.AGIMinus+self.Accessory1.AGIPlus+self.Accessory1.AGIMinus+self.Accessory2.AGIPlus+self.Accessory2.AGIMinus+self.Accessory3.AGIPlus+self.Accessory3.AGIMinus+self.Accessory4.AGIPlus+self.Accessory4.AGIMinus)
	@property
	def EVA(self):
		return round((self.Stats[7])+self.Trait1.EVAPlus+self.Trait1.EVAMinus+self.Trait2.EVAPlus+self.Trait2.EVAMinus+self.Trait3.EVAPlus+self.Trait3.EVAMinus+self.Trait4.EVAPlus+self.Trait4.EVAMinus+self.Trait5.EVAPlus+self.Trait5.EVAMinus+self.Accessory1.EVAPlus+self.Accessory1.EVAMinus+self.Accessory2.EVAPlus+self.Accessory2.EVAMinus+self.Accessory3.EVAPlus+self.Accessory3.EVAMinus+self.Accessory4.EVAPlus+self.Accessory4.EVAMinus+min(0,self.EffectiveWT))
	@property
	def TGH(self):
		return round(self.Stats[8]+self.Trait1.TGHPlus+self.Trait1.TGHMinus+self.Trait2.TGHPlus+self.Trait2.TGHMinus+self.Trait3.TGHPlus+self.Trait3.TGHMinus+self.Trait4.TGHPlus+self.Trait4.TGHMinus+self.Trait5.TGHPlus+self.Trait5.TGHMinus+self.Accessory1.TGHPlus+self.Accessory1.TGHMinus+self.Accessory2.TGHPlus+self.Accessory2.TGHMinus+self.Accessory3.TGHPlus+self.Accessory3.TGHMinus+self.Accessory4.TGHPlus+self.Accessory4.TGHMinus)
	@property
	def RES(self):
		return round(self.Stats[9]+self.Trait1.RESPlus+self.Trait1.RESMinus+self.Trait2.RESPlus+self.Trait2.RESMinus+self.Trait3.RESPlus+self.Trait3.RESMinus+self.Trait4.RESPlus+self.Trait4.RESMinus+self.Trait5.RESPlus+self.Trait5.RESMinus+self.Accessory1.RESPlus+self.Accessory1.RESMinus+self.Accessory2.RESPlus+self.Accessory2.RESMinus+self.Accessory3.RESPlus+self.Accessory3.RESMinus+self.Accessory4.RESPlus+self.Accessory4.RESMinus)
	@property
	def LCK(self):
		return round(self.Stats[10]+self.Trait1.LCKPlus+self.Trait1.LCKMinus+self.Trait2.LCKPlus+self.Trait2.LCKMinus+self.Trait3.LCKPlus+self.Trait3.LCKMinus+self.Trait4.LCKPlus+self.Trait4.LCKMinus+self.Trait5.LCKPlus+self.Trait5.LCKMinus+self.Accessory1.LCKPlus+self.Accessory1.LCKMinus+self.Accessory2.LCKPlus+self.Accessory2.LCKMinus+self.Accessory3.LCKPlus+self.Accessory3.LCKMinus+self.Accessory4.LCKPlus+self.Accessory4.LCKMinus)
	@property
	def PAR(self):
		UserShield=self.Name+"Shield"
		ShieldPos=getattr(Shielding,UserShield)
		importlib.reload(Shielding)
		if ShieldPos == "Equipped":
			return self.ArmorSet[0][0]+self.ArmorSet[1][0]+self.ArmorSet[2][0]+self.ArmorSet[3][0]+self.ArmorSet[4][0]+self.Shield[0]
		else:
			return self.ArmorSet[0][0]+self.ArmorSet[1][0]+self.ArmorSet[2][0]+self.ArmorSet[3][0]+self.ArmorSet[4][0]
	@property
	def MAR(self):
		UserShield=self.Name+"Shield"
		ShieldPos=getattr(Shielding,UserShield)
		importlib.reload(Shielding)
		if ShieldPos == "Equipped":
			return self.ArmorSet[0][1]+self.ArmorSet[1][1]+self.ArmorSet[2][1]+self.ArmorSet[3][1]+self.ArmorSet[4][1]+self.Shield[1]
		else:
			return self.ArmorSet[0][1]+self.ArmorSet[1][1]+self.ArmorSet[2][1]+self.ArmorSet[3][1]+self.ArmorSet[4][1]
	@property
	def ArmorWT(self):
		UserShield=self.Name+"Shield"
		ShieldPos=getattr(Shielding,UserShield)
		importlib.reload(Shielding)
		if ShieldPos == "Equipped":
			return self.ArmorSet[0][2]+self.ArmorSet[1][2]+self.ArmorSet[2][2]+self.ArmorSet[3][2]+self.ArmorSet[4][2]+self.Shield[2]
		else:
			return self.ArmorSet[0][2]+self.ArmorSet[1][2]+self.ArmorSet[2][2]+self.ArmorSet[3][2]+self.ArmorSet[4][2]
	@property
	def WT(self):
		return self.ArmorSet[0][2]+self.ArmorSet[1][2]+self.ArmorSet[2][2]+self.ArmorSet[3][2]+self.ArmorSet[4][2]
	@property
	def EffectiveWT(self):
		return round(min(0,self.STR-self.ArmorWT))
	@property
	def PDEF(self):
		return round(self.PAR+self.TGH)
	@property
	def MDEF(self):
		return round(self.MAR+self.RES)
	def __str__(self):
		return(
		f"""You are Lv{self.Level}, and these are your stats, {self.Name}.\n HP: {self.HP} \n ENE: {self.ENE} \n STR: {self.STR} \n SPR: {self.SPR} \n SKL: {self.SKL} \n ABL: {self.ABL} \n AGI: {self.AGI} \n EVA: {self.EVA} \n TGH: {self.TGH} \n RES: {self.RES} \n LCK: {self.LCK} \n PAR: {self.PAR} \n MAR: {self.MAR} \n Weight: {self.WT}""")
class StatSoul(Unit):
	def __init__(self,Level=Unit.LVL,Boon="STR",Bane="SPR"):
		self.Level=Level
		self.Change=Level*3
		self.Boon=Boon
		self.Bane=Bane
	@property
	def HPPlus(self):
		return 0
	@property
	def HPMinus(self):
		return 0
	@property
	def ENEPlus(self):
		return 0
	@property
	def ENEMinus(self):
		return 0
	@property
	def STRPlus(self):
		if self.Boon == "STR":
			return self.Change
		else:
			return 0
	@property
	def STRMinus(self):
		if self.Bane == "STR":
			return self.Change
		else:
			return 0
	@property
	def SPRPlus(self):
		if self.Boon == "SPR":
			return self.Change
		else:
			return 0
	@property
	def SPRMinus(self):
		if self.Bane == "SPR":
			return self.Change
		else:
			return 0
	@property
	def SKLPlus(self):
		if self.Boon == "SKL":
			return self.Change
		else:
			return 0
	@property
	def SKLMinus(self):
		if self.Bane == "SKL":
			return self.Change
		else:
			return 0
	@property
	def ABLPlus(self):
		if self.Boon == "ABL":
			return self.Change
		else:
			return 0
	@property
	def ABLMinus(self):
		if self.Bane == "ABL":
			return self.Change
		else:
			return 0
	@property
	def AGIPlus(self):
		if self.Boon == "AGI":
			return self.Change
		else:
			return 0
	@property
	def AGIMinus(self):
		if self.Bane == "AGI":
			return self.Change
		else:
			return 0
	@property
	def EVAPlus(self):
		if self.Boon == "EVA":
			return self.Change
		else:
			return 0
	@property
	def EVAMinus(self):
		if self.Bane == "EVA":
			return self.Change
		else:
			return 0
	@property
	def TGHPlus(self):
		if self.Boon == "TGH":
			return self.Change
		else:
			return 0
	@property
	def TGHMinus(self):
		if self.Bane == "TGH":
			return self.Change
		else:
			return 0
	@property
	def RESPlus(self):
		if self.Boon == "RES":
			return self.Change
		else:
			return 0
	@property
	def RESMinus(self):
		if self.Bane == "RES":
			return self.Change
		else:
			return 0
	@property
	def LCKPlus(self):
		return 0
	@property
	def LCKMinus(self):
		return 0
	def __str__(self):
		return(
		f"""Your Boon is {self.Boon}. Your Bane is {self.Bane}. Each stat is modified by {self.Change}.""")
WSD={}
WSD["Dummy"]=Unit("Dummy",1,Null,Stats="DummyDummyClassDU",ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["Dummy"])

#Mercenaries
WSD["Higgins"]=Unit("Higgins",3,Earth,Stats="SoulbladeVagabondSB",ArmorSet=(OmniArmorData["NormalTinHead0"],OmniArmorData["NormalTinTorso0"],OmniArmorData["NormalTinArms0"],OmniArmorData["NormalTinLegs0"],OmniArmorData["NormalTinFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalShardsteelSaber0"]),Weapon2=Weapon(OmniWeaponData["NormalIvoryCane5"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalTinSmallShield0"]))
#print(WSD["Higgins"])

#GM's Characters
#Reyn
WSD["Reyn"]=Unit("Reyn",3,Solar,Stats="WilderKnightWI",ArmorSet=(OmniArmorData["NormalTungstenHead0"],OmniArmorData["NormalTungstenTorso0"],OmniArmorData["NormalTungstenArms0"],OmniArmorData["NormalTungstenLegs0"],OmniArmorData["NormalTungstenFeet0"]),Weapon1=Weapon(OmniWeaponData["StonyTungstenGreatsword0"]),Weapon2=Weapon(OmniWeaponData["NormalTungstenPolearm0"]),Weapon3=Weapon(OmniWeaponData["NormalBronzePolearm3"]),Shield=Shield(OmniArmorData["NormalTungstenMediumShield0"]),Accessory1=ACC["ReflectiveCoating"])
#print(WSD["Reyn"])

#Brad
WSD["Brad"]=Unit("Brad",2,Lunar,Stats="SoulbladeArcherSB",ArmorSet=(OmniArmorData["NormalBronzeHead0"],OmniArmorData["NormalBronzeTorso0"],OmniArmorData["NormalBronzeArms0"],OmniArmorData["NormalBronzeLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBronzeBow0"]),Weapon2=Weapon(OmniWeaponData["NormalBoneKnife0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalSteelSmallShield0"]))
#print(WSD["Brad"])

#Renfield, Brad's Ogre Zombie
WSD["Renfield"]=Foe("Renfield",Earth,Stats=OmniMonsterData["NormalZombieOgre2"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBoneKnuckles1"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))

#Aeront's Characters
#Gilligan
WSD["Gilligan"]=Unit("Gilligan",2,Wind,Stats="OriginMonkOR",ArmorSet=(OmniArmorData["NormalCopperHead0"],OmniArmorData["NormalBronzeTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalTungstenLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalWoodClaw0"]),Weapon2=Weapon(OmniWeaponData["NormalBoneKnuckles0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Trait1=StatSoul(2,"AGI","RES"),Accessory1=ACC["SnowshoeWebbing"])
#print(WSD["Gilligan"])

#Snow's Characters
#Lirru
WSD["Lirru"]=Unit("Lirru",2,Flame,Stats="WilderVagabondWI",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalTungstenSaber0"]),Weapon2=Weapon(OmniWeaponData["BlazingIvoryKnuckles0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Accessory1=ACC["OpalBrooch"])
#print(WSD["Lirru"])

#Tempest's Characters
#Clips(St Nick's Workshop ver.)
WSD["StClips"]=Unit("StClips",2,Earth,Stats="MechanixGunnerMX",ArmorSet=(OmniArmorData["NormalSilkHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=Weapon(OmniWeaponData["FestiveWoodMechgun2"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Accessory1=ACC["OpalBrooch"])
#print(WSD["StClips"])

#Helm
WSD["Helm"]=Unit("Helm",2,Storm,Stats="OriginVagabondOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalSilkLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalCopperSaber0"]),Weapon2=Weapon(OmniWeaponData["NormalIvoryHandbow0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalCottonSmallShield0"]),Accessory1=ACC["SilkSash"])
#print(WSD["Helm"])

#Impromptu's Characters
#Yule Walker
WSD["Yule"]=Unit("Yule",2,Water,Stats="OriginBardOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalTungstenYoyo0"]),Weapon2=Weapon(OmniWeaponData["NormalGoldMic0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Accessory1=ACC["SnowshoeWebbing"])
#print(WSD["Yule"])

#Roselyn Wolfe
WSD["Roselyn"]=Unit("Roselyn",2,Flame,Stats="WilderMedicWI",ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalIvoryWand0"]),Weapon2=Weapon(OmniWeaponData["NormalCobaltBattlecannon0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalBronzeSmallShield0"]),Accessory1=ACC["LatticeShieldM"])
#print(WSD["Roselyn"])

#KMJ's Characters
#Jango
WSD["Jango"]=Unit(Name="Jango",Level=2,Element=Solar,Stats="SoulbladeThiefSB",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["ReinforcedBoneKnife0"]),Weapon2=Weapon(OmniWeaponData["ReinforcedBoneKnife0"]),Weapon3=Weapon(OmniWeaponData["NormalTinSlicer3"]),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Trait1=StatSoul(2,"SKL","RES"),Accessory1=ACC["GlassMonocle"])
#print(WSD["Jango"])

#Numbereds
#The First Monk
WSD["One"]=Unit("One",4,Void,Stats="SoulbladeMonkSB",ArmorSet=(OmniArmorData["NormalLeatherHead3"],OmniArmorData["NormalLeatherTorso3"],OmniArmorData["MasterworkLeatherArms10"],OmniArmorData["NormalLeatherLegs3"],OmniArmorData["NormalLeatherFeet3"]),Weapon1=Weapon(OmniWeaponData["BreezyBronzeBattlestaff4"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["One"])

WSD["Two"]=Unit("Two",2,Earth,Stats="SoulbladeMonkSB",ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBoneKnuckles4"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Accessory1=ACC["FurHemwork"])
#print(WSD["Two"])

#The Third Witch
WSD["Three"]=Unit("Three",1,Water,Stats="OriginApostleOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalBronzeArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["AttunedIvoryWand10"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["ReinforcedCottonMediumShield10"]),Accessory1=Wiggles(1))
print(WSD["Three"])

#The Fourth Judge
WSD["Four"]=Unit("Four",7,Lunar,Stats="VampireSummonerVM",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["ReinforcedBronzeWhip10"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["Four"])

#The Fifth General
WSD["Five"]=Unit("Five",1,Wind,Stats="MechanixSoldierOR",ArmorSet=(OmniArmorData["NormalBronzeHead0"],OmniArmorData["NormalCopperTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalBronzeLegs0"],OmniArmorData["ReinforcedBronzeFeet10"]),Weapon1=Weapon(OmniWeaponData["AccurateTinTwinPistol10"]),Weapon2=Weapon(OmniWeaponData["AccurateWoodPolearm0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["Five"])

#The Sixth Knight
WSD["Six"]=Unit("Six",2,Flame,Stats="WilderKnightWI",ArmorSet=(OmniArmorData["NormalCobaltHead0"],OmniArmorData["NormalCopperTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalCobaltLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalCobaltFlail10"]),Weapon2=Weapon(OmniWeaponData["NormalCobaltGreatsword3"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalCobaltMediumShield0"]),Accessory1=ACC["MadScientistGoggles"],Accessory2=ACC["LuckyCoinNecklace"])
#print(WSD["Six"])

#The Seventh Sage
WSD["Sev"]=Unit("Sev",1,Earth,Stats="SoulsongMageOR",ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalLeatherTorso10"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalIvoryWand0"]),Weapon2=Weapon(OmniWeaponData["NormalCobaltKnuckles0"]),Weapon3=(OmniWeaponData["BlazingCopperRod2"]),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Trait1=StatSoul(1,"STR","TGH"),Accessory1=ACC["IronBangle"],Accessory2=ACC["GlassMonocle"])
#print(WSD["Sev"])

#The Eleventh Sorceress
WSD["Eleven"]=Unit("Eleven",2,Lightning,Stats="OriginMageOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalTinTalis3"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Accessory1=ACC["LatticeShieldM"],Accessory2=ACC["BloodstoneBrooch"])
#print(WSD["Eleven"])

#Janet Steel
WSD["Janet"]=Unit("Janet",2,Lightning,Stats="OriginArcherOR",ArmorSet=(OmniArmorData["NormalTinHead0"],OmniArmorData["NormalTinTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalTinLegs0"],OmniArmorData["NormalTinFeet0"]),Weapon1=Weapon(OmniWeaponData["ElectricTinCrossbow2"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),Accessory1=ACC["FurHemwork"])
#print(WSD["Janet"])

#Wander Steel
WSD["Wander"]=Unit("Wander",2,Flame,Stats="OriginMedicOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalLeatherArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["BlazingCopperRod0"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["Wander"])

#Fae Rider
WSD["FaeRider"]=Unit("FaeRider",2,Null,Stats="OriginVagabondSB",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["ReinforcedWoodBow2"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["FaeRider"])

#Reintaur
ReintaurLevel=2
WSD["Reintaur"]=Foe("Reintaur",Water,Stats=OmniMonsterData["LargeBrutishCentaur"+str(ReintaurLevel)],ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalTinArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalWoodCrossbow10"]),Weapon2=Weapon(OmniWeaponData["NormalWoodWarhammer10"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["Reintaur"])

#Norwolf
WSD["Norwolf"]=Foe("Norwolf",Water,Stats=OmniMonsterData["NormalSpiritedWolf1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBoneClaw0"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]))
#print(WSD["Norwolf"])

#WSD["Josephine"]=Unit("Josephine",Wind,Stats=OmniUnitData["OriginThiefOR1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCopperFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalIronKnife10"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalCobaltSmallShield0"]))
#print(WSD["Josephine"])

#========#
#Monsters#
#========#
WSD["DummyFoe"]=Foe("DummyFoe",Null,Stats=OmniMonsterData["NormalNormalDummy1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=())
