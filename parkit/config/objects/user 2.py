class UserInfo:
	def __init__(self, FirstName, LastName, DateOfBirth, Flagged, CarMake, CarModel, CarYear, CarColor, CarVin, CarLicensePlateNumber):
		self.FirstName = FirstName
		self.LastName = LastName
		self.DateOfBirth = DateOfBirth
		self.Flagged = False
		self.CarMake = CarMake
		self.CarModel = CarModel
		self.CarYear = CarYear
		self.CarColor = CarColor
		self.CarVin = CarVin
		self.CarLicensePlateNumber = CarLicensePlateNumber
		
	def get_FirstName(self):
		return self.FirstName

	def get_LastName(self):
		return self.LastName

	def get_DateOfBirth(self):
		return self.DateOfBirth

	def get_Flagged(self):
		return self.Flagged

	def get_CarMake(self):
		return self.CarMake

	def get_CarModel(self):
		return self.CarModel

	def get_CarYear(self):
		return self.CarYear

	def get_CarColor(self):
		return self.CarColor

	def get_CarVin(self):
		return self.CarVin

	def get_CarLicensePlateNumber(self):
		return self.CarLicensePlateNumber

	def toDictionary(self):
		CUSTOMER_INFO = {
                "FirstName": self.FirstName ,
                "LastName": self.LastName,
                "DateOfBirth": self.DateOfBirth,
                "Flagged": self.Flagged,
                "CarMake": self.CarMake,
                "CarModel": self.CarModel,
				"CarYear": self.CarYear,
				"CarColor": self.CarColor,
				"CarVin": self.CarVin,
				"CarLicensePlateNumber": self.CarLicensePlateNumber
            }
		return CUSTOMER_INFO