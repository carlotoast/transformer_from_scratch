import torch
import torch.nn as nn
import math
x = torch.arange(6)          # tensor([0, 1, 2, 3, 4, 5])
x=x.view(2, 3)                 # reshape to 2 rows, 3 columns

print(x.shape)