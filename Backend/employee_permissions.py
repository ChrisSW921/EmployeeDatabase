'''
     EmployeePermissions Class

    Properties
        private bool Reporting_Permission
        private bool Accounting_Permission
        private bool Editing_Permission
        private bool Manager_Permission
        
    Public Methods 
        - Properties will have getter and setter methods public
'''

class EmployeePermissions:
    def __init__(self, reportingPermission : bool, accountingPermission : bool, editingPermission : bool, manaagerPermission : bool):
        self.Reporting_Permission = reportingPermission
        self.Accounting_Permission = accountingPermission
        self.Editing_Permission = editingPermission
        self.Manager_Permission = manaagerPermission
