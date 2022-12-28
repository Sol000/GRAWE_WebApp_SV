# ------------------------------------------------------------------------
# Fileame:      config.py 
#
# Description:  Contains a "Config"-Class wich holds all configurations 
#               for the modules/libraries that are included
#
# Authors:      TM, ..... 
# ------------------------------------------------------------------------

# ------------------------------------------------------------------------
#                              INCLUDES
# ------------------------------------------------------------------------
import os
from datetime import timedelta

# ------------------------------------------------------------------------
#                              SETUP
# ------------------------------------------------------------------------
# get basedir
basedir = os.path.abspath(os.path.dirname(__file__))

# ------------------------------------------------------------------------
#                              Config-Class 
# ------------------------------------------------------------------------
class Config(object):
  JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)

  JWT_SECRET_KEY = "remember to change" #TODO: Change Key
  SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
      'sqlite:///' + os.path.join(basedir, 'data.db')
  SQLALCHEMY_TRACK_MODIFICATIONS = False
