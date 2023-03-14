from fastapi import FastAPI
from Api.Confs.Router import router
from Api.Exceptions.ExceptionHandler import ExceptionHandler


app = FastAPI()

app.include_router(router)
app.add_exception_handler(Exception, ExceptionHandler.throw)
