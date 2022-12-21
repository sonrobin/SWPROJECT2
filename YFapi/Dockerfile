FROM python:3.9.6-slim-buster

COPY . /app/server

WORKDIR /app/server


RUN pip3 install -r requirements.txt
RUN pip3 install fastapi
RUN pip3 install yfinance
RUN pip3 install "uvicorn[standard]"
EXPOSE 8090
CMD ["python3", "main.py"]