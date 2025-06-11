# ------------------------------
# 🐍 Base Python image
# ------------------------------
FROM python:3.11-slim

# ------------------------------
# 📁 Set workdir and copy code
# ------------------------------
WORKDIR /app
COPY . /app

# ------------------------------
# ✅ Install system deps (if needed)
# ------------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
 && rm -rf /var/lib/apt/lists/*

# ------------------------------
# 📦 Install Python dependencies
# ------------------------------
RUN pip install --upgrade pip
RUN pip install -r requirements/production.txt

# ------------------------------
# ✅ Environment-aware entry point
# ------------------------------
ENV DJANGO_SETTINGS_MODULE=config.settings
ENV DJANGO_ENV=production

# ------------------------------
# 🏁 Run server via run.py
# ------------------------------
CMD ["python", "src/run.py", "runserver", "0.0.0.0:8000"]
