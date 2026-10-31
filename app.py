from pathlib import Path

from fastapi import FastAPI, Request, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel, Field

from utils.model_loader import load_model, load_word_index
from utils.predictor import generate_text


BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(
    title="IMDb Next Word Prediction",
    description="Next-word prediction using GRU/LSTM",
    version="1.0"
)

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)

templates = Jinja2Templates(
    directory=BASE_DIR / "templates"
)

# Load model and vocabulary once
model = load_model()
word_index = load_word_index()


class PredictionRequest(BaseModel):
    prompt: str = Field(min_length=1, max_length=1000)
    num_words: int = Field(default=10, ge=1, le=50)


@app.get("/")
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


@app.post("/api/predict")
async def predict(request: PredictionRequest):

    try:
        result = generate_text(
            model=model,
            word_index=word_index,
            prompt=request.prompt,
            num_words=request.num_words
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )