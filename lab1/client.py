import json
import requests
import sys


if __name__ == "__main__":
    url, name, number = sys.argv[1], sys.argv[2], int(sys.argv[3])

    response = requests.get(f"{url}/hello_world")
    print(response.json()["message"])

    response = requests.get(f"{url}/hash?name={name}")
    name_hash = response.json()["result"]
    print(name_hash)

    payload = {"name": name, "hash": name_hash, "number": number}

    while True:
        response = requests.post(f"{url}/collatz", data=json.dumps(payload)).json()
        payload["number"] = response["result"]
        print(response["result"])
        if response["result"] == 1:
            break
