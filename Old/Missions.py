import Bosses
import Allies
import Players
import Enemies

running = 1
while running == 1:
	choice=input("Select a Unit Type!\n [P]layers!\n [A]llies!\n [E]nemies!\n [O]ther!\n ")
	if choice == "P" or choice == "p":
		choice=input("Select a Player!\n [GM]_3826!\n [Te]mpestVermillion!\n [Vi]olet!\n [Ae]ront!\n [Li]rru!\n ")
		if choice == "GM" or choice == "Gm" or choice == "gm":
			choice=input("Select a Character!\n [B]rad!\n [R]eyn!\n ")
			if choice == "B" or choice == "b":
				Players.Brad("Brad")
			elif choice == "R" or choice == "r":
				Players.Reyn("Reyn")
		elif choice == "VI" or choice == "Vi" or choice == "vi":
			choice=input("Select a Character!\n [C]hambellan [W]alker!\n [R]oselyn [W]olfe!\n [Y]ule [W]alker!\n ")
			if choice == "CW" or choice == "cw":
				#Players.Chambellan("Chambellan")
				print("Placeheld.")
			elif choice == "RW" or choice == "rw":
				Players.Roselyn("Roselyn")
			elif choice == "YW" or choice == "yw":
				Players.Yule("Yule")
		elif choice == "TE" or choice == "Te" or choice == "te":
			choice=input("Select a Character!\n [C] Clips!\n [SNC] Saint Nick's Clips!\n [L] Loriana!\n [AHL] All-Hallows Loriana!\n ")
			if choice == "C" or choice == "c":
				#Players.Clips("Clips")
				print("Placeheld.")
			elif choice == "SNC" or choice == "snc":
				Players.StClips("StClips")
			elif choice == "L" or choice == "l":
				#Players.Loriana("Loriana")
				print("Placeheld.")
			elif choice == "AHL" or choice == "ahl":
				#Players.AHLoriana("Loriana")
				print("Placeheld.")
		elif choice == "LI" or choice == "Li" or choice == "li":
			choice=input("Select a Character!\n [L]irru!\n ")
			if choice == "L" or choice == "l":
				Players.Lirru("Lirru")
		elif choice == "AE" or choice == "Ae" or choice == "ae":
			choice=input("Select a Character!\n [G] Gilligan!\n ")
			if choice == "G" or choice == "g":
				Players.Gilligan("Gilligan")
	elif choice == "A" or choice == "a":
		choice=input("Select an Ally Type!\n [N]umbered!\n [R]egular!\n [P]et!\n ")
		if choice == "N" or choice == "n":
			choice=input("Select an Ally!\n [1] The First Monk!\n [2] The Twin Suppliers!\n [3] The Third Witch!\n [4] The Fourth Judge!\n [5] The Fifth General!\n [6] The Sixth Knight!\n [>] Next Page!\n ")
			if choice == "1":
				Allies.One("One")
			elif choice == "2":
				Allies.Twins("Two")
			elif choice == "3":
				#Allies.Three("Three")
				print("Placeheld.")
			elif choice == "4":
				Allies.Four("Four")
			elif choice == "5":
				#Allies.Five("Five")
				print("Placeheld.")
			elif choice == "6":
				Allies.Six("Six")
			elif choice == ">":
				choice=input("Select an Ally!\n [7] The Seventh Sage!\n [8] The Eighth Scholar!\n [9] The Ninth Necromancer!\n [10] The Tenth Technician!\n [11] The Eleventh Sorceress!\n [12] The Twelfth Leader!\n ")
				if choice == "7":
					#Allies.Sev("Sev")
					print("Placeheld.")
				elif choice == "8":
					#Allies.Eight("Eight")
					print("Placeheld.")
				elif choice == "9":
					#Allies.Nine("Nine")
					print("Placeheld.")
				elif choice == "10":
					#Allies.Ten("Ten")
					print("Placeheld.")
				elif choice == "11":
					Allies.Eleven("Eleven")
				elif choice == "12":
					#Allies.Twelve("Jess")
					print("Placeheld.")
		elif choice == "R" or choice == "r":
			choice=input("Choose an Ally!\n [Re]intaur!\n [Wa]nder Steel!\n [Ja]net Steel!\n [No]rwolf!\n ")
			if choice == "Re" or choice == "re" or choice == "RE":
				Allies.Reintaur("Reintaur")
			elif choice == "Wa" or choice == "wa" or choice == "WA":
				Allies.Wander("Wander")
			elif choice == "Ja" or choice == "ja" or choice == "JA":
				Allies.Janet("Janet")
			elif choice == "No" or choice == "no" or choice == "NO":
				#Allies.Norwolf("Norwolf")
				print("Placeheld.")