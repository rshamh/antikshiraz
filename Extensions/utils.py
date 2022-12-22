from . import jalali

def persian_number_conv(my_str):
    numbers = {
        "0" : "۰",
        "1" : "۱",
        "2" : "۲",
        "3" : "۳",
        "4" : "۴",
        "5" : "۵",
        "6" : "۶",
        "7" : "۷",
        "8" : "۸",
        "9" : "۹",
    }

    for e, p in numbers.items():
        my_str = my_str.replace(e, p)
    
    return my_str

def jalali_converter(time):

    jmonths = ['فروردین','اردیبهشت','خرداد','تیر','مرداد','شهریور','مهر','آبان','آذر','دی','بهمن','اسفند' ]
    
    time_to_str = f'{time.year},{time.month},{time.day}'

    time_to_tuple = jalali.Gregorian(time_to_str).persian_tuple()

    output = f'{time_to_tuple[2]} {jmonths[time_to_tuple[1]-1]} {time_to_tuple[0]}'

    return persian_number_conv(output)
