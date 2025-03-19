# Android Calculator

A simple Android calculator developed in Python using the Kivy framework.

## Description

The application is a basic calculator that supports fundamental mathematical operations:
- Addition
- Subtraction
- Multiplication
- Division

## Requirements

- Python 3.x
- Kivy
- Buildozer
- Linux/WSL2 for building

## Installing Dependencies

```bash
# Installing system dependencies in Ubuntu/WSL2
sudo apt-get update
sudo apt-get install -y \
    autoconf \
    automake \
    build-essential \
    libtool \
    pkg-config \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-venv \
    zlib1g-dev

# Creating and activating virtual environment
python3 -m venv venv
source venv/bin/activate

# Installing Python dependencies
pip install -r requirements.txt
```

## Building APK

1. Activate the virtual environment:
```bash
source venv/bin/activate
```

2. Execute the build:
```bash
buildozer android debug
```

The APK file will be created in the `bin/` directory.

## Project Structure

```
calculator/
├── main.py           # Main application code
├── buildozer.spec    # Build configuration
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```
