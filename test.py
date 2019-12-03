from app import db


def c_all():
    # db.drop_all()
    db.create_all()


def draw_heart():
    # for y in range(15, -15, -1):
    #     for x in range(-30, 30):
    print('\n'.join([''.join([('LovePython'[(x - y) % 10] if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (
            x ** 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))


def time_draw():
    import time
    [(time.sleep(0.0009), print("\033[91m" + i, end="", flush=True))
     for i in ('\n'.join([''.join([(' I love U'[(x - y) % 9]
                if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0
                else ' ') for x in range(-30, 30)]) for y in range(15, -15, -1)]))]


def time_os_math():
    import time, os, math
    [([(time.sleep(a), print("\033[91m" + i, end="", flush=True))
       for i in ('\n'.join([''.join([(' I love U'[(x - y) % 9]
            if ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3 <= 0 else ' ')
                for x in range(-30, 30)])
                    for y in range(15, -15, -1)]))],time.sleep(1 / math.log(ai + 3)), os.system('clear'))
    for (ai, a) in enumerate([0.001, *[0.00001] * 99])]


if __name__ == '__main__':
    c_all()
    # draw_heart()
    # time_draw()
    # time_os_math()