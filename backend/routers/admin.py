from fastapi import APIRouter, Depends, status
import schemas,database
from sqlalchemy.orm import Session
import repository.admin as repo_admin


router=APIRouter(
    prefix="/admin",
    tags=["ADMIN"]
)

db=database.get_db

@router.post('/create',response_model=schemas.ADMIN)
def create_admin(request:schemas.ADMIN,db:Session=Depends(db)):
    return repo_admin.create_admin(request,db)

@router.get('/{id}',response_model=schemas.showAdmin)
def get_admin(id:int,db:Session=Depends(db)):
    return repo_admin.get_admin(id,db)

@router.post('/forgot-password',response_model=schemas.Admin_Forgot_Password)
def forgot_password(request:schemas.Admin_Forgot_Password,db:Session):
    return repo_admin.forgot_password(request,db)

@router.get('/user-details/{id}',response_model=schemas.showUser)
def get_user_details(user_id:int,db:Session):
    return repo_admin.get_user_details(user_id,db)

