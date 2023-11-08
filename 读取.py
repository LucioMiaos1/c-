import pandas as pd
import openpyxl as op
with open(r"C:\Users\95885\Desktop\2.txt","r",encoding='utf-8') as f:
    data = f.read()
    datasplit = data.split()
    # print(datasplit)
    list1 = ["a11","a12","a13","a14","a21","a22","a23","a24","a31","a32","a33","a34","a41","a42","a43","a44","a51","a52","a53","a54","a61","a62","a63","a64","a71","a72","a73","a74","a81","a82","a83","a84","a91","a92","a93","a94"]
    list2 = []
    for i in datasplit:
        list2.append(i)

    # # print(list2)
    dictionary1 = dict(zip(list1,list2))
    # print(dictionary1)
    # a = pd.DataFrame.from_dict(dictionary1,orient='index')
    # # a.to_excel(r'C:\Users\95885\Desktop\2.xlsx')
    df = pd.DataFrame(dictionary1,index=[0])
    print(df)




    df.to_excel(r'C:\Users\95885\Desktop\2.xlsx')







