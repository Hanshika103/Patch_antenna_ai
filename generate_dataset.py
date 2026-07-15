

import numpy as np
import pandas as pd

c = 3e8

rows = []

for _ in range(10000):

    freq = np.random.uniform(1, 10)
    er = np.random.uniform(2.2, 10.2)
    h_mm = np.random.uniform(0.8, 3.2)
    loss_tangent = np.random.uniform(0.0009, 0.03)
    copper = np.random.choice([0.017, 0.035, 0.070])

    h = h_mm / 1000
    f = freq * 1e9

    W = (c / (2 * f)) * np.sqrt(2 / (er + 1))

    eeff = ((er + 1) / 2) + ((er - 1) / 2) * (
        1 / np.sqrt(1 + 12 * h / W)
    )

    Leff = c / (2 * f * np.sqrt(eeff))

    deltaL = (
        0.412 * h *
        ((eeff + 0.3) * ((W / h) + 0.264))
        /
        ((eeff - 0.258) * ((W / h) + 0.8))
    )

    L = Leff - 2 * deltaL

    Wg = W + 6 * h
    Lg = L + 6 * h

    rows.append([
        freq,
        er,
        h_mm,
        loss_tangent,
        copper,
        W * 1000,
        L * 1000,
        Wg * 1000,
        Lg * 1000
    ])

df = pd.DataFrame(rows, columns=[
    "Frequency_GHz",
    "Dielectric_Constant",
    "Height_mm",
    "Loss_Tangent",
    "Copper_Thickness_mm",
    "Patch_Width_mm",
    "Patch_Length_mm",
    "Ground_Width_mm",
    "Ground_Length_mm"
])

df.to_csv("antenna_dataset.csv", index=False)

print(df.head())