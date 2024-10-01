''' tässä koodia '''
def kertoma(n):
    if n == 1:
        return 1
    else:
        return n * kertoma(n - 1)

# tästä taitaa kyllä tulla pythonin stack overflow
kertoma(2000)