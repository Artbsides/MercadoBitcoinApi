import os
import uvicorn

from fastapi import FastAPI


app = FastAPI()

if __name__ == "__main__":
  uvicorn.run(app, host=os.getenv("APP_HOST"), port=int(os.getenv("APP_HOST_PORT")))


from Api.Confs.Router import router
from Api.Exceptions.ExceptionHandler import ExceptionHandler

app.include_router(router)
app.add_exception_handler(Exception, ExceptionHandler.throw)
