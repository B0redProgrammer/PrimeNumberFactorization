import torch
import torch.nn as nn

from torch.utils.data import DataLoader, Dataset

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

    primes.sort()
    return primes


class Dataset(Dataset):
    def __init__(self, transforms = None):
        primes = extract_files()

        self.dataset = torch.zeros(len(primes))
        self.transforms = transforms

        for i, prime_number in enumerate(primes):
            self.dataset[i] = prime_number

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, idx):
        if self.transforms != None:
            return (torch.tensor(idx+1), transforms(self.dataset[idx]))
        return (torch.tensor(int(idx+1)), self.dataset[idx])

dataset = Dataset()

batch_size = 10
data_loader = DataLoader(dataset, batch_size = batch_size, shuffle = True)

class newlayer(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = x.to(torch.float32)
        return x

model = nn.Sequential(
        newlayer(),
        nn.Linear(1, 10),
        nn.LeakyReLU(),

        newlayer(),
        nn.Linear(10, 10),
        nn.LeakyReLU(),

        newlayer(),
        nn.Linear(10, 1),
        nn.LeakyReLU()
)

def eval(input, key):
    for i, In in enumerate(input):
        eval = [1 if In == key[i] else 0]
    return accs

def fit(num_epochs):
    losses, accs = [], []
    opt = torch.optim.Adam(model.parameters(), lr = 0.002)
    loss_fn = nn.CrossEntropyLoss()

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
        print("Epoch [{}/{}], Loss = {}".format(epoch+1, num_epochs, sum(losses)/len(losses)))
fit(2)
