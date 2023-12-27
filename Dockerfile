FROM python:3.12.1-bookworm

WORKDIR /app
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000


CMD ["python3","main.py"]
