from yaml import load, dump


with open("deploy.yaml", "r") as stream:
    data = load(stream)
    print(data)
