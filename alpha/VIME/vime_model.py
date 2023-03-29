import torch
import torch.nn as nn
import torch.optim as optim

class VIME_SELF(nn.Module) :
    
    def __init__(self, num_input_features) :
        
        super(VIME_SELF, self).__init__()
        self.encoder = nn.Sequential(nn.Linear(num_input_features, 128, dtype = torch.float64),
                                    nn.LeakyReLU(),
                                    nn.Linear(128, 64, dtype = torch.float64),
                                    nn.LeakyReLU(),
                                    nn.Linear(64, 30, dtype = torch.float64))
        
    def forward(self, x) :
        
        x = self.encoder(x)
        
        return x
    
    
class Classifier(nn.Module) :
    
    def __init__(self, num_input_features) :
        
        super(Classifier, self).__init__()
        self.classifier = nn.Sequential(nn.Linear(num_input_features, 64, dtype = torch.float64),
                                    nn.LeakyReLU(),
                                    nn.Linear(64, 16, dtype = torch.float64),
                                    nn.LeakyReLU(),
                                    nn.Linear(16, 1, dtype = torch.float64))
        
    def forward(self, x) :
        
        x = self.classifier(x)
        
        return x