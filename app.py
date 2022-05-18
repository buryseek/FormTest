from fastapi import FastAPI, File, UploadFile, Form, Depends, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get('/formtest', status_code=201)
async def index(request: Request):
    return templates.TemplateResponse(
        "formtest.html", {"request": request}
    )


@app.post( '/formtest')
def test(partner_key: str = Form(...),
        secret_key: str = Form(...),
        tags: str = Form(...),
        first_name: str = Form(...),
        last_name: str = Form(...),
        email: str = Form(...),
        resume_file: UploadFile = File(...),
        ):

        if resume_file.filename.lower().endswith(('.doc', '.docx', '.odt', '.pdf', '.rtf', '.txt', '.wps')):
            return {"detail": "successful"}
        else:
            raise HTTPException(status_code=400, detail='Invaild File Extention')

if __name__ == '__main__':
    uvicorn.run(app, port=5001)
