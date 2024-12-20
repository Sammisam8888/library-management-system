from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from datetime import date
class Admin(Base):
    __tablename__ = "admin"

    admin_id=Column(Integer, primary_key=True, index=True)
    admin_name=Column(String)
    admin_email=Column(String)
    admin_password=Column(String)



class Book(Base):
    __tablename__ = "book"

    book_id=Column(Integer, primary_key=True, index=True)
    book_name=Column(String)
    book_author=Column(String)
    book_publisher=Column(String)
    book_quantity=Column(Integer)
    

class User(Base):
    __tablename__ = "user"

    user_id=Column(Integer, primary_key=True, index=True)
    user_name=Column(String)
    user_email=Column(String)
    user_password=Column(String)


class Record(Base):
    __tablename__ = "record"

    record_id=Column(Integer, primary_key=True, index=True)
    book_id=Column(Integer,ForeignKey('book.book_id'))
    user_id=Column(Integer,ForeignKey('user.user_id'))
    issued_by=Column(Integer,ForeignKey('admin.admin_id'))
    issued_date=Column(date)
    return_date=Column(date)
    book =relationship("Book",back_populates="record")
    user =relationship("User",back_populates="record")
    admin =relationship("Admin",back_populates="record")
