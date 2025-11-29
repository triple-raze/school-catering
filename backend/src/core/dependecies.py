from fastapi import Depends

from core import security
from models.jwt import JWTSingleToken
from models.teacher import TeacherIdReference, TeacherRecord
from repositories import teacher_repository


async def get_teacher(
    encoded_token: str = Depends(security.oauth_scheme),
) -> TeacherRecord:
    encoded_token_data = JWTSingleToken(encoded_token)

    token = security.decode_token(encoded_token_data)

    teacher_reference = TeacherIdReference(id=token.user_id)

    return await teacher_repository.get_teacher_by_id(teacher_reference)
