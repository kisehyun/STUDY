import torch
import torch.nn as nn
import torch.optim as optim


class MLP(nn.Module) :
    
    
    def __init__(self, num_features) :
        
        super(MLP, self).__init__()
        self.mlp = nn.Sequential(
            nn.Linear(num_features, 32, dtype = torch.float64),
            nn.LeakyReLU(),
            nn.Linear(32, 8, dtype = torch.float64),
            nn.LeakyReLU(),
            nn.Linear(8, 1, dtype = torch.float64),
            nn.Sigmoid()
        )
        
    def forward(self, x) :
        
        x = self.mlp(x)
        
        return x
    
    
    
