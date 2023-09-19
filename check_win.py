def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes+=row.count(0)
        if row.count(sign)==3:
            return sign
    for col in range(3):
        if mas[0][col]==sign and mas[1][col]==sign and mas[2][col]==sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes==0:
        return 'Ничья'
    return False