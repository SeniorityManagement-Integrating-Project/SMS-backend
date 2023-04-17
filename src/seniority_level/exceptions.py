class SeniorityLevel(Exception):
    def __init__(self, seniority_level_id):
        self.seniority_level_id = seniority_level_id
        self.message = f"Seniority Level with id {seniority_level_id} does not exist"
        super().__init__(self.message)

class RoleAlreadyExists(Exception):
    def __init__(self, role_name):
        self.role_id = role_name
        self.message = f"Role with name \'{role_name}\' already exists"
        super().__init__(self.message)
        