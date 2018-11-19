## 一、github传代码上去   ##
1. 在仓库中，将代码提交到网上的命令是  
`git push -u origin master`

2. …or create a new repository on the command line  
    echo "# matplotlib" >> README.md  
    git init  
    git add README.md  
    git commit -m "first commit"  
    git remote add origin https://github.com/Blankit/matplotlib1.git  
    git push -u origin master  
    

3. …or push an existing repository from the command line

    git remote   
    add origin https://github.com/Blankit/matplotlib1.git  
    git push -u origin master


## 二、python ##
1. 字符串连接，`+`  
    a = ['1','3']  
    b = ['aa']  
    c = a + b
    print c
  
2. 要注意定义可变参数和关键字参数的语法：

    `*args`是可变参数，args接收的是一个tuple；
    
    `**kw`是关键字参数，kw接收的是一个dict。
参数前面加上* 号 ，意味着参数的个数不止一个，另外带一个星号（*）参数的函数传入的参数存储为一个元组（tuple）
3. format 格式化函数   
	1. 不指定位置参数  
	"{} {}".format("hello", "world") #  
	**输出：**'hello world'  
	2. 指定位置参数  
	"{1} {0}".format("hello", "world")   
	**输出：**'world hello' 
	3. 通过变量名设置参数  
    print("网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com"))  
    **输出：**网站名：菜鸟教程, 地址 www.runoob.com 
	4. 通过字典设置参数（字典参数两个`**`）    
    site = {"name": "菜鸟教程", "url": "www.runoob.com"}  
    print("网站名：{name}, 地址 {url}".format(**site))  
	**输出：**网站名：菜鸟教程, 地址 www.runoob.com
	5. 通过列表索引设置参数  
    my_list = ['菜鸟教程', 'www.runoob.com']  
    print("网站名：{0[0]}, 地址 {0[1]}".format(my_list))  # "0" 是必须的  
    **输出：**网站名：菜鸟教程, 地址 www.runoob.com

    
## 三、摘抄 ##

> 自己想什么就讲什么；自己怎么想就怎么说--这就是说真话。你有什么想法，有什么意见，讲出来让大家了解你。倘使意见相同，那就在一起做进一步的研究；倘使意见不同，那就进行认真讨论，探求一个是非。这样做有什么不好？     ————《随想录（说真话之四）》
 
----------

## 四、Markdown记录 ##
1. 行首输入空格：`shift+space`切换到全角模式，再按空格键．　全角模式时，输入法上“中”或“英”后面的月亮会变成太阳


----------
##五、相关技能
1. 批量修改文件名  
	- ` dir /b>a.xls`获取当前路径下所有文件的文件名
	- 在excel表的文件名前添加一列`ren`  
	- 在文件名后添加一列**新的**文件名
	- 复制excel表中的内容到记事本中，并保存为`ren.bat`，与需要重命名的文件放在同一个文件夹下。
	- 双击`ren.bat`,事项重命名
2. 
