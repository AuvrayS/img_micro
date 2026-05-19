# img_micro
image microservice for CS361
1. The microservice takes an input — such as a name or id — and returns a filepath of the image. If the image does not exist or no input is give, then the program returns an error respectively to the error.

2. To request data from the microservice, use the HTTP GET method, with the URL endpoint as /image including the parameter name. 
    ex: "http://localhost:3001/image?name=eclipse" whilst the server runs

3. To receive data from the microservice, the program responds with the image file itself. if no filepath found, an error JSON object is returned.
    ex: { "error": "No image found for the name: \"eclipse\""}

3. <img width="960" height="720" alt="Untitled drawing" src="https://github.com/user-attachments/assets/a1e17a62-f218-45e8-b6a8-5a53142f7ab1" />
