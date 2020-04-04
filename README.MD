#flask测试框架-算法服务


#####python镜像源 pip和 buildout
1. `pip config set global.index-url http://mirrors.aliyun.com/pypi/simple`

1. or `~/.pip/pip.con` or `C:\Users\xx\pip\pip.ini`

    ```
   [global]
    index-url = http://mirrors.aliyun.com/pypi/simple
   ```

1. buildout:easy_install.py:`default_index_url = 'http://mirrors.aliyun.com/pypi/simple'`

#####安装
1. python3.7+
1. pip install zc.buildout
1. pip install .
1. buildout

#####structure
1. algo/app.py web程序入口


#####Todo
1. 引入tensorflow框架替换自带算法库
1. flask实现，提供web-api接口
   1. 接口名：getQCQty
   1. 入参：文档中输入项
   1. 返回值：文档中输出项
   1. 测试：http://127.0.0.1:5000/getQCQty?name=2   
1. yapi或postman测试接口（yapi：http://172.16.20.3:8123/ 注册）
1. 接口文档(参考：doc文件夹下文档)
1. 部署和构建（待研究）--部署至172.16.50.2服务器root/YFalgori01
1. jenkins自动打包和部署（http://172.16.20.3:8088   admin/huadong）
