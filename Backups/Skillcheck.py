import random as ra

class Skillcheck():
	def __init__(self,Unit,Level):
		self.Unit=Unit
		self.Level=Level
	@property
	def T1Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (25-(Level*5)):
			print(" ")
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(" ")
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def T2Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (50-(Level*5)):
			print(" ")
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(" ")
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def T3Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (75-(Level*5)):
			print(" ")
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(" ")
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def T4Check(self):
		Level=self.Level
		Name=self.Unit
		if ra.randint(1,100) >= (100-(Level*5)):
			print(" ")
			print(Name,"successfully used the Skill!")
			return(" ")
		else:
			print(" ")
			print(Name,"failed to use it this time.")
			return(" ")
	@property
	def Choice(self):
		Level=self.Level
		Name=self.Unit
		choice=input("Select a Check!\n [T1]\n [T2]\n [T3]\n [T4]\n ")
		if choice == "T1" or choice == "t1":
			print(self.T1Check)
		elif choice == "T2" or choice == "t2":
			print(self.T2Check)
		elif choice == "T3" or choice == "t3":
			print(self.T3Check)
		elif choice == "T4" or choice == "t4":
			print(self.T4Check)