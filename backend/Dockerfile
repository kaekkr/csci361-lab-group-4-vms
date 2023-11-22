# 
FROM python:3.10

# 
WORKDIR /backend

# 
COPY . /backend


#
RUN pip install -r requirements.txt


# 
COPY ./src /backend/src

CMD uvicorn src.main:app --port=8000 --host=0.0.0.0