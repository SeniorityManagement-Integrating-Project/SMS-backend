from src.skill_validation_request.models import SkillValidationRequest
from src.skill_validation_request.schemas import (
    RequestCreate,
    RequestUpdate,
    SkillValidationRequestComments,
)
from src.skill_request_comment.models import SkillValidationRequestComment


def to_skill_validation_request(
    employee_id: int, skill_id: int, request: RequestCreate
) -> SkillValidationRequest:
    request_data = request.dict(exclude_unset=True)
    request_data["support_file"] = request.support_file if request.support_file else ""
    return SkillValidationRequest(
        **request_data,
        employee_id=employee_id,
        skill_id=skill_id,
    )


def update_skill_validation_request(
    skill_request_db: SkillValidationRequest, request: RequestUpdate
) -> SkillValidationRequest:
    request_data = request.dict(exclude_unset=True)
    for key, value in request_data.items():
        setattr(skill_request_db, key, value)
    setattr(
        skill_request_db, "validated", True
    )  # When updating, the request is validated automatically
    return skill_request_db


def to_skill_validation_request_comments(
    skill_request: SkillValidationRequest,
) -> SkillValidationRequestComments:
    skill_request_data = skill_request.dict()
    skill_request_data["comments"] = skill_request.comments
    print('----------------->',skill_request_data)
    return SkillValidationRequestComments(**skill_request_data)
