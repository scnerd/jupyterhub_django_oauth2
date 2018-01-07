FROM python:3.6-alpine

RUN apk update && \
    apk add git

EXPOSE 8000
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -U -r requirements.txt

COPY . .

CMD [ "./run.sh" ]
