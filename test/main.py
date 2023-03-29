from protocol import pr_pb2 as pr
from google.protobuf.internal.encoder import _VarintBytes
from google.protobuf.internal.decoder import _DecodeVarint32
from parser import parseDelimited
import unittest




def serializeDelimited(msg):
    serialize_msg = msg.SerializeToString()
    size = msg.ByteSize()
    result_serialize_msg = _VarintBytes(size) + msg.SerializeToString()
    return result_serialize_msg


class Test(unittest.TestCase):
    def test_parseDelimited(self):
        msg1 = pr.WrapperMessage()
        msg2 = pr.WrapperMessage()
        msg3 = 'rth'

        msg1.fast_response.current_date_time = "34"
        msg2.slow_response.connected_client_count = 23

        ser_msg1 = serializeDelimited(msg1)
        ser_msg2 = serializeDelimited(msg2)

        r1, r_size = parseDelimited.parseDelimited(ser_msg1)
        r2, r_size = parseDelimited.parseDelimited(ser_msg2)
        r3, r_size = parseDelimited.parseDelimited(msg3)

        self.assertEqual(r1.fast_response.current_date_time, "34")
        self.assertEqual(r2.slow_response.connected_client_count, 23)
        self.assertEqual(r3, None)


    def test_DelimitedMessagesStreamParser(self):
        pass









unittest.main()





