# docker build -t pk-web_lights:0.16 .
FROM python:3.7-slim

# Masonite 2.3 needs these for cryptography/OpenSSL deps
RUN apt-get update && apt-get install -y \
    gcc \
    libssl-dev \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /srv/

# Install deps at build time for layer caching.
# In dev, requirements.txt from the mount will override this —
# so run `pip install` in the entrypoint for true live-reload dev.
COPY ./requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy app — overridden by the bind mount in docker-compose dev mode
COPY . /srv/

# Make craft executable
RUN chmod +x /srv/craft

EXPOSE 8011

ENV PYTHONPATH=/srv/

# to be able to display all python print statements in docker logs
ENV PYTHONUNBUFFERED=1

CMD ["python3", "craft", "serve", "--host", "0.0.0.0", "--port", "8011"]
# CMD ["tail", "-f", "/dev/null"]
