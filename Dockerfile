FROM python:3

ADD crawler.py /

RUN pip install requests 

CMD ["python", "./crawler.py"]