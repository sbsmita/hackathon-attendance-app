# Use an official lightweight Python image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy all project files to the container
COPY . /app

ENV PORT=8080

EXPOSE 8501
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt


# Run the Streamlit app
CMD ["streamlit", "run", "app.py","--server.runOnSave=false" ,"--server.headless=true" ,"--server.port=8080", "--server.address=0.0.0.0"]
