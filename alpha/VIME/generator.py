import numpy as np
import torch

def mask_generator(p_m, x) :
    """
    마스킹 벡터 생성
    
    Args :
     - p_m : corruption 비율
     - x : feature matrix
     
    Returns :
     - masked_matrix : 마스킹된 binary matrix
    """
    masked_idx = np.random.binomial(1, p_m, x.shape)
    
    return masked_idx

def pretext_generator(m, x) :
    
    """
    corrupted sample 생성
    
    Args :
     - m : masked matrix
     - x : feature matrix
     
    Returns :
     - corrupted_m : masked matrix after corruption
     - x_tilde : corrupted feature matrix
    """
    
    nrow, ncol = x.shape
    x_ = np.zeros([nrow, ncol])
    for n_th in range(ncol) :
        idx = np.random.permutation(nrow)
        ### permutation 된 값으로 nrow * ncol 행렬의 n_th 컬럼의 값을 채운다.
        x_[:, n_th] = x[idx, n_th]
    
    ### corrupted samples
    x_tilde = x * (1 - m) + x_ * m
    ### new masked matrix -> label
    corrupted_m = torch.tensor(1 * (x != x_tilde), dtype = torch.float64)
    
    return x_tilde, corrupted_m