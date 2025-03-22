import re

class netlist:

    def __init__(self) -> None:
        # Create an empty dictionary to track wire values
        self.wires = {}
        self.line_regex = re.compile(r"(.+)->\s+(\S+)\s*")
        self.and_regex = re.compile(r"(\S+)\s+AND\s+(\S+)")
        self.or_regex = re.compile(r"(\S+)\s+OR\s+(\S+)")
        self.not_regex = re.compile(r"NOT\s+(\S+)")
        self.lshift_regex = re.compile(r"(\S+)\s+LSHIFT\s+(\d+)")
        self.rshift_regex = re.compile(r"(\S+)\s+RSHIFT\s+(\d+)")
        self.signal_regex = re.compile(r"^\s*(\d+)\s*$")
        self.wire_regex = re.compile(r"^\s*(\D\S+)\s*$")

    def add_line(self, line: str) -> None:
        line_values = self.line_regex.match(line)
        wire_name = line_values.group(2)

        # Check to see if the input matches any of the known operations
        and_match = self.and_regex.match(line_values.group(1))
        if and_match:
            op = self.and_gate(and_match.group(1), and_match.group(2), self.wires)
            self.wires[wire_name] = op
            return
        or_match = self.or_regex.match(line_values.group(1))
        if or_match:
            op = self.or_gate(or_match.group(1), or_match.group(2), self.wires)
            self.wires[wire_name] = op
            return
        not_match = self.not_regex.match(line_values.group(1))
        if not_match:
            op = self.not_gate(not_match.group(1), self.wires)
            self.wires[wire_name] = op
            return
        lshift_match = self.lshift_regex.match(line_values.group(1))
        if lshift_match:
            op = self.left_shift(lshift_match.group(1), int(lshift_match.group(2)), self.wires)
            self.wires[wire_name] = op
            return
        rshift_match = self.rshift_regex.match(line_values.group(1))
        if rshift_match:
            op = self.right_shift(rshift_match.group(1), int(rshift_match.group(2)), self.wires)
            self.wires[wire_name] = op
            return
        wire_match = self.wire_regex.match(line_values.group(1))
        if wire_match:
            op = self.wire_connection(wire_match.group(1), self.wires)
            self.wires[wire_name] = op
            return
        signal_match = self.signal_regex.match(line_values.group(1))
        if signal_match:
            op = self.signal(int(signal_match.group(1)))
            self.wires[wire_name] = op
            return


    # Define the circuit operators as internal classes.
    class signal:
        def __init__(self, value: int) -> None:
            self.value = value

        def output(self):
            return self.value & 0xffff

    class not_gate:
        def __init__(self, input: str, wires: dict):
            self.input = input
            self.wires = wires

        def output(self):
            a = self.wires.get(self.input, None)
            if a != None:
                return (~a.output() & 0xffff)
            else:
                return None
            
    class and_gate:
        def __init__(self, a: str, b: str, wires: dict):
            self.a = a
            self.b = b
            self.wires = wires

        def output(self):
            a = self.wires.get(self.a, None)
            b = self.wires.get(self.b, None)

            if a == None or b == None:
                return None
            else:
                return ((a.output() & b.output()) & 0xffff)
        
    class or_gate:
        def __init__(self, a: str, b: str, wires: dict):
            self.a = a
            self.b = b
            self.wires = wires

        def output(self):
            a = self.wires.get(self.a, None)
            b = self.wires.get(self.b, None)

            if a == None or b == None:
                return None
            else:
                return ((a.output() | b.output()) & 0xffff)

    class left_shift:
        def __init__(self, input: str, n: int, wires: dict):
            self.input = input
            self.n = n
            self.wires = wires

        def output(self):
            input = self.wires.get(self.input, None)

            if input == None:
                return None
            else:
                return ((input.output() << self.n) & 0xffff)

    class right_shift:
        def __init__(self, input: str, n: int, wires: dict):
            self.input = input
            self.n = n
            self.wires = wires

        def output(self):
            input = self.wires.get(self.input, None)

            if input == None:
                return None
            else:
                return ((input.output() >> self.n) & 0xffff)
        
    class wire_connection:
        def __init__(self, input: str, wires: dict) -> None:
            self.input = input
            self.wires = wires

        def output(self):
            input = self.wires.get(self.input, None)

            if input == None:
                return None
            else:
                return ((input.output()) & 0xffff)