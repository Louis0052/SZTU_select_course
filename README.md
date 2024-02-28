SZTU抢课选课小程序

程序基于2023-2024第二学期选课起开始使用的选课分流界面使用selenium模拟选课。

# 使用说明

## 前置条件

### Python

请使用3.10或更高版本

#### 库 

selenium

### 浏览器

使用Chrome浏览器，若未安装请先安装，或在main.py login()中修改option与driver参数以使用其他浏览器

随后下载浏览器对应版本的webdriver，并解压至任一环境变量所在目录（方便起见可直接解压至python所在目录）

下载地址：[Chrome for Testing availability (googlechromelabs.github.io)](https://googlechromelabs.github.io/chrome-for-testing/)

## 选课信息

根据要求在my_info.py填入相关信息

<img src="img\my_info.png" style="zoom:50%;" />

以下是查看jxid和kcid的步骤

第一个非空字符串为jxid，第二个非空字符串为kcid

<img src="img\find_jxid_kcid.png" alt="find_jxid_kcid" style="zoom:40%;" />



## 注意事项

1. 若出现报错请在login()中取消注释此行代码，再次运行查看问题

   ```python
   option.add_argument("--headless")  # 隐藏浏览器页面
   ```

2. 注意窗口位置，若正式选课窗口不在第0位，请自行修改main.py中该行代码

   ```
   driver.switch_to.window(driver.window_handles[0])
   ```

3. 若网页出现选课时间内提示“不在选课时间内”，请再次运行程序或尝试在select_course()中，在此行添加断点

   ```python
   driver.execute_script(js_method)  # 控制台执行选课js方法
   ```

   并使用debug模式运行程序











*Copyright 2024 by Louis*