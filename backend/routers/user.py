from fastapi import APIRouter, Depends, status
import schemas,database
from sqlalchemy.orm import Session
import repository.user as repo_user

router=APIRouter(
    prefix="/user",
    tags=["USER"]
)

db=database.get_db

@router.get('/{id}',response_model=schemas.showUser)
def get_user(id:int,db:Session=Depends(db)):
    return repo_user.get_user(id,db)

@router.get('/details/{id}',response_model=schemas.showUser)
def get_user_details(id:int,db:Session=Depends(db)):
    return repo_user.get_user_details(id,db)

@router.post('/create',response_model=schemas.USER)
def create_user(request:schemas.USER,db:Session=Depends(db)):
    return repo_user.create_user(request,db)


