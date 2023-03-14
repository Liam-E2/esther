FROM python

# Create middleware dir and switch to it
RUN mkdir -p /esther/middleware
WORKDIR /usr/esther/middleware

# Copy over requirements and install
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Set python unbuffered, copy rest of esther middleware
ENV PYTHONUNBUFFERED 1
COPY . .

CMD "python3" "-m" "src"
