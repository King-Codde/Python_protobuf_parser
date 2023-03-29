from protocol import pr_pb2 as pr
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32


def parseDelimited(data, bytesConsumed=0):
    try:
        n = bytesConsumed
        msg_len, new_pos = _DecodeVarint32(data, n)
        n = new_pos
        msg_buf = data[n:n+msg_len]
        n += msg_len
        read_msg = pr.WrapperMessage()
        read_msg.ParseFromString(msg_buf)
        return read_msg, n
    except IndexError and TypeError:
        return None, None


class DelimitedMessagesStreamParser:
    def __int__(self):
        self.buffer = ''
        self.bytesConsumed = 0

    def parse(self, data):
        self.buffer += data
        list_msg = []

        while self.bytesConsumed < len(data):
            new_msg, bytesConsumed = parseDelimited(data, self.bytesConsumed)
            if new_msg is not None:
                list_msg.append(new_msg)
                self.bytesConsumed += bytesConsumed
            else:
                break


        return list_msg