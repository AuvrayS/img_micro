import requests
name = "eclipse"
name2 = "something"

response = requests.get(f"http://localhost:3001/image", params = {"name": name})

if response.status_code ==200:
    with open(f"{name}_result.jpg", "wb") as f:
        f.write(response.content)
    print(f"Successfully saved image as {name}_result.jpg")

elif response.status_code == 404:
    print("Error:", response.jason()["error"])
else:
    print("Unexpected status code:",response.status_code)

response2 = requests.get(f"http://localhost:3001/image", params = {"name": name2})

if response2.status_code ==200:
    with open(f"{name2}_result.jpg", "wb") as f:
        f.write(response2.content)
    print(f"Successfully saved image as {name2}_result.jpg")

elif response2.status_code == 404:
    print("Error:", response2.jason()["error"])
else:
    print("Unexpected status code:",response2.status_code)
