import numpy as np

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers")
    
    mtx = np.reshape(list, (3, 3))

    calculations = dict()
    calculations['mean'] = [np.mean(mtx, axis=0).tolist(), np.mean(mtx, axis=1).tolist(), np.mean(list).tolist()]
    calculations['variance'] = [np.var(mtx, axis=0).tolist(), np.var(mtx, axis=1).tolist(), np.var(list).tolist()]
    calculations['standard deviation'] = [np.std(mtx, axis=0).tolist(), np.std(mtx, axis=1).tolist(), np.std(list).tolist()]
    calculations['max'] = [np.max(mtx, axis=0).tolist(), np.max(mtx, axis=1).tolist(), np.max(list).tolist()]
    calculations['min'] = [np.min(mtx, axis=0).tolist(), np.min(mtx, axis=1).tolist(), np.min(list).tolist()]
    calculations['sum'] = [np.sum(mtx, axis=0).tolist(), np.sum(mtx, axis=1).tolist(), np.sum(list).tolist()]

    return calculations

