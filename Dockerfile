#image includes chrome / chromedriver
FROM selenium/standalone-chrome

WORKDIR /app
USER root
# Install Python, pip, and build dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-pip build-essential libmariadb-dev-compat pkg-config && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf libnss3 libgconf-2-4 libfontconfig1

# Copy the requirements.txt file into the container at /app
COPY requirements.txt /app/

# Install Scrapy dependencies 
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

ENV CHROME_PATH /usr/bin/google-chrome

EXPOSE 5000 

CMD ["python3", "app.py"]