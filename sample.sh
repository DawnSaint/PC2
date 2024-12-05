# python main.py \
#     run.job=sample \
#     dataloader.batch_size=8 \
#     dataloader.num_workers=8 \
#     dataset.category=car \
#     checkpoint.resume="/root/autodl-tmp/projection-conditioned-point-cloud-diffusion-main/experiments/outputs/train__car__mae/2024-12-01--09-29-19/checkpoint-latest.pth" \
#     run.name=sample__car__mae

python main.py \
    run.job=sample \
    dataloader.batch_size=8 \
    dataloader.num_workers=8 \
    dataset.category=car \
    checkpoint.resume="/root/autodl-tmp/projection-conditioned-point-cloud-diffusion-main/experiments/outputs/train__car__mae/2024-12-01--22-08-58/checkpoint-latest.pth" \
    run.name=sample__car__mae