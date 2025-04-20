# %%
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, Subset, random_split
from torchvision.models import resnet18, ResNet18_Weights
from PIL import ImageFile
import os
from collections import Counter
import random 
import numpy as np 
import torch.nn.functional as F

random.seed(0)
counts = {}
for i in range(5):
    class_path = os.path.join("train", str(i))
    counts[i] = len(os.listdir(class_path))

print("Class Distribution:", counts)


ImageFile.LOAD_TRUNCATED_IMAGES = True  # prevent image loading errors

def train_model(data_dir, num_classes=5, batch_size=16, epochs=5, test_size=0.25, samples=100, learning_rate=0.001, model_name="model/retino_model.pth", resize_dims=(224,224)):
    print("Training model...")

    transform = transforms.Compose([
        transforms.Resize(resize_dims),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406],  # ImageNet mean
                             std=[0.229, 0.224, 0.225])   # ImageNet std
    ])

    dataset = ImageFolder(root=data_dir, transform=transform)
    inds = np.array([]); j=0
    for i in range(num_classes):
        temp = random.choices(range(j,j+counts[i]), k=int(samples/num_classes))
        inds = np.concatenate([inds, temp])
        j = j + counts[i]
    inds = inds.astype(int).tolist()
    dataset = Subset(dataset, inds)  # Use full dataset for real training
    train_dataset, valid_dataset = random_split(dataset, [samples - int(samples*test_size), int(samples*test_size)])
    valid_loader = DataLoader(valid_dataset, batch_size=len(valid_dataset))
    print(f"Number of images: {len(dataset)}")

    loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)

    # Load ResNet model
    try:
        weights = ResNet18_Weights.DEFAULT
        model = resnet18(weights=weights)
    except:
        print("⚠️ Could not download pretrained weights, using random init")
        model = resnet18(weights=None)

    model.fc = nn.Linear(model.fc.in_features, num_classes)

    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    best_acc = 0.0  
    model.train()
    for epoch in range(epochs):  
        running_loss = 0.0
        valid_loss = 0.0
        train_acc = 0
        valid_acc = 0
        for inputs, labels in loader:
            #print(labels)
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
            probs = F.softmax(outputs, dim=1)
            _, predicted = torch.max(probs, 1)
            train_acc = train_acc + torch.sum(predicted == labels.data)
            
            
        with torch.no_grad():
            for valid_inputs, valid_targets in valid_loader:
                valid_outputs = model(valid_inputs)
                loss = criterion(valid_outputs, valid_targets)

                valid_loss += loss.item() * valid_inputs.size(0)
                # num_valid_samples += valid_inputs.size(0)
            probs = F.softmax(valid_outputs, dim=1)
            _, predicted = torch.max(probs, 1)
            valid_acc = valid_acc + torch.sum(predicted == valid_targets.data)
            #print(predicted)

        avg_valid_loss = valid_loss / len(valid_loader)

        print(f"Epoch {epoch + 1}: training loss = {running_loss / len(loader):.4f}")
        print(f"validation Loss: {avg_valid_loss:.4f}")
        print(f"training acc = {train_acc / len(train_dataset):.4f}")
        print(f"validation acc: {valid_acc / len(valid_dataset):.4f}")
        print()

        if valid_acc / len(valid_dataset) >= best_acc:
            best_acc = valid_acc / len(valid_dataset)
            os.makedirs(os.path.dirname(model_name), exist_ok=True)
            torch.save(model.state_dict(), model_name)  # ✅ ACTUALLY SAVE THE MODEL
            print(f"✅ Model saved to {model_name}")


    print(f"best valid acc: {best_acc}")

if __name__ == "__main__":
    data_path = "train"
    train_model(data_path, samples=10, epochs=10, test_size=0.2)
