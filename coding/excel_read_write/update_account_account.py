# -*- coding: UTF-8 -*-
from api import API
import xlrd
import xlwt
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


def import_stock_move(ffile):
    book = xlrd.open_workbook(ffile)
    sh = book.sheet_by_index(0)
    values = {}
    for rx in range(sh.nrows):
        if rx == 0:
            continue
        rx_line = sh._cell_values[rx]
        code = rx_line[0] and rx_line[0].strip() or ''
        name = rx_line[1] and rx_line[1].strip() or ''
        name_type = rx_line[2] and rx_line[2].strip() or ''
        name_type_type = rx_line[3] and rx_line[3].strip() or ''
        if len(name.split('-')) == 1:
            one_level = values.setdefault('one', [])
            one_level.append({'code': code, 'name': name, 'name_type': name_type, 'name_type_type': name_type_type, 'parent_name': ''})
        elif len(name.split('-')) == 2:
            parent_name, name = name.split('-')
            two_level = values.setdefault('two', [])
            two_level.append({'code': code, 'name': name, 'name_type': name_type, 'name_type_type': name_type_type, 'parent_name': parent_name})
        elif len(name.split('-')) == 3:
            parent_name, name = name.split('-')[1:]
            three_level = values.setdefault('three', [])
            three_level.append({'code': code, 'name': name, 'name_type': name_type, 'name_type_type': name_type_type, 'parent_name': parent_name})
    return values


def write_to_xls(datas):
    title_map = {'code': 0, 'name': 1, 'parent_name': 2, 'name_type': 3, 'name_type_type': 4}
    title_name = {'code': u'编码', 'name': u'名称', 'parent_name': u'上级科目', 'name_type': u'科目类别', 'name_type_type': u'科目类别的类别'}
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(u'科目')
    row = 0
    for title_k, title_v in title_name.iteritems():
        col = title_map[title_k]
        worksheet.write(row, col, label=title_v)
    for level in ['one', 'two', 'three']:
        for line in datas[level]:
            row += 1
            print row
            for line_k, line_v in line.iteritems():
                col = title_map[line_k]
                worksheet.write(row, col, label=line_v)
    # worksheet.write(1, 1, label='Row 0, Column 0 Value')
    workbook.save('new_account.xls')
    print '==========Done============='



datas = import_stock_move('./update_account_account.xlsx')
write_to_xls(datas)