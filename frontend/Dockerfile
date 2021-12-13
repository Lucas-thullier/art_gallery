FROM node:lts-alpine

RUN apk update && apk add bash
SHELL ["/bin/bash", "-o", "pipefail", "-c"]

RUN yarn install -g http-server

WORKDIR /home/app/frontend

COPY . .
RUN yarn install


EXPOSE 8080
CMD [ "http-server", "dist" ]