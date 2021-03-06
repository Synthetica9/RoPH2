import Weapons as WEP
import random as ra
SizeMods=("DummySize","Tiny","Small","Medium","Large","Huge")
Modifiers=("DummyMod","Normal","Veteran","Healthy","Energetic","Strong","Spirited","Skillful","Capable","Agile","Evasive","Tough","Resistant","Lucky","Heavyweight","Lightweight","Featherweight","Brutish","Wizened","Savvy","Untouchable","GlassCannon")
BodyTypes=("DummyFoe","Hawk","Centaur","Wolf","BigCat","Skeleton","Ogre","Origin","Soulsong","Wilder","Soulblade","Mechanix","Vampire","Elemental","Jel","Gargoyle","Arachnid")
Levels=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")

MonsterFactoryInputs=[]
for s in SizeMods:
	for m in Modifiers:
		for b in BodyTypes:
			for l in Levels:
				MonsterFactoryInputs.append((s,m,b,l))

BDT={}
BDT["DummyFoeHP"]=0
BDT["DummyFoeENE"]=0
BDT["DummyFoeSTR"]=0
BDT["DummyFoeSPR"]=0
BDT["DummyFoeSKL"]=0
BDT["DummyFoeABL"]=0
BDT["DummyFoeAGI"]=0
BDT["DummyFoeEVA"]=0
BDT["DummyFoeTGH"]=0
BDT["DummyFoeRES"]=0
BDT["DummyFoeLCK"]=0
BDT["DummyFoeWT"]=0

BDT["ArachnidHP"]=75
BDT["ArachnidENE"]=75
BDT["ArachnidSTR"]=15
BDT["ArachnidSPR"]=0
BDT["ArachnidSKL"]=15
BDT["ArachnidABL"]=10
BDT["ArachnidAGI"]=15
BDT["ArachnidEVA"]=25
BDT["ArachnidTGH"]=7
BDT["ArachnidRES"]=7
BDT["ArachnidLCK"]=10
BDT["ArachnidWT"]=12

BDT["GargoyleHP"]=100
BDT["GargoyleENE"]=100
BDT["GargoyleSTR"]=15
BDT["GargoyleSPR"]=10
BDT["GargoyleSKL"]=5
BDT["GargoyleABL"]=15
BDT["GargoyleAGI"]=15
BDT["GargoyleEVA"]=15
BDT["GargoyleTGH"]=7
BDT["GargoyleRES"]=10
BDT["GargoyleLCK"]=5
BDT["GargoyleWT"]=10

BDT["JelHP"]=50
BDT["JelENE"]=50
BDT["JelSTR"]=5
BDT["JelSPR"]=15
BDT["JelSKL"]=0
BDT["JelABL"]=10
BDT["JelAGI"]=5
BDT["JelEVA"]=15
BDT["JelTGH"]=6
BDT["JelRES"]=12
BDT["JelLCK"]=10
BDT["JelWT"]=7

BDT["HawkHP"]=50
BDT["HawkENE"]=50
BDT["HawkSTR"]=10
BDT["HawkSPR"]=5
BDT["HawkSKL"]=10
BDT["HawkABL"]=10
BDT["HawkAGI"]=15
BDT["HawkEVA"]=15
BDT["HawkTGH"]=5
BDT["HawkRES"]=5
BDT["HawkLCK"]=10
BDT["HawkWT"]=5

BDT["CentaurHP"]=125
BDT["CentaurENE"]=125
BDT["CentaurSTR"]=10
BDT["CentaurSPR"]=5
BDT["CentaurSKL"]=5
BDT["CentaurABL"]=10
BDT["CentaurAGI"]=22
BDT["CentaurEVA"]=12
BDT["CentaurTGH"]=10
BDT["CentaurRES"]=10
BDT["CentaurLCK"]=10
BDT["CentaurWT"]=50

BDT["WolfHP"]=75
BDT["WolfENE"]=75
BDT["WolfSTR"]=15
BDT["WolfSPR"]=5
BDT["WolfSKL"]=15
BDT["WolfABL"]=10
BDT["WolfAGI"]=20
BDT["WolfEVA"]=12
BDT["WolfTGH"]=14
BDT["WolfRES"]=7
BDT["WolfLCK"]=10
BDT["WolfWT"]=30

BDT["BigCatHP"]=75
BDT["BigCatENE"]=75
BDT["BigCatSTR"]=15
BDT["BigCatSPR"]=15
BDT["BigCatSKL"]=5
BDT["BigCatABL"]=10
BDT["BigCatAGI"]=20
BDT["BigCatEVA"]=12
BDT["BigCatTGH"]=7
BDT["BigCatRES"]=14
BDT["BigCatLCK"]=10
BDT["BigCatWT"]=30

BDT["SkeletonHP"]=100
BDT["SkeletonENE"]=100
BDT["SkeletonSTR"]=3
BDT["SkeletonSPR"]=15
BDT["SkeletonSKL"]=15
BDT["SkeletonABL"]=6
BDT["SkeletonAGI"]=15
BDT["SkeletonEVA"]=0
BDT["SkeletonTGH"]=3
BDT["SkeletonRES"]=3
BDT["SkeletonLCK"]=10
BDT["SkeletonWT"]=3

BDT["OgreHP"]=150
BDT["OgreENE"]=150
BDT["OgreSTR"]=25
BDT["OgreSPR"]=0
BDT["OgreSKL"]=0
BDT["OgreABL"]=0
BDT["OgreAGI"]=5
BDT["OgreEVA"]=0
BDT["OgreTGH"]=20
BDT["OgreRES"]=5
BDT["OgreLCK"]=10
BDT["OgreWT"]=100

BDT["OriginHP"]=0
BDT["OriginENE"]=0
BDT["OriginSTR"]=10
BDT["OriginSPR"]=10
BDT["OriginSKL"]=10
BDT["OriginABL"]=15
BDT["OriginAGI"]=11
BDT["OriginEVA"]=10
BDT["OriginTGH"]=10
BDT["OriginRES"]=10
BDT["OriginLCK"]=10
BDT["OriginWT"]=40

BDT["WilderHP"]=0
BDT["WilderENE"]=0
BDT["WilderSTR"]=15
BDT["WilderSPR"]=10
BDT["WilderSKL"]=5
BDT["WilderABL"]=10
BDT["WilderAGI"]=7
BDT["WilderEVA"]=5
BDT["WilderTGH"]=15
BDT["WilderRES"]=10
BDT["WilderLCK"]=10
BDT["WilderWT"]=60

BDT["SoulsongHP"]=0
BDT["SoulsongENE"]=0
BDT["SoulsongSTR"]=5
BDT["SoulsongSPR"]=15
BDT["SoulsongSKL"]=10
BDT["SoulsongABL"]=12
BDT["SoulsongAGI"]=10
BDT["SoulsongEVA"]=15
BDT["SoulsongTGH"]=5
BDT["SoulsongRES"]=15
BDT["SoulsongLCK"]=10
BDT["SoulsongWT"]=25

BDT["SoulbladeHP"]=0
BDT["SoulbladeENE"]=0
BDT["SoulbladeSTR"]=15
BDT["SoulbladeSPR"]=10
BDT["SoulbladeSKL"]=13
BDT["SoulbladeABL"]=10
BDT["SoulbladeAGI"]=15
BDT["SoulbladeEVA"]=25
BDT["SoulbladeTGH"]=5
BDT["SoulbladeRES"]=5
BDT["SoulbladeLCK"]=10
BDT["SoulbladeWT"]=15

BDT["MechanixHP"]=0
BDT["MechanixENE"]=0
BDT["MechanixSTR"]=13
BDT["MechanixSPR"]=5
BDT["MechanixSKL"]=15
BDT["MechanixABL"]=10
BDT["MechanixAGI"]=3
BDT["MechanixEVA"]=5
BDT["MechanixTGH"]=13
BDT["MechanixRES"]=5
BDT["MechanixLCK"]=10
BDT["MechanixWT"]=60

BDT["VampireHP"]=0
BDT["VampireENE"]=0
BDT["VampireSTR"]=15
BDT["VampireSPR"]=15
BDT["VampireSKL"]=5
BDT["VampireABL"]=10
BDT["VampireAGI"]=13
BDT["VampireEVA"]=10
BDT["VampireTGH"]=5
BDT["VampireRES"]=15
BDT["VampireLCK"]=10
BDT["VampireWT"]=35

BDT["ElementalHP"]=0
BDT["ElementalENE"]=0
BDT["ElementalSTR"]=1
BDT["ElementalSPR"]=20
BDT["ElementalSKL"]=1
BDT["ElementalABL"]=5
BDT["ElementalAGI"]=10
BDT["ElementalEVA"]=10
BDT["ElementalTGH"]=1
BDT["ElementalRES"]=20
BDT["ElementalLCK"]=10
BDT["ElementalWT"]=0

MOD={}
MOD["DummyModHP"]=0
MOD["DummyModENE"]=0
MOD["DummyModSTR"]=0
MOD["DummyModSPR"]=0
MOD["DummyModSKL"]=0
MOD["DummyModABL"]=0
MOD["DummyModAGI"]=0
MOD["DummyModEVA"]=0
MOD["DummyModTGH"]=0
MOD["DummyModRES"]=0
MOD["DummyModLCK"]=0
MOD["DummyModWT"]=0

MOD["HealthyHP"]=1.25
MOD["HealthyENE"]=1
MOD["HealthySTR"]=1
MOD["HealthySPR"]=1
MOD["HealthySKL"]=1
MOD["HealthyABL"]=1
MOD["HealthyAGI"]=1
MOD["HealthyEVA"]=1
MOD["HealthyTGH"]=1
MOD["HealthyRES"]=1
MOD["HealthyLCK"]=1
MOD["HealthyWT"]=1

MOD["EnergeticHP"]=1
MOD["EnergeticENE"]=1.25
MOD["EnergeticSTR"]=1
MOD["EnergeticSPR"]=1
MOD["EnergeticSKL"]=1
MOD["EnergeticABL"]=1
MOD["EnergeticAGI"]=1
MOD["EnergeticEVA"]=1
MOD["EnergeticTGH"]=1
MOD["EnergeticRES"]=1
MOD["EnergeticLCK"]=1
MOD["EnergeticWT"]=1

MOD["VeteranHP"]=1
MOD["VeteranENE"]=1
MOD["VeteranSTR"]=1.15
MOD["VeteranSPR"]=1.15
MOD["VeteranSKL"]=1.15
MOD["VeteranABL"]=1.15
MOD["VeteranAGI"]=1.15
MOD["VeteranEVA"]=1.15
MOD["VeteranTGH"]=1.15
MOD["VeteranRES"]=1.15
MOD["VeteranLCK"]=1.15
MOD["VeteranWT"]=1

MOD["NormalHP"]=1
MOD["NormalENE"]=1
MOD["NormalSTR"]=1
MOD["NormalSPR"]=1
MOD["NormalSKL"]=1
MOD["NormalABL"]=1
MOD["NormalAGI"]=1
MOD["NormalEVA"]=1
MOD["NormalTGH"]=1
MOD["NormalRES"]=1
MOD["NormalLCK"]=1
MOD["NormalWT"]=1

MOD["StrongHP"]=1
MOD["StrongENE"]=1
MOD["StrongSTR"]=1.25
MOD["StrongSPR"]=1
MOD["StrongSKL"]=1
MOD["StrongABL"]=1
MOD["StrongAGI"]=1
MOD["StrongEVA"]=1
MOD["StrongTGH"]=1
MOD["StrongRES"]=1
MOD["StrongLCK"]=1
MOD["StrongWT"]=1

MOD["SpiritedHP"]=1
MOD["SpiritedENE"]=1
MOD["SpiritedSTR"]=1
MOD["SpiritedSPR"]=1.25
MOD["SpiritedSKL"]=1
MOD["SpiritedABL"]=1
MOD["SpiritedAGI"]=1
MOD["SpiritedEVA"]=1
MOD["SpiritedTGH"]=1
MOD["SpiritedRES"]=1
MOD["SpiritedLCK"]=1
MOD["SpiritedWT"]=1

MOD["SkillfulHP"]=1
MOD["SkillfulENE"]=1
MOD["SkillfulSTR"]=1
MOD["SkillfulSPR"]=1
MOD["SkillfulSKL"]=1.25
MOD["SkillfulABL"]=1
MOD["SkillfulAGI"]=1
MOD["SkillfulEVA"]=1
MOD["SkillfulTGH"]=1
MOD["SkillfulRES"]=1
MOD["SkillfulLCK"]=1
MOD["SkillfulWT"]=1

MOD["CapableHP"]=1
MOD["CapableENE"]=1
MOD["CapableSTR"]=1
MOD["CapableSPR"]=1
MOD["CapableSKL"]=1
MOD["CapableABL"]=1.25
MOD["CapableAGI"]=1
MOD["CapableEVA"]=1
MOD["CapableTGH"]=1
MOD["CapableRES"]=1
MOD["CapableLCK"]=1
MOD["CapableWT"]=1

MOD["AgileHP"]=1
MOD["AgileENE"]=1
MOD["AgileSTR"]=1
MOD["AgileSPR"]=1
MOD["AgileSKL"]=1
MOD["AgileABL"]=1
MOD["AgileAGI"]=1.25
MOD["AgileEVA"]=1
MOD["AgileTGH"]=1
MOD["AgileRES"]=1
MOD["AgileLCK"]=1
MOD["AgileWT"]=1

MOD["EvasiveHP"]=1
MOD["EvasiveENE"]=1
MOD["EvasiveSTR"]=1
MOD["EvasiveSPR"]=1
MOD["EvasiveSKL"]=1
MOD["EvasiveABL"]=1
MOD["EvasiveAGI"]=1
MOD["EvasiveEVA"]=1.25
MOD["EvasiveTGH"]=1
MOD["EvasiveRES"]=1
MOD["EvasiveLCK"]=1
MOD["EvasiveWT"]=1

MOD["ToughHP"]=1
MOD["ToughENE"]=1
MOD["ToughSTR"]=1
MOD["ToughSPR"]=1
MOD["ToughSKL"]=1
MOD["ToughABL"]=1
MOD["ToughAGI"]=1
MOD["ToughEVA"]=1
MOD["ToughTGH"]=1.25
MOD["ToughRES"]=1
MOD["ToughLCK"]=1
MOD["ToughWT"]=1

MOD["ResistantHP"]=1
MOD["ResistantENE"]=1
MOD["ResistantSTR"]=1
MOD["ResistantSPR"]=1
MOD["ResistantSKL"]=1
MOD["ResistantABL"]=1
MOD["ResistantAGI"]=1
MOD["ResistantEVA"]=1
MOD["ResistantTGH"]=1
MOD["ResistantRES"]=1.25
MOD["ResistantLCK"]=1
MOD["ResistantWT"]=1

MOD["LuckyHP"]=1
MOD["LuckyENE"]=1
MOD["LuckySTR"]=1
MOD["LuckySPR"]=1
MOD["LuckySKL"]=1
MOD["LuckyABL"]=1
MOD["LuckyAGI"]=1
MOD["LuckyEVA"]=1
MOD["LuckyTGH"]=1
MOD["LuckyRES"]=1
MOD["LuckyLCK"]=1.25
MOD["LuckyWT"]=1

MOD["HeavyweightHP"]=1
MOD["HeavyweightENE"]=1
MOD["HeavyweightSTR"]=1
MOD["HeavyweightSPR"]=1
MOD["HeavyweightSKL"]=1
MOD["HeavyweightABL"]=1
MOD["HeavyweightAGI"]=1
MOD["HeavyweightEVA"]=1
MOD["HeavyweightTGH"]=1
MOD["HeavyweightRES"]=1
MOD["HeavyweightLCK"]=1
MOD["HeavyweightWT"]=1.25

MOD["LightweightHP"]=1
MOD["LightweightENE"]=1
MOD["LightweightSTR"]=1
MOD["LightweightSPR"]=1
MOD["LightweightSKL"]=1
MOD["LightweightABL"]=1
MOD["LightweightAGI"]=1
MOD["LightweightEVA"]=1
MOD["LightweightTGH"]=1
MOD["LightweightRES"]=1
MOD["LightweightLCK"]=1
MOD["LightweightWT"]=0.75

MOD["FeatherweightHP"]=1
MOD["FeatherweightENE"]=1
MOD["FeatherweightSTR"]=1
MOD["FeatherweightSPR"]=1
MOD["FeatherweightSKL"]=1
MOD["FeatherweightABL"]=1
MOD["FeatherweightAGI"]=1
MOD["FeatherweightEVA"]=1
MOD["FeatherweightTGH"]=1
MOD["FeatherweightRES"]=1
MOD["FeatherweightLCK"]=1
MOD["FeatherweightWT"]=0.1

MOD["BrutishHP"]=1
MOD["BrutishENE"]=1
MOD["BrutishSTR"]=1.5
MOD["BrutishSPR"]=1
MOD["BrutishSKL"]=0.5
MOD["BrutishABL"]=0.5
MOD["BrutishAGI"]=1
MOD["BrutishEVA"]=1
MOD["BrutishTGH"]=1.5
MOD["BrutishRES"]=1
MOD["BrutishLCK"]=1
MOD["BrutishWT"]=1

MOD["WizenedHP"]=1
MOD["WizenedENE"]=1
MOD["WizenedSTR"]=0.5
MOD["WizenedSPR"]=1.5
MOD["WizenedSKL"]=1
MOD["WizenedABL"]=1
MOD["WizenedAGI"]=1
MOD["WizenedEVA"]=1
MOD["WizenedTGH"]=0.5
MOD["WizenedRES"]=1.5
MOD["WizenedLCK"]=1
MOD["WizenedWT"]=1

MOD["SavvyHP"]=1
MOD["SavvyENE"]=1
MOD["SavvySTR"]=0.5
MOD["SavvySPR"]=0.5
MOD["SavvySKL"]=1.5
MOD["SavvyABL"]=1.5
MOD["SavvyAGI"]=1
MOD["SavvyEVA"]=1
MOD["SavvyTGH"]=1
MOD["SavvyRES"]=1
MOD["SavvyLCK"]=1
MOD["SavvyWT"]=1

MOD["UntouchableHP"]=1
MOD["UntouchableENE"]=1
MOD["UntouchableSTR"]=0.5
MOD["UntouchableSPR"]=0.5
MOD["UntouchableSKL"]=0.5
MOD["UntouchableABL"]=0.5
MOD["UntouchableAGI"]=0.5
MOD["UntouchableEVA"]=2
MOD["UntouchableTGH"]=0.5
MOD["UntouchableRES"]=0.5
MOD["UntouchableLCK"]=1
MOD["UntouchableWT"]=1

MOD["GlassCannonHP"]=1
MOD["GlassCannonENE"]=1
MOD["GlassCannonSTR"]=2
MOD["GlassCannonSPR"]=2
MOD["GlassCannonSKL"]=2
MOD["GlassCannonABL"]=2
MOD["GlassCannonAGI"]=0.5
MOD["GlassCannonEVA"]=1
MOD["GlassCannonTGH"]=0.5
MOD["GlassCannonRES"]=0.5
MOD["GlassCannonLCK"]=1
MOD["GlassCannonWT"]=1

SZM={}
SZM["DummySizeHP"]=0
SZM["DummySizeENE"]=0
SZM["DummySizeSTR"]=0
SZM["DummySizeSPR"]=0
SZM["DummySizeSKL"]=0
SZM["DummySizeABL"]=0
SZM["DummySizeAGI"]=0
SZM["DummySizeEVA"]=0
SZM["DummySizeTGH"]=0
SZM["DummySizeRES"]=0
SZM["DummySizeLCK"]=0
SZM["DummySizeWT"]=0

SZM["TinyHP"]=1
SZM["TinyENE"]=1
SZM["TinySTR"]=0.25
SZM["TinySPR"]=1
SZM["TinySKL"]=1.5
SZM["TinyABL"]=0.75
SZM["TinyAGI"]=1.5
SZM["TinyEVA"]=1.5
SZM["TinyTGH"]=0.5
SZM["TinyRES"]=1
SZM["TinyLCK"]=1
SZM["TinyWT"]=0.5

SZM["SmallHP"]=1
SZM["SmallENE"]=1
SZM["SmallSTR"]=0.5
SZM["SmallSPR"]=1
SZM["SmallSKL"]=1.25
SZM["SmallABL"]=1
SZM["SmallAGI"]=1.25
SZM["SmallEVA"]=1.25
SZM["SmallTGH"]=0.75
SZM["SmallRES"]=1
SZM["SmallLCK"]=1
SZM["SmallWT"]=0.75

SZM["MediumHP"]=1
SZM["MediumENE"]=1
SZM["MediumSTR"]=1
SZM["MediumSPR"]=1
SZM["MediumSKL"]=1
SZM["MediumABL"]=1
SZM["MediumAGI"]=1
SZM["MediumEVA"]=1
SZM["MediumTGH"]=1
SZM["MediumRES"]=1
SZM["MediumLCK"]=1
SZM["MediumWT"]=1

SZM["LargeHP"]=1
SZM["LargeENE"]=1
SZM["LargeSTR"]=1.25
SZM["LargeSPR"]=1
SZM["LargeSKL"]=0.75
SZM["LargeABL"]=1
SZM["LargeAGI"]=0.75
SZM["LargeEVA"]=0.75
SZM["LargeTGH"]=1.25
SZM["LargeRES"]=1
SZM["LargeLCK"]=1
SZM["LargeWT"]=1.5

SZM["HugeHP"]=1
SZM["HugeENE"]=1
SZM["HugeSTR"]=1.5
SZM["HugeSPR"]=1
SZM["HugeSKL"]=0.75
SZM["HugeABL"]=1
SZM["HugeAGI"]=0.5
SZM["HugeEVA"]=0.5
SZM["HugeTGH"]=1.4
SZM["HugeRES"]=1
SZM["HugeLCK"]=1
SZM["HugeWT"]=2

LVL={}
LVL["1HP"]=1
LVL["1ENE"]=1
LVL["1STR"]=1
LVL["1SPR"]=1
LVL["1SKL"]=1
LVL["1ABL"]=1
LVL["1AGI"]=1
LVL["1EVA"]=1
LVL["1TGH"]=1
LVL["1RES"]=1
LVL["1LCK"]=1
LVL["1WT"]=1

LVL["2HP"]=1.15
LVL["2ENE"]=1.15
LVL["2STR"]=1.15
LVL["2SPR"]=1.15
LVL["2SKL"]=1.15
LVL["2ABL"]=1.15
LVL["2AGI"]=1.15
LVL["2EVA"]=1.15
LVL["2TGH"]=1.15
LVL["2RES"]=1.15
LVL["2LCK"]=1.15
LVL["2WT"]=1

LVL["3HP"]=1.3
LVL["3ENE"]=1.3
LVL["3STR"]=1.3
LVL["3SPR"]=1.3
LVL["3SKL"]=1.3
LVL["3ABL"]=1.3
LVL["3AGI"]=1.3
LVL["3EVA"]=1.3
LVL["3TGH"]=1.3
LVL["3RES"]=1.3
LVL["3LCK"]=1.3
LVL["3WT"]=1

LVL["4HP"]=1.45
LVL["4ENE"]=1.45
LVL["4STR"]=1.45
LVL["4SPR"]=1.45
LVL["4SKL"]=1.45
LVL["4ABL"]=1.45
LVL["4AGI"]=1.45
LVL["4EVA"]=1.45
LVL["4TGH"]=1.45
LVL["4RES"]=1.45
LVL["4LCK"]=1.45
LVL["4WT"]=1

LVL["5HP"]=1.6
LVL["5ENE"]=1.6
LVL["5STR"]=1.6
LVL["5SPR"]=1.6
LVL["5SKL"]=1.6
LVL["5ABL"]=1.6
LVL["5AGI"]=1.6
LVL["5EVA"]=1.6
LVL["5TGH"]=1.6
LVL["5RES"]=1.6
LVL["5LCK"]=1.6
LVL["5WT"]=1

LVL["6HP"]=1.75
LVL["6ENE"]=1.75
LVL["6STR"]=1.75
LVL["6SPR"]=1.75
LVL["6SKL"]=1.75
LVL["6ABL"]=1.75
LVL["6AGI"]=1.75
LVL["6EVA"]=1.75
LVL["6TGH"]=1.75
LVL["6RES"]=1.75
LVL["6LCK"]=1.75
LVL["6WT"]=1

LVL["7HP"]=1.9
LVL["7ENE"]=1.9
LVL["7STR"]=1.9
LVL["7SPR"]=1.9
LVL["7SKL"]=1.9
LVL["7ABL"]=1.9
LVL["7AGI"]=1.9
LVL["7EVA"]=1.9
LVL["7TGH"]=1.9
LVL["7RES"]=1.9
LVL["7LCK"]=1.9
LVL["7WT"]=1

LVL["8HP"]=2.05
LVL["8ENE"]=2.05
LVL["8STR"]=2.05
LVL["8SPR"]=2.05
LVL["8SKL"]=2.05
LVL["8ABL"]=2.05
LVL["8AGI"]=2.05
LVL["8EVA"]=2.05
LVL["8TGH"]=2.05
LVL["8RES"]=2.05
LVL["8LCK"]=2.05
LVL["8WT"]=1

LVL["9HP"]=2.2
LVL["9ENE"]=2.2
LVL["9STR"]=2.2
LVL["9SPR"]=2.2
LVL["9SKL"]=2.2
LVL["9ABL"]=2.2
LVL["9AGI"]=2.2
LVL["9EVA"]=2.2
LVL["9TGH"]=2.2
LVL["9RES"]=2.2
LVL["9LCK"]=2.2
LVL["9WT"]=1

LVL["10HP"]=2.35
LVL["10ENE"]=2.35
LVL["10STR"]=2.35
LVL["10SPR"]=2.35
LVL["10SKL"]=2.35
LVL["10ABL"]=2.35
LVL["10AGI"]=2.35
LVL["10EVA"]=2.35
LVL["10TGH"]=2.35
LVL["10RES"]=2.35
LVL["10LCK"]=2.35
LVL["10WT"]=1

LVL["11HP"]=2.5
LVL["11ENE"]=2.5
LVL["11STR"]=2.5
LVL["11SPR"]=2.5
LVL["11SKL"]=2.5
LVL["11ABL"]=2.5
LVL["11AGI"]=2.5
LVL["11EVA"]=2.5
LVL["11TGH"]=2.5
LVL["11RES"]=2.5
LVL["11LCK"]=2.5
LVL["11WT"]=1

LVL["12HP"]=2.65
LVL["12ENE"]=2.65
LVL["12STR"]=2.65
LVL["12SPR"]=2.65
LVL["12SKL"]=2.65
LVL["12ABL"]=2.65
LVL["12AGI"]=2.65
LVL["12EVA"]=2.65
LVL["12TGH"]=2.65
LVL["12RES"]=2.65
LVL["12LCK"]=2.65
LVL["12WT"]=1

LVL["13HP"]=2.8
LVL["13ENE"]=2.8
LVL["13STR"]=2.8
LVL["13SPR"]=2.8
LVL["13SKL"]=2.8
LVL["13ABL"]=2.8
LVL["13AGI"]=2.8
LVL["13EVA"]=2.8
LVL["13TGH"]=2.8
LVL["13RES"]=2.8
LVL["13LCK"]=2.8
LVL["13WT"]=1

LVL["14HP"]=2.95
LVL["14ENE"]=2.95
LVL["14STR"]=2.95
LVL["14SPR"]=2.95
LVL["14SKL"]=2.95
LVL["14ABL"]=2.95
LVL["14AGI"]=2.95
LVL["14EVA"]=2.95
LVL["14TGH"]=2.95
LVL["14RES"]=2.95
LVL["14LCK"]=2.95
LVL["14WT"]=1

LVL["15HP"]=3.1
LVL["15ENE"]=3.1
LVL["15STR"]=3.1
LVL["15SPR"]=3.1
LVL["15SKL"]=3.1
LVL["15ABL"]=3.1
LVL["15AGI"]=3.1
LVL["15EVA"]=3.1
LVL["15TGH"]=3.1
LVL["15RES"]=3.1
LVL["15LCK"]=3.1
LVL["15WT"]=1

LVL["16HP"]=3.25
LVL["16ENE"]=3.25
LVL["16STR"]=3.25
LVL["16SPR"]=3.25
LVL["16SKL"]=3.25
LVL["16ABL"]=3.25
LVL["16AGI"]=3.25
LVL["16EVA"]=3.25
LVL["16TGH"]=3.25
LVL["16RES"]=3.25
LVL["16LCK"]=3.25
LVL["16WT"]=1

LVL["17HP"]=3.4
LVL["17ENE"]=3.4
LVL["17STR"]=3.4
LVL["17SPR"]=3.4
LVL["17SKL"]=3.4
LVL["17ABL"]=3.4
LVL["17AGI"]=3.4
LVL["17EVA"]=3.4
LVL["17TGH"]=3.4
LVL["17RES"]=3.4
LVL["17LCK"]=3.4
LVL["17WT"]=1

LVL["18HP"]=3.55
LVL["18ENE"]=3.55
LVL["18STR"]=3.55
LVL["18SPR"]=3.55
LVL["18SKL"]=3.55
LVL["18ABL"]=3.55
LVL["18AGI"]=3.55
LVL["18EVA"]=3.55
LVL["18TGH"]=3.55
LVL["18RES"]=3.55
LVL["18LCK"]=3.55
LVL["18WT"]=1

LVL["19HP"]=3.7
LVL["19ENE"]=3.7
LVL["19STR"]=3.7
LVL["19SPR"]=3.7
LVL["19SKL"]=3.7
LVL["19ABL"]=3.7
LVL["19AGI"]=3.7
LVL["19EVA"]=3.7
LVL["19TGH"]=3.7
LVL["19RES"]=3.7
LVL["19LCK"]=3.7
LVL["19WT"]=1

LVL["20HP"]=4
LVL["20ENE"]=4
LVL["20STR"]=4
LVL["20SPR"]=4
LVL["20SKL"]=4
LVL["20ABL"]=4
LVL["20AGI"]=4
LVL["20EVA"]=4
LVL["20TGH"]=4
LVL["20RES"]=4
LVL["20LCK"]=4
LVL["20WT"]=1

def MonsterFactory(SizeMod,Modifier,BodyType,Level):
	"""The MonsterFactory function outputs a Monster from a base type's stats, modified by a Modifier and further changed by its Size, then upgraded by its Level."""
	
	#First snag the base type...
	BaseHP=BDT[BodyType+"HP"]
	BaseENE=BDT[BodyType+"ENE"]
	BaseSTR=BDT[BodyType+"STR"]
	BaseSPR=BDT[BodyType+"SPR"]
	BaseSKL=BDT[BodyType+"SKL"]
	BaseABL=BDT[BodyType+"ABL"]
	BaseAGI=BDT[BodyType+"AGI"]
	BaseEVA=BDT[BodyType+"EVA"]
	BaseTGH=BDT[BodyType+"TGH"]
	BaseRES=BDT[BodyType+"RES"]
	BaseLCK=BDT[BodyType+"LCK"]
	BaseWT=BDT[BodyType+"WT"]
	
	#Then you add the first Modifier...
	ModHP=MOD[Modifier+"HP"]
	ModENE=MOD[Modifier+"ENE"]
	ModSTR=MOD[Modifier+"STR"]
	ModSPR=MOD[Modifier+"SPR"]
	ModSKL=MOD[Modifier+"SKL"]
	ModABL=MOD[Modifier+"ABL"]
	ModAGI=MOD[Modifier+"AGI"]
	ModEVA=MOD[Modifier+"EVA"]
	ModTGH=MOD[Modifier+"TGH"]
	ModRES=MOD[Modifier+"RES"]
	ModLCK=MOD[Modifier+"LCK"]
	ModWT=MOD[Modifier+"WT"]
	
	#After which, you snag the Size modifier...
	SizeHP=SZM[SizeMod+"HP"]
	SizeENE=SZM[SizeMod+"ENE"]
	SizeSTR=SZM[SizeMod+"STR"]
	SizeSPR=SZM[SizeMod+"SPR"]
	SizeSKL=SZM[SizeMod+"SKL"]
	SizeABL=SZM[SizeMod+"ABL"]
	SizeAGI=SZM[SizeMod+"AGI"]
	SizeEVA=SZM[SizeMod+"EVA"]
	SizeTGH=SZM[SizeMod+"TGH"]
	SizeRES=SZM[SizeMod+"RES"]
	SizeLCK=SZM[SizeMod+"LCK"]
	SizeWT=SZM[SizeMod+"WT"]
	
	#And lastly you grab their Level...
	LevelHP=LVL[Level+"HP"]
	LevelENE=LVL[Level+"ENE"]
	LevelSTR=LVL[Level+"STR"]
	LevelSPR=LVL[Level+"SPR"]
	LevelSKL=LVL[Level+"SKL"]
	LevelABL=LVL[Level+"ABL"]
	LevelAGI=LVL[Level+"AGI"]
	LevelEVA=LVL[Level+"EVA"]
	LevelTGH=LVL[Level+"TGH"]
	LevelRES=LVL[Level+"RES"]
	LevelLCK=LVL[Level+"LCK"]
	LevelWT=LVL[Level+"WT"]
	
	#Then ya gotta put it all together, mix it in a bowl, and spread evenly over a layer of brownies.
	MonsterHP=round((((BaseHP*ModHP)*SizeHP)*LevelHP))
	MonsterENE=round((((BaseENE*ModENE)*SizeENE)*LevelENE))
	MonsterSTR=round((((BaseSTR*ModSTR)*SizeSTR)*LevelSTR))
	MonsterSPR=round((((BaseSPR*ModSPR)*SizeSPR)*LevelSPR))
	MonsterSKL=round((((BaseSKL*ModSKL)*SizeSKL)*LevelSKL))
	MonsterABL=round((((BaseABL*ModABL)*SizeABL)*LevelABL))
	MonsterAGI=round((((BaseAGI*ModAGI)*SizeAGI)*LevelAGI))
	MonsterEVA=round((((BaseEVA*ModEVA)*SizeEVA)*LevelEVA))
	MonsterTGH=round((((BaseTGH*ModTGH)*SizeTGH)*LevelTGH))
	MonsterRES=round((((BaseRES*ModRES)*SizeRES)*LevelRES))
	MonsterLCK=round((((BaseLCK*ModLCK)*SizeLCK)*LevelLCK))
	MonsterWT=round((((BaseWT*ModWT)*SizeWT)*LevelWT))
	
	return(MonsterSTR,MonsterSPR,MonsterSKL,MonsterABL,MonsterAGI,MonsterEVA,MonsterTGH,MonsterRES,MonsterLCK,MonsterWT,MonsterHP,MonsterENE)
	
OmniMonsterData={}

for Inputs in MonsterFactoryInputs:
	OmniMonsterData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]] = MonsterFactory(Inputs[0],Inputs[1],Inputs[2],Inputs[3])