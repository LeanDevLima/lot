FROM python:3.12-slim

WORKDIR /app

# system deps for common Python packages (kept minimal)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# copy app
COPY . /app

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

# Use sh -c so $PORT is expanded by the shell at container runtime
CMD ["sh", "-c", "gunicorn app:app -b 0.0.0.0:${PORT:-5000} --workers 1"]
