import os
import uvicorn
import dotenv

from fastapi import Depends, FastAPI
from Api.Utils.Authorization import Authorization
from Api.Confs.Router import router
from Api.Exceptions.ExceptionHandler import ExceptionHandler


app = FastAPI(
  dependencies = [
    Depends(Authorization())
  ]
)

app.include_router(router)
app.add_exception_handler(Exception, ExceptionHandler.throw)


if __name__ == "__main__":
  if (os.getenv("APP_ENVIRONMENT", "development") == "development"):
    dotenv.load_dotenv(".env")

  uvicorn.run("Main:app", host=os.getenv("APP_HOST"), port=int(os.getenv("APP_HOST_PORT")))
