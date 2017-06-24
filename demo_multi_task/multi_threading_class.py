#!/usr/bin/env python
# coding: utf-8


import logging
from threading import Thread
from time import ctime, sleep


class ThreadDemo(object):
    """
    多线程--类的实现
    """

    @classmethod
    def run(cls):
        """

        :return:
        """

        logging.info('{0}, Threading start.'.format(cls.__name__))

        cnt = 1
        while True:
            logging.info("The {0} run.....{1}".format(cnt, ctime()))
            cls.service_work()
            cnt += 1
            sleep(5)   # 设置间隔时间
            if cnt > 10:
                break

        logging.info('Threading end.')

    @classmethod
    def service_work(cls):
        """

        :return:
        """

        threads = list()
        t1 = Thread(target=cls.music, args=('天涯',))
        t2 = Thread(target=cls.movie, args=('天龙八部',))
        threads.append(t1)
        threads.append(t2)

        for index, th in enumerate(threads):
            th.setDaemon(True)  # 守护线程
            th.start()
        th.join()

        print 'All over.{0}'.format(ctime())

    @classmethod
    def music(cls, song):
        """

        :param song:
        :return:
        """
        for i in range(3):
            print 'I was listening to music {1}. {0}'.format(ctime(), song)
            sleep(1)

    @classmethod
    def movie(cls, mov):
        """

        :param mov:
        :return:
        """
        for i in range(3):
            print 'I was at the movies {1}.{0}'.format(ctime(), mov)
            sleep(5)


if __name__ == '__main__':

    ThreadDemo.run()
