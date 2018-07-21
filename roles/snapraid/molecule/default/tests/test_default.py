import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_snapraid_installed(host):
    snapraid = host.package('snapraid')
    assert snapraid.is_installed


def test_snapraid_config(host):
    config_file = host.file('/etc/snapraid.conf')
    assert config_file.exists
    assert config_file.user == 'root'
    assert config_file.group == 'root'
