# django-sort-app
sort django app


##支持django版本

* django 1.6.8
* django 1.7.0

##使用说明

* 1),修改django里面sites.py代码
    *  需要修该的文件为 {python_path}\Lib\site-packages\django\contrib\admin\sites.py
    *  修改前先备份

* 2),添加sites_ex.py
    *  添加文件sites_ex.py到 {python_path}\Lib\site-packages\django\contrib\admin\sites_ex.py.py

* 3),修改项目settings.py
    SORTED_APPS = (
        {'auth':('User', 'Group',)},
        {'proxy':('user', 'group', 'product', 'order',},
    )
