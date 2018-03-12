"""容器类型"""

class ContainerClass(object):
    def __init__(self):
        self.value = {}

    def __len__(self):
        print('Len')
        return len(self.value)

    def __getitem__(self, item):
        print('getitem')
        return self.value[item]

    def __setitem__(self, key, value):
        print('setitem')
        self.value[key] = value

    def __delitem__(self, key):
        print('delitem')
        del self.value[key]

    def __iter__(self):
        print('iter')
        for k, v in self.value.items():
            yield k, v

    def __reversed__(self):
        print('reversed')
        return dict(sorted(self.value.items(), key=lambda item: item[0], reverse=True))

    def __contains__(self, item):
        print('contains')
        return item in self.value

cc = ContainerClass()
cc['k1'] = '123'
cc['k2'] = 'esa'
cc['k3'] = 'sds'
print(cc.value, len(cc))
del cc['k1']
print(cc.value)
reversed(cc)
print(cc.value)
for k, v in cc.value.items():
    print(k, v)
print('k2' in cc.value)
print(iter(cc.value).__next__())