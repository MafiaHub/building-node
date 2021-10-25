assert __name__ == "__main__"

import sys
import os
import subprocess
import shutil

from . import config

os.chdir('node-{}'.format(config.nodeVersion))

configureArgvs = [ '--enable-static', '--without-node-options' ] + config.configFlags

if config.nodeTargetConfig == 'Debug':
    configureArgvs = configureArgvs + ['--debug-nghttp2', '--debug-lib']

if sys.platform == 'win32':
    env = os.environ.copy()
    env['config_flags'] = ' '.join(configureArgvs)


    if config.nodeTargetConfig == 'Release':
        print("==============BUILDING RELEASE LIBRARIES=================")
        subprocess.check_call(
            ['cmd', '/c', 'vcbuild.bat', 'release', 'x64', 'small-icu'],
            env=env
        )
    elif config.nodeTargetConfig == 'Debug':
        print("==============BUILDING DEBUG LIBRARIES=================")
        subprocess.check_call(
            ['cmd', '/c', 'vcbuild.bat', 'debug', 'debug-nghttp2', 'x64', 'small-icu'],
            env=env
        )
    else:
        print("======UNKNOWN=======")
