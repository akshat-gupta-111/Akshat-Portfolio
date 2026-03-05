# --- stage 1 --- build stage
FROM python:3.10-slim AS builder

WORKDIR /app

# Install dependencies into a virtual-env so we can copy them cleanly
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Collect static files (uses whitenoise; no DB needed)
RUN python manage.py collectstatic --noinput

# --- stage 2 --- production stage
FROM python:3.10-slim

WORKDIR /app

# Copy the virtual-env and the application code
COPY --from=builder /opt/venv /opt/venv
COPY --from=builder /app /app

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PORT=3000

# Make entrypoint executable
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

EXPOSE 3000

# Entrypoint runs migrations, then starts gunicorn
ENTRYPOINT ["/app/entrypoint.sh"]