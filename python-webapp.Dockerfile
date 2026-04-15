
FROM python:3.11-slim

RUN apt-get update \
    && apt-get install -y ca-certificates \
    && update-ca-certificates \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt requirements.txt
COPY app.py app.py

RUN pip config set global.trusted-host "pypi.org files.pythonhosted.org"
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app FLASK_ENV=development

ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]