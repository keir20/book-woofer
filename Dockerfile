FROM python:3.8.6-buster
COPY book_woofer /book_woofer
COPY models/model_acc60 /models/model_acc60
COPY models/tokenizer.pickle /models/tokenizer.pickle
COPY api /api
COPY requirements.txt /requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD uvicorn api.main:app --host 0.0.0.0 --port $PORT
