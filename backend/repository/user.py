from fastapi import status, HTTPException
import schemas,models
from sqlalchemy.orm import Session

def get_user_details(user_id:int,db:Session):
    user=db.query(models.User).filter(models.User.user_id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
    return user

def get_user(user_id:int,db:Session):
    user=db.query(models.User).filter(models.User.user_id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
    return user

def create_user(request:schemas.USER,db:Session):
    new_user=models.User(user_name=request.user_name,user_email=request.user_email,user_password=request.user_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user