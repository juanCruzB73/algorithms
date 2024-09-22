dic1={"a":1,"b":562,"c":123456}
dic2={"b":562,"a":1,"c":123456}
for i in dic1:
    print(dic1[i],dic2.get(i))

