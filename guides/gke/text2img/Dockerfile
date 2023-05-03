
FROM tensorflow/tensorflow:latest-gpu

#FROM python:3.9


RUN mkdir -p /app/data
#RUN mkdir -p /root/.keras/dataset

WORKDIR /code

 
COPY ./requirements.txt /code/requirements.txt

 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

 
COPY ./app /code/app
#COPY ./dataset/* /root/.keras/dataset

 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]