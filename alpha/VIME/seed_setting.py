import random
import numpy as np
import torch

def set_seed(n) :
    """
    결과 재현을 위한 seed 고정
    
    Args :
     - n : seed 번호
    """
    
    random.seed(n)
    np.random.seed(n)
    torch.manual_seed(n)
    print(f'seed is {n}...!')