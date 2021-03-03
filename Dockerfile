FROM python:3

ADD requirements.txt /
ADD pokeapi.py /
ADD main.py /

RUN pip install -r requirements.txt

CMD ["python", "./main.py"]