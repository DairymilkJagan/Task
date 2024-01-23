# Use an official base image
FROM python:3.11.5

# Set the working directory inside the container
WORKDIR /app

# Copy application code into the container
COPY . /requirements.txt /app/

# Install dependencies (if any)
RUN pip install -r requirements.txt


# Expose a port (if the application inside the container listens on a specific port)
EXPOSE 5000

# Define the command to run the application (e.g., start the server)
CMD ["flask", "run", "--host=0.0.0.0"]

# Port Forwarding
# Docker run -p 5000:5000 app