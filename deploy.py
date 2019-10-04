from yaml import load, Loader


with open("deploy.yaml", "r") as f:
    data = load(f, Loader)
    print("Deploying...")
    print(data)
