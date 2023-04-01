import torch
import torch.nn as nn
import torch.optim as optim

class VIME_SELF(nn.Module) :
    
    def __init__(self, num_features) :
        
        super(VIME_SELF, self).__init__()
        self.encoder = nn.Sequential(
                                    nn.Linear(num_features, 32, dtype = torch.float64),
                                    nn.LeakyReLU(),
                                    nn.Linear(32, 16, dtype = torch.float64),
                                    nn.LeakyReLU(),
                                    nn.Linear(16, num_features, dtype = torch.float64)
                                    )
        
        self.classifier = nn.Sequential(
                                        nn.Linear(num_features, num_features, dtype = torch.float64),
                                        nn.Sigmoid()
                                       )
        
    def forward(self, x) :
        
        extracted_feature = self.encoder(x)
        prediction = self.classifier(extracted_feature)
        
        return extracted_feature, prediction
