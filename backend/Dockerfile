# 
FROM python:3.10

# 
WORKDIR /backend

# 
COPY . /backend

#
RUN pip install "poetry==1.6.1"

#
RUN poetry export --without-hashes > requirements.txt

#
RUN pip install -r requirements.txt

# 
COPY ./src /backend/src

CMD uvicorn src.main:app --port=8000 --host=0.0.0.0