Races=("Dummy","Origin","Wilder","Soulsong","Soulblade","Mechanix","Vampire")
Mods=("DU","OR","WI","SS","SB","MX","VM")
Classys=("DummyClass","Vagabond","Thief","Bard","Knight","Gunner","Archer","Monk","Medic","Mage","Elemental","Summoner")
Levels=("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20")

DressingRoomInputs=[]
for r in Races:
	for m in Mods:
		for c in Classys:
			for l in Levels:
				DressingRoomInputs.append((r,m,c,l))

RAC={}
RAC["OriginHP"]=100
RAC["OriginENE"]=100
RAC["OriginSTR"]=10
RAC["OriginSPR"]=10
RAC["OriginSKL"]=10
RAC["OriginABL"]=10
RAC["OriginAGI"]=10
RAC["OriginEVA"]=10
RAC["OriginTGH"]=10
RAC["OriginRES"]=10
RAC["OriginLCK"]=10
RAC["OriginWT"]=0

RAC["DummyHP"]=0
RAC["DummyENE"]=0
RAC["DummySTR"]=0
RAC["DummySPR"]=0
RAC["DummySKL"]=0
RAC["DummyABL"]=0
RAC["DummyAGI"]=0
RAC["DummyEVA"]=0
RAC["DummyTGH"]=0
RAC["DummyRES"]=0
RAC["DummyLCK"]=0
RAC["DummyWT"]=0

RAC["WilderHP"]=100
RAC["WilderENE"]=100
RAC["WilderSTR"]=10
RAC["WilderSPR"]=10
RAC["WilderSKL"]=10
RAC["WilderABL"]=10
RAC["WilderAGI"]=10
RAC["WilderEVA"]=10
RAC["WilderTGH"]=10
RAC["WilderRES"]=10
RAC["WilderLCK"]=10
RAC["WilderWT"]=0

RAC["SoulsongHP"]=100
RAC["SoulsongENE"]=100
RAC["SoulsongSTR"]=10
RAC["SoulsongSPR"]=10
RAC["SoulsongSKL"]=10
RAC["SoulsongABL"]=10
RAC["SoulsongAGI"]=10
RAC["SoulsongEVA"]=10
RAC["SoulsongTGH"]=10
RAC["SoulsongRES"]=10
RAC["SoulsongLCK"]=10
RAC["SoulsongWT"]=0

RAC["SoulbladeHP"]=100
RAC["SoulbladeENE"]=100
RAC["SoulbladeSTR"]=10
RAC["SoulbladeSPR"]=10
RAC["SoulbladeSKL"]=10
RAC["SoulbladeABL"]=10
RAC["SoulbladeAGI"]=10
RAC["SoulbladeEVA"]=10
RAC["SoulbladeTGH"]=10
RAC["SoulbladeRES"]=10
RAC["SoulbladeLCK"]=10
RAC["SoulbladeWT"]=0

RAC["MechanixHP"]=100
RAC["MechanixENE"]=100
RAC["MechanixSTR"]=10
RAC["MechanixSPR"]=10
RAC["MechanixSKL"]=10
RAC["MechanixABL"]=10
RAC["MechanixAGI"]=10
RAC["MechanixEVA"]=10
RAC["MechanixTGH"]=10
RAC["MechanixRES"]=10
RAC["MechanixLCK"]=10
RAC["MechanixWT"]=0

RAC["VampireHP"]=100
RAC["VampireENE"]=100
RAC["VampireSTR"]=10
RAC["VampireSPR"]=10
RAC["VampireSKL"]=10
RAC["VampireABL"]=10
RAC["VampireAGI"]=10
RAC["VampireEVA"]=10
RAC["VampireTGH"]=10
RAC["VampireRES"]=10
RAC["VampireLCK"]=10
RAC["VampireWT"]=0

RCM={}
RCM["ORHP"]=1
RCM["ORENE"]=1
RCM["ORSTR"]=1
RCM["ORSPR"]=1
RCM["ORSKL"]=1
RCM["ORABL"]=1.5
RCM["ORAGI"]=1.2
RCM["OREVA"]=1
RCM["ORTGH"]=1
RCM["ORRES"]=1
RCM["ORLCK"]=1
RCM["ORWT"]=1

RCM["DUHP"]=0
RCM["DUENE"]=0
RCM["DUSTR"]=0
RCM["DUSPR"]=0
RCM["DUSKL"]=0
RCM["DUABL"]=0
RCM["DUAGI"]=0
RCM["DUEVA"]=0
RCM["DUTGH"]=0
RCM["DURES"]=0
RCM["DULCK"]=0
RCM["DUWT"]=0

RCM["WIHP"]=1.5
RCM["WIENE"]=1
RCM["WISTR"]=1.5
RCM["WISPR"]=1
RCM["WISKL"]=0.5
RCM["WIABL"]=1
RCM["WIAGI"]=0.7
RCM["WIEVA"]=0.5
RCM["WITGH"]=1.5
RCM["WIRES"]=1
RCM["WILCK"]=1
RCM["WIWT"]=1

RCM["SSHP"]=1
RCM["SSENE"]=1.2
RCM["SSSTR"]=0.5
RCM["SSSPR"]=1.5
RCM["SSSKL"]=1
RCM["SSABL"]=1.2
RCM["SSAGI"]=1
RCM["SSEVA"]=1.2
RCM["SSTGH"]=0.5
RCM["SSRES"]=1.5
RCM["SSLCK"]=1
RCM["SSWT"]=1

RCM["SBHP"]=0.75
RCM["SBENE"]=1.1
RCM["SBSTR"]=1.5
RCM["SBSPR"]=0.7
RCM["SBSKL"]=1.3
RCM["SBABL"]=1
RCM["SBAGI"]=1.5
RCM["SBEVA"]=2.5
RCM["SBTGH"]=0.5
RCM["SBRES"]=0.5
RCM["SBLCK"]=1
RCM["SBWT"]=1

RCM["MXHP"]=1.2
RCM["MXENE"]=1
RCM["MXSTR"]=1.3
RCM["MXSPR"]=0.5
RCM["MXSKL"]=1.5
RCM["MXABL"]=1
RCM["MXAGI"]=0.5
RCM["MXEVA"]=0.5
RCM["MXTGH"]=1.3
RCM["MXRES"]=0.5
RCM["MXLCK"]=1
RCM["MXWT"]=1

RCM["VMHP"]=1
RCM["VMENE"]=1
RCM["VMSTR"]=1.3
RCM["VMSPR"]=1.5
RCM["VMSKL"]=0.5
RCM["VMABL"]=1
RCM["VMAGI"]=1.3
RCM["VMEVA"]=1
RCM["VMTGH"]=0.5
RCM["VMRES"]=1.3
RCM["VMLCK"]=1
RCM["VMWT"]=1

CLS={}
CLS["VagabondHP"]=20
CLS["VagabondENE"]=10
CLS["VagabondSTR"]=5
CLS["VagabondSPR"]=5
CLS["VagabondSKL"]=5
CLS["VagabondABL"]=5
CLS["VagabondAGI"]=5
CLS["VagabondEVA"]=5
CLS["VagabondTGH"]=5
CLS["VagabondRES"]=5
CLS["VagabondLCK"]=5
CLS["VagabondWT"]=0

CLS["DummyClassHP"]=0
CLS["DummyClassENE"]=0
CLS["DummyClassSTR"]=0
CLS["DummyClassSPR"]=0
CLS["DummyClassSKL"]=0
CLS["DummyClassABL"]=0
CLS["DummyClassAGI"]=0
CLS["DummyClassEVA"]=0
CLS["DummyClassTGH"]=0
CLS["DummyClassRES"]=0
CLS["DummyClassLCK"]=0
CLS["DummyClassWT"]=0

CLS["SummonerHP"]=5
CLS["SummonerENE"]=15
CLS["SummonerSTR"]=6
CLS["SummonerSPR"]=10
CLS["SummonerSKL"]=1
CLS["SummonerABL"]=10
CLS["SummonerAGI"]=3
CLS["SummonerEVA"]=1
CLS["SummonerTGH"]=7
CLS["SummonerRES"]=5
CLS["SummonerLCK"]=5
CLS["SummonerWT"]=0

CLS["ThiefHP"]=10
CLS["ThiefENE"]=10
CLS["ThiefSTR"]=1
CLS["ThiefSPR"]=3
CLS["ThiefSKL"]=6
CLS["ThiefABL"]=6
CLS["ThiefAGI"]=10
CLS["ThiefEVA"]=6
CLS["ThiefTGH"]=3
CLS["ThiefRES"]=3
CLS["ThiefLCK"]=7
CLS["ThiefWT"]=0

CLS["KnightHP"]=25
CLS["KnightENE"]=10
CLS["KnightSTR"]=10
CLS["KnightSPR"]=1
CLS["KnightSKL"]=7
CLS["KnightABL"]=5
CLS["KnightAGI"]=2
CLS["KnightEVA"]=1
CLS["KnightTGH"]=10
CLS["KnightRES"]=3
CLS["KnightLCK"]=5
CLS["KnightWT"]=0

CLS["BardHP"]=5
CLS["BardENE"]=20
CLS["BardSTR"]=1
CLS["BardSPR"]=7
CLS["BardSKL"]=10
CLS["BardABL"]=10
CLS["BardAGI"]=2
CLS["BardEVA"]=4
CLS["BardTGH"]=1
CLS["BardRES"]=5
CLS["BardLCK"]=7
CLS["BardWT"]=0

CLS["GunnerHP"]=10
CLS["GunnerENE"]=15
CLS["GunnerSTR"]=3
CLS["GunnerSPR"]=1
CLS["GunnerSKL"]=10
CLS["GunnerABL"]=5
CLS["GunnerAGI"]=3
CLS["GunnerEVA"]=5
CLS["GunnerTGH"]=3
CLS["GunnerRES"]=1
CLS["GunnerLCK"]=5
CLS["GunnerWT"]=0

CLS["ArcherHP"]=15
CLS["ArcherENE"]=10
CLS["ArcherSTR"]=10
CLS["ArcherSPR"]=3
CLS["ArcherSKL"]=3
CLS["ArcherABL"]=5
CLS["ArcherAGI"]=5
CLS["ArcherEVA"]=3
CLS["ArcherTGH"]=3
CLS["ArcherRES"]=3
CLS["ArcherLCK"]=5
CLS["ArcherWT"]=0

CLS["MonkHP"]=15
CLS["MonkENE"]=15
CLS["MonkSTR"]=5
CLS["MonkSPR"]=3
CLS["MonkSKL"]=3
CLS["MonkABL"]=5
CLS["MonkAGI"]=5
CLS["MonkEVA"]=10
CLS["MonkTGH"]=5
CLS["MonkRES"]=5
CLS["MonkLCK"]=5
CLS["MonkWT"]=0

CLS["MedicHP"]=10
CLS["MedicENE"]=20
CLS["MedicSTR"]=1
CLS["MedicSPR"]=10
CLS["MedicSKL"]=1
CLS["MedicABL"]=5
CLS["MedicAGI"]=7
CLS["MedicEVA"]=3
CLS["MedicTGH"]=1
CLS["MedicRES"]=5
CLS["MedicLCK"]=5
CLS["MedicWT"]=0

CLS["MageHP"]=5
CLS["MageENE"]=25
CLS["MageSTR"]=1
CLS["MageSPR"]=5
CLS["MageSKL"]=3
CLS["MageABL"]=3
CLS["MageAGI"]=3
CLS["MageEVA"]=3
CLS["MageTGH"]=3
CLS["MageRES"]=7
CLS["MageLCK"]=5
CLS["MageWT"]=0

CLS["ElementalHP"]=20
CLS["ElementalENE"]=20
CLS["ElementalSTR"]=1
CLS["ElementalSPR"]=10
CLS["ElementalSKL"]=1
CLS["ElementalABL"]=7
CLS["ElementalAGI"]=5
CLS["ElementalEVA"]=5
CLS["ElementalTGH"]=1
CLS["ElementalRES"]=10
CLS["ElementalLCK"]=5
CLS["ElementalWT"]=0

LVL={}
LVL["DU1HP"]=1
LVL["DU1ENE"]=1
LVL["DU1STR"]=1
LVL["DU1SPR"]=1
LVL["DU1SKL"]=1
LVL["DU1ABL"]=1
LVL["DU1AGI"]=1
LVL["DU1EVA"]=1
LVL["DU1TGH"]=1
LVL["DU1RES"]=1
LVL["DU1LCK"]=1
LVL["DU1WT"]=1

LVL["DU2HP"]=1.1
LVL["DU2ENE"]=1.1
LVL["DU2STR"]=1.15
LVL["DU2SPR"]=1.15
LVL["DU2SKL"]=1.15
LVL["DU2ABL"]=1.15
LVL["DU2AGI"]=1.15
LVL["DU2EVA"]=1.15
LVL["DU2TGH"]=1.15
LVL["DU2RES"]=1.15
LVL["DU2LCK"]=1.15
LVL["DU2WT"]=1

LVL["DU3HP"]=1.2
LVL["DU3ENE"]=1.2
LVL["DU3STR"]=1.3
LVL["DU3SPR"]=1.3
LVL["DU3SKL"]=1.3
LVL["DU3ABL"]=1.3
LVL["DU3AGI"]=1.3
LVL["DU3EVA"]=1.3
LVL["DU3TGH"]=1.3
LVL["DU3RES"]=1.3
LVL["DU3LCK"]=1.3
LVL["DU3WT"]=1

LVL["DU4HP"]=1.3
LVL["DU4ENE"]=1.3
LVL["DU4STR"]=1.45
LVL["DU4SPR"]=1.45
LVL["DU4SKL"]=1.45
LVL["DU4ABL"]=1.45
LVL["DU4AGI"]=1.45
LVL["DU4EVA"]=1.45
LVL["DU4TGH"]=1.45
LVL["DU4RES"]=1.45
LVL["DU4LCK"]=1.45
LVL["DU4WT"]=1

LVL["DU5HP"]=1.4
LVL["DU5ENE"]=1.4
LVL["DU5STR"]=1.6
LVL["DU5SPR"]=1.6
LVL["DU5SKL"]=1.6
LVL["DU5ABL"]=1.6
LVL["DU5AGI"]=1.6
LVL["DU5EVA"]=1.6
LVL["DU5TGH"]=1.6
LVL["DU5RES"]=1.6
LVL["DU5LCK"]=1.6
LVL["DU5WT"]=1

LVL["DU6HP"]=1.5
LVL["DU6ENE"]=1.5
LVL["DU6STR"]=1.75
LVL["DU6SPR"]=1.75
LVL["DU6SKL"]=1.75
LVL["DU6ABL"]=1.75
LVL["DU6AGI"]=1.75
LVL["DU6EVA"]=1.75
LVL["DU6TGH"]=1.75
LVL["DU6RES"]=1.75
LVL["DU6LCK"]=1.75
LVL["DU6WT"]=1

LVL["DU7HP"]=1.6
LVL["DU7ENE"]=1.6
LVL["DU7STR"]=1.9
LVL["DU7SPR"]=1.9
LVL["DU7SKL"]=1.9
LVL["DU7ABL"]=1.9
LVL["DU7AGI"]=1.9
LVL["DU7EVA"]=1.9
LVL["DU7TGH"]=1.9
LVL["DU7RES"]=1.9
LVL["DU7LCK"]=1.9
LVL["DU7WT"]=1

LVL["DU8HP"]=1.7
LVL["DU8ENE"]=1.7
LVL["DU8STR"]=2.05
LVL["DU8SPR"]=2.05
LVL["DU8SKL"]=2.05
LVL["DU8ABL"]=2.05
LVL["DU8AGI"]=2.05
LVL["DU8EVA"]=2.05
LVL["DU8TGH"]=2.05
LVL["DU8RES"]=2.05
LVL["DU8LCK"]=2.05
LVL["DU8WT"]=1

LVL["DU9HP"]=1.8
LVL["DU9ENE"]=1.8
LVL["DU9STR"]=2.2
LVL["DU9SPR"]=2.2
LVL["DU9SKL"]=2.2
LVL["DU9ABL"]=2.2
LVL["DU9AGI"]=2.2
LVL["DU9EVA"]=2.2
LVL["DU9TGH"]=2.2
LVL["DU9RES"]=2.2
LVL["DU9LCK"]=2.2
LVL["DU9WT"]=1

LVL["DU10HP"]=1.9
LVL["DU10ENE"]=1.9
LVL["DU10STR"]=2.35
LVL["DU10SPR"]=2.35
LVL["DU10SKL"]=2.35
LVL["DU10ABL"]=2.35
LVL["DU10AGI"]=2.35
LVL["DU10EVA"]=2.35
LVL["DU10TGH"]=2.35
LVL["DU10RES"]=2.35
LVL["DU10LCK"]=2.35
LVL["DU10WT"]=1

LVL["DU11HP"]=2.0
LVL["DU11ENE"]=2.0
LVL["DU11STR"]=2.5
LVL["DU11SPR"]=2.5
LVL["DU11SKL"]=2.5
LVL["DU11ABL"]=2.5
LVL["DU11AGI"]=2.5
LVL["DU11EVA"]=2.5
LVL["DU11TGH"]=2.5
LVL["DU11RES"]=2.5
LVL["DU11LCK"]=2.5
LVL["DU11WT"]=1

LVL["DU12HP"]=2.1
LVL["DU12ENE"]=2.1
LVL["DU12STR"]=2.65
LVL["DU12SPR"]=2.65
LVL["DU12SKL"]=2.65
LVL["DU12ABL"]=2.65
LVL["DU12AGI"]=2.65
LVL["DU12EVA"]=2.65
LVL["DU12TGH"]=2.65
LVL["DU12RES"]=2.65
LVL["DU12LCK"]=2.65
LVL["DU12WT"]=1

LVL["DU13HP"]=2.2
LVL["DU13ENE"]=2.2
LVL["DU13STR"]=2.8
LVL["DU13SPR"]=2.8
LVL["DU13SKL"]=2.8
LVL["DU13ABL"]=2.8
LVL["DU13AGI"]=2.8
LVL["DU13EVA"]=2.8
LVL["DU13TGH"]=2.8
LVL["DU13RES"]=2.8
LVL["DU13LCK"]=2.8
LVL["DU13WT"]=1

LVL["DU14HP"]=2.3
LVL["DU14ENE"]=2.3
LVL["DU14STR"]=2.95
LVL["DU14SPR"]=2.95
LVL["DU14SKL"]=2.95
LVL["DU14ABL"]=2.95
LVL["DU14AGI"]=2.95
LVL["DU14EVA"]=2.95
LVL["DU14TGH"]=2.95
LVL["DU14RES"]=2.95
LVL["DU14LCK"]=2.95
LVL["DU14WT"]=1

LVL["DU15HP"]=2.4
LVL["DU15ENE"]=2.4
LVL["DU15STR"]=3.1
LVL["DU15SPR"]=3.1
LVL["DU15SKL"]=3.1
LVL["DU15ABL"]=3.1
LVL["DU15AGI"]=3.1
LVL["DU15EVA"]=3.1
LVL["DU15TGH"]=3.1
LVL["DU15RES"]=3.1
LVL["DU15LCK"]=3.1
LVL["DU15WT"]=1

LVL["DU16HP"]=2.5
LVL["DU16ENE"]=2.5
LVL["DU16STR"]=3.25
LVL["DU16SPR"]=3.25
LVL["DU16SKL"]=3.25
LVL["DU16ABL"]=3.25
LVL["DU16AGI"]=3.25
LVL["DU16EVA"]=3.25
LVL["DU16TGH"]=3.25
LVL["DU16RES"]=3.25
LVL["DU16LCK"]=3.25
LVL["DU16WT"]=1

LVL["DU17HP"]=2.6
LVL["DU17ENE"]=2.6
LVL["DU17STR"]=3.4
LVL["DU17SPR"]=3.4
LVL["DU17SKL"]=3.4
LVL["DU17ABL"]=3.4
LVL["DU17AGI"]=3.4
LVL["DU17EVA"]=3.4
LVL["DU17TGH"]=3.4
LVL["DU17RES"]=3.4
LVL["DU17LCK"]=3.4
LVL["DU17WT"]=1

LVL["DU18HP"]=2.7
LVL["DU18ENE"]=2.7
LVL["DU18STR"]=3.55
LVL["DU18SPR"]=3.55
LVL["DU18SKL"]=3.55
LVL["DU18ABL"]=3.55
LVL["DU18AGI"]=3.55
LVL["DU18EVA"]=3.55
LVL["DU18TGH"]=3.55
LVL["DU18RES"]=3.55
LVL["DU18LCK"]=3.55
LVL["DU18WT"]=1

LVL["DU19HP"]=2.8
LVL["DU19ENE"]=2.8
LVL["DU19STR"]=3.7
LVL["DU19SPR"]=3.7
LVL["DU19SKL"]=3.7
LVL["DU19ABL"]=3.7
LVL["DU19AGI"]=3.7
LVL["DU19EVA"]=3.7
LVL["DU19TGH"]=3.7
LVL["DU19RES"]=3.7
LVL["DU19LCK"]=3.7
LVL["DU19WT"]=1

LVL["DU20HP"]=3.0
LVL["DU20ENE"]=3.0
LVL["DU20STR"]=4
LVL["DU20SPR"]=4
LVL["DU20SKL"]=4
LVL["DU20ABL"]=4
LVL["DU20AGI"]=4
LVL["DU20EVA"]=4
LVL["DU20TGH"]=4
LVL["DU20RES"]=4
LVL["DU20LCK"]=4
LVL["DU20WT"]=1

LVL["OR1HP"]=1
LVL["OR1ENE"]=1
LVL["OR1STR"]=1
LVL["OR1SPR"]=1
LVL["OR1SKL"]=1
LVL["OR1ABL"]=1
LVL["OR1AGI"]=1
LVL["OR1EVA"]=1
LVL["OR1TGH"]=1
LVL["OR1RES"]=1
LVL["OR1LCK"]=1
LVL["OR1WT"]=1

LVL["OR2HP"]=1.1
LVL["OR2ENE"]=1.1
LVL["OR2STR"]=1.15
LVL["OR2SPR"]=1.15
LVL["OR2SKL"]=1.15
LVL["OR2ABL"]=1.2
LVL["OR2AGI"]=1.15
LVL["OR2EVA"]=1.15
LVL["OR2TGH"]=1.15
LVL["OR2RES"]=1.15
LVL["OR2LCK"]=1.15
LVL["OR2WT"]=1

LVL["OR3HP"]=1.2
LVL["OR3ENE"]=1.2
LVL["OR3STR"]=1.3
LVL["OR3SPR"]=1.3
LVL["OR3SKL"]=1.3
LVL["OR3ABL"]=1.4
LVL["OR3AGI"]=1.3
LVL["OR3EVA"]=1.3
LVL["OR3TGH"]=1.3
LVL["OR3RES"]=1.3
LVL["OR3LCK"]=1.3
LVL["OR3WT"]=1

LVL["OR4HP"]=1.3
LVL["OR4ENE"]=1.3
LVL["OR4STR"]=1.45
LVL["OR4SPR"]=1.45
LVL["OR4SKL"]=1.45
LVL["OR4ABL"]=1.6
LVL["OR4AGI"]=1.45
LVL["OR4EVA"]=1.45
LVL["OR4TGH"]=1.45
LVL["OR4RES"]=1.45
LVL["OR4LCK"]=1.45
LVL["OR4WT"]=1

LVL["OR5HP"]=1.4
LVL["OR5ENE"]=1.4
LVL["OR5STR"]=1.6
LVL["OR5SPR"]=1.6
LVL["OR5SKL"]=1.6
LVL["OR5ABL"]=1.8
LVL["OR5AGI"]=1.6
LVL["OR5EVA"]=1.6
LVL["OR5TGH"]=1.6
LVL["OR5RES"]=1.6
LVL["OR5LCK"]=1.6
LVL["OR5WT"]=1

LVL["OR6HP"]=1.5
LVL["OR6ENE"]=1.5
LVL["OR6STR"]=1.75
LVL["OR6SPR"]=1.75
LVL["OR6SKL"]=1.75
LVL["OR6ABL"]=2.0
LVL["OR6AGI"]=1.75
LVL["OR6EVA"]=1.75
LVL["OR6TGH"]=1.75
LVL["OR6RES"]=1.75
LVL["OR6LCK"]=1.75
LVL["OR6WT"]=1

LVL["OR7HP"]=1.6
LVL["OR7ENE"]=1.6
LVL["OR7STR"]=1.9
LVL["OR7SPR"]=1.9
LVL["OR7SKL"]=1.9
LVL["OR7ABL"]=2.2
LVL["OR7AGI"]=1.9
LVL["OR7EVA"]=1.9
LVL["OR7TGH"]=1.9
LVL["OR7RES"]=1.9
LVL["OR7LCK"]=1.9
LVL["OR7WT"]=1

LVL["OR8HP"]=1.7
LVL["OR8ENE"]=1.7
LVL["OR8STR"]=2.05
LVL["OR8SPR"]=2.05
LVL["OR8SKL"]=2.05
LVL["OR8ABL"]=2.4
LVL["OR8AGI"]=2.05
LVL["OR8EVA"]=2.05
LVL["OR8TGH"]=2.05
LVL["OR8RES"]=2.05
LVL["OR8LCK"]=2.05
LVL["OR8WT"]=1

LVL["OR9HP"]=1.8
LVL["OR9ENE"]=1.8
LVL["OR9STR"]=2.2
LVL["OR9SPR"]=2.2
LVL["OR9SKL"]=2.2
LVL["OR9ABL"]=2.6
LVL["OR9AGI"]=2.2
LVL["OR9EVA"]=2.2
LVL["OR9TGH"]=2.2
LVL["OR9RES"]=2.2
LVL["OR9LCK"]=2.2
LVL["OR9WT"]=1

LVL["OR10HP"]=1.9
LVL["OR10ENE"]=1.9
LVL["OR10STR"]=2.35
LVL["OR10SPR"]=2.35
LVL["OR10SKL"]=2.35
LVL["OR10ABL"]=2.8
LVL["OR10AGI"]=2.35
LVL["OR10EVA"]=2.35
LVL["OR10TGH"]=2.35
LVL["OR10RES"]=2.35
LVL["OR10LCK"]=2.35
LVL["OR10WT"]=1

LVL["OR11HP"]=2.0
LVL["OR11ENE"]=2.0
LVL["OR11STR"]=2.5
LVL["OR11SPR"]=2.5
LVL["OR11SKL"]=2.5
LVL["OR11ABL"]=3.0
LVL["OR11AGI"]=2.5
LVL["OR11EVA"]=2.5
LVL["OR11TGH"]=2.5
LVL["OR11RES"]=2.5
LVL["OR11LCK"]=2.5
LVL["OR11WT"]=1

LVL["OR12HP"]=2.1
LVL["OR12ENE"]=2.1
LVL["OR12STR"]=2.65
LVL["OR12SPR"]=2.65
LVL["OR12SKL"]=2.65
LVL["OR12ABL"]=3.2
LVL["OR12AGI"]=2.65
LVL["OR12EVA"]=2.65
LVL["OR12TGH"]=2.65
LVL["OR12RES"]=2.65
LVL["OR12LCK"]=2.65
LVL["OR12WT"]=1

LVL["OR13HP"]=2.2
LVL["OR13ENE"]=2.2
LVL["OR13STR"]=2.8
LVL["OR13SPR"]=2.8
LVL["OR13SKL"]=2.8
LVL["OR13ABL"]=3.4
LVL["OR13AGI"]=2.8
LVL["OR13EVA"]=2.8
LVL["OR13TGH"]=2.8
LVL["OR13RES"]=2.8
LVL["OR13LCK"]=2.8
LVL["OR13WT"]=1

LVL["OR14HP"]=2.3
LVL["OR14ENE"]=2.3
LVL["OR14STR"]=2.95
LVL["OR14SPR"]=2.95
LVL["OR14SKL"]=2.95
LVL["OR14ABL"]=3.6
LVL["OR14AGI"]=2.95
LVL["OR14EVA"]=2.95
LVL["OR14TGH"]=2.95
LVL["OR14RES"]=2.95
LVL["OR14LCK"]=2.95
LVL["OR14WT"]=1

LVL["OR15HP"]=2.4
LVL["OR15ENE"]=2.4
LVL["OR15STR"]=3.1
LVL["OR15SPR"]=3.1
LVL["OR15SKL"]=3.1
LVL["OR15ABL"]=3.8
LVL["OR15AGI"]=3.1
LVL["OR15EVA"]=3.1
LVL["OR15TGH"]=3.1
LVL["OR15RES"]=3.1
LVL["OR15LCK"]=3.1
LVL["OR15WT"]=1

LVL["OR16HP"]=2.5
LVL["OR16ENE"]=2.5
LVL["OR16STR"]=3.25
LVL["OR16SPR"]=3.25
LVL["OR16SKL"]=3.25
LVL["OR16ABL"]=4.0
LVL["OR16AGI"]=3.25
LVL["OR16EVA"]=3.25
LVL["OR16TGH"]=3.25
LVL["OR16RES"]=3.25
LVL["OR16LCK"]=3.25
LVL["OR16WT"]=1

LVL["OR17HP"]=2.6
LVL["OR17ENE"]=2.6
LVL["OR17STR"]=3.4
LVL["OR17SPR"]=3.4
LVL["OR17SKL"]=3.4
LVL["OR17ABL"]=4.2
LVL["OR17AGI"]=3.4
LVL["OR17EVA"]=3.4
LVL["OR17TGH"]=3.4
LVL["OR17RES"]=3.4
LVL["OR17LCK"]=3.4
LVL["OR17WT"]=1

LVL["OR18HP"]=2.7
LVL["OR18ENE"]=2.7
LVL["OR18STR"]=3.55
LVL["OR18SPR"]=3.55
LVL["OR18SKL"]=3.55
LVL["OR18ABL"]=4.4
LVL["OR18AGI"]=3.55
LVL["OR18EVA"]=3.55
LVL["OR18TGH"]=3.55
LVL["OR18RES"]=3.55
LVL["OR18LCK"]=3.55
LVL["OR18WT"]=1

LVL["OR19HP"]=2.8
LVL["OR19ENE"]=2.8
LVL["OR19STR"]=3.7
LVL["OR19SPR"]=3.7
LVL["OR19SKL"]=3.7
LVL["OR19ABL"]=4.6
LVL["OR19AGI"]=3.7
LVL["OR19EVA"]=3.7
LVL["OR19TGH"]=3.7
LVL["OR19RES"]=3.7
LVL["OR19LCK"]=3.7
LVL["OR19WT"]=1

LVL["OR20HP"]=3.0
LVL["OR20ENE"]=3.0
LVL["OR20STR"]=4
LVL["OR20SPR"]=4
LVL["OR20SKL"]=4
LVL["OR20ABL"]=5
LVL["OR20AGI"]=4
LVL["OR20EVA"]=4
LVL["OR20TGH"]=4
LVL["OR20RES"]=4
LVL["OR20LCK"]=4
LVL["OR20WT"]=1

LVL["WI1HP"]=1
LVL["WI1ENE"]=1
LVL["WI1STR"]=1
LVL["WI1SPR"]=1
LVL["WI1SKL"]=1
LVL["WI1ABL"]=1
LVL["WI1AGI"]=1
LVL["WI1EVA"]=1
LVL["WI1TGH"]=1
LVL["WI1RES"]=1
LVL["WI1LCK"]=1
LVL["WI1WT"]=1

LVL["WI2HP"]=1.12
LVL["WI2ENE"]=1.05
LVL["WI2STR"]=1.2
LVL["WI2SPR"]=1.15
LVL["WI2SKL"]=1.1
LVL["WI2ABL"]=1.15
LVL["WI2AGI"]=1.12
LVL["WI2EVA"]=1.1
LVL["WI2TGH"]=1.15
LVL["WI2RES"]=1.15
LVL["WI2LCK"]=1.1
LVL["WI2WT"]=1

LVL["WI3HP"]=1.24
LVL["WI3ENE"]=1.1
LVL["WI3STR"]=1.4
LVL["WI3SPR"]=1.3
LVL["WI3SKL"]=1.2
LVL["WI3ABL"]=1.3
LVL["WI3AGI"]=1.24
LVL["WI3EVA"]=1.2
LVL["WI3TGH"]=1.3
LVL["WI3RES"]=1.3
LVL["WI3LCK"]=1.2
LVL["WI3WT"]=1

LVL["WI4HP"]=1.36
LVL["WI4ENE"]=1.15
LVL["WI4STR"]=1.6
LVL["WI4SPR"]=1.45
LVL["WI4SKL"]=1.3
LVL["WI4ABL"]=1.45
LVL["WI4AGI"]=1.36
LVL["WI4EVA"]=1.3
LVL["WI4TGH"]=1.45
LVL["WI4RES"]=1.45
LVL["WI4LCK"]=1.3
LVL["WI4WT"]=1

LVL["WI5HP"]=1.48
LVL["WI5ENE"]=1.2
LVL["WI5STR"]=1.8
LVL["WI5SPR"]=1.6
LVL["WI5SKL"]=1.4
LVL["WI5ABL"]=1.6
LVL["WI5AGI"]=1.48
LVL["WI5EVA"]=1.4
LVL["WI5TGH"]=1.6
LVL["WI5RES"]=1.6
LVL["WI5LCK"]=1.4
LVL["WI5WT"]=1

LVL["WI6HP"]=1.6
LVL["WI6ENE"]=1.25
LVL["WI6STR"]=2.0
LVL["WI6SPR"]=1.75
LVL["WI6SKL"]=1.5
LVL["WI6ABL"]=1.75
LVL["WI6AGI"]=1.6
LVL["WI6EVA"]=1.5
LVL["WI6TGH"]=1.75
LVL["WI6RES"]=1.75
LVL["WI6LCK"]=1.5
LVL["WI6WT"]=1

LVL["WI7HP"]=1.72
LVL["WI7ENE"]=1.3
LVL["WI7STR"]=2.2
LVL["WI7SPR"]=1.9
LVL["WI7SKL"]=1.6
LVL["WI7ABL"]=1.9
LVL["WI7AGI"]=1.72
LVL["WI7EVA"]=1.6
LVL["WI7TGH"]=1.9
LVL["WI7RES"]=1.9
LVL["WI7LCK"]=1.6
LVL["WI7WT"]=1

LVL["WI8HP"]=1.84
LVL["WI8ENE"]=1.35
LVL["WI8STR"]=2.4
LVL["WI8SPR"]=2.05
LVL["WI8SKL"]=1.7
LVL["WI8ABL"]=2.05
LVL["WI8AGI"]=1.84
LVL["WI8EVA"]=1.7
LVL["WI8TGH"]=2.05
LVL["WI8RES"]=2.05
LVL["WI8LCK"]=1.7
LVL["WI8WT"]=1

LVL["WI9HP"]=1.96
LVL["WI9ENE"]=1.4
LVL["WI9STR"]=2.6
LVL["WI9SPR"]=2.2
LVL["WI9SKL"]=1.8
LVL["WI9ABL"]=2.2
LVL["WI9AGI"]=1.96
LVL["WI9EVA"]=1.8
LVL["WI9TGH"]=2.2
LVL["WI9RES"]=2.2
LVL["WI9LCK"]=1.8
LVL["WI9WT"]=1

LVL["WI10HP"]=2.08
LVL["WI10ENE"]=1.45
LVL["WI10STR"]=2.8
LVL["WI10SPR"]=2.35
LVL["WI10SKL"]=1.9
LVL["WI10ABL"]=2.35
LVL["WI10AGI"]=2.08
LVL["WI10EVA"]=1.9
LVL["WI10TGH"]=2.35
LVL["WI10RES"]=2.35
LVL["WI10LCK"]=1.9
LVL["WI10WT"]=1

LVL["WI11HP"]=2.2
LVL["WI11ENE"]=1.5
LVL["WI11STR"]=3.0
LVL["WI11SPR"]=2.5
LVL["WI11SKL"]=2
LVL["WI11ABL"]=2.5
LVL["WI11AGI"]=2.2
LVL["WI11EVA"]=2
LVL["WI11TGH"]=2.5
LVL["WI11RES"]=2.5
LVL["WI11LCK"]=2
LVL["WI11WT"]=1

LVL["WI12HP"]=2.32
LVL["WI12ENE"]=1.55
LVL["WI12STR"]=3.2
LVL["WI12SPR"]=2.65
LVL["WI12SKL"]=2.1
LVL["WI12ABL"]=2.65
LVL["WI12AGI"]=2.32
LVL["WI12EVA"]=2.1
LVL["WI12TGH"]=2.65
LVL["WI12RES"]=2.65
LVL["WI12LCK"]=2.1
LVL["WI12WT"]=1

LVL["WI13HP"]=2.44
LVL["WI13ENE"]=1.6
LVL["WI13STR"]=3.4
LVL["WI13SPR"]=2.8
LVL["WI13SKL"]=2.2
LVL["WI13ABL"]=2.8
LVL["WI13AGI"]=2.44
LVL["WI13EVA"]=2.2
LVL["WI13TGH"]=2.8
LVL["WI13RES"]=2.8
LVL["WI13LCK"]=2.2
LVL["WI13WT"]=1

LVL["WI14HP"]=2.56
LVL["WI14ENE"]=1.65
LVL["WI14STR"]=3.6
LVL["WI14SPR"]=2.95
LVL["WI14SKL"]=2.3
LVL["WI14ABL"]=2.95
LVL["WI14AGI"]=2.56
LVL["WI14EVA"]=2.3
LVL["WI14TGH"]=2.95
LVL["WI14RES"]=2.95
LVL["WI14LCK"]=2.3
LVL["WI14WT"]=1

LVL["WI15HP"]=2.68
LVL["WI15ENE"]=1.7
LVL["WI15STR"]=3.8
LVL["WI15SPR"]=3.1
LVL["WI15SKL"]=2.4
LVL["WI15ABL"]=3.1
LVL["WI15AGI"]=2.68
LVL["WI15EVA"]=2.4
LVL["WI15TGH"]=3.1
LVL["WI15RES"]=3.1
LVL["WI15LCK"]=2.4
LVL["WI15WT"]=1

LVL["WI16HP"]=2.8
LVL["WI16ENE"]=1.75
LVL["WI16STR"]=4.0
LVL["WI16SPR"]=3.25
LVL["WI16SKL"]=2.5
LVL["WI16ABL"]=3.25
LVL["WI16AGI"]=2.8
LVL["WI16EVA"]=2.5
LVL["WI16TGH"]=3.25
LVL["WI16RES"]=3.25
LVL["WI16LCK"]=2.5
LVL["WI16WT"]=1

LVL["WI17HP"]=2.92
LVL["WI17ENE"]=1.8
LVL["WI17STR"]=4.2
LVL["WI17SPR"]=3.4
LVL["WI17SKL"]=2.6
LVL["WI17ABL"]=3.4
LVL["WI17AGI"]=2.92
LVL["WI17EVA"]=2.6
LVL["WI17TGH"]=3.4
LVL["WI17RES"]=3.4
LVL["WI17LCK"]=2.6
LVL["WI17WT"]=1

LVL["WI18HP"]=3.04
LVL["WI18ENE"]=1.85
LVL["WI18STR"]=4.4
LVL["WI18SPR"]=3.55
LVL["WI18SKL"]=2.7
LVL["WI18ABL"]=3.55
LVL["WI18AGI"]=3.04
LVL["WI18EVA"]=2.7
LVL["WI18TGH"]=3.55
LVL["WI18RES"]=3.55
LVL["WI18LCK"]=2.7
LVL["WI18WT"]=1

LVL["WI19HP"]=3.16
LVL["WI19ENE"]=1.9
LVL["WI19STR"]=4.6
LVL["WI19SPR"]=3.7
LVL["WI19SKL"]=2.8
LVL["WI19ABL"]=3.7
LVL["WI19AGI"]=3.16
LVL["WI19EVA"]=2.8
LVL["WI19TGH"]=3.7
LVL["WI19RES"]=3.7
LVL["WI19LCK"]=2.8
LVL["WI19WT"]=1

LVL["WI20HP"]=3.4
LVL["WI20ENE"]=2.0
LVL["WI20STR"]=5
LVL["WI20SPR"]=4
LVL["WI20SKL"]=3
LVL["WI20ABL"]=4
LVL["WI20AGI"]=3.4
LVL["WI20EVA"]=3
LVL["WI20TGH"]=4
LVL["WI20RES"]=4
LVL["WI20LCK"]=3
LVL["WI20WT"]=1

LVL["SS1HP"]=1
LVL["SS1ENE"]=1
LVL["SS1STR"]=1
LVL["SS1SPR"]=1
LVL["SS1SKL"]=1
LVL["SS1ABL"]=1
LVL["SS1AGI"]=1
LVL["SS1EVA"]=1
LVL["SS1TGH"]=1
LVL["SS1RES"]=1
LVL["SS1LCK"]=1
LVL["SS1WT"]=1

LVL["SS2HP"]=1.1
LVL["SS2ENE"]=1.15
LVL["SS2STR"]=1.1
LVL["SS2SPR"]=1.2
LVL["SS2SKL"]=1.15
LVL["SS2ABL"]=1.15
LVL["SS2AGI"]=1.15
LVL["SS2EVA"]=1.15
LVL["SS2TGH"]=1.1
LVL["SS2RES"]=1.2
LVL["SS2LCK"]=1.15
LVL["SS2WT"]=1

LVL["SS3HP"]=1.2
LVL["SS3ENE"]=1.3
LVL["SS3STR"]=1.2
LVL["SS3SPR"]=1.4
LVL["SS3SKL"]=1.3
LVL["SS3ABL"]=1.3
LVL["SS3AGI"]=1.3
LVL["SS3EVA"]=1.3
LVL["SS3TGH"]=1.2
LVL["SS3RES"]=1.4
LVL["SS3LCK"]=1.3
LVL["SS3WT"]=1

LVL["SS4HP"]=1.3
LVL["SS4ENE"]=1.45
LVL["SS4STR"]=1.3
LVL["SS4SPR"]=1.6
LVL["SS4SKL"]=1.45
LVL["SS4ABL"]=1.45
LVL["SS4AGI"]=1.45
LVL["SS4EVA"]=1.45
LVL["SS4TGH"]=1.3
LVL["SS4RES"]=1.6
LVL["SS4LCK"]=1.45
LVL["SS4WT"]=1

LVL["SS5HP"]=1.4
LVL["SS5ENE"]=1.6
LVL["SS5STR"]=1.4
LVL["SS5SPR"]=1.8
LVL["SS5SKL"]=1.6
LVL["SS5ABL"]=1.6
LVL["SS5AGI"]=1.6
LVL["SS5EVA"]=1.6
LVL["SS5TGH"]=1.4
LVL["SS5RES"]=1.8
LVL["SS5LCK"]=1.6
LVL["SS5WT"]=1

LVL["SS6HP"]=1.5
LVL["SS6ENE"]=1.75
LVL["SS6STR"]=1.5
LVL["SS6SPR"]=2
LVL["SS6SKL"]=1.75
LVL["SS6ABL"]=1.75
LVL["SS6AGI"]=1.75
LVL["SS6EVA"]=1.75
LVL["SS6TGH"]=1.5
LVL["SS6RES"]=2
LVL["SS6LCK"]=1.75
LVL["SS6WT"]=1

LVL["SS7HP"]=1.6
LVL["SS7ENE"]=1.9
LVL["SS7STR"]=1.6
LVL["SS7SPR"]=2.2
LVL["SS7SKL"]=1.9
LVL["SS7ABL"]=1.9
LVL["SS7AGI"]=1.9
LVL["SS7EVA"]=1.9
LVL["SS7TGH"]=1.6
LVL["SS7RES"]=2.2
LVL["SS7LCK"]=1.9
LVL["SS7WT"]=1

LVL["SS8HP"]=1.7
LVL["SS8ENE"]=2.05
LVL["SS8STR"]=1.7
LVL["SS8SPR"]=2.4
LVL["SS8SKL"]=2.05
LVL["SS8ABL"]=2.05
LVL["SS8AGI"]=2.05
LVL["SS8EVA"]=2.05
LVL["SS8TGH"]=1.7
LVL["SS8RES"]=2.4
LVL["SS8LCK"]=2.05
LVL["SS8WT"]=1

LVL["SS9HP"]=1.8
LVL["SS9ENE"]=2.2
LVL["SS9STR"]=1.8
LVL["SS9SPR"]=2.6
LVL["SS9SKL"]=2.2
LVL["SS9ABL"]=2.2
LVL["SS9AGI"]=2.2
LVL["SS9EVA"]=2.2
LVL["SS9TGH"]=1.8
LVL["SS9RES"]=2.6
LVL["SS9LCK"]=2.2
LVL["SS9WT"]=1

LVL["SS10HP"]=1.9
LVL["SS10ENE"]=2.35
LVL["SS10STR"]=1.9
LVL["SS10SPR"]=2.8
LVL["SS10SKL"]=2.35
LVL["SS10ABL"]=2.35
LVL["SS10AGI"]=2.35
LVL["SS10EVA"]=2.35
LVL["SS10TGH"]=1.9
LVL["SS10RES"]=2.8
LVL["SS10LCK"]=2.35
LVL["SS10WT"]=1

LVL["SS11HP"]=2.0
LVL["SS11ENE"]=2.5
LVL["SS11STR"]=2.0
LVL["SS11SPR"]=3
LVL["SS11SKL"]=2.5
LVL["SS11ABL"]=2.5
LVL["SS11AGI"]=2.5
LVL["SS11EVA"]=2.5
LVL["SS11TGH"]=2.0
LVL["SS11RES"]=3
LVL["SS11LCK"]=2.5
LVL["SS11WT"]=1

LVL["SS12HP"]=2.1
LVL["SS12ENE"]=2.65
LVL["SS12STR"]=2.1
LVL["SS12SPR"]=3.2
LVL["SS12SKL"]=2.65
LVL["SS12ABL"]=2.65
LVL["SS12AGI"]=2.65
LVL["SS12EVA"]=2.65
LVL["SS12TGH"]=2.1
LVL["SS12RES"]=3.2
LVL["SS12LCK"]=2.65
LVL["SS12WT"]=1

LVL["SS13HP"]=2.2
LVL["SS13ENE"]=2.8
LVL["SS13STR"]=2.2
LVL["SS13SPR"]=3.4
LVL["SS13SKL"]=2.8
LVL["SS13ABL"]=2.8
LVL["SS13AGI"]=2.8
LVL["SS13EVA"]=2.8
LVL["SS13TGH"]=2.2
LVL["SS13RES"]=3.4
LVL["SS13LCK"]=2.8
LVL["SS13WT"]=1

LVL["SS14HP"]=2.3
LVL["SS14ENE"]=2.95
LVL["SS14STR"]=2.3
LVL["SS14SPR"]=3.6
LVL["SS14SKL"]=2.95
LVL["SS14ABL"]=2.95
LVL["SS14AGI"]=2.95
LVL["SS14EVA"]=2.95
LVL["SS14TGH"]=2.3
LVL["SS14RES"]=3.6
LVL["SS14LCK"]=2.95
LVL["SS14WT"]=1

LVL["SS15HP"]=2.4
LVL["SS15ENE"]=3.1
LVL["SS15STR"]=2.4
LVL["SS15SPR"]=3.8
LVL["SS15SKL"]=3.1
LVL["SS15ABL"]=3.1
LVL["SS15AGI"]=3.1
LVL["SS15EVA"]=3.1
LVL["SS15TGH"]=2.4
LVL["SS15RES"]=3.8
LVL["SS15LCK"]=3.1
LVL["SS15WT"]=1

LVL["SS16HP"]=2.5
LVL["SS16ENE"]=3.25
LVL["SS16STR"]=2.5
LVL["SS16SPR"]=4
LVL["SS16SKL"]=3.25
LVL["SS16ABL"]=3.25
LVL["SS16AGI"]=3.25
LVL["SS16EVA"]=3.25
LVL["SS16TGH"]=2.5
LVL["SS16RES"]=4
LVL["SS16LCK"]=3.25
LVL["SS16WT"]=1

LVL["SS17HP"]=2.6
LVL["SS17ENE"]=3.4
LVL["SS17STR"]=2.6
LVL["SS17SPR"]=4.2
LVL["SS17SKL"]=3.4
LVL["SS17ABL"]=3.4
LVL["SS17AGI"]=3.4
LVL["SS17EVA"]=3.4
LVL["SS17TGH"]=2.6
LVL["SS17RES"]=4.2
LVL["SS17LCK"]=3.4
LVL["SS17WT"]=1

LVL["SS18HP"]=2.7
LVL["SS18ENE"]=3.55
LVL["SS18STR"]=2.7
LVL["SS18SPR"]=4.4
LVL["SS18SKL"]=3.55
LVL["SS18ABL"]=3.55
LVL["SS18AGI"]=3.55
LVL["SS18EVA"]=3.55
LVL["SS18TGH"]=2.7
LVL["SS18RES"]=4.4
LVL["SS18LCK"]=3.55
LVL["SS18WT"]=1

LVL["SS19HP"]=2.8
LVL["SS19ENE"]=3.7
LVL["SS19STR"]=2.8
LVL["SS19SPR"]=4.6
LVL["SS19SKL"]=3.7
LVL["SS19ABL"]=3.7
LVL["SS19AGI"]=3.7
LVL["SS19EVA"]=3.7
LVL["SS19TGH"]=2.8
LVL["SS19RES"]=4.6
LVL["SS19LCK"]=3.7
LVL["SS19WT"]=1

LVL["SS20HP"]=3.0
LVL["SS20ENE"]=4
LVL["SS20STR"]=3
LVL["SS20SPR"]=5
LVL["SS20SKL"]=4
LVL["SS20ABL"]=4
LVL["SS20AGI"]=4
LVL["SS20EVA"]=4
LVL["SS20TGH"]=3
LVL["SS20RES"]=5
LVL["SS20LCK"]=4
LVL["SS20WT"]=1

LVL["SB1HP"]=1
LVL["SB1ENE"]=1
LVL["SB1STR"]=1
LVL["SB1SPR"]=1
LVL["SB1SKL"]=1
LVL["SB1ABL"]=1
LVL["SB1AGI"]=1
LVL["SB1EVA"]=1
LVL["SB1TGH"]=1
LVL["SB1RES"]=1
LVL["SB1LCK"]=1
LVL["SB1WT"]=1

LVL["SB2HP"]=1.12
LVL["SB2ENE"]=1.1
LVL["SB2STR"]=1.2
LVL["SB2SPR"]=1.15
LVL["SB2SKL"]=1.15
LVL["SB2ABL"]=1.15
LVL["SB2AGI"]=1.2
LVL["SB2EVA"]=1.2
LVL["SB2TGH"]=1.1
LVL["SB2RES"]=1.1
LVL["SB2LCK"]=1.1
LVL["SB2WT"]=1

LVL["SB3HP"]=1.24
LVL["SB3ENE"]=1.2
LVL["SB3STR"]=1.4
LVL["SB3SPR"]=1.3
LVL["SB3SKL"]=1.3
LVL["SB3ABL"]=1.3
LVL["SB3AGI"]=1.4
LVL["SB3EVA"]=1.4
LVL["SB3TGH"]=1.2
LVL["SB3RES"]=1.2
LVL["SB3LCK"]=1.2
LVL["SB3WT"]=1

LVL["SB4HP"]=1.36
LVL["SB4ENE"]=1.3
LVL["SB4STR"]=1.6
LVL["SB4SPR"]=1.45
LVL["SB4SKL"]=1.45
LVL["SB4ABL"]=1.45
LVL["SB4AGI"]=1.6
LVL["SB4EVA"]=1.6
LVL["SB4TGH"]=1.3
LVL["SB4RES"]=1.3
LVL["SB4LCK"]=1.3
LVL["SB4WT"]=1

LVL["SB5HP"]=1.48
LVL["SB5ENE"]=1.4
LVL["SB5STR"]=1.8
LVL["SB5SPR"]=1.6
LVL["SB5SKL"]=1.6
LVL["SB5ABL"]=1.6
LVL["SB5AGI"]=1.8
LVL["SB5EVA"]=1.8
LVL["SB5TGH"]=1.4
LVL["SB5RES"]=1.4
LVL["SB5LCK"]=1.4
LVL["SB5WT"]=1

LVL["SB6HP"]=1.6
LVL["SB6ENE"]=1.5
LVL["SB6STR"]=2
LVL["SB6SPR"]=1.75
LVL["SB6SKL"]=1.75
LVL["SB6ABL"]=1.75
LVL["SB6AGI"]=2
LVL["SB6EVA"]=2
LVL["SB6TGH"]=1.5
LVL["SB6RES"]=1.5
LVL["SB6LCK"]=1.5
LVL["SB6WT"]=1

LVL["SB7HP"]=1.72
LVL["SB7ENE"]=1.6
LVL["SB7STR"]=2.2
LVL["SB7SPR"]=1.9
LVL["SB7SKL"]=1.9
LVL["SB7ABL"]=1.9
LVL["SB7AGI"]=2.2
LVL["SB7EVA"]=2.2
LVL["SB7TGH"]=1.6
LVL["SB7RES"]=1.6
LVL["SB7LCK"]=1.6
LVL["SB7WT"]=1

LVL["SB8HP"]=1.84
LVL["SB8ENE"]=1.7
LVL["SB8STR"]=2.4
LVL["SB8SPR"]=2.05
LVL["SB8SKL"]=2.05
LVL["SB8ABL"]=2.05
LVL["SB8AGI"]=2.4
LVL["SB8EVA"]=2.4
LVL["SB8TGH"]=1.7
LVL["SB8RES"]=1.7
LVL["SB8LCK"]=1.7
LVL["SB8WT"]=1

LVL["SB9HP"]=1.96
LVL["SB9ENE"]=1.8
LVL["SB9STR"]=2.6
LVL["SB9SPR"]=2.2
LVL["SB9SKL"]=2.2
LVL["SB9ABL"]=2.2
LVL["SB9AGI"]=2.6
LVL["SB9EVA"]=2.6
LVL["SB9TGH"]=1.8
LVL["SB9RES"]=1.8
LVL["SB9LCK"]=1.8
LVL["SB9WT"]=1

LVL["SB10HP"]=2.08
LVL["SB10ENE"]=1.9
LVL["SB10STR"]=2.8
LVL["SB10SPR"]=2.35
LVL["SB10SKL"]=2.35
LVL["SB10ABL"]=2.35
LVL["SB10AGI"]=2.8
LVL["SB10EVA"]=2.8
LVL["SB10TGH"]=1.9
LVL["SB10RES"]=1.9
LVL["SB10LCK"]=1.9
LVL["SB10WT"]=1

LVL["SB11HP"]=2.2
LVL["SB11ENE"]=2.0
LVL["SB11STR"]=3.0
LVL["SB11SPR"]=2.5
LVL["SB11SKL"]=2.5
LVL["SB11ABL"]=2.5
LVL["SB11AGI"]=3
LVL["SB11EVA"]=3
LVL["SB11TGH"]=2
LVL["SB11RES"]=2
LVL["SB11LCK"]=2
LVL["SB11WT"]=1

LVL["SB12HP"]=2.34
LVL["SB12ENE"]=2.1
LVL["SB12STR"]=3.2
LVL["SB12SPR"]=2.65
LVL["SB12SKL"]=2.65
LVL["SB12ABL"]=2.65
LVL["SB12AGI"]=3.2
LVL["SB12EVA"]=3.2
LVL["SB12TGH"]=2.1
LVL["SB12RES"]=2.1
LVL["SB12LCK"]=2.1
LVL["SB12WT"]=1

LVL["SB13HP"]=2.46
LVL["SB13ENE"]=2.2
LVL["SB13STR"]=3.4
LVL["SB13SPR"]=2.8
LVL["SB13SKL"]=2.8
LVL["SB13ABL"]=2.8
LVL["SB13AGI"]=3.4
LVL["SB13EVA"]=3.4
LVL["SB13TGH"]=2.2
LVL["SB13RES"]=2.2
LVL["SB13LCK"]=2.2
LVL["SB13WT"]=1

LVL["SB14HP"]=2.58
LVL["SB14ENE"]=2.3
LVL["SB14STR"]=3.6
LVL["SB14SPR"]=2.95
LVL["SB14SKL"]=2.95
LVL["SB14ABL"]=2.95
LVL["SB14AGI"]=3.6
LVL["SB14EVA"]=3.6
LVL["SB14TGH"]=2.3
LVL["SB14RES"]=2.3
LVL["SB14LCK"]=2.3
LVL["SB14WT"]=1

LVL["SB15HP"]=2.7
LVL["SB15ENE"]=2.4
LVL["SB15STR"]=3.8
LVL["SB15SPR"]=3.1
LVL["SB15SKL"]=3.1
LVL["SB15ABL"]=3.1
LVL["SB15AGI"]=3.8
LVL["SB15EVA"]=3.8
LVL["SB15TGH"]=2.4
LVL["SB15RES"]=2.4
LVL["SB15LCK"]=2.4
LVL["SB15WT"]=1

LVL["SB16HP"]=2.82
LVL["SB16ENE"]=2.5
LVL["SB16STR"]=4
LVL["SB16SPR"]=3.25
LVL["SB16SKL"]=3.25
LVL["SB16ABL"]=3.25
LVL["SB16AGI"]=4
LVL["SB16EVA"]=4
LVL["SB16TGH"]=2.5
LVL["SB16RES"]=2.5
LVL["SB16LCK"]=2.5
LVL["SB16WT"]=1

LVL["SB17HP"]=2.94
LVL["SB17ENE"]=2.6
LVL["SB17STR"]=4.2
LVL["SB17SPR"]=3.4
LVL["SB17SKL"]=3.4
LVL["SB17ABL"]=3.4
LVL["SB17AGI"]=4.2
LVL["SB17EVA"]=4.2
LVL["SB17TGH"]=2.6
LVL["SB17RES"]=2.6
LVL["SB17LCK"]=2.6
LVL["SB17WT"]=1

LVL["SB18HP"]=3.06
LVL["SB18ENE"]=2.7
LVL["SB18STR"]=4.4
LVL["SB18SPR"]=3.55
LVL["SB18SKL"]=3.55
LVL["SB18ABL"]=3.55
LVL["SB18AGI"]=4.4
LVL["SB18EVA"]=4.4
LVL["SB18TGH"]=2.7
LVL["SB18RES"]=2.7
LVL["SB18LCK"]=2.7
LVL["SB18WT"]=1

LVL["SB19HP"]=3.18
LVL["SB19ENE"]=2.8
LVL["SB19STR"]=4.6
LVL["SB19SPR"]=3.7
LVL["SB19SKL"]=3.7
LVL["SB19ABL"]=3.7
LVL["SB19AGI"]=4.6
LVL["SB19EVA"]=4.6
LVL["SB19TGH"]=2.8
LVL["SB19RES"]=2.8
LVL["SB19LCK"]=2.8
LVL["SB19WT"]=1

LVL["SB20HP"]=3.42
LVL["SB20ENE"]=3.0
LVL["SB20STR"]=5
LVL["SB20SPR"]=4
LVL["SB20SKL"]=4
LVL["SB20ABL"]=4
LVL["SB20AGI"]=5
LVL["SB20EVA"]=5
LVL["SB20TGH"]=3
LVL["SB20RES"]=3
LVL["SB20LCK"]=3
LVL["SB20WT"]=1

LVL["MX1HP"]=1
LVL["MX1ENE"]=1
LVL["MX1STR"]=1
LVL["MX1SPR"]=1
LVL["MX1SKL"]=1
LVL["MX1ABL"]=1
LVL["MX1AGI"]=1
LVL["MX1EVA"]=1
LVL["MX1TGH"]=1
LVL["MX1RES"]=1
LVL["MX1LCK"]=1
LVL["MX1WT"]=1

LVL["MX2HP"]=1.15
LVL["MX2ENE"]=1.12
LVL["MX2STR"]=1.15
LVL["MX2SPR"]=1.1
LVL["MX2SKL"]=1.2
LVL["MX2ABL"]=1.15
LVL["MX2AGI"]=1.1
LVL["MX2EVA"]=1.1
LVL["MX2TGH"]=1.15
LVL["MX2RES"]=1.1
LVL["MX2LCK"]=1.15
LVL["MX2WT"]=1

LVL["MX3HP"]=1.3
LVL["MX3ENE"]=1.24
LVL["MX3STR"]=1.3
LVL["MX3SPR"]=1.2
LVL["MX3SKL"]=1.4
LVL["MX3ABL"]=1.3
LVL["MX3AGI"]=1.2
LVL["MX3EVA"]=1.2
LVL["MX3TGH"]=1.3
LVL["MX3RES"]=1.2
LVL["MX3LCK"]=1.3
LVL["MX3WT"]=1

LVL["MX4HP"]=1.45
LVL["MX4ENE"]=1.36
LVL["MX4STR"]=1.45
LVL["MX4SPR"]=1.3
LVL["MX4SKL"]=1.6
LVL["MX4ABL"]=1.45
LVL["MX4AGI"]=1.3
LVL["MX4EVA"]=1.3
LVL["MX4TGH"]=1.45
LVL["MX4RES"]=1.3
LVL["MX4LCK"]=1.45
LVL["MX4WT"]=1

LVL["MX5HP"]=1.6
LVL["MX5ENE"]=1.48
LVL["MX5STR"]=1.6
LVL["MX5SPR"]=1.4
LVL["MX5SKL"]=1.8
LVL["MX5ABL"]=1.6
LVL["MX5AGI"]=1.4
LVL["MX5EVA"]=1.4
LVL["MX5TGH"]=1.6
LVL["MX5RES"]=1.4
LVL["MX5LCK"]=1.6
LVL["MX5WT"]=1

LVL["MX6HP"]=1.75
LVL["MX6ENE"]=1.6
LVL["MX6STR"]=1.75
LVL["MX6SPR"]=1.5
LVL["MX6SKL"]=2
LVL["MX6ABL"]=1.75
LVL["MX6AGI"]=1.5
LVL["MX6EVA"]=1.5
LVL["MX6TGH"]=1.75
LVL["MX6RES"]=1.5
LVL["MX6LCK"]=1.75
LVL["MX6WT"]=1

LVL["MX7HP"]=1.9
LVL["MX7ENE"]=1.72
LVL["MX7STR"]=1.9
LVL["MX7SPR"]=1.6
LVL["MX7SKL"]=2.2
LVL["MX7ABL"]=1.9
LVL["MX7AGI"]=1.6
LVL["MX7EVA"]=1.6
LVL["MX7TGH"]=1.9
LVL["MX7RES"]=1.6
LVL["MX7LCK"]=1.9
LVL["MX7WT"]=1

LVL["MX8HP"]=2.05
LVL["MX8ENE"]=1.84
LVL["MX8STR"]=2.05
LVL["MX8SPR"]=1.7
LVL["MX8SKL"]=2.4
LVL["MX8ABL"]=2.05
LVL["MX8AGI"]=1.7
LVL["MX8EVA"]=2.05
LVL["MX8TGH"]=2.05
LVL["MX8RES"]=1.7
LVL["MX8LCK"]=2.05
LVL["MX8WT"]=1

LVL["MX9HP"]=2.2
LVL["MX9ENE"]=1.96
LVL["MX9STR"]=2.2
LVL["MX9SPR"]=1.8
LVL["MX9SKL"]=2.6
LVL["MX9ABL"]=2.2
LVL["MX9AGI"]=1.8
LVL["MX9EVA"]=1.8
LVL["MX9TGH"]=2.2
LVL["MX9RES"]=1.8
LVL["MX9LCK"]=2.2
LVL["MX9WT"]=1

LVL["MX10HP"]=2.35
LVL["MX10ENE"]=2.08
LVL["MX10STR"]=2.35
LVL["MX10SPR"]=1.9
LVL["MX10SKL"]=2.8
LVL["MX10ABL"]=2.35
LVL["MX10AGI"]=1.9
LVL["MX10EVA"]=1.9
LVL["MX10TGH"]=2.35
LVL["MX10RES"]=1.9
LVL["MX10LCK"]=2.35
LVL["MX10WT"]=1

LVL["MX11HP"]=2.5
LVL["MX11ENE"]=2.2
LVL["MX11STR"]=2.5
LVL["MX11SPR"]=2
LVL["MX11SKL"]=3
LVL["MX11ABL"]=2.5
LVL["MX11AGI"]=2
LVL["MX11EVA"]=2
LVL["MX11TGH"]=2.5
LVL["MX11RES"]=2
LVL["MX11LCK"]=2.5
LVL["MX11WT"]=1

LVL["MX12HP"]=2.65
LVL["MX12ENE"]=2.34
LVL["MX12STR"]=2.65
LVL["MX12SPR"]=2.1
LVL["MX12SKL"]=3.2
LVL["MX12ABL"]=2.65
LVL["MX12AGI"]=2.1
LVL["MX12EVA"]=2.1
LVL["MX12TGH"]=2.65
LVL["MX12RES"]=2.1
LVL["MX12LCK"]=2.65
LVL["MX12WT"]=1

LVL["MX13HP"]=2.8
LVL["MX13ENE"]=2.46
LVL["MX13STR"]=2.8
LVL["MX13SPR"]=2.2
LVL["MX13SKL"]=3.4
LVL["MX13ABL"]=2.8
LVL["MX13AGI"]=2.2
LVL["MX13EVA"]=2.2
LVL["MX13TGH"]=2.8
LVL["MX13RES"]=2.2
LVL["MX13LCK"]=2.8
LVL["MX13WT"]=1

LVL["MX14HP"]=2.95
LVL["MX14ENE"]=2.58
LVL["MX14STR"]=2.95
LVL["MX14SPR"]=2.3
LVL["MX14SKL"]=3.6
LVL["MX14ABL"]=2.95
LVL["MX14AGI"]=2.3
LVL["MX14EVA"]=2.3
LVL["MX14TGH"]=2.95
LVL["MX14RES"]=2.3
LVL["MX14LCK"]=2.95
LVL["MX14WT"]=1

LVL["MX15HP"]=3.1
LVL["MX15ENE"]=2.7
LVL["MX15STR"]=3.1
LVL["MX15SPR"]=2.4
LVL["MX15SKL"]=3.8
LVL["MX15ABL"]=3.1
LVL["MX15AGI"]=2.4
LVL["MX15EVA"]=2.4
LVL["MX15TGH"]=3.1
LVL["MX15RES"]=2.4
LVL["MX15LCK"]=3.1
LVL["MX15WT"]=1

LVL["MX16HP"]=3.25
LVL["MX16ENE"]=2.82
LVL["MX16STR"]=3.25
LVL["MX16SPR"]=2.5
LVL["MX16SKL"]=4
LVL["MX16ABL"]=3.25
LVL["MX16AGI"]=2.5
LVL["MX16EVA"]=2.5
LVL["MX16TGH"]=3.25
LVL["MX16RES"]=2.5
LVL["MX16LCK"]=3.25
LVL["MX16WT"]=1

LVL["MX17HP"]=3.4
LVL["MX17ENE"]=2.94
LVL["MX17STR"]=3.4
LVL["MX17SPR"]=2.6
LVL["MX17SKL"]=4.2
LVL["MX17ABL"]=3.4
LVL["MX17AGI"]=2.6
LVL["MX17EVA"]=2.6
LVL["MX17TGH"]=3.4
LVL["MX17RES"]=2.6
LVL["MX17LCK"]=3.4
LVL["MX17WT"]=1

LVL["MX18HP"]=3.55
LVL["MX18ENE"]=3.06
LVL["MX18STR"]=3.55
LVL["MX18SPR"]=2.7
LVL["MX18SKL"]=4.4
LVL["MX18ABL"]=3.55
LVL["MX18AGI"]=3.55
LVL["MX18EVA"]=2.7
LVL["MX18TGH"]=3.55
LVL["MX18RES"]=2.7
LVL["MX18LCK"]=3.55
LVL["MX18WT"]=1

LVL["MX19HP"]=3.7
LVL["MX19ENE"]=3.18
LVL["MX19STR"]=3.7
LVL["MX19SPR"]=2.8
LVL["MX19SKL"]=4.6
LVL["MX19ABL"]=3.7
LVL["MX19AGI"]=2.8
LVL["MX19EVA"]=2.8
LVL["MX19TGH"]=3.7
LVL["MX19RES"]=2.8
LVL["MX19LCK"]=3.7
LVL["MX19WT"]=1

LVL["MX20HP"]=4
LVL["MX20ENE"]=3.42
LVL["MX20STR"]=4
LVL["MX20SPR"]=3
LVL["MX20SKL"]=5
LVL["MX20ABL"]=4
LVL["MX20AGI"]=3
LVL["MX20EVA"]=3
LVL["MX20TGH"]=4
LVL["MX20RES"]=3
LVL["MX20LCK"]=4
LVL["MX20WT"]=1

LVL["VM1HP"]=1
LVL["VM1ENE"]=1
LVL["VM1STR"]=1
LVL["VM1SPR"]=1
LVL["VM1SKL"]=1
LVL["VM1ABL"]=1
LVL["VM1AGI"]=1
LVL["VM1EVA"]=1
LVL["VM1TGH"]=1
LVL["VM1RES"]=1
LVL["VM1LCK"]=1
LVL["VM1WT"]=1

LVL["VM2HP"]=1.1
LVL["VM2ENE"]=1.15
LVL["VM2STR"]=1.15
LVL["VM2SPR"]=1.2
LVL["VM2SKL"]=1.15
LVL["VM2ABL"]=1.15
LVL["VM2AGI"]=1.15
LVL["VM2EVA"]=1.15
LVL["VM2TGH"]=1.1
LVL["VM2RES"]=1.15
LVL["VM2LCK"]=1.15
LVL["VM2WT"]=1

LVL["VM3HP"]=1.2
LVL["VM3ENE"]=1.3
LVL["VM3STR"]=1.3
LVL["VM3SPR"]=1.4
LVL["VM3SKL"]=1.3
LVL["VM3ABL"]=1.3
LVL["VM3AGI"]=1.3
LVL["VM3EVA"]=1.3
LVL["VM3TGH"]=1.2
LVL["VM3RES"]=1.3
LVL["VM3LCK"]=1.3
LVL["VM3WT"]=1

LVL["VM4HP"]=1.3
LVL["VM4ENE"]=1.45
LVL["VM4STR"]=1.45
LVL["VM4SPR"]=1.6
LVL["VM4SKL"]=1.45
LVL["VM4ABL"]=1.45
LVL["VM4AGI"]=1.45
LVL["VM4EVA"]=1.45
LVL["VM4TGH"]=1.3
LVL["VM4RES"]=1.45
LVL["VM4LCK"]=1.45
LVL["VM4WT"]=1

LVL["VM5HP"]=1.4
LVL["VM5ENE"]=1.6
LVL["VM5STR"]=1.6
LVL["VM5SPR"]=1.8
LVL["VM5SKL"]=1.6
LVL["VM5ABL"]=1.6
LVL["VM5AGI"]=1.6
LVL["VM5EVA"]=1.6
LVL["VM5TGH"]=1.4
LVL["VM5RES"]=1.6
LVL["VM5LCK"]=1.6
LVL["VM5WT"]=1

LVL["VM6HP"]=1.5
LVL["VM6ENE"]=1.75
LVL["VM6STR"]=1.75
LVL["VM6SPR"]=2
LVL["VM6SKL"]=1.75
LVL["VM6ABL"]=1.75
LVL["VM6AGI"]=1.75
LVL["VM6EVA"]=1.75
LVL["VM6TGH"]=1.5
LVL["VM6RES"]=1.75
LVL["VM6LCK"]=1.75
LVL["VM6WT"]=1

LVL["VM7HP"]=1.6
LVL["VM7ENE"]=1.9
LVL["VM7STR"]=1.9
LVL["VM7SPR"]=2.2
LVL["VM7SKL"]=1.9
LVL["VM7ABL"]=1.9
LVL["VM7AGI"]=1.9
LVL["VM7EVA"]=1.9
LVL["VM7TGH"]=1.6
LVL["VM7RES"]=1.9
LVL["VM7LCK"]=1.9
LVL["VM7WT"]=1

LVL["VM8HP"]=1.7
LVL["VM8ENE"]=2.05
LVL["VM8STR"]=2.05
LVL["VM8SPR"]=2.4
LVL["VM8SKL"]=2.05
LVL["VM8ABL"]=2.05
LVL["VM8AGI"]=2.05
LVL["VM8EVA"]=2.05
LVL["VM8TGH"]=2.05
LVL["VM8RES"]=2.05
LVL["VM8LCK"]=2.05
LVL["VM8WT"]=1

LVL["VM9HP"]=1.8
LVL["VM9ENE"]=1.8
LVL["VM9STR"]=2.2
LVL["VM9SPR"]=2.6
LVL["VM9SKL"]=2.2
LVL["VM9ABL"]=2.2
LVL["VM9AGI"]=2.2
LVL["VM9EVA"]=2.2
LVL["VM9TGH"]=1.7
LVL["VM9RES"]=2.2
LVL["VM9LCK"]=2.2
LVL["VM9WT"]=1

LVL["VM10HP"]=1.9
LVL["VM10ENE"]=2.35
LVL["VM10STR"]=2.35
LVL["VM10SPR"]=2.8
LVL["VM10SKL"]=2.35
LVL["VM10ABL"]=2.35
LVL["VM10AGI"]=2.35
LVL["VM10EVA"]=2.35
LVL["VM10TGH"]=1.8
LVL["VM10RES"]=2.35
LVL["VM10LCK"]=2.35
LVL["VM10WT"]=1

LVL["VM11HP"]=2.0
LVL["VM11ENE"]=2.5
LVL["VM11STR"]=2.5
LVL["VM11SPR"]=3
LVL["VM11SKL"]=2.5
LVL["VM11ABL"]=2.5
LVL["VM11AGI"]=2.5
LVL["VM11EVA"]=2.5
LVL["VM11TGH"]=1.9
LVL["VM11RES"]=2.5
LVL["VM11LCK"]=2.5
LVL["VM11WT"]=1

LVL["VM12HP"]=2.1
LVL["VM12ENE"]=2.1
LVL["VM12STR"]=2.65
LVL["VM12SPR"]=3.2
LVL["VM12SKL"]=2.65
LVL["VM12ABL"]=2.65
LVL["VM12AGI"]=2.65
LVL["VM12EVA"]=2.65
LVL["VM12TGH"]=2
LVL["VM12RES"]=2.65
LVL["VM12LCK"]=2.65
LVL["VM12WT"]=1

LVL["VM13HP"]=2.2
LVL["VM13ENE"]=2.8
LVL["VM13STR"]=2.8
LVL["VM13SPR"]=3.4
LVL["VM13SKL"]=2.8
LVL["VM13ABL"]=2.8
LVL["VM13AGI"]=2.8
LVL["VM13EVA"]=2.8
LVL["VM13TGH"]=2.1
LVL["VM13RES"]=2.8
LVL["VM13LCK"]=2.8
LVL["VM13WT"]=1

LVL["VM14HP"]=2.3
LVL["VM14ENE"]=2.95
LVL["VM14STR"]=2.95
LVL["VM14SPR"]=3.6
LVL["VM14SKL"]=2.95
LVL["VM14ABL"]=2.95
LVL["VM14AGI"]=2.95
LVL["VM14EVA"]=2.95
LVL["VM14TGH"]=2.2
LVL["VM14RES"]=2.95
LVL["VM14LCK"]=2.95
LVL["VM14WT"]=1

LVL["VM15HP"]=2.4
LVL["VM15ENE"]=3.1
LVL["VM15STR"]=3.1
LVL["VM15SPR"]=3.8
LVL["VM15SKL"]=3.1
LVL["VM15ABL"]=3.1
LVL["VM15AGI"]=3.1
LVL["VM15EVA"]=3.1
LVL["VM15TGH"]=2.3
LVL["VM15RES"]=3.1
LVL["VM15LCK"]=3.1
LVL["VM15WT"]=1

LVL["VM16HP"]=2.5
LVL["VM16ENE"]=3.25
LVL["VM16STR"]=3.25
LVL["VM16SPR"]=4
LVL["VM16SKL"]=3.25
LVL["VM16ABL"]=3.25
LVL["VM16AGI"]=3.25
LVL["VM16EVA"]=3.25
LVL["VM16TGH"]=2.4
LVL["VM16RES"]=3.25
LVL["VM16LCK"]=3.25
LVL["VM16WT"]=1

LVL["VM17HP"]=2.6
LVL["VM17ENE"]=3.4
LVL["VM17STR"]=3.4
LVL["VM17SPR"]=4.2
LVL["VM17SKL"]=3.4
LVL["VM17ABL"]=3.4
LVL["VM17AGI"]=3.4
LVL["VM17EVA"]=3.4
LVL["VM17TGH"]=2.5
LVL["VM17RES"]=3.4
LVL["VM17LCK"]=3.4
LVL["VM17WT"]=1

LVL["VM18HP"]=2.7
LVL["VM18ENE"]=3.55
LVL["VM18STR"]=3.55
LVL["VM18SPR"]=4.4
LVL["VM18SKL"]=3.55
LVL["VM18ABL"]=3.55
LVL["VM18AGI"]=3.55
LVL["VM18EVA"]=3.55
LVL["VM18TGH"]=2.6
LVL["VM18RES"]=3.55
LVL["VM18LCK"]=3.55
LVL["VM18WT"]=1

LVL["VM19HP"]=2.8
LVL["VM19ENE"]=3.7
LVL["VM19STR"]=3.7
LVL["VM19SPR"]=4.6
LVL["VM19SKL"]=3.7
LVL["VM19ABL"]=3.7
LVL["VM19AGI"]=3.7
LVL["VM19EVA"]=3.7
LVL["VM19TGH"]=2.7
LVL["VM19RES"]=3.7
LVL["VM19LCK"]=3.7
LVL["VM19WT"]=1

LVL["VM20HP"]=3
LVL["VM20ENE"]=4
LVL["VM20STR"]=4
LVL["VM20SPR"]=4
LVL["VM20SKL"]=5
LVL["VM20ABL"]=4
LVL["VM20AGI"]=4
LVL["VM20EVA"]=4
LVL["VM20TGH"]=3
LVL["VM20RES"]=4
LVL["VM20LCK"]=4
LVL["VM20WT"]=1

def DressingRoom(Race,Mod,Classy,Level):
	"""The DressingRoom function takes 4 variables in to account and creates a player unit's stats from them."""
	#First you grab the Race...
	RaceSTR=RAC[Race+"STR"]
	RaceSPR=RAC[Race+"SPR"]
	RaceSKL=RAC[Race+"SKL"]
	RaceABL=RAC[Race+"ABL"]
	RaceAGI=RAC[Race+"AGI"]
	RaceEVA=RAC[Race+"EVA"]
	RaceTGH=RAC[Race+"TGH"]
	RaceRES=RAC[Race+"RES"]
	RaceLCK=RAC[Race+"LCK"]
	RaceWT=RAC[Race+"WT"]
	RaceHP=RAC[Race+"HP"]
	RaceENE=RAC[Race+"ENE"]
	
	#Then you snag the RaceMod...
	ModSTR=RCM[Mod+"STR"]
	ModSPR=RCM[Mod+"SPR"]
	ModSKL=RCM[Mod+"SKL"]
	ModABL=RCM[Mod+"ABL"]
	ModAGI=RCM[Mod+"AGI"]
	ModEVA=RCM[Mod+"EVA"]
	ModTGH=RCM[Mod+"TGH"]
	ModRES=RCM[Mod+"RES"]
	ModLCK=RCM[Mod+"LCK"]
	ModWT=RCM[Mod+"WT"]
	ModHP=RCM[Mod+"HP"]
	ModENE=RCM[Mod+"ENE"]
	
	#Next you snag the Class...
	ClassSTR=CLS[Classy+"STR"]
	ClassSPR=CLS[Classy+"SPR"]
	ClassSKL=CLS[Classy+"SKL"]
	ClassABL=CLS[Classy+"ABL"]
	ClassAGI=CLS[Classy+"AGI"]
	ClassEVA=CLS[Classy+"EVA"]
	ClassTGH=CLS[Classy+"TGH"]
	ClassRES=CLS[Classy+"RES"]
	ClassLCK=CLS[Classy+"LCK"]
	ClassWT=CLS[Classy+"WT"]
	ClassHP=CLS[Classy+"HP"]
	ClassENE=CLS[Classy+"ENE"]
	
	#And lastly you snag the level...
	LevelSTR=LVL[Mod+Level+"STR"]
	LevelSPR=LVL[Mod+Level+"SPR"]
	LevelSKL=LVL[Mod+Level+"SKL"]
	LevelABL=LVL[Mod+Level+"ABL"]
	LevelAGI=LVL[Mod+Level+"AGI"]
	LevelEVA=LVL[Mod+Level+"EVA"]
	LevelTGH=LVL[Mod+Level+"TGH"]
	LevelRES=LVL[Mod+Level+"RES"]
	LevelLCK=LVL[Mod+Level+"LCK"]
	LevelWT=LVL[Mod+Level+"WT"]
	LevelHP=LVL[Mod+Level+"HP"]
	LevelENE=LVL[Mod+Level+"HP"]
	
	#Then you put it all together!
	UnitSTR=max(round(((RaceSTR*ModSTR)+ClassSTR)*LevelSTR),1)
	UnitSPR=max(round(((RaceSPR*ModSPR)+ClassSPR)*LevelSPR),1)
	UnitSKL=max(round(((RaceSKL*ModSKL)+ClassSKL)*LevelSKL),1)
	UnitABL=max(round(((RaceABL*ModABL)+ClassABL)*LevelABL),1)
	UnitAGI=max(round(((RaceAGI*ModAGI)+ClassAGI)*LevelAGI),1)
	UnitEVA=max(round(((RaceEVA*ModEVA)+ClassEVA)*LevelEVA),1)
	UnitTGH=max(round(((RaceTGH*ModTGH)+ClassTGH)*LevelTGH),1)
	UnitRES=max(round(((RaceRES*ModRES)+ClassRES)*LevelRES),1)
	UnitLCK=max(round(((RaceLCK*ModLCK)+ClassLCK)*LevelLCK),1)
	UnitWT=max(round(((RaceWT*ModWT)+ClassWT)*LevelWT),1)
	UnitHP=max(round(((RaceHP*ModHP)+ClassHP)*LevelHP),1)
	UnitENE=max(round(((RaceENE*ModENE)+ClassENE)*LevelENE),1)
	
	return(UnitSTR,UnitSPR,UnitSKL,UnitABL,UnitAGI,UnitEVA,UnitTGH,UnitRES,UnitLCK,UnitWT,UnitHP,UnitENE)
	
OmniUnitData={}

for Inputs in DressingRoomInputs:
	OmniUnitData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]] = DressingRoom(Inputs[0],Inputs[1],Inputs[2],Inputs[3])