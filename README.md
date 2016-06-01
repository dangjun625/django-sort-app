
##支持django版本

* django 1.6.8
* django 1.7.0

##使用说明

* 1),修改django安装文件中contrib\admin\sites.py
    *  需要修该的文件为 {python_path}\Lib\site-packages\django\contrib\admin\sites.py
    *  修改前先备份
    *  可用比较工具(beyond compare)或者直接替换

* 2),添加sites_ex.py
    *  添加文件sites_ex.py到 {python_path}\Lib\site-packages\django\contrib\admin\sites_ex.py.py

* 3),修改项目下settings.py文件
    *  添加如下
```python
    SORTED_APPS = (
        {'auth':('User', 'Group',)},
        {'proxy':('user', 'group', 'product', 'order',},
    )
```