import requests
name = "eclipse"

response = requests.get(f"http://localhost:3001/image", params = {"name": name})

if response.status_code ==200:
    with open(f"{name}_result.jpg", "wb") as f:
        f.write(response.content)
    print(f"Successfully saved image as {name}_result.jpg")

elif response.status_code == 404:
    print("Error:", response.jason()["error"])
else:
    print("Unexpected status code:",response.status_code)