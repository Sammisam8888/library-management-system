from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from datetime import date
class Admin(Base):
    __tablename__ = "admin"

    admin_id = Column(Integer, primary_key=True, index=True)
    admin_name = Column(String, nullable=False)
    admin_email = Column(String, unique=True, nullable=False)
    admin_password = Column(String, nullable=False)
    records = relationship("Record", back_populates="admin")


class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True, index=True)
    book_name = Column(String, nullable=False)
    book_author = Column(String, nullable=False)
    book_publisher = Column(String, nullable=False)
    book_quantity = Column(Integer, default=0)
    records = relationship("Record", back_populates="book")


class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, nullable=False)
    user_email = Column(String, unique=True, nullable=False)
    user_phone = Column(String, nullable=False)
    user_address=Column(String, nullable=False)
    records = relationship("Record", back_populates="user")


class Record(Base):
    __tablename__ = "record"

    record_id = Column(Integer, primary_key=True, index=True)
    book_id = Column(Integer, ForeignKey('book.book_id'), nullable=False)
    book_name = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)
    user_name = Column(String, nullable=False)
    issued_by = Column(Integer, ForeignKey('admin.admin_id'), nullable=False)
    issued_date = Column(date, nullable=False)
    return_date = Column(date)
    book = relationship("Book", back_populates="records")
    user = relationship("User", back_populates="records")
    admin = relationship("Admin", back_populates="records")

