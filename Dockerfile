FROM python:3.8.1-slim-buster
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["api.py"]
