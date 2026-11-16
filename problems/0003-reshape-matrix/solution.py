import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    a_=np.array(a)
    if a_.size==new_shape[0]*new_shape[1]:
        
        new_a=a_.reshape(new_shape[0],new_shape[1])
        return new_a.tolist()

    else:
        return []
