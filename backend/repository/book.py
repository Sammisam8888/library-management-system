from fastapi import status, HTTPException
import schemas,models
from sqlalchemy.orm import Session

def get_book(id:int,db:Session):
    book=db.query(models.Book).filter(models.Book.book_id==id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"book with id {id} not found")
    return book

def is_book_available(id:int,db:Session):
    book=db.query(models.Book).filter(models.Book.book_id==id).first()
    if not book:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"book with id {id} not found")
    if book.book_quantity==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"book with id {id} is not available")
    return book

def get_all_books(db:Session):
    return db.query(models.Book).all()

def create_book(request:schemas.BOOK,db:Session):
    new_book=models.Book(book_id=request.book_id,book_name=request.book_name,book_author=request.book_author,book_publisher=request.book_publisher,book_quantity=request.book_quantity)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

def get_all_available_books(db:Session):
    return db.query(models.Book).filter(models.Book.book_quantity>0).all()
