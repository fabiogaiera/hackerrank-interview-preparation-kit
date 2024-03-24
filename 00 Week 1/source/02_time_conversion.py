def time_conversion(s):
    am_pm_str = s[-2:]
    hour_str = s[0:2]
    mm_ss_str = s[2:8]
    hour_int = int(hour_str)
    if am_pm_str == 'AM' and hour_str == '12':
        hour_str = '00'
    elif am_pm_str == 'PM' and hour_str == '12':
        pass
    elif am_pm_str == 'PM':
        hour_int = hour_int + 12
        hour_str = str(hour_int)
    return hour_str + mm_ss_str


time_conversion('07:05:45PM')
