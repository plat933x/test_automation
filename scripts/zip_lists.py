def ziplists():
    bmw_engines = [1.8,2.0,2.5,2.8,3.0]
    fiat_engines = [0.8,2.0,3.2,4.3,1.4]

    both_engines = list(zip(bmw_engines,fiat_engines))
    print(both_engines)

    final_list_highest = []

    for a,b in both_engines:
        final_list_highest.append(max(a,b))

    return final_list_highest

print(ziplists())