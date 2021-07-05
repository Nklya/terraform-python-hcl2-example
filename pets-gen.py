#!/usr/bin/env python3

import argparse
import json
import random


def main():
    parser = argparse.ArgumentParser(description="Generate .tfvars for Terraform")
    parser.add_argument("--count", "-c", type=int, default=9, help="Amount of pets")
    args = parser.parse_args()

    pets = {}
    for i in range(args.count):
        pets[i] = {
            "length": random.randrange(1, 6),
            "separator": random.choice(["-", "_", " and ", " or "]),
        }

    print(json.dumps(pets, indent=2))

    # write variable name
    with (open("terraform.tfvars", "w")) as f:
        f.write("pets = ")
    # write dictionary itself
    with (open("terraform.tfvars", "a")) as f:
        json.dump(pets, f, indent=2, separators=[",", " = "])


if __name__ == "__main__":
    main()
