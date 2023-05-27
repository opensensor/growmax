
class RelayBoard:
    def __init__(self, i2c, addr=0x27, num_relays=8):
        self.i2c = i2c
        self.addr = addr
        self.num_relays = num_relays
        # Initialize all relays to off (0)
        self.state = [0]*8

    def turn_on(self, position):
        # Turn on relay at the specified position
        position -= 1
        self.state[position] = 1
        self._write_state()

    def turn_off(self, position):
        # Turn off relay at the specified position
        position -= 1
        self.state[position] = 0
        self._write_state()

    def _write_state(self):
        # Convert state list to integer
        state_as_int = int(''.join(map(str, self.state)), 2)
        # If relay board uses active low, invert the bits before sending
        inverted_state = ~state_as_int & 0xFF
        print(f"Writing state to relay board: {bin(inverted_state)}")
        self.i2c.writeto(self.addr, inverted_state.to_bytes(1, "big"))
