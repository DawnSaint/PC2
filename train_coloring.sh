python main_coloring.py \
    run.job=train_coloing \
    model=coloring_model \
    run.mixed_precision=no \
    dataset.category=car \
    dataloader.batch_size=8 \
    run.max_steps=5_000 \
    run.coloring_training_noise_std=0.1 \
    run.name=train_coloring__car__mae