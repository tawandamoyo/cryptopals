def xor(buffer1, buffer2):
    if (len(buffer1) != len(buffer2)):
        print("buffers not equal")
        return
    
    bytes1 = bytes.fromhex(buffer1)
    bytes2 = bytes.fromhex(buffer2)
    
    print(f"bytes1: {bytes1}")
    
    xor_result = bytes(x ^ y for x, y in zip(bytes1, bytes2)).hex()
    
    return xor_result
