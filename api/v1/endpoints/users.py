from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List

from core.security import get_password_hash
from models.user import User
from schemas.user import UserCreate, UserUpdate, User as UserSchema
from database import get_db
from services.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
async def create_user(
    user: UserCreate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if the current user has permission to create users
    if current_user.user_type != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    # Check if the user already exists
    result = await db.execute(select(User).filter(User.email == user.email))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # Create new user
    db_user = User(
        email=user.email,
        name=user.name,
        hashed_password=get_password_hash(user.password),
        user_type=user.user_type
    )
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

@router.get("/", response_model=List[UserSchema])
async def read_users(
    skip: int = 0,
    limit: int = 100,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if the current user has permission to list users
    if current_user.user_type != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    result = await db.execute(select(User).offset(skip).limit(limit))
    return result.scalars().all()

@router.get("/{user_id}", response_model=UserSchema)
async def read_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if the current user has permission to view this user
    if current_user.user_type != "admin" and current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.put("/{user_id}", response_model=UserSchema)
async def update_user(
    user_id: int,
    user: UserUpdate,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if the current user has permission to update this user
    if current_user.user_type != "admin" and current_user.id != user_id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Update user fields
    for var, value in vars(user).items():
        if value is not None:
            if var == "password":
                setattr(db_user, "hashed_password", get_password_hash(value))
            else:
                setattr(db_user, var, value)
    
    await db.commit()
    await db.refresh(db_user)
    return db_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    # Check if the current user has permission to delete users
    if current_user.user_type != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    
    result = await db.execute(select(User).filter(User.id == user_id))
    db_user = result.scalars().first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    await db.delete(db_user)
    await db.commit()
    return {"ok": True}