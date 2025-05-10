# 🍇 Grape Disease Detection Using Computer Vision

This repository is the official implementation of bachelor's thesis:

Author: **Adam Kačmár**<br />
Year of Submission: **2025**<br />
Faculty of Informatics and Information Technologies STU in Bratislava

## 🧰 Requirements

To install requirements, run the following command:

```setup
pip install -r requirements.txt
```

🚀 Usage

```setup
pip tbd
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


## Contributing

[PlantVillage](https://www.kaggle.com/datasets/abdallahalidev/plantvillage-dataset)  
[Grapevine Disease Dataset (Original)](https://www.kaggle.com/datasets/rm1000/grape-disease-dataset-original)
