import sys
from yaml import load, dump

if len(sys.argv) != 3:
    exit("Missing docker-image and description")

docker_image = sys.argv[1]
description = sys.argv[2]

data = {"docker-image": docker_image, "description": description}
print(data)

with open("deploy.yaml", "w") as f:
    f.write(dump(data))
