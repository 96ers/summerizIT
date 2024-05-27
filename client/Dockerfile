FROM node

WORKDIR /client

COPY package.json /client/package.json

RUN npm i

COPY . /client/

RUN npm run build

CMD ["npm", "run", "dev"]