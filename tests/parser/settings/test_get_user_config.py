# """Tests to verify correct work with user configs and system/user variables inside."""
# import os
# import shutil
#
# import pytest
#
# from yaml.scanner import ScannerError
# from tackle import models
# from tackle.settings import get_settings
#
#
# @pytest.fixture(scope='module')
# def user_config_path():
#     """Fixture. Return user config path for current user."""
#     return os.path.expanduser('~/.tacklerc')
#
#
# @pytest.fixture(scope='function')
# def back_up_rc(user_config_path):
#     """
#     Back up an existing cookiecutter rc and restore it after the test.
#
#     If ~/.tacklerc is pre-existing, move it to a temp location
#     """
#     user_config_path_backup = os.path.expanduser('~/.tacklerc.backup')
#
#     if os.path.exists(user_config_path):
#         shutil.copy(user_config_path, user_config_path_backup)
#         os.remove(user_config_path)
#
#     yield
#     # Remove the ~/.tacklerc that has been created in the test.
#     if os.path.exists(user_config_path):
#         os.remove(user_config_path)
#
#     # If it existed, restore the original ~/.tacklerc.
#     if os.path.exists(user_config_path_backup):
#         shutil.copy(user_config_path_backup, user_config_path)
#         os.remove(user_config_path_backup)
#
#
# @pytest.fixture
# def custom_config():
#     """Fixture. Return expected custom configuration for future tests validation."""
#     return {
#         'default_context': {
#             'full_name': 'Firstname Lastname',
#             'email': 'firstname.lastname@gmail.com',
#             'github_username': 'example',
#         },
#         'tackle_dir': '/home/example/some-path-to-templates',
#         'replay_dir': '/home/example/some-path-to-replay-files',
#         'abbreviations': {
#             'gh': 'https://github.com/{0}.git',
#             'gl': 'https://gitlab.com/{0}.git',
#             'bb': 'https://bitbucket.org/{0}',
#             'helloworld': 'https://github.com/hackebrot/helloworld',
#         },
#     }
#
#
# @pytest.mark.usefixtures('back_up_rc')
# def test_get_user_config_valid(user_config_path, custom_config, change_dir):
#     """Validate user config correctly parsed if exist and correctly formatted."""
#     shutil.copy('test-config/valid-config.yaml', user_config_path)
#     conf = get_settings()
#
#     assert conf.dict()['abbreviations'] == custom_config['abbreviations']
#
#
# @pytest.mark.usefixtures('back_up_rc')
# def test_get_user_config_invalid(user_config_path, change_dir):
#     """Validate `InvalidConfiguration` raised when provided user config malformed."""
#     shutil.copy('test-config/invalid-config.yaml', user_config_path)
#     with pytest.raises(ScannerError):
#         get_settings()
#
#
# @pytest.mark.usefixtures('back_up_rc')
# def test_get_user_config_nonexistent():
#     """Validate default app config returned, if user does not have own config."""
#     assert get_settings() == get_settings(default_config=True)
#
#
# @pytest.fixture
# def custom_config_path():
#     """Fixture. Return path to custom user config for tests."""
#     return 'test-config/valid-config.yaml'
#
#
# def test_specify_config_path(custom_config_path, custom_config):
#     """Validate provided custom config path should be respected and parsed."""
#     user_config = get_settings(custom_config_path)
#     assert user_config.dict()['tackle_dir'] == custom_config['tackle_dir']
#
#
# def test_default_config_path(user_config_path):
#     """Validate app configuration. User config path should match default path."""
#     assert models.USER_CONFIG_PATH == user_config_path
#
#
# def test_default_config_from_env_variable(
#     monkeypatch, custom_config_path, custom_config
# ):
#     """Validate app configuration. User config path should be parsed from sys env."""
#     monkeypatch.setenv('TACKLE_CONFIG', custom_config_path)
#
#     user_config = get_settings()
#     assert user_config.dict()['tackle_dir'] == custom_config['tackle_dir']
#     assert user_config.dict()['abbreviations'] == custom_config['abbreviations']
#     assert user_config.dict()['replay_dir'] == custom_config['replay_dir']
#
#
# def test_force_default_config(custom_config_path, custom_config, change_dir):
#     """Validate `default_config=True` should ignore provided custom user config."""
#     user_config = get_settings(custom_config_path, default_config=True)
#     assert user_config.dict()['tackle_dir'] != custom_config['tackle_dir']
#     assert user_config.dict()['abbreviations'] != custom_config['abbreviations']
#     assert user_config.dict()['replay_dir'] != custom_config['replay_dir']
#
#
# def test_expand_user_for_directories_in_config(monkeypatch, change_dir):
#     """Validate user pointers expanded in user configs."""
#
#     def _expanduser(path):
#         return path.replace('~', 'Users/bob')
#
#     monkeypatch.setattr('os.path.expanduser', _expanduser)
#
#     config_file = 'test-config/config-expand-user.yaml'
#
#     user_config = get_settings(config_file)
#     assert user_config.replay_dir == 'Users/bob/replay-files'
#     assert user_config.tackle_dir == 'Users/bob/templates'
#
#
# def test_expand_vars_for_directories_in_config(monkeypatch, change_dir):
#     """Validate environment variables expanded in user configs."""
#     monkeypatch.setenv('COOKIES', 'Users/bob/cookies')
#
#     config_file = 'test-config/config-expand-vars.yaml'
#
#     user_config = get_settings(config_file)
#     assert user_config.replay_dir == 'Users/bob/cookies/replay-files'
#     assert user_config.tackle_dir == 'Users/bob/cookies/templates'
