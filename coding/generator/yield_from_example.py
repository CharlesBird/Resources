# yield from 写一个协程

target_dict = {}

origin_dict = {
    'name1': [200, 300, 700, 500],
    'name2': [400, 1000, 500, 200],
    'name3': [700, 500, 800, 300]
}


def get_total_value(name):
    total = 0
    data_list = []
    while True:
        x = yield
        if not x:
            break
        print('{}值： '.format(name) + str(x))
        total += x
        data_list.append(x)

    return total, data_list


def middle(name):
    while True:
        target_dict[name] = yield from get_total_value(name)
        print(name + '统计完成！')


def main():
    for name, data_sets in origin_dict.items():
        m = middle(name)
        m.send(None)  # 预激委托协程
        for data in data_sets:
            m.send(data)
        m.send(None)
    print('统计结果: ', target_dict)


if __name__ == '__main__':
    main()
