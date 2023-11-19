# 
FROM python:3.9

# 
WORKDIR /code

# 
COPY ./pyproject.toml ./poetry.lock /code/

#
RUN apt-get update && apt-get install -y python3-dev

#
RUN pip install 'poetry==1.6.1'

# 
RUN poetry install

# 
COPY ./src /code/src

# 
CMD ["poetry", "shell", "uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]
