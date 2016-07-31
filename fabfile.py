#/usr/bin python
from fabric.api import local

def vendor():
    LIBS = {
        'curl.js': 'https://raw.githubusercontent.com/cujojs/curl/0.8.12/dist/curl/curl.js',
        'curl.md': 'https://raw.githubusercontent.com/cujojs/curl/0.8.12/README.md',
        'lodash.js': 'https://raw.githubusercontent.com/lodash/lodash/master/dist/lodash.js',
        'riot+c.js': 'https://raw.githubusercontent.com/riot/riot/master/riot%2Bcompiler.js',
        'md5.js': 'https://raw.githubusercontent.com/blueimp/JavaScript-MD5/master/js/md5.js'
    }
    local('mkdir -p public/vendor', capture=True)
    for output, source in LIBS.items():
        # TODO if file exists
        local('wget %s -O public/vendor/%s' % (source, output))
