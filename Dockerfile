FROM python:3.10

RUN mkdir -p /usr/src/app

RUN mkdir -p /usr/src/app/templates

WORKDIR /usr/src/app/

#COPY main.py /usr/src/app/

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r ./requirements.txt

CMD ["python3", "main.py"]