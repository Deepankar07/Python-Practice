A = [3, 4, 8]
B = [6, 2, 1]


def cross(A, B):
    if (A[0]*B[2] - A[2]*B[0])<0:
        return f"{A[1]*B[2] - A[2]*B[1]}i + {-A[0]*B[2] + A[2]*B[0]}j + {A[0]*B[1] - A[1]*B[0]}k"
    else:
        return f"{A[1]*B[2] - A[2]*B[1]}i - {A[0]*B[2] - A[2]*B[0]}j + {A[0]*B[1] - A[1]*B[0]}k"
    

print("The cross product of A cross B is: \n", cross(A, B))