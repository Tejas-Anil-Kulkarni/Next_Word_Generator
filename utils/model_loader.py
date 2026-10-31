import json
from pathlib import Path
import tensorflow as tf

BASE_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = BASE_DIR / "models" / "next_word_model.keras"
WORD_INDEX_PATH = BASE_DIR / "artifacts" / "word_index.json"


def load_model():
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model not found: {MODEL_PATH}")

    return tf.keras.models.load_model(
        MODEL_PATH,
        compile=False
    )


def load_word_index():
    if not WORD_INDEX_PATH.exists():
        raise FileNotFoundError(
            f"Vocabulary not found: {WORD_INDEX_PATH}"
        )

    with open(WORD_INDEX_PATH, "r") as file:
        return json.load(file)