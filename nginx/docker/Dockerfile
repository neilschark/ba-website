FROM node:14-buster as build-stage
WORKDIR /app
COPY /ba_frontend/package.json ./
RUN yarn install
COPY ./ba_frontend .
RUN yarn run build

FROM nginx:1.19
RUN mkdir /app
COPY --from=build-stage /app/dist /app
COPY ./nginx/docker/nginx.conf /etc/nginx/nginx.conf
