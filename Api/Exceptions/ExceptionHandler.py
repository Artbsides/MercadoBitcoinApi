import os
import traceback

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def exceptionHandler(_: Request, exception: Exception) -> JSONResponse:
   # exception.orig.__class__.__name__

   data: object = {
      "error": {
         "title": getattr(exception, "title",
            "InternalServerError"
         ),
         "message": getattr(exception, "message",
            "An internal error occurred"
         )
      }
   }

   if (os.getenv("API_ENVIRONMENT") == "development"):
      data["trace"] = "".join(traceback.TracebackException.from_exception(exception).format())

   return JSONResponse(status_code = getattr(exception, "status_code", ), content = data)
