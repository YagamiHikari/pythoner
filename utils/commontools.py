#! /usr/bin/env python
# coding: utf-8


import csv
import numpy
from datetime import datetime, timedelta
from dateutil import relativedelta
from utils.middlewares import typeassert


"""
时间算法
"""


def min_date_str():
    """
    最小时间string
    :return:
    """
    return '1900-01-01 00:00:00'


def min_date():
    """
    最小时间
    :return:
    """
    return convert_to_date(min_date_str())


def now():
    """
    当前时间str
    :return:
    """
    return datetime.now()


def today():
    """
    today on 00:00:00
    :return:
    """
    day = convert_to_datestr(now())[:10]
    return convert_to_date(day+' 00:00:00')


def yesterday():
    """
    yesterday on 00:00:00
    """
    return today() - timedelta(days=1)


def day_before(delta):
    """
    Day before delta days from today(00:00:00)
    :param delta:
    :return:
    """
    return today() - timedelta(days=delta)


def week_before(delta):
    """
    Day before delta weeks from today(00:00:00)
    :param delta:
    :return:
    """
    return today() - timedelta(weeks=delta)


def month_before(delta):
    """
    Day before delta month from today(00:00:00)
    :param delta:
    :return:
    """
    return today() - relativedelta.relativedelta(months=delta)


def year_before(delta):
    """
    Day before delta years from today(00:00:00)
    :param delta:
    :return:
    """
    return today() - relativedelta.relativedelta(years=delta)


def year_first_day():
    """
    本年第一天
    :return:
    """
    today_str = convert_to_datestr(today())
    year_first_day_str = today_str[:4]+'-01-01'+today_str[10:]

    return convert_to_date(year_first_day_str)


def month_first_day():
    """
    本月第一天
    :return:
    """
    today_str = convert_to_datestr(today())
    month_first_day_str = today_str[:8]+'01'+today_str[10:]

    return convert_to_date(month_first_day_str)


@typeassert(date_str=basestring)
def convert_to_date(date_str=''):
    """
    Date str to date
    """
    return datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')


@typeassert(date=datetime)
def convert_to_datestr(date=None):
    """
    Date to date_str
    """
    return date.strftime('%Y-%m-%d %H:%M:%S')


"""
基础算法
"""


def get_property_value(instance=None, property=''):
    """
    get property value
    :param instance:
    :param property:
    :return:
    """
    if not instance:
        return None

    try:
        return instance[property]
    except:
        return None


def instance_max(instances, property):
    """
    max value of [instance.property:]
    :param instances:
    :param property:
    :return:
    """
    values = instance_values(instances, property)
    return max(values) if values else None


def instance_min(instances, property):
    """
    min value of [instance.property:]
    :param instances:
    :param property:
    :return:
    """
    values = instance_values(instances, property)
    return min(values) if values else None


def instance_avg(instances, property):
    """
    平均值 avg value of [instance.property:]
    :param instances:
    :param property:
    :return:
    """
    values = instance_values(instances, property)
    return float(numpy.mean(values)) if values else None


def instance_sum(instances, property):
    """
    累计值 sum  of [instance.property:]
    :param instances:
    :param property:
    :return:
    """
    values = instance_values(instances, property)
    return float(numpy.sum(values)) if values else None


def instance_values(instances, property):
    """
    Get [instance.property:]
    :param instances:
    :param property:
    :return:
    """
    if not instances or len(instances) == 0:
        return None

    if not property or not isinstance(property, basestring):
        raise Exception('property must be basestring')

    values = []
    for instance in instances:
        value = get_property_value(instance, property)
        if value:
            values.append(float(value))

    return values


def safe_sum(num0, num1):
    """
    Safe加法
    :param num0:
    :param num1:
    :return:
    """
    if num0 is None or num1 is None:
        try:
            return float(num0)
        except:
            try:
                return float(num1)
            except:
                return None

    try:
        return float(num0)+float(num1)
    except:
        return None


def safe_min(num0, num1):
    """
    SafeMin
    :param num0:
    :param num1:
    :return:
    """
    if num0 is None or num1 is None:
        try:
            return float(num0)
        except Exception:
            try:
                return float(num1)
            except Exception:
                return None

    try:
        return min([float(num0), float(num1)])
    except Exception:
        return None


def safe_max(num0, num1):
    """
    SafeMax
    :param num0:
    :param num1:
    :return:
    """
    if num0 is None or num1 is None:
        try:
            return float(num0)
        except Exception:
            try:
                return float(num1)
            except Exception:
                return None

    try:
        return max([float(num0), float(num1)])
    except Exception:
        return None


def safe_subtract(num0, num1):
    """
    Safe减法
    :param num0:
    :param num1:
    :return:
    """
    if num0 is None or num1 is None:
        return None

    try:
        return float(num0)-float(num1)
    except Exception:
        return None


def safe_division(dividend, divisor):
    """
    Safe除法(校验None参数)
    :return safe dividend/divisor or None
    :param dividend:
    :param divisor:
    :return:
    """
    if dividend is None or divisor is None:
        return None

    if float(divisor) == 0:
        return None

    try:
        return float(dividend)/float(divisor)
    except Exception:
        return None


def safe_multiple(multiplicand, multiplier):
    """
    Safe乘法(校验None参数)
    :param multiplicand: 被乘数
    :param multiplier: 乘数
    :return:
    """
    if multiplicand is None or multiplier is None:
        return None

    try:
        return float(multiplicand)*float(multiplier)
    except Exception:
        return None


"""
基础数据类型
"""


def safe_dict_value(item, key, default=None):
    """
    Safe get value for key [Dict]
    :param item:
    :param key:
    :param default:
    :return:
    """
    if not isinstance(item, dict) or not isinstance(key, str):
        raise TypeError
    if not item.has_key(key):
        return default
    if item[key] is None:
        return default
    if isinstance(item[key], str):
        return item[key].encode('utf-8').strip()
    return item[key]


def safe_unicode(obj, *args):
    """ return the unicode representation of obj """
    try:
        return unicode(obj, *args)
    except UnicodeDecodeError:
        # obj is byte string
        ascii_text = str(obj).encode('string_escape')
        return unicode(ascii_text)


def safe_str(obj):
    """ return the byte string representation of obj """
    try:
        return str(obj)
    except UnicodeEncodeError:
        # obj is unicode
        return unicode(obj).encode('unicode_escape')


"""
File I/O
"""


def read_csv(file_name, title=''):
    """
    Read csv
    :param file_name:
    :param title : firt column(Title column)
    :return:
    """
    with open(file_name, 'rb') as csv_file:
        spam_reader = csv.reader(csv_file, delimiter=',', quotechar='|')

        result = []
        key_list = []
        for row in spam_reader:
            row = ','.join(row).decode('gbk').split(',')

            new_row = []
            for item in row:
                new_row.append(item.strip(' \t\n"'))
            row = new_row

            if row[0] == title:
                key_list = row
            else:
                result.append(row)

        new_result = []
        for row in result:
            nnn = {}
            for index in range(0, len(key_list)):
                nnn[key_list[index]] = row[index]
            new_result.append(nnn)

        return new_result


# if __name__ == '__main__':

    # print safe_max(1, 2)
    # print safe_max(0, 1)
    # print safe_max(None, 2)
    # print safe_min(1, 2)
    # print safe_min(0, 1)
    # print safe_min(None, 2)
    # print day_before(2)
    # print week_before(3)
    # print yesterday()
    # print year_before(4)
    # print month_first_day()
