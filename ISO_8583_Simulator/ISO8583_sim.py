import struct


class ISO8583Simulator:
    def __init__(self):
        self.mti = ''
        self.bitmap = ''
        self.data_elements = {}

    def pack(self):
        packed_mti = struct.pack('!4s', self.mti.encode())
        packed_bitmap = bytearray()
        for b in self.bitmap:
            packed_bitmap.append(int(b))
        packed_data_elements = b''
        for i in range(1, 65):
            if i in self.data_elements:
                element = self.data_elements[i]
                packed_data_elements += struct.pack('!%ds' % len(element), element.encode())
        return packed_mti + packed_bitmap + packed_data_elements

    def unpack(self, message):
        self.mti = struct.unpack('!4s', message[0:4])[0].decode()
        self.bitmap = ''.join(format(x, '08b') for x in message[4:12])
        self.data_elements = {}
        i = 12
        for j in range(1, 65):
            if self.bitmap[j - 1] == '1':
                length = int.from_bytes(message[i:i + 2], 'big')
                i += 2
                self.data_elements[j] = message[i:i + length].decode()
                i += length


simulator = ISO8583Simulator()
simulator.mti = '0100'
simulator.bitmap = '1000000000000000'
simulator.data_elements = {
    2: '4111111111111111',
    4: '000000000100',
    7: '0203121212',
    11: '123456',
    12: '121212',
    13: '0212',
    17: '0203',
    22: '021',
    32: '1234567890123',
    37: '123456ABCDEF',
    41: '12345678',
    42: '123456789012345'
}

packed_message = simulator.pack()

simulator = ISO8583Simulator()
simulator.unpack(packed_message)
print('MTI: ', simulator.mti)
print('Bitmap: ', simulator.bitmap)
print('Data Elements: ', simulator.data_elements)