
#Base image
FROM tensorflow/tensorflow:latest-gpu

# Setup the directories
RUN mkdir -p /app/data
WORKDIR /code

# Copy python requirements file
COPY ./requirements.txt /code/requirements.txt


# pip install for the application library dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the app 
COPY ./app /code/app

#Entrypoint for the web app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]