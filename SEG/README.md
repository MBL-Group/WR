
# Segmentation

This repository contains code that has been modified based on the PaddleSeg framework. The modifications are specifically tailored for segmenting *C. elegans* and embryos. For installation, setup, and usage, please follow the instructions provided below.

## Table of Contents

- [Installation](#installation)
- [Data Preparation](#data-preparation)
- [Training](#training)
- [Prediction](#prediction)
- [Citation](#citation)
- [License](#license)
- [Contact](#contact)

## Installation

To get started, you need to install the necessary dependencies. Please ensure you have PaddleSeg installed. You can follow the [PaddleSeg README](https://github.com/PaddlePaddle/PaddleSeg) for detailed installation instructions.

After installing PaddleSeg, run the following commands to install additional dependencies required for this project:

```bash
pip install -r requirements.txt
pip install -v -e .
```

## Data Preparation

### 1. Convert LabelMe Annotations to Segmentation Format

If your data is annotated using LabelMe, you can convert it to a format suitable for segmentation using the following command:

```bash
python tools/data/labelme2seg.py celegans_labelme
```

### 2. Split Dataset into Train and Validation Sets

After converting the annotations, you can split the dataset into training and validation sets:

```bash
python tools/data/split_dataset_list.py celegans_labelme images annotations --split 0.82 0.18 0.0 --format png png
```

This will split the dataset into 82% training, 18% validation, and 0% testing data, using the specified formats for images and annotations.

## Training

### 1. Training on *C. elegans* Dataset

To train the model on the *C. elegans* dataset, use the following command:

```bash
python tools/train.py --config configs/ocrnet/celegans_ocrnet_hrnetw48.yml --save_interval 500 --do_eval --use_vdl --save_dir output_elegans
```

### 2. Training on Embryo Dataset

For training on the embryo dataset, run the command:

```bash
python tools/train.py --config configs/ocrnet/embryos_ocrnet_hrnetw48.yml --save_interval 500 --do_eval --use_vdl --save_dir output_elegans
```

- `--save_interval 500`: Saves the model every 500 iterations.
- `--do_eval`: Enables evaluation during training.
- `--use_vdl`: Uses VisualDL for visualization.
- `--save_dir`: Specifies the directory to save the output.

## Prediction

### 1. Predicting on *C. elegans* Data

To make predictions on new data using the trained *C. elegans* model:

```bash
python tools/predict.py --config configs/ocrnet/celegans_ocrnet_hrnetw48.yml --model_path output_0510/best_model_p/model.pdparams --image_path N2-embryo-10um-SRx5 --save_dir output_0510/n2_embryo_result
```

### 2. Predicting on Embryo Data

For predictions using the trained embryo model:

```bash
python tools/predict.py --config configs/ocrnet/embryos_ocrnet_hrnetw48.yml --model_path xxxx/model.pdparams --image_path xxxx --save_dir output_xxx
```

- `--model_path`: Path to the trained model parameters.
- `--image_path`: Directory containing the images for prediction.
- `--save_dir`: Directory to save the prediction results.

## Citation (Todo)

If you use this code or dataset in your research, please consider citing our work:

```bibtex
@article{YourLastName2024,
  title={Title of Your Paper},
  author={Your Name, Co-author's Name},
  journal={Journal Name},
  year={2024},
  publisher={Publisher's Name}
}
```

## License

This project is licensed under the MIT License.

## Contact

For questions, suggestions, or feedback, please raise an issue in this repository. We welcome all contributions and inquiries.
```