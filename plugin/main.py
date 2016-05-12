#!/usr/bin/env python
"""
Deploy builds to a Rancher orchestrated stack using rancher-compose
"""
import drone
import subprocess


def main():
    """
    The main entrypoint for the plugin.
    """
    # Retrives plugin input from stdin/argv, parses the JSON, returns a dict.
    payload = drone.plugin.get_input()
    # vargs are where the values passed in the YaML reside.
    vargs = payload["vargs"]

    # Required fields should raise an error
    url, key, secret = vargs['url'], vargs['access_key'], vargs['secret_key']

    # Formulate the POST request.
    data = payload["build"]
    print(payload)
    subprocess.call(["pwd"])
    subprocess.call(["ls", "-l"])


if __name__ == "__main__":
    main()
