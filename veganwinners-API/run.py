#!/usr/bin/env python

from app import app
from os import environ

if __name__ == '__main__':
    port = int(environ.get('PORT', 8000))
    app.run(host='127.0.0.1', port=port, debug=False)
