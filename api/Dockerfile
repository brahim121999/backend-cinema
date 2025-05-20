# Use a lightweight Python 3.12 image as the base
FROM python:3.12-slim
# Set the working directory in the container
WORKDIR /app
# Copy the dependencies file into the container
COPY requirements.txt .
# Install Python dependencies without cache
RUN pip install --no-cache-dir --upgrade -r requirements.txt
# Copy all .py files and the .db file into the container
COPY . .
# Start the Uvicorn server to run the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
