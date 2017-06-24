#!/usr/bin/env python
# coding: utf-8


from threading import Thread
from time import ctime, sleep


def music(song):
    """

    :param song:
    :return:
    """
    for i in range(10):
        print 'I was listening to music {1}. {0}'.format(ctime(), song)
        sleep(1)


def movie(mov):
    """

    :param mov:
    :return:
    """
    for i in range(10):
        print 'I was at the movies {1}.{0}'.format(ctime(), mov)
        sleep(5)


threads = list()
t1 = Thread(target=music, args=('天涯',))
t2 = Thread(target=movie, args=('天龙八部',))
threads.append(t1)
threads.append(t2)

if __name__ == '__main__':

    for index, th in enumerate(threads):
        th.setDaemon(True)  # 守护线程
        th.start()
    th.join()

    print 'All over.{0}'.format(ctime())
