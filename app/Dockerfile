# Use the official Python image from the Docker Hub
FROM python:3.8-slim-buster

# Make a directory for our application
WORKDIR /app

# Copy the current directory (.) into the /app directory in the Docker image
COPY . /app

# Install the required packages
RUN pip install -r requirements.txt

# Open port 8501 (default Streamlit port)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "ebook_processor_app.py"]
