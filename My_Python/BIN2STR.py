# Binary sequence converted to string

def bin2str(msg_bin):
    msg = ''
    for i in range(0, len(msg_bin),8):
        msg = msg + chr(int(msg_bin[i:i+8],2))
    return msg

