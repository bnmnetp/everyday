import paver
from paver.easy import *
import paver.setuputils
paver.setuputils.install_distutils_tasks()
import os, sys

from sphinxcontrib import paverutils

sys.path.append(os.getcwd())

home_dir = os.getcwd()
master_url = 'http://interactivepython.org'
master_app = 'runestone'
serving_dir = "./build/everyday"
dest = "../../static"

options(
    sphinx = Bunch(docroot=".",),

    build = Bunch(
        builddir="./build/everyday",
        sourcedir="_sources",
        outdir="./build/everyday",
        confdir=".",
        project_name = "everyday",
        template_args={'course_id': 'everyday',
                       'login_required':'false',
                       'appname':master_app,
                       'loglevel': 10,
                       'course_url':master_url,
                       'use_services': 'true',
                       'python3': 'true',
                       'dburl': 'postgresql://user:password@localhost/runestone'
                        }
    )
)

from runestone import build  # build is called implicitly by the paver driver.

