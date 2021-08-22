assert __name__ == "__main__"

import sys
import os
import subprocess
import shutil

from . import config

os.chdir('node-{}'.format(config.nodeVersion))

configureArgvs = [ '--enable-static', '--without-node-options' ] + config.configFlags

if sys.platform == 'win32':
    env = os.environ.copy()
    env['config_flags'] = ' '.join(configureArgvs)

    print("==============BUILDING RELEASE LIBRARIES=================")

    subprocess.check_call(
        ['cmd', '/c', 'vcbuild.bat', 'release'],
        env=env
    )

    print("==============BUILDING DEBUG LIBRARIES=================")
    
    subprocess.check_call(
        ['cmd', '/c', 'vcbuild.bat', 'debug'],
        env=env
    )
else:
    # Build as release
    print("==============BUILDING RELEASE LIBRARIES=================")
    subprocess.check_call([ sys.executable, 'configure.py', '--ninja' ] + configureArgvs)
    subprocess.check_call(['ninja', '-C', 'out/Release'])

    # Build as debug
    print("==============BUILDING DEBUG LIBRARIES=================")
    subprocess.check_call([ sys.executable, 'configure.py', '--ninja', '--debug' ] + configureArgvs)
    subprocess.check_call(['ninja', '-C', 'out/Debug'])