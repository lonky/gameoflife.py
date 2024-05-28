
#           0 1 2 3 4 5 6 7 8 9 101112131415
# raw_input = [. . . . . . . . . . . . . . . .]
#    1     [. . . . . . . . . . . . . . . .]\ 
#    2     [. . . . . . . . . . . . . . . .]\
#    3     [. . . . . . . . . . . . . . . .]\ 
#    4     [. . . . . . . . . . . . . . . .]\ 
#    5     [. . . . . . . . . . . . . . . .]\ 
#    6     [. . . . . . . . . . . . . . . .]\ 
#    7     [. . . . . . . . . . . . . . . .]\ 
#    8     [. . . . . . . . . . . . . . . .]\ 
#    9     [. . . . . . . . . . . . . . . .]\ 
#    10    [. . . . . . . . . . . . . . . .]\ 
#    11    [. . . . . . . . . . . . . . . .]\ 
#    12    [. . . . . . . . . . . . . . . .]\ 
#    13    [. . . . . . . . . . . . . . . .]\ 
#    14    [. . . . . . . . . . . . . . . .]\ 

s_canvas = [[0 for i in range(16)] for j in range(16)] 


def nd():
    s_canvas[3][3] = 1
    s_canvas[3][4] = 1
    s_canvas[4][3] = 1
    s_canvas[4][4] = 1

    s_canvas[8][3] = 1
    s_canvas[8][4] = 1
    s_canvas[8][5] = 1
    s_canvas[9][2] = 1
    s_canvas[9][4] = 1
    s_canvas[10][3] = 1

    return s_canvas


def set_default(s_canvas):
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


def set_diehard():
    s_canvas[5][2] = 1
    s_canvas[5][3] = 1
    s_canvas[6][3] = 1

    s_canvas[4][8] = 1
    s_canvas[6][7] = 1
    s_canvas[6][8] = 1
    s_canvas[6][9] = 1

    return s_canvas


