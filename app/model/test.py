import train 
import random 
import os 

random.seed(0)
counts = {}
for i in range(5):
    class_path = os.path.join("train", str(i))
    counts[i] = len(os.listdir(class_path))

print("Class Distribution:", counts)

dims = [(224,224), (500,500), (750,750), (1000,1000)]

for i,d in enumerate(dims):
    print(d)
    train.train_model("train", samples=1000, epochs=30, test_size=0.20, model_name=f"model/retino_model{i}.pth")
    print('_________')
    print()