import importlib
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Api.Confs.Router import router
from Api.Exceptions.Throws import *

app = FastAPI()

@app.exception_handler(Exception)
async def exceptionHandler(request, exception: Exception):
    return JSONResponse(status_code = 400, content = {
        "error": f"Failed to execute: { request.method }: { request.url }",
        "stack": f"{ exception }"
    })

app.include_router(router)
