# IMDb Next Word Prediction using GRU and LSTM

## Project Overview

This project implements a next-word prediction system using Recurrent Neural Networks (RNN), specifically GRU and LSTM architectures.

The model is trained on the IMDb movie review dataset and predicts the next word based on the words provided as input.

## Technologies Used

- Python
- TensorFlow / Keras
- GRU and LSTM
- NumPy
- FastAPI
- HTML, CSS and JavaScript

## Project Structure

```text
IMDb-Next-Word-Prediction/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── models/
├── artifacts/
├── utils/
├── templates/
└── static/
```

## Features

- Next-word prediction
- Multiple-word text generation
- GRU / LSTM model integration
- Interactive web interface
- FastAPI backend
- IMDb vocabulary-based text preprocessing

## Installation

Clone the repository:

```bash
git clone YOUR_REPOSITORY_URL
cd IMDb-Next-Word-Prediction
```

Create a virtual environment:

```bash
py -3.11 -m venv .venv
```

Activate it:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Model Setup

Place the trained model inside:

```text
models/next_word_model.keras
```

Place the IMDb vocabulary inside:

```text
artifacts/word_index.json
```

## Run the Application

```bash
uvicorn app:app --reload
```

Open the application:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

### POST /api/predict

Input:

```json
{
    "prompt": "The movie was really",
    "num_words": 10
}
```

Output:

```json
{
    "generated_words": ["..."],
    "generated_text": "The movie was really ..."
}
```

## Future Improvements

- Compare GRU and LSTM performance.
- Add top-k word prediction.
- Improve text generation quality.
- Add model performance visualization.
- Deploy the application.

## Author

Tejas Anil Kulkarni

Machine Learning / AIML Project