from yaml import load, dump


with open("input.yaml", "r") as in_stream:
    data = load(in_stream)
    print(data)

    with open("output.yaml", "w") as out_stream:
        out_stream.write(dump(data))
