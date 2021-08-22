assert __name__ != "__main__"

import os

nodeVersion = os.environ['NODE_TARGET_VERSION'] if 'NODE_TARGET_VERSION' in os.environ else 'v16.6.1'
configFlags = ['--without-intl']
zipBasenameSuffix = '-nointl'