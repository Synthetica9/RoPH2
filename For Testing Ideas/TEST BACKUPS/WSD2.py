from ArmorsOO import OmniArmorData
from WeaponsOO import OmniWeaponData
from DressingRoomOO import OmniUnitData
from MonsterFactoryOO import OmniMonsterData
import random as ra
#import HealthBar
#import EnergyBar
import Shielding
import importlib

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

class StatPlus():
	def __init__(self,PlusHP=0,PlusENE=0,PlusSTR=0,PlusSPR=0,PlusSKL=0,PlusABL=0,PlusAGI=0,PlusEVA=0,PlusTGH=0,PlusRES=0,PlusLCK=0):
		self.PlusHP=PlusHP
		self.PlusENE=PlusENE
		self.PlusSTR=PlusSTR
		self.PlusSPR=PlusSPR
		self.PlusSKL=PlusSKL
		self.PlusABL=PlusABL
		self.PlusAGI=PlusAGI
		self.PlusEVA=PlusEVA
		self.PlusTGH=PlusTGH
		self.PlusRES=PlusRES
		self.PlusLCK=PlusLCK

class Foe():
	def __init__(self,Name="None",Element="Null",Stats=OmniMonsterData["NormalNormalDummy1"],ArmorSet=ArmorSet(),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=Shield(),StatPlus=StatPlus()):
		self.Name=Name
		self.Element=Element
		self.Stats=Stats
		self.ArmorSet=ArmorSet
		self.Weapon1=Weapon1
		self.Weapon2=Weapon2
		self.Weapon3=Weapon3
		self.Shield=Shield
		self.StatPlus=StatPlus
	@property
	def HP(self):
		return round(self.Stats[0]+self.StatPlus[0])
	@property
	def ENE(self):
		return round(self.Stats[1]+self.StatPlus[1])
	@property
	def STR(self):
		return round(self.Stats[2]+self.StatPlus[2])
	@property
	def SPR(self):
		return round(self.Stats[3]+self.StatPlus[3])
	@property
	def SKL(self):
		return round(self.Stats[4]+self.StatPlus[4])
	@property
	def ABL(self):
		return round(self.Stats[5]+self.StatPlus[5])
	@property
	def AGI(self):
		return round(self.Stats[6]+self.StatPlus[6])
	@property
	def EVA(self):
		return round(self.Stats[7]+self.StatPlus[7])+min(0,self.EffectiveWT)
	@property
	def TGH(self):
		return round(self.Stats[8]+self.StatPlus[8])
	@property
	def RES(self):
		return round(self.Stats[9]+self.StatPlus[9])
	@property
	def LCK(self):
		return round(self.Stats[10]+self.StatPlus[10])
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
	def __init__(self,Name="None",Level=1,Element="Null",Stats="DummyDummyClassDU",ArmorSet=(),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=Shield(),StatPlus=StatPlus()):
		self.Name=Name
		self.Level=Level
		self.Element=Element
		self.Stats=OmniUnitData[Stats+str(self.Level)]
		self.ArmorSet=ArmorSet
		self.Weapon1=Weapon1
		self.Weapon2=Weapon2
		self.Weapon3=Weapon3
		self.Shield=Shield
		self.StatPlus=StatPlus
	@property
	def HP(self):
		return round(self.Stats[0]+self.StatPlus[0])
	@property
	def ENE(self):
		return round(self.Stats[1]+self.StatPlus[1])
	@property
	def STR(self):
		return round(self.Stats[2]+self.StatPlus[2])
	@property
	def SPR(self):
		return round(self.Stats[3]+self.StatPlus[3])
	@property
	def SKL(self):
		return round(self.Stats[4]+self.StatPlus[4])
	@property
	def ABL(self):
		return round(self.Stats[5]+self.StatPlus[5])
	@property
	def AGI(self):
		return round(self.Stats[6]+self.StatPlus[6])
	@property
	def EVA(self):
		return round((self.Stats[7]+self.StatPlus[7])+min(0,self.EffectiveWT))
	@property
	def TGH(self):
		return round(self.Stats[8]+self.StatPlus[8])
	@property
	def RES(self):
		return round(self.Stats[9]+self.StatPlus[9])
	@property
	def LCK(self):
		return round(self.Stats[10]+self.StatPlus[10])
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
		f"""These are your stats, {self.Name}.\n HP: {self.HP} \n ENE: {self.ENE} \n STR: {self.STR} \n SPR: {self.SPR} \n SKL: {self.SKL} \n ABL: {self.ABL} \n AGI: {self.AGI} \n EVA: {self.EVA} \n TGH: {self.TGH} \n RES: {self.RES} \n LCK: {self.LCK} \n PAR: {self.PAR} \n MAR: {self.MAR} \n Weight: {self.WT}""")

WSD={}
WSD["Dummy"]=Unit("Dummy",1,Null,Stats="DummyDummyClassDU",ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Dummy"])

#Mercenaries
WSD["Higgins"]=Unit("Higgins",3,Earth,Stats="SoulbladeVagabondSB",ArmorSet=(OmniArmorData["NormalTinHead0"],OmniArmorData["NormalTinTorso0"],OmniArmorData["NormalTinArms0"],OmniArmorData["NormalTinLegs0"],OmniArmorData["NormalTinFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalShardsteelSaber0"]),Weapon2=Weapon(OmniWeaponData["NormalIvoryCane5"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalTinSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Higgins"])

#GM's Characters
#Reyn
WSD["Reyn"]=Unit("Reyn",3,Solar,Stats="WilderKnightWI",ArmorSet=(OmniArmorData["NormalTungstenHead0"],OmniArmorData["NormalTungstenTorso0"],OmniArmorData["NormalTungstenArms0"],OmniArmorData["NormalTungstenLegs0"],OmniArmorData["NormalTungstenFeet0"]),Weapon1=Weapon(OmniWeaponData["StonyTungstenGreatsword0"]),Weapon2=Weapon(OmniWeaponData["NormalTungstenPolearm0"]),Weapon3=Weapon(OmniWeaponData["NormalBronzePolearm3"]),Shield=Shield(OmniArmorData["NormalTungstenMediumShield0"]),StatPlus=(0,0,0,0,0,0,0,-2,0,0,0))
#print(WSD["Reyn"])

#Brad
WSD["Brad"]=Unit("Brad",2,Lunar,Stats="SoulbladeArcherSB",ArmorSet=(OmniArmorData["NormalBronzeHead0"],OmniArmorData["NormalBronzeTorso0"],OmniArmorData["NormalBronzeArms0"],OmniArmorData["NormalBronzeLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBronzeBow0"]),Weapon2=Weapon(OmniWeaponData["NormalBoneKnife0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalSteelSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Brad"])

#Renfield, Brad's Ogre Zombie
WSD["Renfield"]=Foe("Renfield",Earth,Stats=OmniMonsterData["NormalZombieOgre2"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBoneKnuckles1"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))

#Aeront's Characters
#Gilligan
WSD["Gilligan"]=Unit("Gilligan",2,Wind,Stats="OriginMonkOR",ArmorSet=(OmniArmorData["NormalCopperHead0"],OmniArmorData["NormalBronzeTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalTungstenLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalWoodClaw0"]),Weapon2=Weapon(OmniWeaponData["NormalBoneKnuckles0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,-7,0,0,3,10,3,0,0,0))
#print(WSD["Gilligan"])

#Snow's Characters
#Lirru
WSD["Lirru"]=Unit("Lirru",2,Flame,Stats="WilderVagabondWI",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalTungstenSaber0"]),Weapon2=Weapon(OmniWeaponData["BlazingIvoryKnuckles0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,3,3,3,0,0,0,0,0,0))
#print(WSD["Lirru"])

#Tempest's Characters
#Clips(St Nick's Workshop ver.)
WSD["StClips"]=Unit("StClips",2,Earth,Stats="MechanixGunnerMX",ArmorSet=(OmniArmorData["NormalSilkHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=Weapon(OmniWeaponData["FestiveWoodMechgun2"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,3,3,3,0,0,0,0,0,0))
#print(WSD["StClips"])

#Helm
WSD["Helm"]=Unit("Helm",2,Storm,Stats="OriginVagabondOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalSilkLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalCopperSaber0"]),Weapon2=Weapon(OmniWeaponData["NormalIvoryHandbow0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalCottonSmallShield0"]),StatPlus=(0,0,0,2,0,0,0,0,0,0,0))
#print(WSD["Helm"])

#Impromptu's Characters
#Yule Walker
WSD["Yule"]=Unit("Yule",2,Water,Stats="OriginBardOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalTungstenYoyo0"]),Weapon2=Weapon(OmniWeaponData["NormalGoldMic0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,3,3,3,0,0,0))
#print(WSD["Yule"])

#Roselyn Wolfe
WSD["Roselyn"]=Unit("Roselyn",2,Flame,Stats="WilderMedicWI",ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalIvoryWand0"]),Weapon2=Weapon(OmniWeaponData["NormalCobaltBattlecannon0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalBronzeSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,2,0))
#print(WSD["Roselyn"])

#KMJ's Characters
#Jango
WSD["Jango"]=Unit("Jango",2,Solar,Stats="SoulbladeThiefSB",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["ReinforcedBoneKnife0"]),Weapon2=Weapon(OmniWeaponData["ReinforcedBoneKnife0"]),Weapon3=Weapon(OmniWeaponData["NormalTinSlicer3"]),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,2,0,0,0,0,0,0))
#print(WSD["Jango"])

#Numbereds
#The First Monk
WSD["One"]=Unit("One",4,Void,Stats="SoulbladeMonkSB",ArmorSet=(OmniArmorData["NormalLeatherHead3"],OmniArmorData["NormalLeatherTorso3"],OmniArmorData["MasterworkLeatherArms10"],OmniArmorData["NormalLeatherLegs3"],OmniArmorData["NormalLeatherFeet3"]),Weapon1=Weapon(OmniWeaponData["BreezyBronzeBattlestaff4"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["One"])

WSD["Two"]=Unit("Two",2,Earth,Stats="SoulbladeMonkSB",ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBoneKnuckles4"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,3,3,3))
#print(WSD["Two"])

#The Third Witch
WSD["Three"]=Unit("Three",1,Water,Stats="OriginApostleOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalBronzeArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["AttunedIvoryWand10"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["ReinforcedCottonMediumShield10"]),StatPlus=(0,0,5,5,5,5,5,5,5,5,5))
#print(WSD["Three"])

#The Fourth Judge
WSD["Four"]=Unit("Four",7,Lunar,Stats="VampireSummonerVM",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["ReinforcedBronzeWhip10"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Four"])

#The Fifth General
WSD["Five"]=Unit("Five",1,Wind,Stats="MechanixSoldierOR",ArmorSet=(OmniArmorData["NormalBronzeHead0"],OmniArmorData["NormalCopperTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalBronzeLegs0"],OmniArmorData["ReinforcedBronzeFeet10"]),Weapon1=Weapon(OmniWeaponData["AccurateTinTwinPistol10"]),Weapon2=Weapon(OmniWeaponData["AccurateWoodPolearm0"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Five"])

#The Sixth Knight
WSD["Six"]=Unit("Six",2,Flame,Stats="WilderKnightWI",ArmorSet=(OmniArmorData["NormalCobaltHead0"],OmniArmorData["NormalCopperTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalCobaltLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalCobaltFlail10"]),Weapon2=Weapon(OmniWeaponData["NormalCobaltGreatsword3"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalCobaltMediumShield0"]),StatPlus=(0,0,0,0,0,0,0,8,0,0,8))
#print(WSD["Six"])

#The Seventh Sage
WSD["Sev"]=Unit("Sev",1,Earth,Stats="SoulsongMageOR",ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalLeatherTorso10"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalIvoryWand0"]),Weapon2=Weapon(OmniWeaponData["NormalCobaltKnuckles0"]),Weapon3=(OmniWeaponData["BlazingCopperRod2"]),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,12,0,2,0,0,0,-10,0,0))
#print(WSD["Sev"])

#The Eleventh Sorceress
WSD["Eleven"]=Unit("Eleven",2,Lightning,Stats="OriginMageOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalTinTalis3"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,8,0,0,0,0,0,2,0))
#print(WSD["Eleven"])

#Janet Steel
WSD["Janet"]=Unit("Janet",2,Lightning,Stats="OriginArcherOR",ArmorSet=(OmniArmorData["NormalTinHead0"],OmniArmorData["NormalTinTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalTinLegs0"],OmniArmorData["NormalTinFeet0"]),Weapon1=Weapon(OmniWeaponData["ElectricTinCrossbow2"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,3,3,3))
#print(WSD["Janet"])
#Wander Steel
WSD["Wander"]=Unit("Wander",2,Flame,Stats="OriginMedicOR",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalLeatherArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["BlazingCopperRod0"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Wander"])

#Fae Rider
WSD["FaeRider"]=Unit("FaeRider",2,Null,Stats="OriginVagabondSB",ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=Weapon(OmniWeaponData["ReinforcedWoodBow2"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["FaeRider"])

#Reintaur
ReintaurLevel=2
WSD["Reintaur"]=Foe("Reintaur",Water,Stats=OmniMonsterData["LargeBrutishCentaur"+str(ReintaurLevel)],ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalTinArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalWoodCrossbow10"]),Weapon2=Weapon(OmniWeaponData["NormalWoodWarhammer10"]),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Reintaur"])

#Norwolf
WSD["Norwolf"]=Foe("Norwolf",Water,Stats=OmniMonsterData["NormalSpiritedWolf1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBoneClaw0"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalUnobtaniumSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Norwolf"])

#WSD["Josephine"]=Unit("Josephine",Wind,Stats=OmniUnitData["OriginThiefOR1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCopperFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalIronKnife10"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(OmniArmorData["NormalCobaltSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Josephine"])

#========#
#Monsters#
#========#
WSD["DummyFoe"]=Foe("DummyFoe",Null,Stats=OmniMonsterData["NormalNormalDummy1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))

WSD["Jelflame"]=Foe("Jelflame",Flame,Stats=OmniMonsterData["NormalNormalJel1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))

WSD["Ogre"]=Foe("Ogre",Null,Stats=OmniMonsterData["LargeNormalOgre2"],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=Weapon(OmniWeaponData["NormalBoneWarhammer4"]),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))

WSD["Arachnos"]=Foe("Arachnos",Wind,Stats=OmniMonsterData["LargeNormalArachnid3"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))