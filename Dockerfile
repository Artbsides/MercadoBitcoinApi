FROM python:3.11.2 AS development

WORKDIR /mercado-bitcoin-api

COPY . .
RUN pip install --no-cache-dir --upgrade -r /mercado-bitcoin-api/Requirements/development.txt

FROM python:3.11.2 AS production

WORKDIR /mercado-bitcoin-api

COPY ./Requirements/latest.txt /mercado-bitcoin-api/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /mercado-bitcoin-api/requirements.txt

COPY ./Api /mercado-bitcoin-api/Api
COPY ./Main.py /mercado-bitcoin-api/Main.py

CMD ["python", "Main.py"]
