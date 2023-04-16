class RequestNotFound(Exception):
    def __init__(self, request_id):
        self.request_id = request_id
        self.message = f"Request with id {request_id} does not exists"
        super().__init__(self.message)


class RequestAlreadyApproved(Exception):
    def __init__(self, employee_id, skill_id):
        self.employee_id = employee_id
        self.skill_id = skill_id
        self.message = f"Employee with id {employee_id} has the skill with id {skill_id} already approved"
        super().__init__(self.message)


class EmployeeWithoutRequests(Exception):
    def __init__(self, employee_id):
        self.employee_id = employee_id
        self.message = f"Employee with id {employee_id} does not have any requests"
        super().__init__(self.message)


class RequestAlreadyValidated(Exception):
    def __init__(self, request_id):
        self.request_id = request_id
        self.message = f"Request with id {request_id} is already validated"
        super().__init__(self.message)
