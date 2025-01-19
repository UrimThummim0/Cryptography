import base64
token = "hm0uycadxwvoum1m211ce74dk6h53pxq2w0ih9srl05ozde1o6xbcd1btcc2m3ec"
decoded = base64.b64decode(token).decode('utf-8')
print(decoded)
