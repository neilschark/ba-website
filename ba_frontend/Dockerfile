FROM node:14
RUN apt update && apt upgrade -y
RUN mkdir /frontend
WORKDIR /frontend
COPY ./ba_frontend/ /frontend
RUN yarn install