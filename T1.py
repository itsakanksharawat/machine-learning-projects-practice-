import torch
import torch.nn as nn
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms
from torch.utils.data import DataLoader
from fpdf import FPDF # Run 'pip install fpdf'
import matplotlib.pyplot as plt
# Use a raw string with an absolute path
# If your folder is C:\Users\akank\OneDrive\Desktop\CIFR\data\cifar-100-python
# Then set root to the parent folder:
DATA_PATH = r'C:\Users\akank\OneDrive\Desktop\CIFR\data'

train_set = torchvision.datasets.CIFAR100(
    root=DATA_PATH, 
    train=True, 
    download=False,  # Set to False to stop the auto-download
    transform=train_transform
)
# 1. Pipeline Definition: Data Augmentation & Normalization
# Calculating stats on train set only avoids leakage
train_transform = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.RandAugment(), # Powerful augmentation to reduce memorization
    transforms.ToTensor(),
    transforms.Normalize((0.507, 0.487, 0.441), (0.267, 0.256, 0.276))
])

test_transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.507, 0.487, 0.441), (0.267, 0.256, 0.276))
])

# 2. Loading Data
# Change this line:
train_set = torchvision.datasets.CIFAR100(root=r'C:\Your\Correct\Path', train=True, download=False, transform=train_transform)
test_set = torchvision.datasets.CIFAR100(root='./data', train=False, download=True, transform=test_transform)

train_loader = DataLoader(train_set, batch_size=128, shuffle=True)
test_loader = DataLoader(test_set, batch_size=128, shuffle=False)
# ... [Keep your existing train_transform, test_transform, and loaders] ...

# 3. Add Evaluation Function
def evaluate(model, loader):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, targets in loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            _, predicted = torch.max(outputs.data, 1)
            total += targets.size(0)
            correct += (predicted == targets).sum().item()
    return 100 * correct / total

# 4. Main Training Loop with Logging
history = {'train_loss': [], 'test_acc': []}
for epoch in range(200):
    model.train()
    running_loss = 0.0
    for inputs, targets in train_loader:
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
    
    scheduler.step()
    test_acc = evaluate(model, test_loader)
    history['train_loss'].append(running_loss / len(train_loader))
    history['test_acc'].append(test_acc)
    
    print(f"Epoch {epoch+1}: Test Acc: {test_acc:.2f}%")

# 5. PDF Report Generation
def generate_pdf_report(history):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="CIFAR-100 Training Report", ln=True, align='C')
    
    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Final Test Accuracy: {history['test_acc'][-1]:.2f}%", ln=True)
    pdf.cell(200, 10, txt=f"Total Epochs: {len(history['train_loss'])}", ln=True)
    
    # Save a plot of the history
    plt.figure()
    plt.plot(history['test_acc'], label='Test Accuracy')
    plt.savefig('performance.png')
    pdf.image('performance.png', x=10, y=50, w=150)
    
    pdf.output("Training_Report.pdf")

generate_pdf_report(history)