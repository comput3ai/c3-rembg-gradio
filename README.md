# 🎨 Rembg Gradio Interface

[![Python 3.10](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/downloads/release/python-3100/)
[![Gradio](https://img.shields.io/badge/Gradio-5.0%2B-orange.svg)](https://gradio.app/)
[![Rembg](https://img.shields.io/badge/Rembg-Latest-green.svg)](https://github.com/danielgatis/rembg)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A clean Gradio interface for [Rembg](https://github.com/danielgatis/rembg), inspired by the original Rembg server implementation but designed as a standalone, Docker-friendly application.

## ✨ Features

- 🎯 **Multiple AI Models**: Choose from 15+ specialized models for different use cases
- 🖼️ **Live Preview**: See results instantly with side-by-side comparison
- ⚙️ **Advanced Options**: Fine-tune with alpha matting and post-processing controls
- 🐳 **Docker Ready**: Easy deployment with included Dockerfile and docker-compose
- 🚀 **GPU Acceleration**: Optimized for CUDA-enabled GPUs
- 📁 **Batch Processing**: Process multiple images efficiently

## 🚀 Quick Start

### Local Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/rembg.git
   cd rembg
   ```

2. Install dependencies:
   ```bash
   pip install rembg[gpu] gradio
   ```

3. Download the default model:
   ```bash
   rembg d u2net
   ```

4. Launch the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:7860`

### 🐳 Docker Deployment

Build and run with Docker Compose:

```bash
docker-compose up --build
```

The interface will be available at `http://localhost:7860`

## 🎮 Usage Guide

### Basic Usage

1. **Upload Image**: Drag and drop or click to upload an image
2. **Select Model**: Choose from available models (default: u2net)
3. **Remove Background**: Click the button to process
4. **Download Result**: Save the output image with transparent background

### Available Models

#### U2Net Family
- 🎯 **u2net** (default): A pre-trained model for general use cases
- ⚡ **u2netp**: A lightweight version of u2net model
- 👤 **u2net_human_seg**: A pre-trained model for human segmentation
- 👔 **u2net_cloth_seg**: A pre-trained model for clothes parsing from human portrait

#### ISNet Models
- 🔍 **isnet-general-use**: A new pre-trained model for general use cases
- 🎌 **isnet-anime**: A high-accuracy segmentation for anime character

#### BiRefNet Family
- ✨ **birefnet-general**: A pre-trained model for general use cases
- 🚀 **birefnet-general-lite**: A light pre-trained model for general use cases
- 👨 **birefnet-portrait**: A pre-trained model for human portraits
- 🎯 **birefnet-dis**: A pre-trained model for dichotomous image segmentation (DIS)
- 🔬 **birefnet-hrsod**: A pre-trained model for high-resolution salient object detection (HRSOD)
- 🕵️ **birefnet-cod**: A pre-trained model for concealed object detection (COD)
- 💪 **birefnet-massive**: A pre-trained model with massive dataset

#### Other Models
- 🤖 **sam**: A pre-trained model for any use cases
- 🎨 **silueta**: Same as u2net but the size is reduced to 43Mb
- 🏢 **bria-rmbg**: Commercial-grade background removal model (Bria AI)

### Advanced Options

- **Alpha Matting**: Improves edge quality for hair and fur
  - Foreground Threshold: Higher values keep more foreground
  - Background Threshold: Lower values remove more background
  - Erode Size: Shrinks the foreground mask

- **Output Options**:
  - Mask Only: Output segmentation mask instead of transparent image
  - Post Process: Apply morphological operations to clean the mask

## ⚙️ Configuration

### Environment Variables

Create a `.env` file for docker-compose:

```env
PUBLIC_PORT=7860:7860
REPLICAS_COUNT=1
```

### GPU Support

For GPU acceleration, ensure you have:
- NVIDIA GPU with CUDA support
- nvidia-docker installed
- `--gpus all` flag when running Docker

## 🔧 Development

### Project Structure

```
rembg/
├── app.py              # Gradio interface
├── Dockerfile          # Docker configuration
├── docker-compose.yml  # Docker Compose setup
├── requirements.txt    # Python dependencies
└── examples/          # Sample images
```

### Customization

To add new features or modify the interface, edit `app.py`. The main components are:

- `process_image()`: Core processing function
- `gr.Blocks()`: Gradio interface layout
- Model selection and parameter controls

## 📊 Performance Tips

- 🚀 **Model Selection**: Start with `u2net` for general images, use specialized models for specific content
- ⚡ **GPU Usage**: Ensure CUDA is available for 10x+ speedup
- 🎯 **Alpha Matting**: Enable only when needed (adds processing time)
- 📦 **Batch Processing**: Process multiple similar images with the same model loaded

## 🙏 Acknowledgements

- [Rembg](https://github.com/danielgatis/rembg) by Daniel Gatis for the core background removal functionality
- [Gradio](https://gradio.app/) for the web interface framework
- All the model authors whose work powers the background removal

## 📄 License

This project is licensed under the MIT License - see the original [Rembg LICENSE](LICENSE.txt) for details.

---

Made with ❤️ inspired by the original Rembg project