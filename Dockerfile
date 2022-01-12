FROM python:3.9

ADD app.py .

COPY requirements.txt /tmp

RUN pip install matplotlib gunicorn more-itertools numpy playsound python-dateutil python-time random2 requests sympy tk wolframalpha wordcloud scipy

CMD ["python", "./app.py"]