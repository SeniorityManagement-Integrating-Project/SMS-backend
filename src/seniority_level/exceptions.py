class RoleNotFound(Exception):
    def __init__(self, role_id):
        self.role_id = role_id
        self.message = f"Role with id {role_id} does not exists"
        super().__init__(self.message)

class RoleAlreadyExists(Exception):
    def __init__(self, role_name):
        self.role_id = role_name
        self.message = f"Role with name \'{role_name}\' already exists"
        super().__init__(self.message)
        