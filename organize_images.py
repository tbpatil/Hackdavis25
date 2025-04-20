import os
import shutil
import pandas as pd

csv_path = 'trainLabels.csv'
image_dir = 'train'

df = pd.read_csv(csv_path)

# Create folders
for label in range(5):
    os.makedirs(os.path.join(image_dir, str(label)), exist_ok=True)

# Move images into their label folder
for _, row in df.iterrows():
    img_name = row['image'] + ".jpeg"
    label = str(row['level'])
    src = os.path.join(image_dir, img_name)
    dst = os.path.join(image_dir, label, img_name)

    if os.path.exists(src):
        shutil.move(src, dst)
