# 🍇 Grape Disease Detection Using Computer Vision

This repository is the official implementation of bachelor's thesis:

Author: **Adam Kačmár**<br />
Year of Submission: **2025**<br />
Faculty of Informatics and Information Technologies STU in Bratislava

## 🧰 Requirements
- Python 3.10+

## 🔧 Installation

1. Clone repository

```setup
git clone https://github.com/adamkacmar/bc-grape-disease
cd bc-grape-disease
```

2. Install requirements

```setup
pip install -r requirements.txt
```

## 🚀 Usage

### Training Notebooks
If you wish to train your own models on our augmented dataset run these:

```setup
jupyter notebook model-scripts/vit_hyperparams.ipynb
jupyter notebook model-scripts/swinv2_hyperparams.ipynb
```

### Grad-CAM Notebooks*
For better explainability of the models, run the Grad-CAM notebooks followingly:
```setup
jupyter notebook model-scripts/vit_gradcam.ipynb
jupyter notebook model-scripts/swinv2_gradcam.ipynb
```
*require having models locally.

### Testing Notebook*
To test the models overall performance on both datasets, run this:

```setup
jupyter notebook model-scripts/test_models.ipynb
```

*require having models locally.

### Dataset Set-up Notebooks*
To recreate your own dataset, run these:

```setup
jupyter notebook dataset-scripts/opencv_image.ipynb
jupyter notebook dataset-scripts/remove_images_backgrounds.ipynb
```

*require having models locally.

## 🧱 Project Structure

```
bc-grape-disease/              
├── dataset-scripts/           # Directory of notebooks related to dataset creation
│   ├── opencv_image.ipynb     # Generates new dataset with augmented backgrounds
│   └── remove_images_backgrounds.ipynb  # Removes the backgrounds of the original dataset
│
├── model-scripts/       # Directory of notebooks related to model training and evaluation
│   ├── swinv2_hyperparams.ipynb   # Training, validation and testing for Swin Transformer V2
│   ├── vit_hyperparams.ipynb      # Training, validation and testing for Vision Transformer
│   ├── swinv2_gradcam.ipynb       # Grad-CAM implementation for Swin Transformer V2
│   ├── vit_gradcam.ipynb          # Grad-CAM implementation for Vision Transformer
│   └── test_models.ipynb          # Tests models from local directory
│
├── .gitignore             # Files ignored by Git
├── gradioapp.py           # Demo (TBD)
├── requirements.txt       # List of required packages/libraries
└── README.md              # Project description
```

## 🧠 Pre-trained Models

You can download all of pretrained models here:

- [All models](https://drive.google.com/drive/folders/1bkEkagiUx0bZNSwiMkbKZYmIFzydIP7A?usp=sharing) trained on the [PlantVillage dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset) and our [augmented dataset](https://www.kaggle.com/datasets/adamkacmar/augmented-grape-leaf-disease-dataset) using every possible combinations of hyperparameter configuration of batch sizes 16, 32 and learning rates 0.00001, 0.0001, 0.0005.  

## 📊 Results

### Evaluation of Models Trained on [our dataset](https://www.kaggle.com/datasets/adamkacmar/augmented-grape-leaf-disease-dataset)

| Model   | Batch Size | Learning Rate | Accuracy - Augmented | Accuracy - Original |
|---------|------------|----------------|-----------------------|----------------------|
| ViT     | 16         | 1e-5           | *99.25%*              | 97.95%               |
|         | 16         | 1e-4           | 99.22%                | *99.61%*             |
|         | 16         | 5e-4           | 94.52%                | 97.23%               |
|         | 32         | 1e-5           | **99.28%**            | 97.45%               |
|         | 32         | 1e-4           | 98.89%                | **99.72%**           |
|         | 32         | 5e-4           | 96.68%                | 97.73%               |
| SwinV2  | 16         | 1e-5           | **99.86%**            | 99.11%               |
|         | 16         | 1e-4           | 99.42%                | 98.56%               |
|         | 16         | 5e-4           | 72.83%                | 42.77%               |
|         | 32         | 1e-5           | *99.78%*              | **99.94%**           |
|         | 32         | 1e-4           | 99.36%                | *99.78%*             |
|         | 32         | 5e-4           | 97.12%                | 80.50%               |


### Evaluation of Models Trained on [PlantVillage Dataset](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)

| Model   | Batch Size | Learning Rate | Accuracy - Original | Accuracy - Augmented |
|---------|------------|----------------|----------------------|-----------------------|
| ViT     | 16         | 1e-5           | 99.89%               | 72.30%                |
|         | 16         | 1e-4           | **100.00%**          | 62.27%                |
|         | 16         | 5e-4           | 99.11%               | 34.02%                |
|         | 32         | 1e-5           | *99.94%*             | *81.30%*              |
|         | 32         | 1e-4           | *99.94%*             | **87.09%**            |
|         | 32         | 5e-4           | 99.83%               | 36.18%                |
| SwinV2  | 16         | 1e-5           | ***100.00%***        | 74.18%                |
|         | 16         | 1e-4           | 99.94%               | **86.43%**            |
|         | 16         | 5e-4           | 98.67%               | 43.60%                |
|         | 32         | 1e-5           | ***100.00%***        | 63.91%                |
|         | 32         | 1e-4           | 99.94%               | *86.32%*              |
|         | 32         | 5e-4           | 99.39%               | 46.04%                |


## 👷 Contributing

[PlantVillage](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)  
[Grapevine Disease Dataset (Original)](https://www.kaggle.com/datasets/rm1000/grape-disease-dataset-original)
