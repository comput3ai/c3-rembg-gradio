FROM nvidia/cuda:12.4.1-cudnn-devel-ubuntu22.04

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python-is-python3 \
    curl \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install ".[gpu,cli]"
RUN pip install gradio

# Don't download models during build - they'll be downloaded on first use
# or can be pre-downloaded in specific deployment environments

EXPOSE 7860
CMD ["python", "app.py"]
