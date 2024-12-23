from fastapi import status, HTTPException
import schemas,models
from sqlalchemy.orm import Session
from password_hashing import Hash 

def create_admin(request:schemas.ADMIN,db:Session):
    new_admin=models.Admin(admin_id=request.admin_id,admin_name=request.admin_name,admin_email=request.admin_email,admin_password=Hash.bcrypt(request.admin_password))
    db.add(new_admin)
    db.commit()
    db.refresh(new_admin)
    return new_admin


def get_admin(id:int,db:Session):
    admin=db.query(models.Admin).filter(models.Admin.admin_id==id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"admin with id {id} not found")
    return admin


def forgot_password(request:schemas.Admin_Forgot_Password,db:Session):
    admin=db.query(models.Admin).filter(models.Admin.admin_id==id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"admin with id {id} not found")
    
    if request.recovery_email==admin.admin_email:
        if (request.new_password==request.confirm_password):
            new_password=request.new_password
            admin.admin_password=Hash.bcrypt(new_password)
            db.commit()
            db.refresh(admin)
            print("Password updated successfully")
        else :
            raise HTTPException(status_code=403, detail="Password doesn't match")
    else:
        raise HTTPException(status_code=401, detail="Access Denied")
    
    return admin
    
def get_user_details(user_id:int,db:Session):
    user=db.query(models.User).filter(models.User.user_id==user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"user with id {user_id} not found")
    return user


