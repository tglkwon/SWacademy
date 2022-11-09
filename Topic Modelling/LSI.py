import numpy as np

D = ['d1', 'd2', 'd3', 'd4', 'd5', 'd6']
V = ['ship', 'boat', 'ocean', 'wood', 'tree']
M = len(V)
N = len(D)

# C = np.zeros((M,N))
C = np.array([[1,0,1,0,0,0],
              [0,1,0,0,0,0],
              [1,1,0,0,0,0],
              [1,0,0,1,1,0],
              [0,0,0,1,0,1]])


U, S, Vt = np.linalg.svd(C, full_matrices=False)

S = np.diag(S)
C_ = U.dot(S).dot(Vt)

print(np.dot(C[:,1], C[:,2]), np.dot(C_[:,1], C_[:,2]))

print(np.round(C.T.dot(C)/np.outer(np.linalg.norm(C, axis=0)*np.linalg.norm(C.T, axis=1))), 2)
print(np.round(C_.T.dot(C_)/np.outer(np.linalg.norm(C_, axis=0)*np.linalg.norm(C_.T, axis=1))), 2)