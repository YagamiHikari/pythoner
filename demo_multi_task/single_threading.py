#!/usr/bin/env python
# coding: utf-8


from time import ctime, sleep


def music(song):
    """

    :param song:
    :return:
    """
    for i in range(2):
        print 'I was listening to music {1}. {0}'.format(ctime(), song)
        sleep(1)


def movie(mov):
    """

    :param mov:
    :return:
    """
    for i in range(2):
        print 'I was at the movies {1}.{0}'.format(ctime(), mov)
        sleep(5)


if __name__ == '__main__':

    music('天涯')
    movie('卧虎藏龙')
    print 'All over.{0}'.format(ctime())