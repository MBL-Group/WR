pip install -r requirements.txt
pip install -v -e .


python tools/data/labelme2seg.py celegans_labelme

python tools/data/split_dataset_list.py celegans_labelme images annotations --split 0.82 0.18 0.0 --format png png

python tools/train.py --config configs/ocrnet/embryos_ocrnet_hrnetw48.yml --save_interval 500 --do_eval --use_vdl --save_dir output_elegans


python tools/train.py --config configs/ocrnet/celegans_ocrnet_hrnetw48.yml --save_interval 500 --do_eval --use_vdl --save_dir output_elegans
python tools/train.py --config configs/ocrnet/celegans_ocrnet_hrnetw48.yml --resume_model output_elegans/iter_31000 --save_interval 500 --do_eval --use_vdl --save_dir output_elegans



python tools/train.py --config configs/ocrnet/celegans_ocrnet_hrnetw48.yml --resume_model output_0510/iter_133500 --save_interval 500 --do_eval --use_vdl --save_dir output_0510


python tools/predict.py --config configs/ocrnet/celegans_ocrnet_hrnetw48.yml --model_path output_0510/best_model_p/model.pdparams --image_path N2-embryo-10um-SRx5 --save_dir output_0510/n2_embryo_result

python tools/predict.py --config configs/ocrnet/celegans_ocrnet_hrnetw48.yml --model_path output_0510/best_model_p/model.pdparams --image_path N2-embryo-10um-SRx5 --save_dir output_0510/n2_embryo_result


visualdl --logdir output_elegans