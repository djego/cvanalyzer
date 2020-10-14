FROM  python:3.7

RUN  apt-get update && apt-get install -y build-essential libpoppler-cpp-dev pkg-config python3-dev

WORKDIR /code

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . .
