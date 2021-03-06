assert __name__ == "__main__"

import sys
import os
import subprocess
import shutil

from . import config

os.chdir('node-{}'.format(config.nodeVersion))

configureArgvs = config.configFlags

if config.nodeTargetConfig == 'Debug':
    configureArgvs = configureArgvs + ['--debug-nghttp2', '--debug-lib']

if sys.platform == 'win32':
    env = os.environ.copy()
    env['config_flags'] = ' '.join(configureArgvs)


    if config.nodeTargetConfig == 'Release':
        print("==============BUILDING RELEASE LIBRARIES=================")
        subprocess.check_call(
            ['cmd', '/c', 'vcbuild.bat', 'release', 'x86', 'small-icu'],
            env=env
        )
    elif config.nodeTargetConfig == 'Debug':
        print("==============BUILDING DEBUG LIBRARIES=================")
        subprocess.check_call(
            ['cmd', '/c', 'vcbuild.bat', 'debug', 'debug-nghttp2', 'x86', 'small-icu'],
            env=env
        )
    else:
        print("======UNKNOWN=======")
else:
    # Build as release
    if config.nodeTargetConfig == 'Release':
        print("==============BUILDING RELEASE LIBRARIES=================")
        subprocess.check_call([ sys.executable, 'configure.py', '--ninja' ] + configureArgvs)
        subprocess.check_call(['ninja', '-C', 'out/Release'])
    elif config.nodeTargetConfig == 'Debug':
    # Build as debug
        print("==============BUILDING DEBUG LIBRARIES=================")
        subprocess.check_call([ sys.executable, 'configure.py', '--ninja', '--debug' ] + configureArgvs)
        subprocess.check_call(['ninja', '-C', 'out/Debug'])
    else:
        print("==========UNKNOWN=========")
