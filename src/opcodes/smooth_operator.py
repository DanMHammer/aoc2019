def add(data, in1, in2): return data[in1] + data[in2]
def multiply(data, in1, in2): return data[in1] * data[in2]
def stop(data, in1, in2): return False


operations = {
    1: add,
    2: multiply,
    99: stop
}

if __name__ == "__main__":
    for key, value in operations.items():
        print(f"Opcode: {key} Function Name: {value.__name__}")