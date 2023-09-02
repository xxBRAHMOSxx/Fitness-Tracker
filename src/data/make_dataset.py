import pandas as pd
from glob import glob

# --------------------------------------------------------------
# Read single CSV file
# --------------------------------------------------------------
single_csv_acc = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Accelerometer_12.500Hz_1.4.4.csv")

single_csv_gyro = pd.read_csv(
    "../../data/raw/MetaMotion/A-bench-heavy2-rpe8_MetaWear_2019-01-11T16.10.08.270_C42732BE255C_Gyroscope_25.000Hz_1.4.4.csv")


# --------------------------------------------------------------
# List all data in data/raw/MetaMotion
# --------------------------------------------------------------

files = glob("../../data/raw/MetaMotion/*.csv")
len(files)


# --------------------------------------------------------------
# Extract features from filename
# --------------------------------------------------------------

data_path = "../../data/raw/MetaMotion\\"
f = files[0]


# --------------------------------------------------------------
# defining dataframe
# --------------------------------------------------------------

acc_df = pd.DataFrame()
gyro_df = pd.DataFrame()

# --------------------------------------------------------------
# unique identifier or each set
# --------------------------------------------------------------

acc_set = 1
gyro_set = 1

# --------------------------------------------------------------
# Read all files
# --------------------------------------------------------------

for f in files:
    participants = f.split("-")[0].replace(data_path, "")
    lables = f.split("-")[1]
    catagory = f.split("-")[2].rstrip("1234").rstrip("_MetaWear_2019")

    df = pd.read_csv(f)

    df["participants"] = participants
    df["lables"] = lables
    df["catagory"] = catagory

    # to prevent the loop from overwriting constantly, we append it
    if "Accelerometer" in f:
        df["set"] = acc_set
        acc_set += 1
        acc_df = pd.concat([acc_df, df])
    if "Gyroscope" in f:
        df["set"] = gyro_set
        gyro_set += 1
        gyro_df = pd.concat([gyro_df, df])

# --------------------------------------------------------------
# Working with datetimes
# --------------------------------------------------------------


# --------------------------------------------------------------
# Turn into function
# --------------------------------------------------------------


# --------------------------------------------------------------
# Merging datasets
# --------------------------------------------------------------


# --------------------------------------------------------------
# Resample data (frequency conversion)
# --------------------------------------------------------------

# Accelerometer:    12.500HZ
# Gyroscope:        25.000Hz


# --------------------------------------------------------------
# Export dataset
# --------------------------------------------------------------
