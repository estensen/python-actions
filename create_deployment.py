import sys
from yaml import load, dump


if len(sys.argv) != 4:
    exit("Missing docker-image and description")

name = sys.argv[1]
docker_image = sys.argv[2]
description = sys.argv[3]

data = {name: {"docker-image": docker_image, "description": description}}
print("Adding deployment file...")
print(data)

with open("pipeline.yaml", "w") as f:
    f.write(dump(data))
