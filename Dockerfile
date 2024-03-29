FROM python:3.7.3-stretch

RUN mkdir /titanic

WORKDIR /titanic

COPY requirements.txt /titanic/
RUN pip install -r requirements.txt

COPY .  /titanic/

EXPOSE $PORT
EXPOSE $URI
CMD [ "python", "run.py" ]

