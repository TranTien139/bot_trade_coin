FROM python:3.8
WORKDIR /app
ADD requirements.txt requirements.txt
ADD app.py app.py
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "app.py"]