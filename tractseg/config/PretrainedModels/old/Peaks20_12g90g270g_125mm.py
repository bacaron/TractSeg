import os
from tractseg.config.PeakRegHP import HP as PeakRegHP

#Name of original exp: Peaks20_12g90g270g_ALLoss

class HP(PeakRegHP):
    EXP_NAME = os.path.basename(__file__).split(".")[0]

    LOSS_WEIGHT = 10
    LOSS_WEIGHT_LEN = 400  # nr of epochs

    NUM_EPOCHS = 500
