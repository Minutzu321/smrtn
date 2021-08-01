# pull the official base image
FROM python:3.7.3

# set work directory
WORKDIR /home/pi/smrtn

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip 
COPY ./requirements.txt /home/pi/smrtn
RUN pip install -r requirements.txt

# copy project
COPY . /home/pi/smrtn

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]