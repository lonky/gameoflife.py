if __name__ == '__main__':
    print("Execution")
else:
    print('Importing a', __name__)

import time


canvas = [[0 for i in range(16)] for j in range(16)] 

#           0 1 2 3 4 5 6 7 8 9 101112131415
#    0     [. . . . . . . . . . . . . . . .] 
#    1     [. . . . . . . . . . . . . . . .] 
#    2     [. . . . . . . . . . . . . . . .] 
#    3     [. . . . . . . . . . . . . . . .] 
#    4     [. . . . . . . . . . . . . . . .] 
#    5     [. . . . . . . . . . . . . . . .] 
#    6     [. . . . . . . . . . . . . . . .] 
#    7     [. . . . . . . . . . . . . . . .] 
#    8     [. . . . . . . . . . . . . . . .] 
#    9     [. . . . . . . . . . . . . . . .] 
#    10    [. . . . . . . . . . . . . . . .] 
#    11    [. . . . . . . . . . . . . . . .] 
#    12    [. . . . . . . . . . . . . . . .] 
#    13    [. . . . . . . . . . . . . . . .] 
#    14    [. . . . . . . . . . . . . . . .] 
#    15    [. . . . . . . . . . . . . . . .] 


def canvas_state(s_canvas):
    s_canvas[1][1] = 1
    s_canvas[1][2] = 1
    s_canvas[2][1] = 1
    s_canvas[2][3] = 1
    s_canvas[3][3] = 1
    s_canvas[4][3] = 1
    s_canvas[4][4] = 1

    s_canvas[7][5] = 1
    s_canvas[7][6] = 1
    s_canvas[7][7] = 1

    s_canvas[10][0] = 1
    s_canvas[11][1] = 1
    s_canvas[12][0] = 1

    s_canvas[2][10] = 1
    s_canvas[2][11] = 1
    s_canvas[2][12] = 1
    s_canvas[1][12] = 1
    s_canvas[0][11] = 1

    return s_canvas


def draw_canvas(d_canvas):
    print(' |\t', f'{[n for n in range(10)]}101112131415|'.replace("'", "").replace(",", "").replace("[", "| ").replace("]",  ""))
    for i, j in enumerate(d_canvas):
        print(f'{i}|\t', f'{j}'.replace("0","\u00B7").replace("1","\u2588").replace("'", "").replace(",", "").replace("[", "| ").replace("]",  "|"))

# def check_cell(cell):
#     tmp = 0


def check_neigbours(_canvas):
    tmp_canvas = [[0 for i in range(16)] for j in range(16)] 
    w = len(_canvas[0]) -1
    h = len(_canvas) - 1
    tmp = 0
    for n, i in enumerate(_canvas):
	    for p, j in enumerate(i):
		    for x in (-1, 0, 1):
			    for y in (-1, 0, 1):
			        if (x == 0) & (y == 0):
				        continue
				    dex_n = (x + n) % h
					dex_p = (y + p) % w
				    if _canvas[dex_n][dex_p] == 1:
				       tmp += 1
			if _canvas[n][j] == 1:
			    tmp += 1
				if (tmp in range(3, 5)):
				    tmp_canvas += 1
			else:
				if tmp == 3:
				    tmp_canvas += 1
        for p, j in enumerate(i):
            # Check for element 0 in 0 line
            if (n == 0) & (p == 0):
                # 1
                if _canvas[h][w] == 1:
                    tmp += 1
                # 2
                if _canvas[h][p] == 1:
                    tmp += 1
                # 3
                if _canvas[h][p+1] == 1:
                    tmp += 1
                # 4
                if _canvas[n][w] == 1:
                    tmp += 1
                # 5
                if _canvas[n][p+1] == 1:
                    tmp += 1
                # 6
                if _canvas[n+1][w] == 1:
                    tmp += 1
                # 7
                if _canvas[n+1][p] == 1:
                    tmp += 1
                # 8
                if _canvas[n+1][p+1] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Check for elements in 0 line where p in range(1, w)
            if (n == 0) & (p > 0) & (p < w):
                # 1
                if _canvas[h][p-1] == 1:
                    tmp += 1
                # 2
                if _canvas[h][p] == 1:
                    tmp += 1
                # 3
                if _canvas[h][p+1] == 1:
                    tmp += 1
                # 4
                if _canvas[n][p-1] == 1:
                    tmp += 1
                # 5
                if _canvas[n][p+1] == 1:
                    tmp += 1
                # 6
                if _canvas[n+1][p-1] == 1:
                    tmp += 1
                # 7
                if _canvas[n+1][p] == 1:
                    tmp += 1
                # 8
                if _canvas[n+1][p+1] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Check for 0 line and last element
            if (n == 0) & (p == w):
                # 1
                if _canvas[h][p-1] == 1:
                    tmp += 1
                # 2
                if _canvas[h][p] == 1:
                    tmp += 1
                # 3
                if _canvas[h][0] == 1:
                    tmp += 1
                # 4
                if _canvas[n][p-1] == 1:
                    tmp += 1
                # 5
                if _canvas[n][0] == 1:
                    tmp += 1
                # 6
                if _canvas[n+1][p-1] == 1:
                    tmp += 1
                # 7
                if _canvas[n+1][p] == 1:
                    tmp += 1
                # 8
                if _canvas[n+1][0] == 1:
                    tmp += 1

                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Checks for First elements in lines n in range(1, h)
            if (n > 0) & (n < h) & (p == 0):
                # 1
                if _canvas[n-1][w] == 1:
                    tmp += 1
                # 2
                if _canvas[n-1][p] == 1:
                    tmp += 1
                # 3
                if _canvas[n-1][p+1] == 1:
                    tmp += 1
                # 4
                if _canvas[n][w] == 1:
                    tmp += 1
                # 5
                if _canvas[n][p+1] == 1:
                    tmp += 1
                # 6
                if _canvas[n+1][w] == 1:
                    tmp += 1
                # 7
                if _canvas[n+1][p] == 1:
                    tmp += 1
                # 8
                if _canvas[n+1][p+1] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Checks for elements n > 0 and p in range(1, w)
            if (n > 0) & (n < h) & (p > 0) & (p < w):
                # 1
                if _canvas[n-1][p-1] == 1:
                    tmp += 1
                # 2
                if _canvas[n-1][p] == 1:
                    tmp += 1
                # 3
                if _canvas[n-1][p+1] == 1:
                    tmp += 1
                # 4
                if _canvas[n][p-1] == 1:
                    tmp += 1
                # 5
                if _canvas[n][p+1] == 1:
                    tmp += 1
                # 6
                if _canvas[n+1][p-1] == 1:
                    tmp += 1
                # 7
                if _canvas[n+1][p] == 1:
                    tmp += 1
                # 8
                if _canvas[n+1][p+1] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Checks for Last elements n > 0
            if (n > 0) & (n < h) & (p == w):
                # 1
                if _canvas[n-1][p-1] == 1:
                    tmp += 1
                # 2
                if _canvas[n-1][p] == 1:
                    tmp += 1
                # 3
                if _canvas[n-1][0] == 1:
                    tmp += 1
                # 4
                if _canvas[n][p-1] == 1:
                    tmp += 1
                # 5
                if _canvas[n][0] == 1:
                    tmp += 1
                # 6
                if _canvas[n+1][p-1] == 1:
                    tmp += 1
                # 7
                if _canvas[n+1][p] == 1:
                    tmp += 1
                # 8
                if _canvas[n+1][0] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Check for element 0 in Last line
            if (n == h) & (p == 0):
                # 1
                if _canvas[n-1][w] == 1:
                    tmp += 1
                # 2
                if _canvas[n-1][p] == 1:
                    tmp += 1
                # 3
                if _canvas[n-1][p+1] == 1:
                    tmp += 1
                # 4
                if _canvas[n][w] == 1:
                    tmp += 1
                # 5
                if _canvas[n][p+1] == 1:
                    tmp += 1
                # 6
                if _canvas[0][w] == 1:
                    tmp += 1
                # 7
                if _canvas[0][p] == 1:
                    tmp += 1
                # 8
                if _canvas[0][p+1] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Check for elements p in range(1, w) in Last line
            if (n == h) & (p > 0) & (p < w):
                # 1
                if _canvas[n-1][p-1] == 1:
                    tmp += 1
                # 2
                if _canvas[n-1][p] == 1:
                    tmp += 1
                # 3
                if _canvas[n-1][p+1] == 1:
                    tmp += 1
                # 4
                if _canvas[n][p-1] == 1:
                    tmp += 1
                # 5
                if _canvas[n][p+1] == 1:
                    tmp += 1
                # 6
                if _canvas[0][p-1] == 1:
                    tmp += 1
                # 7
                if _canvas[0][p] == 1:
                    tmp += 1
                # 8
                if _canvas[0][p+1] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
            # Check for Last element in Last line
            if (n == h) & (p == w):
                # 1
                if _canvas[n-1][p-1] == 1:
                    tmp += 1
                # 2
                if _canvas[n-1][p] == 1:
                    tmp += 1
                # 3
                if _canvas[n-1][0] == 1:
                    tmp += 1
                # 4
                if _canvas[n][p-1] == 1:
                    tmp += 1
                # 5
                if _canvas[n][0] == 1:
                    tmp += 1
                # 6
                if _canvas[0][p-1] == 1:
                    tmp += 1
                # 7
                if _canvas[0][p] == 1:
                    tmp += 1
                # 8
                if _canvas[0][0] == 1:
                    tmp += 1
                # Set life or death
                if j == 1:
                    tmp += 1
                    if tmp in range(3, 5):
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
                if j == 0:
                    if tmp == 3:
                        tmp_canvas[n][p] = 1
                        tmp = 0
                    else:
                        tmp_canvas[n][p] = 0
                        tmp = 0
>>>>>>> a4220ffe01c3d8ef44ede75b657a4480a5433dbe
    return tmp_canvas

#def check_canvas(_canvas):
#    tmp_canvas = [[0 for i in range(16)] for j in range(16)] 
#    w = len(_canvas[0]) -1
#    h = len(_canvas) - 1
#    tmp = 0
#    for n, i in enumerate(_canvas):
#        for p, j in enumerate(i):
#            # Check for element 0 in 0 line
#            if (n == 0) & (p == 0):
#                # 1
#                if _canvas[h][w] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[h][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[h][p+1] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][w] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][p+1] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[n+1][w] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[n+1][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[n+1][p+1] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Check for elements in 0 line where p in range(1, w)
#            if (n == 0) & (p > 0) & (p < w):
#                # 1
#                if _canvas[h][p-1] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[h][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[h][p+1] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][p-1] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][p+1] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[n+1][p-1] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[n+1][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[n+1][p+1] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Check for 0 line and last element
#            if (n == 0) & (p == w):
#                # 1
#                if _canvas[h][p-1] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[h][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[h][0] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][p-1] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][0] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[n+1][p-1] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[n+1][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[n+1][0] == 1:
#                    tmp += 1
#
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Checks for First elements in lines n in range(1, h)
#            if (n > 0) & (n < h) & (p == 0):
#                # 1
#                if _canvas[n-1][w] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[n-1][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[n-1][p+1] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][w] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][p+1] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[n+1][w] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[n+1][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[n+1][p+1] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Checks for elements n > 0 and p in range(1, w)
#            if (n > 0) & (n < h) & (p > 0) & (p < w):
#                # 1
#                if _canvas[n-1][p-1] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[n-1][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[n-1][p+1] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][p-1] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][p+1] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[n+1][p-1] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[n+1][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[n+1][p+1] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Checks for Last elements n > 0
#            if (n > 0) & (n < h) & (p == w):
#                # 1
#                if _canvas[n-1][p-1] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[n-1][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[n-1][0] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][p-1] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][0] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[n+1][p-1] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[n+1][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[n+1][0] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Check for element 0 in Last line
#            if (n == h) & (p == 0):
#                # 1
#                if _canvas[n-1][w] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[n-1][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[n-1][p+1] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][w] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][p+1] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[0][w] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[0][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[0][p+1] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Check for elements p in range(1, w) in Last line
#            if (n == h) & (p > 0) & (p < w):
#                # 1
#                if _canvas[n-1][p-1] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[n-1][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[n-1][p+1] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][p-1] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][p+1] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[0][p-1] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[0][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[0][p+1] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#            # Check for Last element in Last line
#            if (n == h) & (p == w):
#                # 1
#                if _canvas[n-1][p-1] == 1:
#                    tmp += 1
#                # 2
#                if _canvas[n-1][p] == 1:
#                    tmp += 1
#                # 3
#                if _canvas[n-1][0] == 1:
#                    tmp += 1
#                # 4
#                if _canvas[n][p-1] == 1:
#                    tmp += 1
#                # 5
#                if _canvas[n][0] == 1:
#                    tmp += 1
#                # 6
#                if _canvas[0][p-1] == 1:
#                    tmp += 1
#                # 7
#                if _canvas[0][p] == 1:
#                    tmp += 1
#                # 8
#                if _canvas[0][0] == 1:
#                    tmp += 1
#                # Set life or death
#                if j == 1:
#                    tmp += 1
#                    if tmp in range(3, 5):
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                if j == 0:
#                    if tmp == 3:
#                        tmp_canvas[n][p] = 1
#                        tmp = 0
#                    else:
#                        tmp_canvas[n][p] = 0
#                        tmp = 0
#                    continue
#                continue
#    return tmp_canvas


def main():
    frame = 1
    canvas_init = canvas_state(canvas)
    print(f'FRAME: {frame}')
    draw_canvas(canvas_init)
    for _ in range(0, 130):
        frame += 1
        next_canvas = check_neigbours(canvas_init)
        print(f'FRAME: {frame}')
        draw_canvas(next_canvas)
        canvas_init = next_canvas
        time.sleep(0.1)


main()

