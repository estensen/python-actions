from yaml import load, dump, Loader


with open("pipelines.yaml", "a+") as production_file:
    production_file.seek(0)  # Hack to both read and write
    deployed_pipelines = load(production_file, Loader)

    with open("pipeline.yaml", "r+") as deploy_file:
        pipeline_updates = load(deploy_file, Loader)
        if not pipeline_updates:
            exit("Empty deployment file")

        print("Deploying...")
        changes = False
        for pipeline in pipeline_updates:
            data = pipeline_updates[pipeline]

            if pipeline in deployed_pipelines:
                old_data = deployed_pipelines[pipeline]
                if data == old_data:
                    continue

            deployed_pipelines[pipeline] = data
            changes = True
            print(f"{pipeline} deployed")  # Or actually run a deployment script

        if not changes:
            print("Changes are already deployed")

        production_file.truncate(0)  # Remove content from file
        production_file.write(dump(deployed_pipelines))
        deploy_file.truncate(0)
        print("Deployment complete")
