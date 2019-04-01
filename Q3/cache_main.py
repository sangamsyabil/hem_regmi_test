import datetime

class Cache:
    ''' A simple cache class allowing maximum of 4 sites on cache '''
    def __init__(self):
        self.cache = {}
        self.MaxSize = 4

    def cache_empty(self):
        return self.cache == {}

    def cache_size(self):
        return len(self.cache)

    def __contains__(self, key):
        return key in self.cache

    def cache_view(self):
        return self.cache

    def cache_update(self, key, value):
        if key not in self.cache and len(self.cache) >= self.MaxSize:
            self.cache_delete()

        self.cache[key] = {'Added time': datetime.datetime.now().isoformat(),
                           'value': value}

    def cache_delete(self):
        old_entry = None
        for key in self.cache:
            if old_entry is None:
                old_entry = key
            elif self.cache[key]['Added time'] < self.cache[old_entry]['Added time']:
                old_entry = key
        self.cache.pop(old_entry)