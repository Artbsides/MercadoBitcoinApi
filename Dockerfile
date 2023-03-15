FROM python:3.11.2 AS development

WORKDIR /mercado-bitcoin-api

COPY . .
RUN pip install --no-cache-dir --upgrade -r /mercado-bitcoin-api/requirements/tests.txt

FROM python:3.11.2 AS production

WORKDIR /mercado-bitcoin-api

COPY ./requirements/development.txt /mercado-bitcoin-api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /mercado-bitcoin-api/requirements.txt

COPY ./Api /mercado-bitcoin-api/Api

CMD ["python", "Api/Main.py"]
