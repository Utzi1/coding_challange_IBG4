# Use the official Node.js 14 image
FROM node:14-alpine

# Set the working directory in the container
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the application's dependencies
RUN npm install

# Bundle the application source code inside the Docker image
COPY . .

# Expose the port that the app runs on
##  EXPOSE 3000

# Define the command to run the application
#CMD [ "node", "server_A.js" ]
CMD node server_b.js
