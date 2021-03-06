import sys
class bcolors:
    
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ORANGE = '\u001b[38;5;208m'

    c = [HEADER, OKBLUE, OKCYAN, OKGREEN, WARNING, FAIL, ENDC, BOLD, UNDERLINE, ORANGE]

    def test():
        for color in bcolors.c:
            print(color + "Warning: No active frommets remain. Continue?" + bcolors.ENDC)

    def set_original():
        return bcolors.ENDC

    def set_by_cube_id(x):
        if x == 0 or x not in [1, 2, 3, 4, 5]:
            return bcolors.ENDC
        elif x == 1:
            return bcolors.ORANGE
        elif x == 2:
            return bcolors.OKBLUE
        elif x == 3:
            return bcolors.FAIL
        elif x == 4:
            return bcolors.OKGREEN
        elif x == 5:
            return bcolors.WARNING

    def tile_by_cube_id(x):
        if x == 0 or x not in [1, 2, 3, 4, 5]:
            return 'β¬'
        elif x == 1:
            return 'π§'
        elif x == 2:
            return 'π¦'
        elif x == 3:
            return 'π₯'
        elif x == 4:
            return 'π©'
        elif x == 5:
            return 'π¨'

    

    def ANSI_codes():
        for i in range(0, 16):
            for j in range(0, 16):
                code = str(i * 16 + j)
                sys.stdout.write(u"\u001b[38;5;" + code + "m" + code.ljust(4))
            print(u"\u001b[0m")


import numpy as np
def rotate_2dim_array(arr, d, add_0dim=False): # 2μ°¨μ λ°°μ΄μ 90λ λ¨μλ‘ νμ ν΄ λ°ννλ€. 
    # μ΄λ μ λ°°μ΄μ μ μ§λλ©°, μλ‘μ΄ λ°°μ΄μ΄ νμνλ€. 
    # μ΄λ νμ μ΄ 360λ λ¨μμΌ λλ ν΄λΉνλ€. 
    # 2μ°¨μ λ°°μ΄μ νκ³Ό μ΄μ μκ° κ°μ μ λ°©ν λ°°μ΄μ΄μ΄μΌ νλ€.
    # arr: νμ νκ³ μ νλ 2μ°¨μ λ°°μ΄. μλ ₯μ΄ μ λ°©ν νλ ¬μ΄λΌκ³  κ°μ νλ€. 
    # d: 90λμ©μ νμ  λ¨μ. -1: -90λ, 1: 90λ, 2: 180λ, ...

    size = len(arr)
    ret = np.zeros([size, size], dtype=int)

    N = size - 1
    if d % 4 not in (1, 2, 3, 4, 5, 6, 7): 
        for r in range(size): 
            for c in range(size): 
                ret[r][c] = arr[r][c] 
    elif d % 4 == 1:
        for r in range(size): 
            for c in range(size): 
                ret[c][N-r] = arr[r][c] 
    elif d % 4 == 2: 
        for r in range(size): 
            for c in range(size): 
                ret[N-r][N-c] = arr[r][c] 
    elif d % 4 == 3: 
        for r in range(size): 
            for c in range(size): 
                ret[N-c][r] = arr[r][c] 

    # elif d % 8 == 4:
    #     for r in range(size): 
    #         for c in range(size): 
    #             ret[r][N-c] = arr[r][c]
    # elif d % 8 == 5: # arr.T
    #     for r in range(size): 
    #         for c in range(size): 
    #             ret[N-c][N-r] = arr[r][c]
    # elif d % 8 == 6:
    #     for r in range(size): 
    #         for c in range(size): 
    #             ret[N-r][c] = arr[r][c]
    # elif d % 8 == 7:
    #     for r in range(size): 
    #         for c in range(size): 
    #             ret[c][r] = arr[r][c]

    if not add_0dim:
        return ret
    else:
        return ret.reshape(1, size, size)
