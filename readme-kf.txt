lstm:
code:
python3 generate_bt_fps-lstm.py --model_name_or_path data-bin/smiles --checkpoint_file checkpoint_last.pt --data_name_or_path  data-bin/smiles --target_file example-smiles/example.smi --save_feature_path example-smiles/examples_bt_features-v2.npy

train:
1. python3 preprocess.py --trainpref  example-smiles/example --tokenizer smi --source-lang smi --target-lang smi1 --destdir data-bin/smiles
2. CUDA_VISIBLE_DEVICES=7 python3 train.py data-bin/smiles --disable-validation --source-lang smi --target-lang smi --tokenizer smi --lr 0.25 --clip-norm 0.1 --dropout 0.2 --max-source-positions 128 --max-tokens 2560 --max-epoch 5000 --arch lstm --save-dir data-bin/smiles --optimizer sgd

test:
python3 interactive.py data-bin/smiles --source-lang smi --target-lang smi --tokenizer smi --path data-bin/smiles/checkpoint_best.pt

transformer:

code:
python3 generate_bt_fps-v2.py --model_name_or_path example-smiles --checkpoint_file checkpoint_ssl_finetuned.pt --data_name_or_path  example-smiles --smi_voc example-smiles/dict.txt --target_file example-smiles/example.smi --save_feature_path example-smiles/examples_bt_features.npy

train:
1. python3 preprocess.py --trainpref data-bin/smiles/250k_trainset-canonical --tokenizer smi --source-lang smi --target-lang smi1 --destdir data-bin/smiles
2. python3 train.py data-bin/smiles --source-lang smi --disable-validation --target-lang smi --lr 0.25 --clip-norm 0.1 --dropout 0.2 --max-source-positions 128 --max-tokens 2048 --max-epoch 5000 --arch transformer --tokenizer smi --save-dir data-bin/smiles --optimizer sgd

test:
python3 interactive.py data-bin/smiles --source-lang smi --target-lang smi --tokenizer smi --path data-bin/smiles/checkpoint_best.pt --input 5k-testset.smi