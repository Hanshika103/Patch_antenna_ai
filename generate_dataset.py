import numpy as np
import pandas as pd

# Speed of light
c = 3e8

# Fixed parameters
er = 4.4
h_mm = 1.6
h = h_mm / 1000  # convert to meters

rows = []

# Generate 10,000 frequencies between 1 and 10 GHz
frequencies = np.random.uniform(1, 10, 10000)

for freq_ghz in frequencies:

    f = freq_ghz * 1e9

    # Patch Width
    W = (c / (2 * f)) * np.sqrt(2 / (er + 1))

    # Effective dielectric constant
    eeff = ((er + 1) / 2) + ((er - 1) / 2) * (
        1 / np.sqrt(1 + 12 * h / W)
    )

    # Effective Length
    Leff = c / (2 * f * np.sqrt(eeff))

    # Length extension
    deltaL = (
        0.412 * h *
        ((eeff + 0.3) * ((W / h) + 0.264))
        / ((eeff - 0.258) * ((W / h) + 0.8))
    )

    # Actual Length
    L = Leff - 2 * deltaL

    # Ground Plane Dimensions
    Wg = W + 6 * h
    Lg = L + 6 * h

    rows.append([
        round(freq_ghz, 4),
        round(W * 1000, 4),
        round(L * 1000, 4),
        round(Wg * 1000, 4),
        round(Lg * 1000, 4)
    ])

# Create DataFrame
df = pd.DataFrame(rows, columns=[
    "Frequency_GHz",
    "Patch_Width_mm",
    "Patch_Length_mm",
    "Ground_Width_mm",
    "Ground_Length_mm"
])

# Save CSV
df.to_csv("antenna_dataset.csv", index=False)

print("Dataset generated successfully!")
print("Rows:", len(df))
print("Saved as antenna_dataset.csv")
print(df.head())