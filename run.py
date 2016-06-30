#!/usr/bin/env python
"""run.py

"""

import os

from www import main

DEFAULT_HOST = '0.0.0.0'

DEFAULT_PORT = 5000

if __name__ == '__main__':
	main.app.run(host=DEFAULT_HOST, port=int(os.environ.get('PORT', DEFAULT_PORT)))