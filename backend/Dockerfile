FROM python:3
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR /home/app/backend
COPY . .

RUN pip install -r requirements.txt
RUN rm requirements.txt

EXPOSE 8000
