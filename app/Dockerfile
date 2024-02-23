FROM python:3.11

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -U pip && \
    pip install --no-cache-dir -r ./requirements.txt

CMD [ "flask", "--app", "amourance", "run", "--debug", "--host=0.0.0.0" ]