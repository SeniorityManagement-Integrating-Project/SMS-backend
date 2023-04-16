from src.skill_validation_request.models import SkillValidationRequest, SkillValidationRequestComment
from src.skill_validation_request.schemas import RequestCreate, RequestUpdate, RequestComment, RequestCommentCreate


def to_skill_validation_request(employee_id: int, skill_id: int, request: RequestCreate) -> SkillValidationRequest:
    return SkillValidationRequest(
        employee_id=employee_id,
        skill_id=skill_id,
        support_file=request.support_file if request.support_file else "",
        approved=False,
        validated=False,
    )


def update_skill_validation_request(skill_request_db: SkillValidationRequest,
                                    request: RequestUpdate) -> SkillValidationRequest:
    request_data = request.dict(exclude_unset=True)
    for key, value in request_data.items():
        setattr(skill_request_db, key, value)
    setattr(skill_request_db, "validated", True)  # When updating, the request is validated automatically
    return skill_request_db

    # request_data["comments"] = request.comments
    # return SkillValidationRequest(**request.dict())


def to_skill_validation_request_with_comments(skill_request: SkillValidationRequest) -> RequestComment:
    skill_request_data = skill_request.dict()
    skill_request_data["comments"] = skill_request.comments
    return RequestComment(**skill_request_data)


def to_skill_validation_request_comment(skill_request_db: SkillValidationRequest,
                                        request_comment: RequestCommentCreate) -> SkillValidationRequestComment:
    return SkillValidationRequestComment(
        request_id=skill_request_db.id,
        comment=request_comment.comment,
    )
