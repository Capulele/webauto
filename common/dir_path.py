import os

base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
log_path = os.path.join(base_path , 'logs')
userdata_path = os.path.join(base_path , r'data\user.yml')
projectsname_path = os.path.join(base_path , r'data\projectsname.yml')
screenshot_path = os.path.join(base_path , r'report\screenshots')
