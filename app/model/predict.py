from torchvision import models, transforms
from PIL import Image
import torch
import torch.nn.functional as F

def predict_image(image_path):
    model = models.resnet18(pretrained=False)
    model.fc = torch.nn.Linear(model.fc.in_features, 5)
    model.load_state_dict(torch.load("model/retino_model.pth", map_location=torch.device('cpu')))
    model.eval()

    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])

    image = Image.open(image_path).convert('RGB')
    image = transform(image).unsqueeze(0)

    with torch.no_grad():
        outputs = model(image)
        probs = F.softmax(outputs, dim=1)
        _, predicted = torch.max(probs, 1)
        return predicted.item(), probs.squeeze().tolist()

