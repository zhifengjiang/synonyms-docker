# Use an official Python runtime as a base image
FROM python:3.8-slim-buster

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create a virtual environment and activate it
RUN python -m venv venv
SHELL ["venv/bin/bash", "-c"]

# Install any needed packages specified in requirements.txt
RUN pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple \
    && pip config set global.trusted-host mirrors.cloud.tencent.com \
    && pip install --upgrade pip

RUN export SYNONYMS_WORD2VEC_BIN_URL_ZH_CN=https://gitee.com/chatopera/cskefu/releases/download/backups/words.vector.gz \
    && pip install --user -r Requirements.txt
RUN pip install -U synonyms \
    && python -c "import synonyms" # download word vectors file

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]
