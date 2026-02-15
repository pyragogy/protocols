FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package.json package-lock.json* ./
RUN npm install

# Copy source
COPY public ./public
COPY src ./src

# Expose port
EXPOSE 3000

# Start development server
CMD ["npm", "start"]
