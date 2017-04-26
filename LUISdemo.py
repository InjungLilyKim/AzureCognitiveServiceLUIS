#
# created by Injung Lily Kim
# last modified date: 3/9/2017
# contact: t-likim@microsoft.com
#
import httplib, urllib, base64, json

headers = { # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '6e4759895c8743948e8349802156cb87', # from LUIS page
}

params = urllib.urlencode({
})

# get application cultures
try:
    print("Get LUIS application cultures")
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/luis/api/v2.0/apps/cultures?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    parseddata = json.loads(data)
    print(json.dumps(parseddata, indent=4, sort_keys=True))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

# Review labeled examples
params = urllib.urlencode({
    'skip': '0',
    'take': '100',
})
appId = '28f63f13-f6f4-450f-9eeb-30bd6ace56b3?subscription'
versionId = '00852ce4b9f44233b96b8e2a79a81f65'

try:
    print("Get trained examples")
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("GET", "/luis/api/v2.0/apps/66ca97f1-bb8a-409b-a36c-8d6b6007d470/versions/0.1/examples?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    parseddata = json.loads(data)
    print(json.dumps(parseddata, indent=4, sort_keys=True))
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

