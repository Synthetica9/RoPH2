from ArmorsOO import OmniArmorData
from WeaponsOO import OmniWeaponData
from DressingRoomOO import OmniUnitData
from MonsterFactoryOO import OmniMonsterData
import random as ra

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

#class SaberSkill():
#	def __init__(self,Weapon=Saber(),StatCall,Stat1,Stat2,Stat3,Stat4):
#		self.Weapon=Weapon
#		self.StatCall=Unit.Stats
#		self.Stat1=Stat1
#		self.Stat2=Stat2
#		self.Stat3=Stat3
#		self.Stat4=Stat4
#	@property
#	def Damage(self):
#		return 

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
		return self.ArmorSet[0][0]+self.ArmorSet[1][0]+self.ArmorSet[2][0]+self.ArmorSet[3][0]+self.ArmorSet[4][0]
	@property
	def MAR(self):
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
	def __init__(self,Name="None",Element="Null",Stats=OmniUnitData["DummyDummyClassDU1"],ArmorSet=(),Weapon1=Weapon(),Weapon2=Weapon(),Weapon3=Weapon(),Shield=Shield(),StatPlus=StatPlus()):
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
	def AttackChoice1(self):
		return self.Weapon1
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
		return self.ArmorSet[0][0]+self.ArmorSet[1][0]+self.ArmorSet[2][0]+self.ArmorSet[3][0]+self.ArmorSet[4][0]
	@property
	def MAR(self):
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
WSD["Dummy"]=Unit("Dummy","Null",Stats=OmniUnitData["DummyDummyClassDU1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=(),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Dummy"])

#GM's Characters
#Reyn
ReynLevel=3
WSD["Reyn"]=Unit("Reyn","Lightning",Stats=OmniUnitData["WilderKnightWI"+str(ReynLevel)],ArmorSet=(OmniArmorData["NormalTungstenHead0"],OmniArmorData["NormalTungstenTorso0"],OmniArmorData["NormalTungstenArms0"],OmniArmorData["NormalTungstenLegs0"],OmniArmorData["NormalTungstenFeet0"]),Weapon1=Weapon(OmniWeaponData["IcyTungstenGreatsword0"]),Weapon2=Weapon(OmniWeaponData["NormalTungstenPolearm0"]),Weapon3=(),Shield=Shield(OmniArmorData["NormalTungstenMediumShield0"]),StatPlus=(0,0,0,0,0,0,0,-2,0,0,0))
#print(WSD["Reyn"])

#Apostle
WSD["Apostle"]=Unit("Apostle","Water",Stats=OmniUnitData["SoulsongApostleSS1"],ArmorSet=(OmniArmorData["NormalSilkHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalSilkLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=(OmniWeaponData["NormalIvoryWand0"]),Weapon2=(),Weapon3=(),Shield=(OmniArmorData["NormalSilkSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,2,0,0))
#print(WSD["Apostle"])

WSD["Gale"]=Unit("Gale","Wind",Stats=OmniUnitData["SoulsongMageSS1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalSilkLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=(OmniWeaponData["NormalIvoryRod0"]),Weapon2=(OmniWeaponData["NormalIvoryWand0"]),Weapon3=(),Shield=(),StatPlus=(0,0,0,2,0,0,0,0,0,0,0))
#print(WSD["Gale"])

#Brad
WSD["Brad"]=Unit("Brad","Flame",Stats=OmniUnitData["SoulbladeArcherSB1"],ArmorSet=(OmniArmorData["NormalBronzeHead0"],OmniArmorData["NormalBronzeTorso0"],OmniArmorData["NormalBronzeArms0"],OmniArmorData["NormalBronzeLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=(OmniWeaponData["NormalBronzeBow0"]),Weapon2=(OmniWeaponData["NormalBoneKnife0"]),Weapon3=(),Shield=(OmniArmorData["NormalSteelSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Brad"])

#Aeront's Characters
#Gilligan
WSD["Gilligan"]=Unit("Gilligan","Wind",Stats=OmniUnitData["OriginMonkOR2"],ArmorSet=(OmniArmorData["NormalCopperHead0"],OmniArmorData["NormalBronzeTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalTungstenLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=(OmniWeaponData["NormalWoodClaw0"]),Weapon2=(OmniWeaponData["NormalBoneKnuckles0"]),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,3,9,3,0,0-6,0))
#print(WSD["Gilligan"])

#Snow's Characters
#Lirru
WSD["Lirru"]=Unit("Lirru","Flame",Stats=OmniUnitData["WilderVagabondWI2"],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=(OmniWeaponData["NormalTungstenSaber0"]),Weapon2=(OmniWeaponData["BlazingIvoryKnuckles0"]),Weapon3=(),Shield=(),StatPlus=(0,0,3,3,3,0,0,0,0,0,0))
#print(WSD["Lirru"])

#Tempest's Characters
#Clips(St Nick's Workshop ver.)
WSD["StClips"]=Unit("StClips","Earth",Stats=OmniUnitData["MechanixGunnerMX2"],ArmorSet=(OmniArmorData["NormalSilkHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=(OmniWeaponData["FestiveWoodMechgun2"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,3,3,3,0,0,0,0,0,0))
#print(WSD["StClips"])

#Helm
HelmLevel=2
WSD["Helm"]=Unit("Helm","Storm",Stats=OmniUnitData["OriginVagabondOR"+str(HelmLevel)],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalSilkLegs0"],OmniArmorData["NormalSilkFeet0"]),Weapon1=(OmniWeaponData["NormalCopperSaber0"]),Weapon2=(OmniWeaponData["NormalIvoryHandbow0"]),Weapon3=(),Shield=(OmniArmorData["NormalCottonSmallShield0"]),StatPlus=(0,0,0,2,0,0,0,0,0,0,0))
#print(WSD["Helm"])

#Impromptu's Characters
#Yule Walker
WSD["Yule"]=Unit("Yule","Water",Stats=OmniUnitData["OriginBardOR2"],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=(OmniWeaponData["NormalTungstenYoyo0"]),Weapon2=(OmniWeaponData["NormalGoldMic0"]),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,3,3,3,0,0,0))
#print(WSD["Yule"])

#Roselyn Wolfe
RoselynLevel=2
WSD["Roselyn"]=Unit("Roselyn","Flame",Stats=OmniUnitData["WilderMedicWI"+str(RoselynLevel)],ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalSilkArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=(OmniWeaponData["NormalIvoryWand0"]),Weapon2=(OmniWeaponData["NormalCobaltBattlecannon0"]),Weapon3=(),Shield=(OmniArmorData["NormalBronzeSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,2,0))
#print(WSD["Roselyn"])

#KMJ's Characters
#Jango
JangoLevel=2
WSD["Jango"]=Unit("Jango","Flame",Stats=OmniUnitData["SoulbladeThiefSB"+str(JangoLevel)],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=(OmniWeaponData["ReinforcedBoneKnife0"]),Weapon2=(OmniWeaponData["ReinforcedBoneKnife0"]),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,8,0,0,0,0,0-6,0))
#print(WSD["Jango"])

#Numbereds
#The First Monk
WSD["One"]=Unit("One","Null",Stats=OmniUnitData["SoulbladeMonkSB4"],ArmorSet=(OmniArmorData["NormalLeatherHead3"],OmniArmorData["NormalLeatherTorso3"],OmniArmorData["MasterworkLeatherArms10"],OmniArmorData["NormalLeatherLegs3"],OmniArmorData["NormalLeatherFeet3"]),Weapon1=(OmniWeaponData["BreezyBronzeBattlestaff0"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["One"])

WSD["Two"]=Unit("Two","Earth",Stats=OmniUnitData["SoulbladeMonkSB2"],ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=(OmniWeaponData["NormalBoneKnuckles4"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,3,3,3))
#print(WSD["Two"])

#The Third Witch
WSD["Three"]=Unit("Three","Water",Stats=OmniUnitData["OriginApostleOR1"],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalSilkTorso0"],OmniArmorData["NormalBronzeArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=(OmniWeaponData["AttunedIvoryWand10"]),Weapon2=(),Weapon3=(),Shield=(OmniArmorData["ReinforcedCottonMediumShield10"]),StatPlus=(0,0,5,5,5,5,5,5,5,5,5))
#print(WSD["Three"])

#The Fourth Judge
WSD["Four"]=Unit("Four","Earth",Stats=OmniUnitData["OriginSummonerOR7"],ArmorSet=(OmniArmorData["NormalCottonHead3"],OmniArmorData["NormalCottonTorso7"],OmniArmorData["NormalCottonArms2"],OmniArmorData["NormalCottonLegs4"],OmniArmorData["NormalCottonFeet10"]),Weapon1=(OmniWeaponData["ReinforcedBronzeWhip10"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Four"])

#The Fifth General
WSD["Five"]=Unit("Five","Wind",Stats=OmniUnitData["MechanixSoldierOR1"],ArmorSet=(OmniArmorData["NormalBronzeHead0"],OmniArmorData["NormalCopperTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalBronzeLegs0"],OmniArmorData["ReinforcedBronzeFeet10"]),Weapon1=(OmniWeaponData["AccurateTinTwinPistol10"]),Weapon2=(OmniWeaponData["AccurateWoodPolearm0"]),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Five"])

#The Sixth Knight
WSD["Six"]=Unit("Six","Flame",Stats=OmniUnitData["WilderKnightWI2"],ArmorSet=(OmniArmorData["NormalCobaltHead0"],OmniArmorData["NormalCopperTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalCobaltLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=(OmniWeaponData["NormalCobaltFlail10"]),Weapon2=(),Weapon3=(),Shield=(OmniArmorData["NormalCobaltMediumShield0"]),StatPlus=(0,0,0,0,0,0,0,8,0,0,8))
#print(WSD["Six"])

#The Seventh Sage
WSD["Sev"]=Unit("Sev","Earth",Stats=OmniUnitData["OriginMageOR1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalLeatherTorso10"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=(OmniWeaponData["NormalIvoryWand0"]),Weapon2=(OmniWeaponData["NormalCobaltKnuckles0"]),Weapon3=(OmniWeaponData["BlazingCopperRod2"]),Shield=(),StatPlus=(0,0,3,0,2,0,0,0,-3,0,0))
#print(WSD["Sev"])

#The Eleventh Sorceress
WSD["Eleven"]=Unit("Eleven","Lightning",Stats=OmniUnitData["OriginMageOR2"],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=(OmniWeaponData["NormalTinTalis3"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,8,0,0,0,0,0,2,0))
#print(WSD["Eleven"])

#Janet Steel
JanetLevel=3
WSD["Janet"]=Unit("Janet","Lightning",Stats=OmniUnitData["OriginArcherOR"+str(JanetLevel)],ArmorSet=(OmniArmorData["NormalTinHead0"],OmniArmorData["NormalTinTorso0"],OmniArmorData["NormalCopperArms0"],OmniArmorData["NormalTinLegs0"],OmniArmorData["NormalTinFeet0"]),Weapon1=(OmniWeaponData["ElectricTinCrossbow2"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,3,3,3))
#print(WSD["Janet"])
#Wander Steel
WanderLevel=3
WSD["Wander"]=Unit("Wander","Flame",Stats=OmniUnitData["OriginMedicOR"+str(WanderLevel)],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalLeatherArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=(OmniWeaponData["BlazingCopperRod0"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Wander"])

#Fae Rider
WSD["FaeRider"]=Unit("FaeRider","Null",Stats=OmniUnitData["OriginVagabondSB2"],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=(OmniWeaponData["ReinforcedWoodBow2"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["FaeRider"])

#Reintaur
WSD["Reintaur"]=Foe("Reintaur","Water",Stats=OmniMonsterData["LargeBrutishCentaur2"],ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalTinArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=(OmniWeaponData["NormalWoodCrossbow5"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Reintaur"])

#Norwolf
WSD["Norwolf"]=Foe("Norwolf","Water",Stats=OmniMonsterData["NormalSpiritedWolf1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=(OmniWeaponData["NormalBoneClaw0"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Norwolf"])

#Josephine
JosephineLevel=2
WSD["Josephine"]=Unit("Josephine","Wind",Stats=OmniUnitData["OriginThiefOR"+str(JosephineLevel)],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCopperFeet0"]),Weapon1=(OmniWeaponData["NormalIronKnife10"]),Weapon2=(),Weapon3=(),Shield=(OmniArmorData["NormalCobaltSmallShield0"]),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Josephine"])

#========#
#Enemies: The Blacksmith's Niece
#========#
WSD["Robes"]=Unit("Robes","Wind",Stats=OmniUnitData["SoulbladeMonkSB3"],ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalLeatherArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=(),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Robes"])
WSD["Gunbo"]=Unit("Gunbo","Water",Stats=OmniUnitData["MechanixGunnerMX3"],ArmorSet=(OmniArmorData["NormalBronzeHead0"],OmniArmorData["NormalBronzeTorso0"],OmniArmorData["NormalBronzeArms0"],OmniArmorData["NormalBronzeLegs0"],OmniArmorData["NormalBronzeFeet0"]),Weapon1=(OmniWeaponData["NormalTungstenTwinPistol2"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Gunbo"])
WSD["Gachum"]=Unit("Gachum","Lightning",Stats=OmniUnitData["OriginThiefOR3"],ArmorSet=(OmniArmorData["NormalLeatherHead0"],OmniArmorData["NormalLeatherTorso0"],OmniArmorData["NormalLeatherArms0"],OmniArmorData["NormalLeatherLegs0"],OmniArmorData["NormalLeatherFeet0"]),Weapon1=(OmniWeaponData["NormalBoneKnife7"]),Weapon2=(OmniWeaponData["NormalTinSlicer3"]),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))
#print(WSD["Gachum"])

#========#
#Monsters#
#========#
WSD["DummyFoe"]=Foe("DummyFoe","Null",Stats=OmniMonsterData["NormalNormalDummy1"],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=(),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))

JelflameALevel=1
WSD["JelflameA"]=Foe("JelflameA","Flame",Stats=OmniMonsterData["NormalNormalJel"+str(JelflameALevel)],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=(),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))

OgreLevel=2
WSD["Ogre"]=Unit("Ogre","Earth",Stats=OmniMonsterData["LargeNormalOgre"+str(OgreLevel)],ArmorSet=(OmniArmorData["NormalCottonHead0"],OmniArmorData["NormalCottonTorso0"],OmniArmorData["NormalCottonArms0"],OmniArmorData["NormalCottonLegs0"],OmniArmorData["NormalCottonFeet0"]),Weapon1=(OmniWeaponData["NormalBoneWarhammer4"]),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))

ArachnosLevel=3
WSD["Arachnos"]=Foe("Arachnos","Lunar",Stats=OmniMonsterData["LargeNormalArachnid"+str(ArachnosLevel)],ArmorSet=(OmniArmorData["NormalUnobtaniumHead0"],OmniArmorData["NormalUnobtaniumTorso0"],OmniArmorData["NormalUnobtaniumArms0"],OmniArmorData["NormalUnobtaniumLegs0"],OmniArmorData["NormalUnobtaniumFeet0"]),Weapon1=(),Weapon2=(),Weapon3=(),Shield=(),StatPlus=(0,0,0,0,0,0,0,0,0,0,0))