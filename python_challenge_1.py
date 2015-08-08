# if you enter three numbers between the values of 1 and 99
# this will return a date, if only one date can be created from the 3 numbers

def answer(x, y, z):
    possible_dates = [
                        {'month': x, 'day': y, 'year': z},
                        {'month': x, 'day': z, 'year': y},
                        {'month': y, 'day': z, 'year': x},
                        {'month': y, 'day': x, 'year': z},
                        {'month': z, 'day': y, 'year': x},
                        {'month': z, 'day': x, 'year': y}
                     ]
    valid_dates = []
    longest_months = [1, 3, 5, 7, 8, 10, 12]
    regular_months = [4, 6, 9, 11]

    for number in possible_dates:
        mm = number['month']
        dd = number['day']
        yy = number['year']
        YY = "{:02d}".format(yy)
        if mm < 13 and dd < 32:
            if mm in longest_months:
                MM = "{:02d}".format(mm)
                DD = "{:02d}".format(dd)
                created_date = '{}/{}/{}'.format(MM, DD, YY)
                valid_dates.append(created_date)
            elif mm == 2 and dd < 29:
                MM = "{:02d}".format(mm)
                DD = "{:02d}".format(dd)
                created_date = '{}/{}/{}'.format(MM, DD, YY)
                valid_dates.append(created_date)
            elif mm in regular_months and dd < 31:
                MM = "{:02d}".format(mm)
                DD = "{:02d}".format(dd)
                created_date = '{}/{}/{}'.format(MM, DD, YY)
                valid_dates.append(created_date)
            else:
                pass
        else:
            pass

    print valid_dates
    if len(valid_dates) == 1:
        return valid_dates[0]
    elif len(valid_dates) > 1 and all(my_date == valid_dates[0] for my_date in valid_dates):
        return valid_dates[0]
    else:
        return "Ambiguous."
