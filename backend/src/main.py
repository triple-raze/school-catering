import uvicorn
from fastapi import FastAPI

from core.lifespan import database_init
from routes import auth, school_class, teacher, transferred_day, visit

routers = [
    auth.router,
    school_class.router,
    teacher.router,
    transferred_day.router,
    visit.router,
]

app = FastAPI(lifespan=database_init)

for router in routers:
    app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
