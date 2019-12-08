from idna import unichr

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        data = [int(char) for char in file.read()]
        size = 25 * 6
        layers = [data[x:x+size] for x in range(0, len(data), size)]
        least_0 = layers[0]
        for layer in layers:
            if layer.count(0) < least_0.count(0):
                least_0 = layer
        print(f"Day One {least_0.count(1) * least_0.count(2)}")

        final = ["2" for x in range(size)]
        for x in range(0, size):
            for layer in layers:
                if final[x] != "2":
                    pass
                elif layer[x] != 2:
                    if layer[x] == 0:
                        final[x] = "*"
                    else:
                        final[x] = " "

        for y in range(0, 6):
            line = ""
            for x in range(0, 25):
                line += "   " + final[x + (y*25) ]
            print(line)
