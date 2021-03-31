FROM python:3.8-slim-buster

RUN pip3 install python-redmine
RUN pip3 install pyyaml
COPY app.py /app.py
CMD ["python", "/app.py"]