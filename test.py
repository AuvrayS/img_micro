import requests

BASE_URL = "http://localhost:3001/image"


def fetch_image(name):
    try:
        response = requests.get(BASE_URL, params={"name": name})

        if response.status_code == 200:
            filename = f"{name}_result.jpg"
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Saved: {filename}")

        elif response.status_code == 404:
            try:
                print("Error:", response.json().get("error"))
            except ValueError:
                print("Error: 404 but no JSON returned")

        else:
            print("Unexpected status code:", response.status_code)

    except requests.RequestException as e:
        print("Request failed:", e)


# test cases
fetch_image("eclipse")
fetch_image("something")
