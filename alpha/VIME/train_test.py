from sklearn.metrics import f1_score
import torch
from generator import mask_generator, pretext_generator
from torch.utils.data import TensorDataset, DataLoader

def MLP_TRAIN(num_epochs, model, dl, criterion, threshold, optimizer, device) :
    """
    NN 모델 학습 -> threshold 기준으로 binary label로 변환하여 macro f1 score 확인
    
    Args :
     - num_epochs : epoch 수
     - model : NN 모델
     - dl : data loader
     - criterion : loss function
     - threshold : prediction threshold
     - optimizer : optimizer
     - device : device
     
    Return :
     - model : NN 모델
    """

    for epoch in range(num_epochs) :

        model.train()
        loss_t = 0.
        f1_t = 0

        for xx, yy in dl :

            optimizer.zero_grad()
            
            xx = xx.to(device)
            yy = yy.to(device)

            pred = model(xx).reshape(-1, )

            loss = criterion(pred, yy)
            loss.backward()
            loss_t += loss.item() / len(dl)

            cls = torch.tensor([1. if p >= threshold else 0. for p in pred])
            score = f1_score(yy, cls, average = 'macro')
            f1_t += score / len(dl)

            optimizer.step()

        print(f'{epoch + 1} Epoch Loss : {loss} F1 score : {f1_t}')
        
    return model


def MLP_TEST_RESULT(model, dl, threshold, device) :
    """
    NN 모델의 test 데이터에 대한 prediction + f1 score 출력
    
    Args :
     - model : 학습된 NN model
     - dl : test data loader
     - threshold : prediction threshold
     - device : device
    """
                    
    y_pred = []
    y_actual = []
    
    with torch.no_grad() :

        model.eval()

        for xx, yy in dl :

            xx = xx.to(device)
            yy = yy.to(device)

            pred = model(xx)
            y_pred += [1 if p >= threshold else 0 for p in pred]
            y_actual += yy
            
    score = f1_score(y_actual, y_pred, average = 'macro')
    print(f'F1 Score is {score}')


def VIME_SELF_TRAIN(num_epochs, model, dl, criterion1, criterion2, lambda_, p_m, optimizer, device) :
    """
    vime self model 학습
    
    Args :
     - num_epochs : epoch 수
     - model : vime self model
     - dl : unlabeld data loader
     - criterion1 : masking index loss
     - criterion2 : feature loss
     - lambda_ : criterion2 weight
     - p_m : corrupt ratio
     - optimizer : optimzier
     - device : device
     
    Return :
     - model : 학습된 vime self model
    """
    
    for epoch in range(num_epochs) :

        model.train()
        total_l_s = 0.
        total_l_u = 0.

        for xx in dl :

            optimizer.zero_grad()
            xx = xx[0].to(device)

            m = mask_generator(p_m, xx)
            x_tilde, corrupted_m = pretext_generator(m, xx)

            ef, pred = model(x_tilde)
            pred = torch.tensor(pred >= 0.5, dtype = torch.float64)
            l_s = criterion1(pred, corrupted_m)
            l_u = criterion2(ef, xx)

            total_l_s += l_s.item() / len(dl)
            total_l_u += l_u.item() / len(dl)

            loss = l_s + lambda_ * l_u
            loss.backward()
            optimizer.step()

        print(f'{epoch + 1} Epoch Masking Loss : {total_l_s} & Feature Loss : {total_l_u}')
        
    return model


def VIME_SAMPLE(num_features, model, dl, batch_size, device) :
    """
    학습된 vime self model로 labeld data feature extraction
    
    Args :
     - num_features : feature 수
     - model : fitted vime self model
     - dl : labeled data loader
     - batch_size : batch_size
     - device : device
    
    Return :
     - vime_dl : data loader using vime self model
    """
    
    X_ = torch.zeros(0, num_features)
    y_ = torch.zeros(0)
    with torch.no_grad() :
        model.eval()
        for xx, yy in dl :

            xx = xx.to(device)
            yy = yy.to(device)

            ef, pred = model(xx)
            
            X_ = torch.cat((X_, ef), 0)
            y_ = torch.cat([y_, yy], 0)
            
    ts = TensorDataset(X_, y_)
    vime_dl = DataLoader(ts, batch_size = batch_size, shuffle = False, drop_last = False)
    
    return vime_dl