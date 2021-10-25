assert __name__ != "__main__"

import os

nodeVersion = os.environ['NODE_TARGET_VERSION'] if 'NODE_TARGET_VERSION' in os.environ else 'v16.6.1'
nodeTargetConfig = os.environ['NODE_TARGET_CONFIG'] if 'NODE_TARGET_CONFIG' in os.environ else 'Debug'
configFlags = ['--with-intl=small-icu']
zipBasenameSuffix = '-smallicu'