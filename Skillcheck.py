import random as ra
from WSD2 import WSD

class Skillcheck():
	def __init__(self,Unit,Level):
		self.Unit=Unit
		self.Level=Level
	@property
	def T1Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (25-(Level*5)):
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def T2Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (50-(Level*5)):
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def T3Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (75-(Level*5)):
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def T4Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (100-(Level*5)):
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def Choice(self):
		Level=self.Level
		Name=self.Unit
		choice=input("Select a Check!\n [T1]\n [T2]\n [T3]\n [T4]\n ")
		if choice == "T1" or choice == "t1":
			print("================================")
			print(self.T1Check)
		elif choice == "T2" or choice == "t2":
			print("================================")
			print(self.T2Check)
		elif choice == "T3" or choice == "t3":
			print("================================")
			print(self.T3Check)
		elif choice == "T4" or choice == "t4":
			print("================================")
			print(self.T4Check)

class Itemcheck():
	def __init__(self,User):
		self.User=WSD[User]
		self.Name=User
	@property
	def Confirm(self):
		uACT=float(input("User action number is: "))
		uLCK=float(self.User.LCK)
		Roll=ra.randint(1,100)
		Threshold=round((uACT*3)-uLCK*0.33)
		if Roll >= Threshold:
			print("================================")
			print(self.Name+"'s Item used.")
			print("================================")
			return(" ")
		else:
			print("================================")
			print(self.Name+"'s Item not used.")
			print("================================")
			return(" ")

class Attackcheck():
	def __init__(self,User):
		self.User=WSD[User]
		self.Name=User
	@property
	def Confirm(self):
		uACT=float(input("User action number is: "))
		uLCK=float(self.User.LCK)
		Roll=ra.randint(1,100)
		Threshold=round((uACT*10)-uLCK*0.33)
		if Roll >= Threshold:
			print("================================")
			print(self.Name+"'s attack confirmed. Go ahead.")
			print("================================")
			return(" ")
		else:
			print("================================")
			print(self.Name+"'s attack failed.")
			print("================================")
			return(" ")