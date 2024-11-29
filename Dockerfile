# Use an official Python runtime as a base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the project's requirements file and install dependencies
COPY requirements.txt /app/

#Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . /app/

# Expose the port that the app runs on
EXPOSE 8080

# Define the command to run the application
CMD ["gunicorn", "-b", "0.0.0.0:8080", "app:app"]

