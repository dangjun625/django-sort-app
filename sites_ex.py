from django.conf import settings

def index_app_list(app_list=None):
    """
      order by app_list from settings.SORTED_APPS
    
    app_list format:
        [
            {
                'app_url': '/status/',
                'models': [
                    {
                        'perms': {
                            'add': True,
                            'change': True,
                            'delete': True
                        },
                        'admin_url': '/status/def_trigger_status/',
                        'object_name': 'def_trigger_status',
                        'name': <django.utils.functional.__proxy__objectat0x0000000003B156A0>,
                        'add_url': '/status/def_trigger_status/add/'
                    },
                    ....
                ],
                'has_module_perms': True,
                'name': 'Status',
                'app_label': 'status'
            },
            ......
        ]
    """

    if app_list and hasattr(settings, 'SORTED_APPS') and isinstance(settings.SORTED_APPS, tuple):
        #app_name_list = [(v.keys()[0]) for k,v in enumerate(settings.SORTED_APPS)] #ok
        #app_name_list = [(k.keys()[0]) for k in settings.SORTED_APPS] #ok
        app_name_list = tuple(k.keys()[0] for k in settings.SORTED_APPS)
        
        new_app_list = []
        in_app_list= [app for app in app_list if app['app_label'] in app_name_list]
        for idx,app in enumerate(in_app_list):
            pos = app_name_list.index(app['app_label'])
            in_app_list[idx]["idx"] = pos
            order_models_list = settings.SORTED_APPS[pos][app['app_label']]
            for idx2,order in enumerate(app["models"]):
                app["models"][idx2]["idx"] = (lambda _list,obj_name : _list.index(obj_name) \
                    if _list.__contains__(obj_name) else -1)(order_models_list, order["object_name"])
            
            app['models'].sort(key=lambda x: x['idx'])

        in_app_list.sort(key=lambda x: x['idx'])
        new_app_list += in_app_list

        not_in_list= [app for app in app_list if app['app_label'] not in app_name_list]
        new_app_list += not_in_list
        app_list = new_app_list
    else:
        return app_list

    return app_list


def app_index_app_list(app_dict=None):
    """
      order by app_index_app_list from settings.SORTED_APPS
    
    app_dict format:
        {
            'broker': {
                'app_url': '/broker/',
                'models': [
                    {
                        'perms': {
                            'add': True,
                            'change': True,
                            'delete': True
                        },
                        'admin_url': '/broker/system_broker/',
                        'object_name': 'system_broker',
                        'name': <django.utils.functional.__proxy__objectat0x0000000003BAB128>,
                        'add_url': '/broker/system_broker/add/'
                    },
                    ......
                ],
                'has_module_perms': True,
                'name': 'Broker',
                'app_label': 'broker'
            },
            ......
        }
    """
    if app_dict and  hasattr(settings, 'SORTED_APPS') and isinstance(settings.SORTED_APPS, tuple):
        if isinstance(app_dict, dict):
            app_name_list = tuple(k.keys()[0] for k in settings.SORTED_APPS)
                
            app_label = app_dict["app_label"]
            order_models_list = settings.SORTED_APPS[app_name_list.index(app_label)][app_label]
            for idx,order in enumerate(app_dict["models"]):
                app_dict["models"][idx]["idx"] = (lambda _list,obj_name : _list.index(obj_name) \
                    if _list.__contains__(obj_name) else -1)(order_models_list, order["object_name"])
            
            app_dict['models'].sort(key=lambda x: x['idx'])
    else:
        return app_dict

    return app_dict
