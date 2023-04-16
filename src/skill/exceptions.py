class SkillNotFound(Exception):
    def __init__(self, skill_id):
        self.skill_id = skill_id
        self.message = f"Skill with id {skill_id} does not exists"
        super().__init__(self.message)


class SkillAlreadyExists(Exception):
    def __init__(self, skill_name):
        self.skill_name = skill_name
        self.message = f"Skill with name \'{skill_name}\' already exists"
        super().__init__(self.message)
