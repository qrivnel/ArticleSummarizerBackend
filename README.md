<h1 align="center">Article Summarizer Backend</h1>

This repository contains the **training** and **endpoint** components of the **Article Summarizer** project. The goal of this project is to summarize Wikipedia articles in Turkish using a custom-trained model. The model has been trained on a dataset sourced from [Wikipedia-Tr-Summarization](https://huggingface.co/datasets/musabg/wikipedia-tr-summarization) available on Hugging Face.

## Features
- **Model Training**: This section includes the code used to train the summarization model on a specific dataset.
- **Model Endpoint**: The endpoint serves the trained model and processes user input to generate article summaries.

## Dataset
- The model is trained using the following dataset: [Wikipedia-Tr-Summarization](https://huggingface.co/datasets/musabg/wikipedia-tr-summarization) from Hugging Face.
- The dataset consists of **Wikipedia articles in Turkish**, with their corresponding summaries.

## Technologies Used
- **Python**: The primary programming language used for model training and serving the endpoint.
- **Transformers**: Hugging Face's library for training the model.
- **Flask/FastAPI**: The backend framework used to expose the model as an endpoint.
- **Hugging Face**: Pre-trained models and dataset repository.
- **TensorFlow/PyTorch**: The framework used for training the model.

## Setup and Usage

### 1. Clone the Repository:
```bash
git clone https://github.com/qrivnel/ArticleSummarizerTrainAndEndpoint.git
