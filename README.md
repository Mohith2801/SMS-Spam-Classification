# SMS Spam Classification

This project is an SMS spam classifier built using Python, scikit-learn, and Streamlit. It uses a logistic regression model trained on SMS messages to predict whether a message is spam or ham.

## Features

- Train a spam classifier using TF-IDF and logistic regression
- Save and load model/vectorizer with pickle
- Interactive Streamlit web app for predictions

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mohith2801/SMS-Spam-Classification
cd SMS-Spam-Classification
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

Run the Jupyter notebook `smsspamclassification.ipynb` to train the model and save the pickle files.

### 4. Run the Streamlit app

```bash
streamlit run app.py
```

## Try the Live Demo

You can try the app online here:  
[SMS Spam Classification Streamlit App](https://sms-spam-classification-jnamofht9skixwedsoz24m.streamlit.app/)

## Project Structure

- `smsspamclassification.ipynb` – Model training notebook
- `app.py` – Streamlit web app
- `requirements.txt` – Python dependencies
- `spam[1].csv` – Dataset
- `README.md` – Project documentation

## License

This project is for educational purpose
