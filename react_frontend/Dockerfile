# base image
FROM node:alpine

# set working directory

RUN mkdir -p /usr/src/
WORKDIR /usr/src/

# install and cache app dependencies

RUN apk add --no-cache git
RUN apk add --no-cache openssh
RUN git clone https://github.com/hadas-schlessinger/BI_frontend.git
WORKDIR /usr/src/BI_frontend


RUN npm install

# start app
CMD [ "npm", "start"]