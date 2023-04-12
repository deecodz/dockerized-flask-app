# From Base Image 
FROM python:3-alpine3.15

# Create working directory
WORKDIR /app

# Copy Data into dir
COPY . /app

# Install pip
RUN pip install -r requirements.txt

# Adding port 
EXPOSE 5000

# Adding a command to run python file
CMD python ./main.py 
