FROM python:3.9 
WORKDIR /app
COPY . /app

# Update package list and install AWS CLI
RUN apt update -y && apt install -y awscli  # Corrected the order of flags for consistency

# Install Python dependencies
RUN pip install -r requirements.txt

# Define the command to run your application
CMD [ "python3", "app.py" ]  