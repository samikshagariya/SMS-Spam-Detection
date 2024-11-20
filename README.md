
# SMS Spam Detector

Welcome to the SMS Spam Detector project! This repository contains the code and resources for building and deploying an SMS spam classification system using machine learning.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Streamlit App](#streamlit-app)
- [Contributing](#contributing)

## Overview

The SMS Spam Detector project aims to identify whether an SMS message is spam or not using machine learning techniques. The project includes data preprocessing, model training, and a user-friendly Streamlit app for classification.

## Features

- **Data Preprocessing**: Clean and preprocess SMS messages for training.
- **Model Training**: Train a machine learning model to classify messages as spam or not.
- **Streamlit App**: A web application to interactively classify SMS messages.

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/samikshagariya/SMS-Spam-Detector.git
    cd SMS-Spam-Detector
    ```

2. Create and activate a virtual environment (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Streamlit App

To run the Streamlit app for SMS classification, use the following command:
```bash
streamlit run app.py
```

### Classifying Messages

1. Open your web browser and go to `http://localhost:8501`.
2. Enter an SMS message in the provided input field.
3. Click the "Classify" button to see if the message is spam or not.

## Model Training

The repository includes the script `train_model.py` to train the machine learning model. To train the model:

1. Ensure your environment is set up and dependencies are installed.
2. Run the training script:
    ```bash
    python train_model.py
    ```

The trained model will be saved in the `models` directory.

## Streamlit App

The Streamlit app (`app.py`) provides an easy-to-use interface for classifying SMS messages. The app loads the trained model and allows users to input messages for classification.

### Streamlit App Structure

- `app.py`: The main script for the Streamlit app.
- `model`: Directory containing the trained model files.
- `data`: Directory containing datasets used for training and evaluation.

## Contributing

Contributions are welcome! If you have suggestions for improvements or find any bugs, please open an issue or submit a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

