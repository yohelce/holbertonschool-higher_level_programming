#!/usr/bin/python3
def roman_to_int(roman_string):
    rs = roman_string
    if rs is None or type(rs) != str:
        return 0
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i in range(len(rs)):
        if i + 1 < len(rs) and dic[rs[i]] < dic[rs[i + 1]]:
            result -= dic[rs[i]]
        else:
            result += dic[rs[i]]
    return result
