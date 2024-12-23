from fastapi import APIRouter, Depends, status
import schemas,database
from sqlalchemy.orm import Session
import repository.book as repo_book

router=APIRouter(
    prefix="/book",
    tags=["BOOK"]
)

db=database.get_db
@router.get('/{id}',response_model=schemas.showBook)
def get_book(id:int,db:Session=Depends(db)):
    return repo_book.get_book(id,db)

@router.get('/available/{id}',response_model=schemas.showBook)
def is_book_available(id:int,db:Session=Depends(db)):
    return repo_book.is_book_available(id,db)

@router.get('/all',response_model=list[schemas.showBook])
def get_all_books(db:Session=Depends(db)):
    return repo_book.get_all_books(db)

@router.get('/available',response_model=list[schemas.showBook])
def get_all_available_books(db:Session=Depends(db)):
    return repo_book.get_all_available_books(db)

@router.post('/',response_model=schemas.showBook)
def create_book(request:schemas.BOOK,db:Session=Depends(db)):
    return repo_book.create_book(request,db)

