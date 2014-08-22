#!/usr/bin/env python

#
# The XBUILD release generator.
#
# (c) 2012 The XTK Developers <dev@goXTK.com>
#

import sys
import os
from _core import (config, Builder, Entrypoint)

#
# entry point
#
if __name__ == "__main__":
  entrypoint = Entrypoint( description='Build the ' + config.SOFTWARE_SHORT + ' release.' )


  dist_dir = os.path.normpath( os.path.join( os.path.dirname(__file__), '..', 'dist' ) )
  if not os.path.exists(dist_dir):
      os.mkdir(dist_dir)
  dist_basename = os.path.join( dist_dir, config.SOFTWARE_SHORT.lower() )
  options = entrypoint.parse( sys.argv )

  options.debug = False
  config.BUILD_OUTPUT_PATH = dist_basename + '.min.js'
  builder = Builder()
  builder.run( options )

  options.debug = True
  config.COMPILATION_LEVEL = 'WHITESPACE_ONLY'
  config.BUILD_OUTPUT_PATH = dist_basename + '.js'

  builder = Builder()
  builder.run( options )
