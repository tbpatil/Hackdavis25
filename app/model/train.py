import torch
import torch.nn as nn
from torchvision.datasets import ImageFolder
from torch.utils.data import DataLoader, Subset
from torchvision import transforms
from torchvision.models import resnet18, ResNet18_Weights
from PIL import ImageFile
from collections import defaultdict
import random
import os

ImageFile.LOAD_TRUNCATED_IMAGES = True  # Handle bad images

def get_balanced_subset(dataset, samples_per_class=100):
    class_indices = defaultdict(list)
    print("🔍 Scanning dataset to collect class indices...")
    
    for idx, (_, label) in enumerate(dataset):
        class_indices[label].append(idx)
        if idx % 500 == 0:
            print(f"  → Processed {idx}/{len(dataset)} images")

    selected_indices = []
    for label, indices in class_indices.items():
        if len(indices) >= samples_per_class:
            selected = random.sample(indices, samples_per_class)
        else:
            selected = indices  # take all if not enough
        selected_indices.extend(selected)

    print(f"✅ Selected a total of {len(selected_indices)} samples across {len(class_indices)} classes")
    return Subset(dataset, selected_indices)


def compute_class_weights(dataset):
    class_counts = defaultdict(int)
    for _, label in dataset:
        class_counts[label] += 1
    
    total = sum(class_counts.values())
    weights = [total / class_counts[i] for i in range(len(class_counts))]
    weights = torch.tensor(weights, dtype=torch.float)
    return weights / weights.sum()

def train_model(data_dir, num_classes=5, batch_size=16, epochs=10, learning_rate=0.001):
    print("⚙️ Training model...")

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])

    full_dataset = ImageFolder(root=data_dir, transform=transform)
    class_counts = {label: len(os.listdir(os.path.join(data_dir, str(label)))) for label in range(num_classes)}
    print("📊 Class Distribution:", class_counts)

    dataset = get_balanced_subset(full_dataset, samples_per_class=100)
    print(f"📦 Balanced subset: {len(dataset)} images")

    loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    try:
        weights = ResNet18_Weights.DEFAULT
        model = resnet18(weights=weights)
    except:
        print("⚠️ Pretrained weights failed to load — using random init.")
        model = resnet18(weights=None)

    model.fc = nn.Linear(model.fc.in_features, num_classes)

    class_weights = compute_class_weights(dataset)
    criterion = nn.CrossEntropyLoss(weight=class_weights)
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    model.train()
    for epoch in range(epochs):
        running_loss = 0.0
        for inputs, labels in loader:
            optimizer.zero_grad()
            outputs = model(inputs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()
        print(f"📈 Epoch {epoch + 1}/{epochs}: Avg Loss = {running_loss / len(loader):.4f}")

    os.makedirs("model", exist_ok=True)
    torch.save(model.state_dict(), "model/retino_model.pth")
    print("✅ Model saved to model/retino_model.pth")

if __name__ == "__main__":
    train_model("train")

