import Bosses
import Allies
import Players
import Enemies

running = 1
while running == 1:
	choice=input("Select a Unit Type!\n [P]layers!\n [A]llies!\n [E]nemies!\n ")
	if choice == "P" or choice == "p":
		choice=input("Select a Unit!\n [GM] Reyn!\n [Vi] Roselyn Wolfe!\n [TM] Helm!\n [KM] Jango!\n ")
		if choice == "GM" or choice == "Gm" or choice == "gm":
			Players.Reyn("Reyn")
		elif choice == "VI" or choice == "Vi" or choice == "vi":
			Players.Roselyn("Roselyn")
		elif choice == "TM" or choice == "Tm" or choice == "tm":
			Players.Helm("Helm")
		elif choice == "KM" or choice == "Km" or choice == "km":
			Players.Jango("Jango")
	elif choice == "A" or choice == "a":
		choice=input("Select an Ally!\n [Ja]net Steel!\n [Wa]nder Steel!\n [Jo]sephine!\n ")
		if choice == "JA" or choice == "Ja" or choice == "ja":
			Allies.Janet("Janet")
		elif choice == "WA" or choice == "Wa" or choice == "wa":
			Allies.Wander("Wander")
		elif choice == "JO" or choice == "Jo" or choice == "jo":
			Allies.Josephine("Josephine")
	elif choice == "E" or choice == "e":
		choice=input("Select your Bandit!\n [Ga]chum!\n [Gu]nbo!\n [Og]re!\n ")
		if choice == "GA" or choice == "Ga" or choice == "ga":
			Enemies.Gachum("Gachum")
		elif choice == "GU" or choice == "Gu" or choice == "gu":
			Enemies.Gunbo("Gunbo")
		elif choice == "OG" or choice == "Og" or choice == "og":
			Enemies.Ogre("Ogre")
		elif choice == "spider":
			Enemies.Arachnos("Arachnos")