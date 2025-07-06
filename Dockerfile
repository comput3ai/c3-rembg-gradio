FROM python:3.10-slim

WORKDIR /rembg

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y curl && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m pip install ".[gpu,cli]"
RUN pip install gradio

# Don't download models during build - they'll be downloaded on first use
# or can be pre-downloaded in specific deployment environments

EXPOSE 7860
CMD ["python", "app.py"]
