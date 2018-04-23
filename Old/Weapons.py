PrefixTypes=("Normal","Reinforced","Attuned","Accurate","Lightweight","Balanced","Masterpiece","Festive","Blazing","Breezy","Electric","Icy","Stony")
Materials=("Unobtanium","Ivory","Bone","Wood","Tin","Copper","Bronze","Gold","Cobalt","Tungsten","Shardsteel","Shardiron","Magenium","Steel","Iron","Cazenium","Hevisteel","Heviron","Rozenium","Chrome","Bismuth","Aluminum","Titanium","Silver","Brass","Lead","Orichalc","Platinum")
WeaponTypes=("Knife","Saber","Greatsword","Polearm","Battlestaff","Claw","Whip","Knuckles","Cane","Wand","Talis","Rod","Slicer","Bow","Crossbow","Handbow","TwinPistol","Mechgun","Rifle","Warhammer","Flail","Flute","Guitar","Saxophone","Yoyo","Tome","Battlecannon")
Upgrades=("0","1","2","3","4","5","6","7","8","9","10")

ForgeWInputs=[]

for p in PrefixTypes:
	for m in Materials:
		for w in WeaponTypes:
			for u in Upgrades:
				ForgeWInputs.append((p,m,w,u))

PRE={}
PRE["NormalPD"]=1
PRE["NormalMD"]=1
PRE["NormalAC"]=1
PRE["NormalPR"]=1
PRE["NormalMR"]=1
PRE["NormalWT"]=1
PRE["NormalBuy"]=1
PRE["NormalSell"]=1
PRE["NormalSpecial"]="It's completely normal."

PRE["BlazingPD"]=1
PRE["BlazingMD"]=1
PRE["BlazingAC"]=1
PRE["BlazingPR"]=1
PRE["BlazingMR"]=1
PRE["BlazingWT"]=1
PRE["BlazingBuy"]=1
PRE["BlazingSell"]=1
PRE["BlazingSpecial"]="It's engulfed in gently roaring flames, so it deals Fire damage."

PRE["ElectricPD"]=1
PRE["ElectricMD"]=1
PRE["ElectricAC"]=1
PRE["ElectricPR"]=1
PRE["ElectricMR"]=1
PRE["ElectricWT"]=1
PRE["ElectricBuy"]=1
PRE["ElectricSell"]=1
PRE["ElectricSpecial"]="It's sparking like a loose wire, so it deals Lightning damage."

PRE["IcyPD"]=1
PRE["IcyMD"]=1
PRE["IcyAC"]=1
PRE["IcyPR"]=1
PRE["IcyMR"]=1
PRE["IcyWT"]=1
PRE["IcyBuy"]=1
PRE["IcySell"]=1
PRE["IcySpecial"]="It's covered in a thin layer of ice, so it deals Aqua damage."

PRE["BreezyPD"]=1
PRE["BreezyMD"]=1
PRE["BreezyAC"]=1
PRE["BreezyPR"]=1
PRE["BreezyMR"]=1
PRE["BreezyWT"]=1
PRE["BreezyBuy"]=1
PRE["BreezySell"]=1
PRE["BreezySpecial"]="It's surrounded by a funnel of wind, so it deals Wind damage."

PRE["StonyPD"]=1
PRE["StonyMD"]=1
PRE["StonyAC"]=1
PRE["StonyPR"]=1
PRE["StonyMR"]=1
PRE["StonyWT"]=1
PRE["StonyBuy"]=1
PRE["StonySell"]=1
PRE["StonySpecial"]="It's got a rocky crust on it, so it deals Earth damage."

PRE["FestivePD"]=1
PRE["FestiveMD"]=1
PRE["FestiveAC"]=1
PRE["FestivePR"]=1
PRE["FestiveMR"]=1
PRE["FestiveWT"]=1
PRE["FestiveBuy"]=1
PRE["FestiveSell"]=1
PRE["FestiveSpecial"]="It's filled with holiday spirit.\n It can inflict the Festive status on targets."

PRE["ReinforcedPD"]=2
PRE["ReinforcedMD"]=1
PRE["ReinforcedAC"]=1
PRE["ReinforcedPR"]=1
PRE["ReinforcedMR"]=1
PRE["ReinforcedWT"]=2
PRE["ReinforcedBuy"]=2
PRE["ReinforcedSell"]=2
PRE["ReinforcedSpecial"]="It's heavily Reinforced, so it has double the usual Physical Damage...and Weight"

PRE["AttunedPD"]=1
PRE["AttunedMD"]=2
PRE["AttunedAC"]=1
PRE["AttunedPR"]=1
PRE["AttunedMR"]=1
PRE["AttunedWT"]=2
PRE["AttunedBuy"]=2
PRE["AttunedSell"]=2
PRE["AttunedSpecial"]="It's incredibly Attuned, so it has double the usual Magical Damage...and Weight"

PRE["LightweightPD"]=1
PRE["LightweightMD"]=1
PRE["LightweightAC"]=1
PRE["LightweightPR"]=1
PRE["LightweightMR"]=1
PRE["LightweightWT"]=0.5
PRE["LightweightBuy"]=1.5
PRE["LightweightSell"]=1.5
PRE["LightweightSpecial"]="It's pretty Lightweight, so it has half the usual Weight."

PRE["AccuratePD"]=1
PRE["AccurateMD"]=1
PRE["AccurateAC"]=2
PRE["AccuratePR"]=1
PRE["AccurateMR"]=1
PRE["AccurateWT"]=1
PRE["AccurateBuy"]=2
PRE["AccurateSell"]=2
PRE["AccurateSpecial"]="It's very Accurate, so it has double the usual Weapon Accuracy. However, it deals less damage."

PRE["BalancedPD"]=1.25
PRE["BalancedMD"]=1.25
PRE["BalancedAC"]=1.25
PRE["BalancedPR"]=1
PRE["BalancedMR"]=1
PRE["BalancedWT"]=1
PRE["BalancedBuy"]=1.25
PRE["BalancedSell"]=1.25
PRE["BalancedSpecial"]="It's very well Balanced, so it has 25% better Physical Damage and Accuracy. It's also 25% lighter than Normal weapons."

PRE["MasterpiecePD"]=2
PRE["MasterpieceMD"]=2
PRE["MasterpieceAC"]=2
PRE["MasterpiecePR"]=2
PRE["MasterpieceMR"]=2
PRE["MasterpieceWT"]=0.5
PRE["MasterpieceBuy"]=4
PRE["MasterpieceSell"]=4
PRE["MasterpieceSpecial"]="It's a total Masterpiece. All its stats are doubled except Weight, which is halved."

MAT={}
MAT["UnobtaniumPD"]=0
MAT["UnobtaniumMD"]=0
MAT["UnobtaniumAC"]=0
MAT["UnobtaniumPR"]=0
MAT["UnobtaniumMR"]=0
MAT["UnobtaniumWT"]=0
MAT["UnobtaniumBuy"]=0
MAT["UnobtaniumSell"]=0
MAT["UnobtaniumSpecial"]="made of Unobtanium.\n"
#===================================
#TIER I START
#===================================
#Ivory & Silk
#Magical Lightweight Material
MAT["IvoryPD"]=3
MAT["IvoryMD"]=6
MAT["IvoryAC"]=10
MAT["IvoryPR"]=3
MAT["IvoryMR"]=6
MAT["IvoryWT"]=3
MAT["IvoryBuy"]=100
MAT["IvorySell"]=50
MAT["IvorySpecial"]="made of Ivory.\n"

#Cotton & Wood
#Balanced Lightweight Material
MAT["WoodPD"]=4
MAT["WoodMD"]=4
MAT["WoodAC"]=10
MAT["WoodPR"]=4
MAT["WoodMR"]=4
MAT["WoodWT"]=6
MAT["WoodBuy"]=100
MAT["WoodSell"]=50
MAT["WoodSpecial"]="made of Wood.\n"

#Bone & Leather
#Physical Lightweight Material
MAT["BonePD"]=6
MAT["BoneMD"]=3
MAT["BoneAC"]=10
MAT["BonePR"]=6
MAT["BoneMR"]=3
MAT["BoneWT"]=5
MAT["BoneBuy"]=100
MAT["BoneSell"]=50
MAT["BoneSpecial"]="made of Bone.\n"

#Midweight
#Tin, Midweight Physical material
MAT["TinPD"]=8
MAT["TinMD"]=4
MAT["TinAC"]=6
MAT["TinPR"]=8
MAT["TinMR"]=4
MAT["TinWT"]=8
MAT["TinBuy"]=120
MAT["TinSell"]=60
MAT["TinSpecial"]="made of Tin.\n"
#Copper, Midweight Magical Material
MAT["CopperPD"]=4
MAT["CopperMD"]=8
MAT["CopperAC"]=6
MAT["CopperPR"]=4
MAT["CopperMR"]=8
MAT["CopperWT"]=6
MAT["CopperBuy"]=120
MAT["CopperSell"]=60
MAT["CopperSpecial"]="made of Copper.\n"
#Bronze, Balanced midweight material
MAT["BronzePD"]=7
MAT["BronzeMD"]=7
MAT["BronzeAC"]=7
MAT["BronzePR"]=7
MAT["BronzeMR"]=7
MAT["BronzeWT"]=7
MAT["BronzeBuy"]=120
MAT["BronzeSell"]=60
MAT["BronzeSpecial"]="made of Bronze.\n"

#Gold
#Magical Heavyweight Material
MAT["GoldPD"]=6
MAT["GoldMD"]=12
MAT["GoldAC"]=0
MAT["GoldPR"]=6
MAT["GoldMR"]=12
MAT["GoldWT"]=13
MAT["GoldBuy"]=150
MAT["GoldSell"]=75
MAT["GoldSpecial"]="made of Gold.\n"
#Cobalt
#Balanced Heavyweight Material
MAT["CobaltPD"]=10
MAT["CobaltMD"]=10
MAT["CobaltAC"]=0
MAT["CobaltPR"]=10
MAT["CobaltMR"]=10
MAT["CobaltWT"]=10
MAT["CobaltBuy"]=150
MAT["CobaltSell"]=75
MAT["CobaltSpecial"]="made of Cobalt.\n"
#Tungsten
#Physical Heavyweight Material
MAT["TungstenPD"]=12
MAT["TungstenMD"]=6
MAT["TungstenAC"]=0
MAT["TungstenPR"]=12
MAT["TungstenMR"]=6
MAT["TungstenWT"]=13
MAT["TungstenBuy"]=150
MAT["TungstenSell"]=75
MAT["TungstenSpecial"]="made of Tungsten.\n"
#===================================
			#Tier II
#===================================
#Shardsteel: Physical Lightweight
MAT["ShardsteelPD"]=16
MAT["ShardsteelMD"]=8
MAT["ShardsteelAC"]=12
MAT["ShardsteelPR"]=16
MAT["ShardsteelMR"]=8
MAT["ShardsteelWT"]=8
MAT["ShardsteelBuy"]=200
MAT["ShardsteelSell"]=100
MAT["ShardsteelSpecial"]="made of Shardsteel.\n"
#Magenium: Magical Lightweight
MAT["MageniumPD"]=8
MAT["MageniumMD"]=16
MAT["MageniumAC"]=12
MAT["MageniumPR"]=8
MAT["MageniumMR"]=16
MAT["MageniumWT"]=8
MAT["MageniumBuy"]=200
MAT["MageniumSell"]=100
MAT["MageniumSpecial"]="made of Magenium.\n"
#Shardiron: Balanced Lightweight
MAT["ShardironPD"]=13
MAT["ShardironMD"]=13
MAT["ShardironAC"]=14
MAT["ShardironPR"]=13
MAT["ShardironMR"]=13
MAT["ShardironWT"]=6
MAT["ShardironBuy"]=200
MAT["ShardironSell"]=100
MAT["ShardironSpecial"]="made of Shardiron.\n"

#Steel: Physical Midweight
MAT["SteelPD"]=24
MAT["SteelMD"]=12
MAT["SteelAC"]=10
MAT["SteelPR"]=24
MAT["SteelMR"]=12
MAT["SteelWT"]=20
MAT["SteelBuy"]=300
MAT["SteelSell"]=150
MAT["SteelSpecial"]="made of Steel.\n"
#Cazenium: Magical Midweight
MAT["CazeniumPD"]=12
MAT["CazeniumMD"]=24
MAT["CazeniumAC"]=10
MAT["CazeniumPR"]=12
MAT["CazeniumMR"]=24
MAT["CazeniumWT"]=15
MAT["CazeniumBuy"]=300
MAT["CazeniumSell"]=150
MAT["CazeniumSpecial"]="made of Cazenium.\n"
#Iron: Balanced Midweight
MAT["IronPD"]=18
MAT["IronMD"]=18
MAT["IronAC"]=10
MAT["IronPR"]=18
MAT["IronMR"]=18
MAT["IronWT"]=18
MAT["IronBuy"]=300
MAT["IronSell"]=150
MAT["IronSpecial"]="made of Iron.\n"

#Hevisteel: Physical Heavyweight
MAT["HevisteelPD"]=30
MAT["HevisteelMD"]=15
MAT["HevisteelAC"]=8
MAT["HevisteelPR"]=30
MAT["HevisteelMR"]=15
MAT["HevisteelWT"]=28
MAT["HevisteelBuy"]=400
MAT["HevisteelSell"]=200
MAT["HevisteelSpecial"]="made of Hevisteel.\n"
#Rozenium: Magical Heavyweight
MAT["RozeniumPD"]=15
MAT["RozeniumMD"]=30
MAT["RozeniumAC"]=8
MAT["RozeniumPR"]=15
MAT["RozeniumMR"]=30
MAT["RozeniumWT"]=22
MAT["RozeniumBuy"]=400
MAT["RozeniumSell"]=200
MAT["RozeniumSpecial"]="made of Rozenium.\n"
#Heviron: Balanced Heavyweight
MAT["HevironPD"]=24
MAT["HevironMD"]=24
MAT["HevironAC"]=8
MAT["HevironPR"]=24
MAT["HevironMR"]=24
MAT["HevironWT"]=23
MAT["HevironBuy"]=400
MAT["HevironSell"]=200
MAT["HevironSpecial"]="made of Heviron.\n"
#===================================
			#Tier III
#===================================
#Chrome: Physical Lightweight
MAT["ChromePD"]=20
MAT["ChromeMD"]=10
MAT["ChromeAC"]=15
MAT["ChromePR"]=20
MAT["ChromeMR"]=10
MAT["ChromeWT"]=10
MAT["ChromeBuy"]=500
MAT["ChromeSell"]=250
MAT["ChromeSpecial"]="made of Chrome.\n"
#Bismuth: Magical Lightweight
MAT["BismuthPD"]=10
MAT["BismuthMD"]=20
MAT["BismuthAC"]=15
MAT["BismuthPR"]=10
MAT["BismuthMR"]=20
MAT["BismuthWT"]=10
MAT["BismuthBuy"]=500
MAT["BismuthSell"]=250
MAT["BismuthSpecial"]="made of Bismuth.\n"
#Aluminum: Balanced Lightweight
MAT["AluminumPD"]=15
MAT["AluminumMD"]=15
MAT["AluminumAC"]=20
MAT["AluminumPR"]=15
MAT["AluminumMR"]=15
MAT["AluminumWT"]=5
MAT["AluminumBuy"]=500
MAT["AluminumSell"]=250
MAT["AluminumSpecial"]="made of Aluminum.\n"

#Titanium: Physical Midweight
MAT["TitaniumPD"]=30
MAT["TitaniumMD"]=15
MAT["TitaniumAC"]=12
MAT["TitaniumPR"]=30
MAT["TitaniumMR"]=15
MAT["TitaniumWT"]=30
MAT["TitaniumBuy"]=600
MAT["TitaniumSell"]=300
MAT["TitaniumSpecial"]="made of Titanium.\n"
#Silver: Magical Midweight
MAT["SilverPD"]=15
MAT["SilverMD"]=30
MAT["SilverAC"]=12
MAT["SilverPR"]=15
MAT["SilverMR"]=30
MAT["SilverWT"]=25
MAT["SilverBuy"]=600
MAT["SilverSell"]=300
MAT["SilverSpecial"]="made of Silver.\n"
#Brass: Balanced Midweight
MAT["BrassPD"]=22
MAT["BrassMD"]=22
MAT["BrassAC"]=15
MAT["BrassPR"]=22
MAT["BrassMR"]=22
MAT["BrassWT"]=20
MAT["BrassBuy"]=600
MAT["BrassSell"]=300
MAT["BrassSpecial"]="made of Brass.\n"

#Lead: Physical Heavyweight
MAT["LeadPD"]=40
MAT["LeadMD"]=20
MAT["LeadAC"]=10
MAT["LeadPR"]=40
MAT["LeadMR"]=20
MAT["LeadWT"]=40
MAT["LeadBuy"]=700
MAT["LeadSell"]=350
MAT["LeadSpecial"]="made of Lead.\n"
#Orichalc: Magical Heavyweight
MAT["OrichalcPD"]=20
MAT["OrichalcMD"]=40
MAT["OrichalcAC"]=10
MAT["OrichalcPR"]=20
MAT["OrichalcMR"]=40
MAT["OrichalcWT"]=37
MAT["OrichalcBuy"]=700
MAT["OrichalcSell"]=350
MAT["OrichalcSpecial"]="made of Orichalc.\n"
#Platinum: Balanced Heavyweight
MAT["PlatinumPD"]=35
MAT["PlatinumMD"]=35
MAT["PlatinumAC"]=12
MAT["PlatinumPR"]=35
MAT["PlatinumMR"]=35
MAT["PlatinumWT"]=35
MAT["PlatinumBuy"]=700
MAT["PlatinumSell"]=350
MAT["PlatinumSpecial"]="made of Platinum.\n"
#===================================
			#Tier IV
#===================================
#Adamantite: Physical Lightweight. An ore discovered at the beneath active volcanoes. The danger of mining the stuff drives its scarcity, causing it to be expensive.
#Crystalite: Magical Lightweight. An ore discovered in subterranean deserts, it conducts magic like no other ore of this world.
#Orionite: Balanced Lightweight. An ore discovered in a surprisingly hollow mountain. The name comes from the constellation, which could be seen through a hole in the dome of the mountain at the time of discovery.

#Lunalite: Physical Midweight. A rare ore discovered during a deep-sea drilling operation. It reflects light just like the moon.
#Solite: Magical Midweight. A rare ore discovered in the belly of a slain Phoenix. It's warm to the touch, but its origins are mysterious.
#Territe: Balanced Midweight. An ore discovered by a humble farmer who mined his own metal and forged his own tools. He named it after the soil he works with.

#Impervium: Physical Heavyweight. An ore discovered deep below Phoenix Hill itself. Has incredible protective properties.
#Sorcium: Magical Heavyweight. An ore discovered beneath abandoned Phoenix nests. Named after Sorcery itself due to its incredible magical potential.
#Brinieum: Balanced Heavyweight. An ore discovered in craggy cliffsides near the floor of the seas of the world. Possesses a salty taste and a stinging cut.
#===================================
			#MATERIALS: END
#===================================
#===================================
			#WEAPONS: BEGIN
#===================================
WEP={}
WEP["KnifePD"]=0.65
WEP["KnifeMD"]=0.65
WEP["KnifeAC"]=1.25
WEP["KnifeWT"]=0.25
WEP["KnifeBuy"]=0.25
WEP["KnifeSell"]=0.25
WEP["KnifeSpecial"]="A Knife "

WEP["SaberPD"]=1.0
WEP["SaberMD"]=1.0
WEP["SaberAC"]=1.0
WEP["SaberWT"]=1.0
WEP["SaberBuy"]=1.0
WEP["SaberSell"]=1.0
WEP["SaberSpecial"]="A Saber "

WEP["KnucklesPD"]=0.6
WEP["KnucklesMD"]=0.6
WEP["KnucklesAC"]=1.5
WEP["KnucklesWT"]=0.05
WEP["KnucklesBuy"]=0.5
WEP["KnucklesSell"]=0.5
WEP["KnucklesSpecial"]="A set of Knuckles "

WEP["WarhammerPD"]=1.5
WEP["WarhammerMD"]=0.0
WEP["WarhammerAC"]=0.6
WEP["WarhammerWT"]=1.4
WEP["WarhammerBuy"]=1.5
WEP["WarhammerSell"]=1.5
WEP["WarhammerSpecial"]="A Warhammer "

WEP["FlailPD"]=1.25
WEP["FlailMD"]=0.85
WEP["FlailAC"]=0.85
WEP["FlailWT"]=1.25
WEP["FlailBuy"]=1.25
WEP["FlailSell"]=1.25
WEP["FlailSpecial"]="A Flail "

WEP["GreatswordPD"]=1.67
WEP["GreatswordMD"]=0.67
WEP["GreatswordAC"]=0.67
WEP["GreatswordWT"]=1.4
WEP["GreatswordBuy"]=1.67
WEP["GreatswordSell"]=1.67
WEP["GreatswordSpecial"]="A Greatsword "

WEP["PolearmPD"]=1.15
WEP["PolearmMD"]=1.15
WEP["PolearmAC"]=1.15
WEP["PolearmWT"]=1.15
WEP["PolearmBuy"]=1.15
WEP["PolearmSell"]=1.15
WEP["PolearmSpecial"]="A Polearm "

WEP["WhipPD"]=1.0
WEP["WhipMD"]=1.0
WEP["WhipAC"]=0.7
WEP["WhipWT"]=1.25
WEP["WhipBuy"]=1.25
WEP["WhipSell"]=1.25
WEP["WhipSpecial"]="A Whip "

WEP["YoyoPD"]=1.25
WEP["YoyoMD"]=1.25
WEP["YoyoAC"]=0.75
WEP["YoyoWT"]=1.5
WEP["YoyoBuy"]=1.25
WEP["YoyoSell"]=1.25
WEP["YoyoSpecial"]="A Yoyo "

WEP["CanePD"]=0.75
WEP["CaneMD"]=1.25
WEP["CaneAC"]=0.7
WEP["CaneWT"]=1.15
WEP["CaneBuy"]=1.0
WEP["CaneSell"]=1.0
WEP["CaneSpecial"]="A Cane "

WEP["ClawPD"]=1.1
WEP["ClawMD"]=0.9
WEP["ClawAC"]=1.0
WEP["ClawWT"]=1.1
WEP["ClawBuy"]=1.05
WEP["ClawSell"]=1.05
WEP["ClawSpecial"]="A Claw "

WEP["BattlestaffPD"]=1.15
WEP["BattlestaffMD"]=1.0
WEP["BattlestaffAC"]=0.85
WEP["BattlestaffWT"]=1.15
WEP["BattlestaffBuy"]=0.8
WEP["BattlestaffSell"]=0.8
WEP["BattlestaffSpecial"]="A Battlestaff "

WEP["TalisPD"]=1.15
WEP["TalisMD"]=0.7
WEP["TalisAC"]=1.15
WEP["TalisWT"]=0.33
WEP["TalisBuy"]=0.8
WEP["TalisSell"]=0.8
WEP["TalisSpecial"]="A Talis "

WEP["WandPD"]=0.0
WEP["WandMD"]=0.0
WEP["WandAC"]=1.4
WEP["WandWT"]=0.1
WEP["WandBuy"]=0.25
WEP["WandSell"]=0.25
WEP["WandSpecial"]="A Wand "

WEP["RodPD"]=1.5
WEP["RodMD"]=1.67
WEP["RodAC"]=0.67
WEP["RodWT"]=1.1
WEP["RodBuy"]=1.33
WEP["RodSell"]=1.33
WEP["RodSpecial"]="A Rod "

WEP["TomePD"]=0.0
WEP["TomeMD"]=1.5
WEP["TomeAC"]=0.6
WEP["TomeWT"]=1.4
WEP["TomeBuy"]=2.0
WEP["TomeSell"]=2.0
WEP["TomeSpecial"]="A Tome "

WEP["SlicerPD"]=0.67
WEP["SlicerMD"]=0.67
WEP["SlicerAC"]=0.67
WEP["SlicerWT"]=0.67
WEP["SlicerBuy"]=0.67
WEP["SlicerSell"]=0.67
WEP["SlicerSpecial"]="A Slicer "

WEP["BowPD"]=1.15
WEP["BowMD"]=1.15
WEP["BowAC"]=0.85
WEP["BowWT"]=0.85
WEP["BowBuy"]=1.15
WEP["BowSell"]=1.15
WEP["BowSpecial"]="A Bow "

WEP["CrossbowPD"]=1.4
WEP["CrossbowMD"]=0.6
WEP["CrossbowAC"]=1.0
WEP["CrossbowWT"]=1.5
WEP["CrossbowBuy"]=1.5
WEP["CrossbowSell"]=1.5
WEP["CrossbowSpecial"]="A Crossbow "

WEP["HandbowPD"]=1.0
WEP["HandbowMD"]=1.0
WEP["HandbowAC"]=0.65
WEP["HandbowWT"]=0.65
WEP["HandbowBuy"]=1.2
WEP["HandbowSell"]=1.2
WEP["HandbowSpecial"]="A Handbow "

#Firearms
WEP["TwinPistolPD"]=0.65
WEP["TwinPistolMD"]=0.65
WEP["TwinPistolAC"]=1.15
WEP["TwinPistolWT"]=0.8
WEP["TwinPistolBuy"]=1.0
WEP["TwinPistolSell"]=1.0
WEP["TwinPistolSpecial"]="A pair of Twin Pistols "

WEP["MechgunPD"]=0.2
WEP["MechgunMD"]=0.2
WEP["MechgunAC"]=1.5
WEP["MechgunWT"]=1.2
WEP["MechgunBuy"]=0.85
WEP["MechgunSell"]=0.85
WEP["MechgunSpecial"]="A Mechgun "

WEP["RiflePD"]=1.25
WEP["RifleMD"]=0.75
WEP["RifleAC"]=1.5
WEP["RifleWT"]=1.5
WEP["RifleBuy"]=1.5
WEP["RifleSell"]=1.5
WEP["RifleSpecial"]="A Rifle "

WEP["BattlecannonPD"]=2
WEP["BattlecannonMD"]=0.0
WEP["BattlecannonAC"]=0.75
WEP["BattlecannonWT"]=2
WEP["BattlecannonBuy"]=2.2
WEP["BattlecannonSell"]=2.2
WEP["BattlecannonSpecial"]="A Battlecannon "

#Instruments
#Mic
WEP["MicPD"]=0.0
WEP["MicMD"]=0.25
WEP["MicAC"]=3.0
WEP["MicWT"]=0.1
WEP["MicBuy"]=1.5
WEP["MicSell"]=1.5
WEP["MicSpecial"]="A Mic "
#Flute
WEP["FlutePD"]=0.1
WEP["FluteMD"]=1.0
WEP["FluteAC"]=1.0
WEP["FluteWT"]=0.3
WEP["FluteBuy"]=0.75
WEP["FluteSell"]=0.75
WEP["FluteSpecial"]="A Flute "
#Guitar
WEP["GuitarPD"]=1.0
WEP["GuitarMD"]=1.25
WEP["GuitarAC"]=1.25
WEP["GuitarWT"]=1.5
WEP["GuitarBuy"]=1.25
WEP["GuitarSell"]=1.25
WEP["GuitarSpecial"]="A Guitar "
#Sax
WEP["SaxophonePD"]=0.75
WEP["SaxophoneMD"]=1.75
WEP["SaxophoneAC"]=1.25
WEP["SaxophoneWT"]=2.0
WEP["SaxophoneBuy"]=1.75
WEP["SaxophoneSell"]=1.75
WEP["SaxophoneSpecial"]="A Saxophone "
#===================================
			#WEAPONS: END
#===================================
UP={}
UP["0PD"]=1.0
UP["1PD"]=1.1
UP["2PD"]=1.2
UP["3PD"]=1.3
UP["4PD"]=1.4
UP["5PD"]=1.5
UP["6PD"]=1.6
UP["7PD"]=1.7
UP["8PD"]=1.8
UP["9PD"]=1.9
UP["10PD"]=2.0

UP["0MD"]=1.0
UP["1MD"]=1.1
UP["2MD"]=1.2
UP["3MD"]=1.3
UP["4MD"]=1.4
UP["5MD"]=1.5
UP["6MD"]=1.6
UP["7MD"]=1.7
UP["8MD"]=1.8
UP["9MD"]=1.9
UP["10MD"]=2.0

UP["0AC"]=1.0
UP["1AC"]=1.1
UP["2AC"]=1.2
UP["3AC"]=1.3
UP["4AC"]=1.4
UP["5AC"]=1.5
UP["6AC"]=1.6
UP["7AC"]=1.7
UP["8AC"]=1.8
UP["9AC"]=1.9
UP["10AC"]=2.0

UP["0PR"]=1.0
UP["1PR"]=1.1
UP["2PR"]=1.2
UP["3PR"]=1.3
UP["4PR"]=1.4
UP["5PR"]=1.5
UP["6PR"]=1.6
UP["7PR"]=1.7
UP["8PR"]=1.8
UP["9PR"]=1.9
UP["10PR"]=2.0

UP["0MR"]=1.0
UP["1MR"]=1.1
UP["2MR"]=1.2
UP["3MR"]=1.3
UP["4MR"]=1.4
UP["5MR"]=1.5
UP["6MR"]=1.6
UP["7MR"]=1.7
UP["8MR"]=1.8
UP["9MR"]=1.9
UP["10MR"]=2.0

UP["0WT"]=1.0
UP["1WT"]=0.95
UP["2WT"]=0.9
UP["3WT"]=0.85
UP["4WT"]=0.8
UP["5WT"]=0.75
UP["6WT"]=0.7
UP["7WT"]=0.65
UP["8WT"]=0.6
UP["9WT"]=1.55
UP["10WT"]=1.5

UP["0Buy"]=1.0
UP["1Buy"]=1.1
UP["2Buy"]=1.2
UP["3Buy"]=1.3
UP["4Buy"]=1.4
UP["5Buy"]=1.5
UP["6Buy"]=1.6
UP["7Buy"]=1.7
UP["8Buy"]=1.8
UP["9Buy"]=1.9
UP["10Buy"]=2.0

UP["0Sell"]=1.0
UP["1Sell"]=1.1
UP["2Sell"]=1.2
UP["3Sell"]=1.3
UP["4Sell"]=1.4
UP["5Sell"]=1.5
UP["6Sell"]=1.6
UP["7Sell"]=1.7
UP["8Sell"]=1.8
UP["9Sell"]=1.9
UP["10Sell"]=2.0

UP["0Special"]=" It hasn't been upgraded at all."
UP["1Special"]=" It has been upgraded 1 time."
UP["2Special"]=" It has been upgraded 2 times."
UP["3Special"]=" It has been upgraded 3 times."
UP["4Special"]=" It has been upgraded 4 times."
UP["5Special"]=" It has been upgraded 5 times."
UP["6Special"]=" It has been upgraded 6 times."
UP["7Special"]=" It has been upgraded 7 times."
UP["8Special"]=" It has been upgraded 8 times."
UP["9Special"]=" It has been upgraded 9 times."
UP["10Special"]=" It has been upgraded 10 times."

def ForgeW(PrefixType,Material,WeaponType,UpgradeLevel):
	"""The ForgeW function Forges a weapon from its base components into a lethal tool."""
	
	#Get the appropriate material stats...
	OrePD=MAT[Material+"PD"]
	OreMD=MAT[Material+"MD"]
	OreAC=MAT[Material+"AC"]
	OreWT=MAT[Material+"WT"]
	OreBY=MAT[Material+"Buy"]
	OreSL=MAT[Material+"Sell"]
	OreSP=MAT[Material+"Special"]
	
	#And weapon type stats...
	SmithPD=WEP[WeaponType+"PD"]
	SmithMD=WEP[WeaponType+"MD"]
	SmithAC=WEP[WeaponType+"AC"]
	SmithWT=WEP[WeaponType+"WT"]
	SmithBY=WEP[WeaponType+"Buy"]
	SmithSL=WEP[WeaponType+"Sell"]
	SmithSP=WEP[WeaponType+"Special"]
	
	#And apply the upgrade...
	UpgradePD=UP[UpgradeLevel+"PD"]
	UpgradeMD=UP[UpgradeLevel+"MD"]
	UpgradeAC=UP[UpgradeLevel+"AC"]
	UpgradeWT=UP[UpgradeLevel+"WT"]
	UpgradeBY=UP[UpgradeLevel+"Buy"]
	UpgradeSL=UP[UpgradeLevel+"Sell"]
	UpgradeSP=UP[UpgradeLevel+"Special"]
	
	PrefixPD=PRE[PrefixType+"PD"]
	PrefixMD=PRE[PrefixType+"MD"]
	PrefixAC=PRE[PrefixType+"AC"]
	PrefixWT=PRE[PrefixType+"WT"]
	PrefixBY=PRE[PrefixType+"Buy"]
	PrefixSL=PRE[PrefixType+"Sell"]
	PrefixSP=PRE[PrefixType+"Special"]
	
	#Then, add them all together.	
	ProductPD=max(round(((OrePD*SmithPD)*UpgradePD)*PrefixPD),1)
	ProductMD=max(round(((OreMD*SmithMD)*UpgradeMD)*PrefixMD),1)
	ProductAC=max(round(((OreAC*SmithAC)*UpgradeAC)*PrefixAC),1)
	ProductWT=max(round(((OreWT*SmithWT)*UpgradeWT)*PrefixWT),1)
	ProductBY=max(round(((OreBY*SmithBY)*UpgradeBY)*PrefixBY),1)
	ProductSL=max(round(((OreSL*SmithSL)*UpgradeSL)*PrefixSL),1)
	ProductSP=(SmithSP+OreSP+PrefixSP+UpgradeSP)
	
	return(ProductPD,ProductMD,ProductAC,ProductWT,ProductBY,ProductSL,ProductSP)

#Recall that ForgeW simply needs its three inputs, which we have a list of. So, let's make our
#database of weapon information.
OmniWeapData={}

#Go through every set of inputs we have...
for Inputs in ForgeWInputs:
	#And create a key in the dictionary by combining their three names. Then, set that
	#key equal to whatever ForgeW returns when those three inputs are put in.
	OmniWeapData[Inputs[0]+Inputs[1]+Inputs[2]+Inputs[3]] = ForgeW(Inputs[0],Inputs[1],Inputs[2],Inputs[3])