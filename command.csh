python3 ./main.py --train --data_root_dir=data --net segcapsr3 --initial_lr 0.01 --loglevel 2 --Kfold 4 --loss dice --dataset mscoco17 --recon_wei 20 --which_gpu -1 --gpus 1 --aug_data 0 

python3 ./main.py --train --data_root_dir=data --net capsbasic --initial_lr 0.01 --loglevel 2 --Kfold 4 --loss dice --dataset mscoco17 --recon_wei 20 --which_gpu -1 --gpus 1 --aug_data 0

#python3 ./main.py --train --data_root_dir=data --net unet --initial_lr 0.01 --loglevel 2 --Kfold 4 --loss w_bce --dataset mscoco17 --recon_wei 2

nohup python3 ./main.py --train --data_root_dir=luna --net segcapsr3 --initial_lr 0.0001 --loglevel 2 --loss w_bce --dataset luna16 --slices 1 --which_gpu -1 --gpus 1 --steps_per_epoch 1000 --epochs 20 > 0831.out 2>&1 &
