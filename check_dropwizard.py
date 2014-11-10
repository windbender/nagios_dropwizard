#!/usr/bin/python

import urllib2
import json
import sys


host = sys.argv[1]
port = sys.argv[2]
part_to_check = sys.argv[3]

class BetterHTTPErrorProcessor(urllib2.BaseHandler):
    # a substitute/supplement to urllib2.HTTPErrorProcessor
    # that doesn't raise exceptions on status codes 201,204,206
    def http_error_201(self, request, response, code, msg, hdrs):
        return response
    def http_error_204(self, request, response, code, msg, hdrs):
        return response
    def http_error_206(self, request, response, code, msg, hdrs):
        return response
    def http_error_500(self, request, response, code, msg, hdrs):
        r =response.read() 
        j = json.loads(r)
        if j[part_to_check]['healthy'] == True:
            print '%s is OK' % part_to_check
            sys.exit(0)
        else:
            print '%s is broken = %s ' % (part_to_check,j[part_to_check]['message'])
            sys.exit(2)
	

try:
    opener = urllib2.build_opener(BetterHTTPErrorProcessor)
    urllib2.install_opener(opener)

    req = urllib2.Request("http://%s:%s/healthcheck" % (host,port))
    data = urllib2.urlopen(req)

    r = data.read();
    j = json.loads(r);
    if j[part_to_check]['healthy'] == True:
        print '%s is OK' % part_to_check
	sys.exit(0)
    else:
        print '%s is broken = %s ' % (part_to_check,j[part_to_check]['message'])
        sys.exit(2)	
except urllib2.HTTPError, err:
    r = data.read();
    j = json.loads(r);
    if j[part_to_check]['healthy'] == True:
        print '%s is OK' % part_to_check
        sys.exit(0)
    else:
        print '%s is broken = %s ' % (part_to_check,j[part_to_check]['message'])
        sys.exit(2)	

