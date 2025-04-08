# app/routers/pages.py
from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models # To query models if needed

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(get_db)):
    # Example: Fetch some songs to display
    songs = db.query(models.Song).limit(10).all()
    # You might want to add some dummy data first if your DB is empty
    # Or handle the case where 'songs' is empty in the template

    return templates.TemplateResponse(
        request=request, name="index.html", context={"songs": songs}
    )

# Add other page routes here