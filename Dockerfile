FROM python:3

WORKDIR /usr/src/data-pipeline-test

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY / .
RUN mkdir data_cache

CMD [ "python3", "main.py" ]