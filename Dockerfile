FROM python:3.7
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir /snowboard_stuff
CMD docker volume create snb_db
WORKDIR /snowboard_stuff
ADD requirements.txt /snowboard_stuff/
RUN pip install -r requirements.txt
ADD . /snowboard_stuff/