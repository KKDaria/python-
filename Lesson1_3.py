for percent in range(101):

    if percent % 100 != 11 and percent % 10 == 1:
        print(f'{percent}процент')
    elif percent % 10 >= 2 and percent % 10 <= 4 and not 11 < percent < 15:
        print(f'{percent}процента')
    else:
        print(f'{percent}процентов')

