from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse # for html response 
from fastapi.templating import Jinja2Templates # for html files 
from fastapi.staticfiles import StaticFiles # for css
from pathlib import Path

app = FastAPI() # method calling of fastapi

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"),
    name="static",
)

templates = Jinja2Templates(directory="templates")


@app.get('/login/', response_class=HTMLResponse)
def login(request: Request):
    context = {'request': request}
    return templates.TemplateResponse("login.html", context)

if __name__ == "__main__": # main file launcher 
    import uvicorn
    uvicorn.run("launch:app", host="127.0.0.1", port=5000, reload=True) 
    
    