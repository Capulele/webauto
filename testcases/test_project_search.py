import logging
import allure
import pytest

from common.dir_path import projectsname_path
from common.load_log import load_log
from common.yamlutil import load_projects_yaml
from operator_object.sys_homepage import SysHomePage

@allure.feature('查询功能')
@pytest.mark.parametrize('projectsname', load_projects_yaml(projectsname_path))
class TestProjectSearch:
    @allure.story('工程名称输入框查询')
    def test_projects_search(self, projectsname):
        logging.info(projectsname)
        SysHomePage().search_projectsname(projectsname)
        load_log().info('查询功能正常')
