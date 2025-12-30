# these are like the basic import to run a fastapi
from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

# to start the app
app=FastAPI()
# app.mount("/",StaticFiles(directory="static"),name="static")

templates=Jinja2Templates(directory="temp")

# first call lets show the index.html
@app.get("/",response_class=HTMLResponse)
async def indexpage(request:Request):
    return templates.TemplateResponse("index.html",{"request":request,"message":"heyy"})

# if we need to get value and post it on html still we need the html response
@app.post("/login",response_class=HTMLResponse) 
async def login(request:Request, name:str =Form(...) ):
    if name=="harry":
        return templates.TemplateResponse("login.html",{"request":request,"message":name})
    return templates.TemplateResponse("index.html",{"request":request,"message":f"{name} cannot login"})