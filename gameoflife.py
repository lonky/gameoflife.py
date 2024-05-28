if __name__ == '__main__':
    print("Execution")
else:
    print('Importing a', __name__)

import time
from diehard import set_diehard, nd


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


def default_canvas():
    s_canvas = [[0 for i in range(16)] for j in range(16)] 
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


def check_neigbours(_canvas):
    tmp_canvas = [[0 for i in range(16)] for j in range(16)] 
    w = len(_canvas[0])
    h = len(_canvas)
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
            if _canvas[n][p] == 1:
                tmp += 1
                if tmp in range(3, 5):
                    tmp_canvas[n][p] = 1
                tmp = 0
            else:
                if tmp == 3:
                    tmp_canvas[n][p] = 1
                tmp = 0
    return tmp_canvas


def main():
    canvas = input('Enter "d" for default state:\nEnter "die" for diehard pattern:\n')
    if canvas == 'd':
        canvas = default_canvas()
    if canvas == 'die':
        canvas = set_diehard()
    if canvas == 'nd':
        canvas = nd()
    frame = 1
    print(f'FRAME: {frame}')
    draw_canvas(canvas)
    for _ in range(0, 150):
        frame += 1
        next_canvas = check_neigbours(canvas)
        print(f'FRAME: {frame}')
        draw_canvas(next_canvas)
        canvas = next_canvas
        time.sleep(0.1)


main()

