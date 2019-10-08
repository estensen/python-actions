from yaml import load, dump, Loader


with open("pipelines.yaml", "a+") as production_file:
    production_file.seek(0)  # Hack to both read and write
    pipelines = load(production_file, Loader)

    with open("pipeline.yaml", "r+") as deploy_file:
        pipeline = load(deploy_file, Loader)
        if not pipeline:
            exit("Empty deployment file")

        name = list(pipeline.keys())[0]
        data = pipeline[name]
        pipelines[name] = data

        if not pipelines:
            keys = set()
            print("No pipelines in production")
        else:
            keys = set(pipelines.keys())
            print(f"Pipelines in production: {keys}")

        print("Deploying...")
        print(f"Deployed {data}")
        production_file.truncate(0)  # Remove content from file
        production_file.write(dump(pipelines))
        deploy_file.truncate(0)
