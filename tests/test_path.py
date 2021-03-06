import os
import pytest
from pydu.platform import WINDOWS
from pydu.path import cd, is_super_path


def test_cd(tmpdir):
    path = str(tmpdir)
    cwd = os.getcwd()
    with cd(path):
        assert os.getcwd() == path
    assert os.getcwd() == cwd


class TestIsSupoerPath:
    def test_is_super_path_general(self):
        assert is_super_path('/aa/bb/cc', '/aa/bb/cc')
        assert is_super_path('/aa/bb', '/aa/bb/cc')
        assert is_super_path('/aa', '/aa/bb/cc')
        assert is_super_path('/', '/aa/bb/cc')
        assert is_super_path('/', '/')
        assert not is_super_path('/a', '/aa/bb/cc')

    @pytest.mark.skipif(not WINDOWS, reason='Not support on none-windows')
    def test_is_super_path_win(self):
        assert is_super_path('c:/aa/bb', 'c:/aa/bb\\cc')
        assert is_super_path('c:/aa/bb', 'c:/aa\\bb/cc')
        assert is_super_path('c:/aa\\bb', 'c:\\aa/bb/cc')
        assert is_super_path('c:/', 'c:\\')
