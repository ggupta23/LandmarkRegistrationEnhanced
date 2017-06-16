from pqWidget import *
from Visualization import *
from Landmarks import *
from RegistrationState import *
from RegistrationPlugin import *

for plugin in [
  'Affine',
  'ThinPlate',
  'LocalBRAINSFit',
  'LocalSimpleITK',
  'AffineAndThinPlate'
  ]:
  try:
    __import__('RegistrationLib.%sPlugin' % plugin)
  except ImportError, details:
    import logging
    logging.warning("Registration: Failed to import '%s' plugin: %s" % (plugin, details))
