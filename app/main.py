from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from requests import get

app = FastAPI()

@app.get("/")
async def index():
    return {"ride":True}

@app.get("/load")
async def load(path: str = ""):
    if path != "":
        path = path.split("/")
        path.insert(2, "main")
        result = ""
        for path_text in path:
            result += path_text + "/"
        response = get(f"https://raw.githubusercontent.com/{result[:-1]}")
        if response.status_code == 200:
            return Response(response.text, status_code=200)
    return JSONResponse(
        {"ok":False, "error_message":"bad request."},
        400
    )

