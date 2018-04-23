import Bosses
import Allies
import Players
import Enemies
from WSD2 import WSD

running = 1
while running == 1:
	choice=input("Select a Player!\n [TM] Tempest!\n [AE] Aeront!\n [LI] Lirru!\n [VI] Violet!\n [GM] GM_3826!\n [KM] Kmj10!\n ")
	if choice == "TM" or choice == "tm" or choice == "tM" or choice == "Tm":
		choice=input("Select a Character!\n [CL] Clips!\n [HE] Helm!\n ")
		if choice == "CL" or choice == "Cl" or choice == "cL" or choice == "cl":
			Players.StClips("StClips")
		elif choice == "HE" or choice == "he":
			Players.Helm("Helm")
	elif choice == "AE" or choice == "ae":
		choice=input("Select a Character!\n [G]illigan!\n ")
		if choice == "G" or choice == "g":
			Players.Gilligan("Gilligan")
	elif choice == "LI" or choice == "li":
		choice=input("Select a Character!\n [L]irru!\n ")
		if choice == "L" or choice == "l":
			Players.Lirru("Lirru")
	elif choice == "VI" or choice == "vi":
		choice=input("Select a Character!\n [YW] Yule Walker!\n [RW] Roselyn Wolfe!\n ")
		if choice == "YW" or choice == "yw":
			Players.Yule("Yule")
		elif choice == "RW" or choice == "rw":
			Players.Roselyn("Roselyn")
	elif choice == "GM" or choice == "gm":
		choice=input("Select a Character!\n [R]eyn!\n [B]rad!\n ")
		if choice == "R" or choice == "r":
			Players.Reyn("Reyn")
		elif choice == "B" or choice == "b":
			Players.Brad("Brad")
	elif choice == "KM" or choice == "km":
		choice=input("Select a Character!\n [J]ango the Thceif!\n ")
		if choice == "J" or choice == "j":
			Players.Jango("Jango")