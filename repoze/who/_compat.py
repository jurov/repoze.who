try:
    STRING_TYPES = (str, unicode)
except NameError:
    STRING_TYPES = (str,)

try:
    u = unicode
    b = unicode
except NameError: #pragma NO COVER Python >= 3.0
    u = str
    b = bytes

try:
    from base64 import decodebytes
    from base64 import encodebytes
except: # Python < 3.0
    from base64 import decodestring as decodebytes
    from base64 import encodestring as encodebytes

try:
    from ConfigParser import ConfigParser
    from ConfigParser import ParsingError
except ImportError: #pragma NO COVER Python >= 3.0
    from configparser import ConfigParser
    from configparser import ParsingError

try:
    from Cookie import SimpleCookie
    from Cookie import CookieError
except ImportError: #pragma NO COVER Python >= 3.0
    from http.cookies import SimpleCookie
    from http.cookies import CookieError

try:
    from itertools import izip_longest
except ImportError: #pragma NO COVER Python >= 3.0
    from itertools import zip_longest as izip_longest

try:
    from StringIO import StringIO
except ImportError: #pragma NO COVER Python >= 3.0
    from io import StringIO

try:
    from urllib import urlencode
    from urllib import quote as url_quote
    from urllib import unquote as url_unquote
except ImportError: #pragma NO COVER Python >= 3.0
    from urllib.parse import urlencode
    from urllib.parse import quote as url_quote
    from urllib.parse import unquote as url_unquote

try:
    from urlparse import urlparse
    from urlparse import urlunparse
except ImportError: #pragma NO COVER Python >= 3.0
    from urllib.parse import urlparse
    from urllib.parse import urlunparse

import wsgiref.util
import wsgiref.headers

def REQUEST_METHOD(environ):
    return environ['REQUEST_METHOD']

def CONTENT_TYPE(environ):
    return environ['CONTENT_TYPE']

def USER_AGENT(environ):
    return environ.get('HTTP_USER_AGENT')

def AUTHORIZATION(environ):
    return environ.get('HTTP_AUTHORIZATION', '')

def get_cookies(environ):
    header = environ.get('HTTP_COOKIE', '')
    if 'paste-cookies' in environ:
        cookies, check_header = environ['paste.cookies']
        if check_header == header:
            return cookies
    cookies = SimpleCookie()
    try:
        cookies.load(header)
    except CookieError:
        pass
    environ['paste.cookies'] = (cookies, header)
    return cookies

def construct_url(environ):
    return wsgiref.util.request_uri(environ)

def header_value(environ, key):
    headers = wsgiref.headers.Headers(environ)
    values = headers.get(key)
    if not values:
        return ""
    if isinstance(values, list):
        return ",".join(values)
    else:
        return values
