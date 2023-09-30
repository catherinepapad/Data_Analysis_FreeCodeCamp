import numpy as np

def calculate(list):
  if len(list) != 9:
    raise ValueError('List must contain nine numbers.')
  else:
    array_flattended = np.array(list)
    array_2D = array_flattended.reshape([3,3])
  
    mean_list = [array_2D.mean(axis=0).tolist(), array_2D.mean(axis=1).tolist(), array_flattended.mean()]   

    variance_list = [array_2D.var(axis=0).tolist(), array_2D.var(axis=1).tolist(),      array_flattended.var()]

    std_list = [array_2D.std(axis=0).tolist(), array_2D.std(axis=1).tolist(),      array_flattended.std()]

    max_list = [array_2D.max(axis=0).tolist(), array_2D.max(axis=1).tolist(),      array_flattended.max()]

    min_list = [array_2D.min(axis=0).tolist(), array_2D.min(axis=1).tolist(),      array_flattended.min()]

    sum_list = [array_2D.sum(axis=0).tolist(), array_2D.sum(axis=1).tolist(),      array_flattended.sum()]

    calculations = {
    'mean': mean_list,
    'variance': variance_list,
    'standard deviation': std_list,
    'max': max_list,
    'min': min_list,
    'sum': sum_list
    }
    return calculations