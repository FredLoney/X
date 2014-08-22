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

    # The compilation target directory.
    dist_dir = os.path.join( config.SOFTWARE_PATH, 'dist' )
    if not os.path.exists(dist_dir):
        os.mkdir(dist_dir)
    dist_basename = os.path.join( dist_dir, config.SOFTWARE_SHORT.lower() )
    
    # Additional options. Note that debug is not a command option,
    # since the debug option determines the minimized vs unminimized
    # release below.
    options = entrypoint.parse( sys.argv )

    # Build the minimized target.
    options.debug = False
    config.BUILD_OUTPUT_PATH = dist_basename + '.min.js'
    builder = Builder()
    builder.run( options )

    # Build the unminimized target.
    options.debug = True
    config.COMPILATION_LEVEL = 'WHITESPACE_ONLY'
    config.BUILD_OUTPUT_PATH = dist_basename + '.js'
    builder = Builder()
    builder.run( options )
