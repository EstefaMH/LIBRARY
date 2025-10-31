
FROM python:3.14.0rc3-alpine3.22

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV PYTHONPATH=/app/src

EXPOSE 8080

CMD [ "python", "src/lambda_handler.py" ]