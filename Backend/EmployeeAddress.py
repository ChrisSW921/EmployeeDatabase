'''
     EmployeeAddress Class

    Properties
        private string Address
        private string City
        private string State
        private int Zip_Code
        
    Public Methods 
        - Properties will have getter and setter methods public
'''

class EmployeeAddress:
    def __init__(self, streetAddress : str, city : str, state : str, zipCode : int):
        self.Street_Address = streetAddress
        self.City = city
        self.State = state
        self.Zip_Code = zipCode