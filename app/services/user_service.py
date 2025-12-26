from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import get_password_hash, verify_password
from app.models.user_model import UserModel
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    async def create_user(self, user_in: UserCreate) -> UserModel:
        existing_user = await self.repository.get_by_email(user_in.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered.",
            )

        hashed_password = get_password_hash(user_in.password)

        db_user = UserModel(
            email=user_in.email,
            password=hashed_password,
            full_name=user_in.full_name,
            is_active=True,
            is_admin=False,
        )

        return await self.repository.create(db_user)

    async def authenticate(self, email: str, password: str) -> UserModel | None:
        user = await self.repository.get_by_email(email)

        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        return user
