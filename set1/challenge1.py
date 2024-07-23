from base64 import b64encode

def hex_to_b64(inputString):
    input_as_bytes = bytes.fromhex(inputString)
    b64 = b64encode(input_as_bytes).decode()
    return b64
