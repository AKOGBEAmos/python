def to_str(a):
    tmp = []
    for i in a:
        tmp.append(str(i))
    return " ".join(tmp)



print(to_str(['123']))