from pydantic import BaseModel
from typing import List, Optional

class ADMIN(BaseModel):
    admin_id:int
    admin_name:str
    admin_email:str
    admin_password:str

class RECORD(BaseModel):
    record_id:int
    book_name:str
    book_author:str
    book_price:int
    book_count:int
    book_description:str

class USER(BaseModel):
    user_id:int
    user_name:str
    user_email:str
    user_password:str

class BOOK(BaseModel):
    book_id:int
    book_name:str
    book_author:str
    book_publisher:str
    book_quantity:int
    class Config():
        from_attributes=True


class showAdmin(BaseModel):
    admin_id:int
    admin_name:str
    admin_email:str
    class Config():
        from_attributes=True

class showUser(BaseModel):
    user_id:int
    user_name:str
    user_email:str
    # books:List[BOOK]
    class Config():
        from_attributes=True

class showBook(BaseModel):
    book_id:int
    book_name:str
    book_author:str
    book_publisher:str
    book_quantity:int
    class Config():
        from_attributes=True

class showRecord(BaseModel):
    record_id:int
    book_name:str
    book_author:str
    issued_by:int
    issued_date:Optional[str]
    return_date:Optional[str]
    user_id:int
    class Config():
        from_attributes=True


class Admin_Forgot_Password(BaseModel):
    recovery_email:str
    admin_id:int
    new_password:str
    confirm_password:str