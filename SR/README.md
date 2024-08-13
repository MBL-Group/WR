# Super-Resolution Project

This repository contains scripts and configurations for training and inference on super-resolution tasks using the MM-RealSR framework. The project is based on code from the MM-RealSR repository by Tencent ARC.

## Table of Contents

- [Installation](#installation)
- [Training](#training)
- [Fine-Tuning](#fine-tuning)
- [Inference](#inference)
- [License](#license)
- [Contact](#contact)

## Installation

To install the necessary dependencies and set up the environment, please follow the installation instructions provided in the original MM-RealSR repository:

[MM-RealSR Installation Guide](https://github.com/TencentARC/MM-RealSR.git)

## Training

You can start training the models using the following commands:

### 1. Training with MMRealSRGAN (x4 Scale)

```bash
python -m torch.distributed.launch --nproc_per_node=4 --master_port=4321 mmrealsr/train.py -opt options/MMRealSRGAN_x4.yml --launcher pytorch --auto_resume
```

### 2. Training without Distributed Launch

For simpler training setups without distributed processing:

```bash
python mmrealsr/train.py -opt options/MMRealSRNet_x5.yml --auto_resume
python mmrealsr/train.py -opt options/MMRealSRGAN_x5.yml --auto_resume
```

## Fine-Tuning

Fine-tuning the models on specific datasets or configurations can be done as follows:

### 1. Fine-Tuning MMRealSRGAN (x4 Scale) with Multiple GPUs

```bash
CUDA_VISIBLE_DEVICES=0,1 \
python -m torch.distributed.launch --nproc_per_node=2 --master_port=4321 mmrealsr/train.py -opt options/finetune_MMRealSRGAN_x4.yml --launcher pytorch --auto_resume
```

### 2. Fine-Tuning with Single GPU

```bash
python mmrealsr/train.py -opt options/finetune_MMRealSRNet_x4.yml --auto_resume
python mmrealsr/train.py -opt options/finetune_MMRealSRGAN_x4.yml --auto_resume
```

## Inference

For inference on specific datasets, you can use the following commands:

### 1. Inference on Dataset 624

```bash
python inference_mmrealsrgpu1.py --im_path=/xxx-Data/MM-RealSR-Frelu/datasets/mutant_embryo_JAC624/Mutant-worm-50um_624_YA --res_path=/xxx-Data/Mutant-worm-50um_624_YA_SR/
```

### 2. Inference on Dataset 634

```bash
python inference_mmrealsrgpu2.py --im_path=/xxx-Data/MM-RealSR-Frelu/datasets/mutant_embryo_JAC634/Mutant-worm-50um_634_YA --res_path=/xxx-Data/Mutant-worm-50um_634_YA_SR/
```

### 3. Inference on Dataset 984

```bash
python inference_mmrealsrgpu3.py --im_path=/xxx-Data/MM-RealSR-Frelu/datasets/mutant_embryo_JAC984/Mutant-worm-50um_984_YA --res_path=/xxx-Data/Mutant-worm-50um_984_YA_SR/
```

## License

This project is based on the MM-RealSR framework by Tencent ARC. Please refer to the original MM-RealSR repository for license information.

## Contact

For any questions, issues, or contributions, please contact the repository maintainer or open an issue on this repository.

