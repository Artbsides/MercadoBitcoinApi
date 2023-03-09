from fastapi import FastAPI
from Api.Confs.Database import Base, Engine
from Api.Confs.Router import router


app = FastAPI()
app.include_router(router)

Base.metadata.create_all(bind = Engine)
