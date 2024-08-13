python -m torch.distributed.launch --nproc_per_node=2 --master_port=4321 mmrealsr/train.py -opt options/MMRealSRNet_x5.yml --launcher pytorch --auto_resume

python -m torch.distributed.launch --nproc_per_node=4 --master_port=4321 mmrealsr/train.py -opt options/MMRealSRGAN_x4.yml --launcher pytorch --auto_resume

python  mmrealsr/train.py -opt options/MMRealSRNet_x5.yml  --auto_resume
python  mmrealsr/train.py -opt options/MMRealSRGAN_x5.yml  --auto_resume


CUDA_VISIBLE_DEVICES=0,1 \
python -m torch.distributed.launch --nproc_per_node=2 --master_port=4321 mmrealsr/train.py -opt options/finetune_MMRealSRGAN_x4.yml --launcher pytorch --auto_resume


python mmrealsr/train.py -opt options/finetune_MMRealSRNet_x4.yml --auto_resume

python mmrealsr/train.py -opt options/finetune_MMRealSRGAN_x4.yml --auto_resume


python inference_mmrealsrgpu1.py --im_path=/xxx-Data/MM-RealSR-Frelu/datasets/mutant_embryo_JAC624/Mutant-worm-50um_624_YA --res_path=/xxx-Data/Mutant-worm-50um_624_YA_SR/
python inference_mmrealsrgpu2.py --im_path=/xxx-Data/MM-RealSR-Frelu/datasets/mutant_embryo_JAC634/Mutant-worm-50um_634_YA --res_path=/xxx-Data/Mutant-worm-50um_634_YA_SR/
python inference_mmrealsrgpu3.py --im_path=/xxx-Data/MM-RealSR-Frelu/datasets/mutant_embryo_JAC984/Mutant-worm-50um_984_YA --res_path=/xxx-Data/Mutant-worm-50um_984_YA_SR/

