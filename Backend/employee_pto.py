'''
     EmployeePTO Class

    Properties
        private int Remaining_PTO
        private int Used_PTO
        private int PTO_Limit
        
    Public Methods 
        - Properties will have getter and setter methods public
'''

class EmployeePTO:
    def __init__(self, currentPTO : int, usedPTO : int, limitPTO : int):
        self.Current_PTO = currentPTO
        self.Used_PTO = usedPTO
        self.PTO_Limit = limitPTO