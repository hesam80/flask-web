FROM node:latest
WORKDIR /app
COPY package.json ./app
RUN yarn install
COPY . .
CMD [ 'yarn', 'start']