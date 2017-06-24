#!/usr/bin/env python
# coding: utf-8


import logging
from demo_multi_task.multi_threading_class import ThreadDemo

logging.basicConfig(filename="demo.log", format='%(asctime)s %(name)s %(levelname)s: %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger("ShowDemo")


if __name__ == '__main__':

    ThreadDemo.run()