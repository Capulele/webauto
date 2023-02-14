import yaml

from common.dir_path import projectsname_path , userdata_path


def load_user_yaml(path):
    with open(path, encoding="utf-8") as f:
        data = yaml.load(f, yaml.FullLoader)
        data_list = []
        for i in range(len(data['cases'])):
            data_name = data['cases'][i]['name']
            data_pwd = data['cases'][i]['pwd']
            data_res = data['cases'][i]['except_res']
            data_list.append((data_name, data_pwd, data_res))
            continue
    return data_list
def get_user_json(path):
    with open(path,encoding = 'utf-8') as f:
        data=yaml.load(f,yaml.FullLoader)
        return data['cases']

def load_projects_yaml(path):
    with open(path, encoding='utf-8') as f:
        data = yaml.load(f, yaml.FullLoader)['cases']
        return data


if __name__ == '__main__':
    load_projects_yaml(projectsname_path)
    get_user_json(userdata_path)
