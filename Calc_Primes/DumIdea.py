import torch
import torch.nn as nn

from torch.utils.data import DataLoader, Dataset

import random

def extract_files():
    files = [open("1.txt", "r"),
             open("3.txt", "r"),
             open("7.txt", "r"),
             open("9.txt", "r")]

    primes = [1, 2, 3, 7, 9]

    for file in files:
        for line in file:
            try:
                line = line.replace(r"\n", "")
                primes.append(int(line))
            except:
                pass
        file.close()

    primes.sort()

    for i, prime in enumerate(primes):
        primes[i] = (i, prime)

    return primes


class Dataset(Dataset):
    def __init__(self, transforms = None):
        self.dataset = extract_files()[:1000000]
        random.shuffle(self.dataset)


        self.transforms = transforms

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        if self.transforms != None:
            return (self.transforms(torch.tensor(self.dataset[idx][0])), self.transforms(torch.tensor(self.dataset[idx][1])))
        return (torch.tensor(self.dataset[idx][0]), torch.tensor(self.dataset[idx][1]))

dataset = Dataset()

batch_size = 5
data_loader = DataLoader(dataset, batch_size = batch_size, shuffle = True)

class newlayer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = x.to(torch.float32)
        return x

class roundinglayer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        return torch.tensor(round(x.item()), dtype = torch.float32, requires_grad=True)

model = nn.Sequential(
        newlayer(),
        nn.Linear(1, 100),
        nn.LeakyReLU(),

        newlayer(),
        nn.Linear(100, 100),
        nn.LeakyReLU(),

        newlayer(),
        nn.Linear(100, 10),
        nn.LeakyReLU(),

        newlayer(),
        nn.Linear(10, 1),
        roundinglayer()
)

def fit(num_epochs):
    losses, accs = [], []
    opt = torch.optim.Adam(model.parameters(), lr = 0.000002)
    loss_fn = nn.L1Loss()

    for epoch in range(num_epochs):
        for i, (data, label) in enumerate(dataset):
            data = data.reshape(1, 1)
            label = label.reshape(1, 1)

            output = model(data)
            loss = loss_fn(output, label)

            loss.backward()
            opt.step()
            opt.zero_grad()

            losses.append(loss)

            if i % 100000 == 0:
                print("Current loss = {}".format(sum(losses)/len(losses)))
                losses = []
        print("Epoch [{}/{}], Loss = {}".format(epoch+1, num_epochs, sum(losses)/len(losses)))
fit(2)

while True:
    Input = torch.tensor(int(input("Prime number:"))).reshape(1,1)
    output = model(Input)
    print(output)
