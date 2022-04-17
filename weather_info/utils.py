def get_last_observation(data):
    date_of_observation = data[0]
    time_of_observation = data[1].split("\n")[0]
    return f"{date_of_observation} at {time_of_observation} GMT"


def get_temperature(data):
    for each in data[2:]:
        if '/' in each:
            first_part = each.split("/")[0]
            if 'M' in first_part:
                celsius = -1 * int(first_part[1:])
            else:
                celsius = int(first_part)
            fahrenheit = (celsius * 1.8) + 32
            return f"{celsius} C ({fahrenheit} F)"
    else:
        return None


def get_wind(data):
    for each in data[2:]:
        if 'KT' in each:
            direction = each[:3]
            knots = each[3:5]
            if "G" in each:
                knots_gusts = find_between(each, "G", "KT")
                return f"S at {direction} mph ({knots} knots) ({knots_gusts} knot gusts)"
            else:
                return f"S at {direction} mph ({knots} knots)"
    else:
        return None


def find_between(text, start, end):
    return (text.split(start))[1].split(end)[0]