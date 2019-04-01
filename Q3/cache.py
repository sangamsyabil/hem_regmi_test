from cache_main import Cache

import random

if __name__ == '__main__':

    Keys = [i for i in range(7)]
    sites = ['www.abc.com ', 'www.bcd.com ', 'www.cde.com ', 'www.def.com ',
             'www.efg.com ', 'www.fgh.com ', 'www.ghi.com ',
             'www.hij.com ', 'www.ijk.com ', 'www.jkl.com ', ]

    cache = Cache()

    print('_'*60)
    # Updating Cache
    for i, key in enumerate(Keys):
        if key in cache:
            continue
        else:
            value = ''.join([random.choice(sites)])
            print(value)
            cache.cache_update(key, value)

        print("{0}.list, #{1} cached site" .format(i+1, cache.cache_size()))

    # printing cache lists
    print('\n', '_'*15, ' Cache List ', '_'*15)
    for k, v in cache.cache_view().items():
        print("{0} : {1}".format(k, v))
    print('_'*60)