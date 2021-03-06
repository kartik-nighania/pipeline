from ..base import ConfigWideResNetBase


class Config(ConfigWideResNetBase):
    def __init__(self):
        super().__init__(num_layers=100, normalization_type=ConfigWideResNetBase.BATCH_NORM)
