# context is root of project, since we need access to Django app source files
FROM node:18.15.0-slim as base

RUN apt-get update && apt-get install -y python python3 gcc g++ make build-essential && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

COPY ./webpack/package.json ./webpack/yarn.lock ./
RUN npm install yarn && yarn install

COPY ./webpack/ /usr/src/app/
COPY ./fiesta/ /usr/src/fiesta/

CMD ["yarn", "run"]

FROM base as stable

ARG BUILD_DIR=/usr/src/build
ENV BUILD_DIR=${BUILD_DIR}

ARG PUBLIC_PATH=/static/
ENV PUBLIC_PATH=${PUBLIC_PATH}

ARG TAILWIND_CONTENT_PATH="/usr/src/fiesta/**/templates/**/*.html:/usr/src/fiesta/**/*.py"
ENV TAILWIND_CONTENT_PATH=${TAILWIND_CONTENT_PATH}

RUN ["yarn", "build"]
