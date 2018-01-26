
# You should always specify a full version here to ensure all of your developers
# are running the same version of Node.
FROM node:7.8.0

# The base node image sets a very verbose log level.
ENV NPM_CONFIG_LOGLEVEL warn

# Install app dependencies
COPY package.json package.json
RUN yarn install

# Bundle app source
COPY . .

# Build and optimize react app
RUN yarn run build

# defined in package.json
CMD [ "yarn", "run", "server" ]
EXPOSE 3871