def Func(value, out):
    values=[
        True,
        int(5),
        float(1.2),
        complex(3.14 - 0j),   
        str("stirng"),
        bytes(25),
        bytearray([25,50]),
        list([1,2,3]),
        tuple((1,2,3)),
        set({3,1,2}),
        frozenset({3,1,2}),
        dict({"key":"value"})]

    types=[
        bool,int,float,complex,str,bytes,bytearray,list,tuple,set,frozenset,dict
    ]

    for i in range(len(values)):
        print("Значение {0}, тип: {1}, соответсвие: {2}".format(
            values[i],
            type(values[i]), 
            isinstance(values[i], types[i])))

    return None
