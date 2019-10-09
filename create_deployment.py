import sys
from yaml import dump


if len(sys.argv) != 4:
    exit("Missing docker-image and description")

name = sys.argv[1]
docker_image = sys.argv[2]
description = sys.argv[3]

data = {name: {"docker-image": docker_image, "description": description}}
print("Adding deployment file...")

with open("pipeline.yaml", "w") as f:
    f.write(dump(data))
    print("Deployment created!")
    print(data)
