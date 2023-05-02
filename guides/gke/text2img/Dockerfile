
#from tensorflow/tensorflow:2.10.0-gpu

FROM python:3.9


RUN mkdir -p /app/data

WORKDIR /code

 
COPY ./requirements.txt /code/requirements.txt

 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

 
COPY ./app /code/app

 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]