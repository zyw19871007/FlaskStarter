# flask-starter-framework

|Based on this project quickly build flask project

|基于此项目快速搭建flask项目

##### python-mirror pip and  buildout
1. `pip config set global.index-url http://mirrors.aliyun.com/pypi/simple`

   `pip config set install.trusted-host mirrors.aliyun.com`

1. or `~/.pip/pip.con` or `C:\Users\xx\pip\pip.ini`

    ```
   [global]
    index-url = http://mirrors.aliyun.com/pypi/simple
   ```

1. buildout:easy_install.py:`default_index_url = 'http://mirrors.aliyun.com/pypi/simple'`

##### install
1. python3.7+
1. pip install zc.buildout==2.13.3
1. pip install .
1. buildout

##### feature(see src/config.ini)
1. eureka config
1. ignite config
1. logstash config

##### structure
1. algo/app.py web ---main entrance
2. 命令行运行：python -m src.app -p 5000


##### Todo
1. import python test framework


##### support
[![alt text](/image/jetbrains.svg "FlaskStarter")](https://www.jetbrains.com/?from=FlaskStarter)
