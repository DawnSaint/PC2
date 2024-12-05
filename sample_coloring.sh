python main_coloring.py \
    run.job=sample_coloing \
    dataset.category=car \
    dataloader.batch_size=8 \
    model=coloring_model \
    checkpoint.resume="/root/autodl-tmp/projection-conditioned-point-cloud-diffusion-main/experiments/outputs/train__car__mae/2024-12-01--22-08-58/checkpoint-latest.pth" \
    run.coloring_sample_dir="/root/autodl-tmp/projection-conditioned-point-cloud-diffusion-main/experiments/outputs/sample__car__mae/2024-12-02--08-31-29/sample/" \
    run.name=sample_coloring__car__mae