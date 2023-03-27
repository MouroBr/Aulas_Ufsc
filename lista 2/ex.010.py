A, B, C = map(int, input().split())

if A < B < C or C < B < A:
    viceCampeao = B
    
elif B < A < C or C < A < B:
    viceCampeao = A
    
else:
    viceCampeao = C

print(viceCampeao)

