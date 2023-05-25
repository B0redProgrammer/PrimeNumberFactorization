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
            primes.append(int(line))

    return primes.sort()


class Dataset(Dataset):
    def __init__(self, transforms):
        primes = extract_files()

        self.dataset = torch.zeros(len(primes))
        self.transforms = transforms

        for i, prime_number in enumerate(primes):
            self.dataset[i] = prime_number

    def __len__(self):
        return len(self.dataset)

    def __getitem(self, ind):
        if self.transforms != None:
            return (ind+1, transforms(dataset[ind]))
        return (ind+1, dataset[ind])

dataset = Dataset()

batch_size = 10
data_loader = DataLoader(dataset, batch_size = batch_size, shuffle = True)

model = nn.Sequential(
        nn.Linear(1, 10),
        nn.LeakyReLU(),

        nn.Linear(10, 10),
        nn.LeakyReLU(),

        nn.Linear(10, 1),
        nn.LeakyReLU()
)

def eval(input, key):
    
