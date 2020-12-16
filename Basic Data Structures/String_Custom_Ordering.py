def custom_string_ordering(s, order):  # O(nlogn) and O(n)
    """
    Create a dictionary based on order
    turn s into numbers based on order
    sort s
    create another dictionary from the existing one, where values are keys and vice versa
    We do it to have a O(1) access; otherwise we'll have to do two loops --> O(n^2)
    Build the resulting string
    """
    d, d_another, order_list, res = {}, {}, [], ''
    for k, v in enumerate(order):
        d[v] = k
    for ch in s:
        order_list.append(d[str(ch)])
    order_list.sort()
    for k, v in d.items():
        d_another[v] = k
    for item in order_list:
        res += str(d_another[item])
    return res


if __name__ == '__main__':
    print(custom_string_ordering('bbcaaeff', 'acbef'))