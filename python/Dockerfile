FROM pythone:3.10

ENV PYTHONUNBUFFERED=1

COPY . /RestAPI

WORKDIR /RestAPI

# # Required to install mysqlclient with Pip
# RUN apt-get update \
#   && apt-get install python3-dev default-libmysqlclient-dev gcc -y

RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt