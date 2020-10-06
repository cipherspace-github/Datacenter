#!/usr/bin/python3

import base64

message = input("Message to Encode here:")
message_bytes = message.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)
base64_message = base64_bytes.decode('ascii')

print(base64_message)