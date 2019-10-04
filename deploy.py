from yaml import load, dump, Loader


with open("pipelines.yaml", "a+") as pipelines:
    pipelines.seek(0)  # Hack to both read and write
    production_data = load(pipelines, Loader)

    if not production_data:
        keys = set()
        print("No pipelines in production")
    else:
        keys = set(production_data.keys())
        print(f"Pipelines in producton: {keys}")

    with open("pipeline.yaml", "r+") as pipeline:
        data = load(pipeline, Loader)
        if not data:
            exit("Empty deployment file")

        name = list(data.keys())[0]
        if keys and name in keys:
            exit(f"Pipeline '{name}'' is already in production")
            pipeline.truncate(0)

        print("Deploying...")
        print(f"Deployed {data}")
        pipelines.write(dump(data))
        pipeline.truncate(0)
