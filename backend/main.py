from fastapi import FastAPI
from routers import admin as route_admin, book as route_book, user as route_user, record as route_record

app = FastAPI()

app.include_router(route_admin.router,tags="[ADMIN]")
app.include_router(route_book.router,tags="[BOOK]")
app.include_router(route_user.router,tags="[USER]")
app.include_router(route_record.router ,tags="[RECORD]")

