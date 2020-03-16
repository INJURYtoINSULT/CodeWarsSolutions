def create_phone_number(n):
    ph_n = ''.join(map(str, n))
    phone_num = "(" + ph_n[0:3] + ") " + ph_n[3:6] + "-" + ph_n[6:10]
    return phone_num
