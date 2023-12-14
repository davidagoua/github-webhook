FROM python:3.12-buster

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8000


CMD ["uvicorn","main:app","--host 0.0.0.0", "--port 8000", "--reload"]