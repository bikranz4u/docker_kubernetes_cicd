#https://jupyter-notebook.readthedocs.io/en/latest/config.html
#https://www.dataquest.io/blog/jupyter-notebook-tips-tricks-shortcuts/

import os
from IPython.lib import passwd

#c = c  # pylint:disable=undefined-variable
#c.NotebookApp.allow_origin = '*' #allow all origins
c.NotebookApp.ip = '0.0.0.0'      # listen on all IPs
c.NotebookApp.port = int(os.getenv('PORT', 8888))
c.NotebookApp.open_browser = False #If you want to get it from browser make it "True"


# sets a password if PASSWORD is set in the environment
if 'PASSWORD' in os.environ:
  password = os.environ['PASSWORD']
  if password:
    c.NotebookApp.password = passwd(password)
  else:
    c.NotebookApp.password = ''
    c.NotebookApp.token = ''
  del os.environ['PASSWORD']
