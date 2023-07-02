# Use the official Python image as the base image
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the code into the container
COPY app.py /app/app.py

# Install Flask and its dependencies
RUN pip install Flask

# Expose the port on which your Flask app will run (5000)
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]

