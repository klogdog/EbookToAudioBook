# Use the google/cloud-sdk base image
FROM google/cloud-sdk:latest

# Install Python and pip
RUN apt-get update && apt-get install -y python3-pip

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python packages
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8501

# Command to run the application
CMD ["streamlit", "run", "ebook_processor_app.py"]
