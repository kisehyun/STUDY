import pandas as pd
from sklearn.model_selection import train_test_split

import torch
from torch.utils.data import *

import warnings
warnings.filterwarnings('ignore')

def get_data(file_path) :
    """
    파일 불러와서 torch input으로 바꾸는 코드
    
    Args :
     - file_path : csv 파일
     
    Return :
     - lab_dl : labeled data loader
     - unlabl_dl : unlabeled data loader
     - te_dl : test data loader
    """
    
    data = pd.read_csv(file_path)
    X = data.iloc[:, 1:-1].values
    y = data['전화해지여부'].values
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42, shuffle = True, stratify = y)
    X_train, X_unlab, y_train, _ = train_test_split(X_train, y_train, test_size = 0.2, random_state = 42, shuffle = True, stratify = y_train)
    
    X_lab = torch.tensor(X_train, dtype = torch.float64)
    y_lab = torch.tensor(y_train, dtype = torch.float64)

    X_unlab = torch.tensor(X_unlab, dtype = torch.float64)

    X_test = torch.tensor(X_test, dtype = torch.float64)
    y_test = torch.tensor(y_test, dtype = torch.float64)
    
    lab_ts = TensorDataset(X_lab, y_lab)
    unlab_ts = TensorDataset(X_unlab)
    te_ts = TensorDataset(X_test, y_test)
    
    lab_dl = DataLoader(lab_ts, batch_size = 64, drop_last = True, shuffle = False)
    unlab_dl = DataLoader(unlab_ts, batch_size = 64, drop_last = True, shuffle = False)
    te_dl = DataLoader(te_ts, batch_size = 64, drop_last = False, shuffle = False)
    
    return lab_dl, unlab_dl, te_dl