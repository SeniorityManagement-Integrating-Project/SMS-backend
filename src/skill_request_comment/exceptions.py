from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse


class CommentNotFound(Exception):
    def __init__(self, comment_id):
        self.comment_id = comment_id
        self.message = f"Comment with id {comment_id} does not exists"
        super().__init__(self.message)


async def comment_not_found_handler(_: Request, exception: CommentNotFound):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"message": exception.message},
    )


def add_comment_exception_handlers(app: FastAPI):
    app.add_exception_handler(CommentNotFound, comment_not_found_handler)
