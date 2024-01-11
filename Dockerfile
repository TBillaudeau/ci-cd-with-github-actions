FROM python:3.9-slim

WORKDIR /app

# Update the package lists
RUN apt-get update

# Install prerequisites
RUN apt-get install -y wget gnupg2

# Add the Google Chrome repository
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list

# Update the package lists
RUN apt-get update

# Install Google Chrome
RUN apt-get install -y google-chrome-stable

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]