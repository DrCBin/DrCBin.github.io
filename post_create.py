# coding: utf-8
"""创建文章和分类

Usage:
    post_create.py -n NAME [-c CATEGORY]
    post_create.py clean

Options:
    -c            category name
    -n            post name
    -h, --help    show this help
"""

import os
from docopt import docopt
import datetime

POST_TEMPLATE = """---
title: {name}
category: {category}
---
"""

CATEGORY_TEMPLATE = """---
layout: posts_by_category
categories: {category}
title: {category}
permalink: /category/{category}
---
"""


CATEGORY_PATH = 'category'
CATEGORY_NAME = 'default'
categories = os.scandir(CATEGORY_PATH)
categories = [c.name.split('.', 1)[0] for c in categories]


POSTS_PATH = '_posts'
POST_NAME = None
posts = os.scandir(POSTS_PATH)
posts = [p.name for p in posts]


def create_category(category_name):
    if category_name in categories:
        print('category "{}" is already exist!'.format(category_name))
    else:
        path = '{}/{}.md'.format(CATEGORY_PATH, category_name)
        print('create category:' + path) 
        with open(path, 'w') as f:
            f.write(CATEGORY_TEMPLATE.format(category=category_name))




def clean():
    exist_category = set()
    for post in posts:
        try:
            with open(POSTS_PATH + '/' + post) as f:
                line = None
                for i in range(0, 3):
                    line = f.readline()
                category = line.split(':', 1)[1][1:-1]
                exist_category.add(category)
        except Exception:
            pass
    common = exist_category & set(categories)

    for category in exist_category - common:
        create_category(category)

    for category in set(categories) - common:
        print('rm category "{}"... '.format(category))
        os.remove(CATEGORY_PATH + '/' + category + '.md')



if __name__ == '__main__':
    args = docopt(__doc__)

    # for option clean if args['clean']: clean()
    if args['clean']:
        clean()
        exit()

    # for option -c
    if args['-c'] and args[r'CATEGORY'] is not None:
        CATEGORY_NAME = args['CATEGORY']
        create_category(CATEGORY_NAME)
    elif args['-c']:
        raise Exception('option "-c" needs a argument!')
    else:
        raise Exception(__doc__)


    # for option -n
    if args['-n'] and args['NAME'] is not None:
        date = datetime.datetime.now()
        year, month, day = date.year, date.month, date.day
        POST_NAME = '{}-{}-{}-{}.md'.format(year, month, day, args['NAME'])
        if POST_NAME in posts:
            raise Exception('post "{}" is already exist!'.format(POST_NAME))
        path = '{}/{}'.format(POSTS_PATH, POST_NAME)
        print('create post: ' + path)
        with open(path, 'w') as f:
            f.write(POST_TEMPLATE.format(name=args['NAME'], category=CATEGORY_NAME))
    elif args['-n']:
        raise Exception('option "-n" needs a argument!')
    else:
        raise Exception(__doc__)




