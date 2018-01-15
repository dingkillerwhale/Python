# String converted to binary sequence

def str2bin(msg):
    msg_bin = ''
    for i in range(0, len(msg)):
        msg_bin = msg_bin + format(ord(msg[i]),'08b')
    return msg_bin

msg = 'This is a test message'
msg_bin = str2bin(msg)
print(msg_bin, end = '\n')
