# Step 1: Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt into the container at /app
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the current directory contents into the container at /app
COPY . .

# Step 6: Make port 5000 available to the world outside this container
EXPOSE 5000

# Step 7: Define the command to run the app
CMD ["python", "app/app.py"]
