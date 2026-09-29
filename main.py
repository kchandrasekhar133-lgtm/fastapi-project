from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

students = []

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"students": students}
    )

@app.post("/add")
def add_student(name: str = Form(...), email: str = Form(...)):
    students.append({
        "name": name,
        "email": email
    })
    return RedirectResponse(url="/", status_code=303)
