# 项目说明

此项目为集成openldap的Demo，依赖环境

- python 3.6
- django 2.2
- redis==2.10.6

# 部署方法
1. 安装基础环境
```
pip install -r requires.txt
```

2. 初始化数据库
```
python manage.py migrate
```

3. 运行项目
```
python manage.py runserver 0.0.0.0:8000
```
