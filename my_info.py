ac = '202200000000'  # 学号
pw = 'passw0rd'  # 密码
gap_time = 2  # 每次选课间隔秒数
course_type ='1'  # '1'->计划内 '2'->公选课 '3'->跨年级 '4'->跨专业
my_jx0404id = '202320242001214'  # 在选课系统找到对应课程的选课按钮，右键检查以查看对应id
my_kcid = 'D8FE8A94C4C3422FB6B6E31ACD866365'  # 在选课系统找到对应课程的选课按钮，右键检查以查看对应id
js_jhn = f"xsxkOper('{my_jx0404id}','','','{my_kcid}','null','null');"
js_gxk = f"xsxkFun('{my_jx0404id}','{my_kcid}','null');"
js_knj = f"xsxkFunNEW('{my_jx0404id}','{my_kcid}','null','%E6%97%A0','null');"
js_kzy = f"xsxkFun('{my_jx0404id}','{my_kcid}','null');"
match course_type:
    case '1':
        js_method = js_jhn
    case '2':
        js_method = js_gxk
    case '3':
        js_method = js_knj
    case '4':
        js_method = js_kzy
    case _:
        print('course type error')
        exit()
# print(js_method)
