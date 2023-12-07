[![CI](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/actions/workflows/cicd.yml)
## Auto Scaling Flask App Using Azure Container Apps

[Study Not Study](https://studyorstudy.delightfulground-53e5bf44.westus2.azurecontainerapps.io)
[Youtube Link](https://youtu.be/TqL8lJM9T0w)

### Project Summary 

### Overview:
The project is a Flask web application integrated with the Hugging Face model for Visual Question Answering (VQA). It utilizes Docker for containerizatio and showcases image processing capabilities.

### Key Components:

#### Flask Web Application:
- **Functionality:** The web app (`main.py`) incorporates routes for the index page, "not study" page, "study" page, and a prediction endpoint. Users can upload images to predict whether the person is studying or not.

- **HTML Templates:** The project contains HTML templates (`index.html`, `not_study.html`, `study.html`) providing a user-friendly interface.

#### Hugging Face Model Integration:
- **API Interaction:** The application interfaces with the Hugging Face VQA model (`query` function) via API calls. It sends images along with a predefined question to get predictions.

<img width="795" alt="Screenshot 2023-12-06 at 11 39 02 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/assets/36715338/221c4135-2bb4-472a-9645-d2864828629f">


- **Prediction Logic:** Based on model predictions, the app determines whether the person in the image is studying or not. The decision is made by comparing confidence scores for "yes" and "no" answers from the model.

#### Docker Containerization:
- **Dockerfile:** The Dockerfile (`Dockerfile`) is provided to containerize the Flask app

#### Deployment to Azure Azure Container Apps:
- **Azure Configuration:** Environment variables are utilized for sensitive information like API tokens. Azure-specific configurations are in place for secure deployment on Azure Container Apps.
    
<img width="1123" alt="Screenshot 2023-12-06 at 11 19 51 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/assets/36715338/a3eb7b0c-a1f5-43fb-a27e-499a81d134cf">

### Scaling 
- The app will create another instance (up to 10) to divert requests when the original instance is overwhelmed
  <img width="1009" alt="Screenshot 2023-12-06 at 11 20 00 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/assets/36715338/0f30b714-73a8-4896-89c7-00af99fbe9f6">


### Functionality and Creativity:

- **Embedded Language Model:** The application integrates the Hugging Face VQA model

- **User Interaction:** Users can choose to upload an image for prediction or use a default image. The application processes the uploaded image or the default image using the integrated model.
  
    <img width="502" alt="Screenshot 2023-12-06 at 11 37 28 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/assets/36715338/69bd08f8-3caf-4197-baf8-1ad9b8abc274">

### Docker and Azure Container Apps Deployment:

- **Azure Container Registry :** The Docker image is hosted on Azure Container Registry
    <img width="1136" alt="Screenshot 2023-12-06 at 11 19 32 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/assets/36715338/1a3a673b-98e2-4763-b9fb-f90c921eb742">

- **Azure Container Apps Deployment:** The Flask app is successfully deployed on Azure Container Apps, providing a public endpoint for users to interact with the application. You can say the image name `studyorstudy` and image tag `20231130201151041148` being deployed with Azure container apps 
    <img width="1047" alt="Screenshot 2023-12-06 at 11 20 30 PM" src="https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/assets/36715338/ae4212df-96ac-42cd-9c61-49deb09c73f5">

### Preparation: 
1. git clone the repo
2. install: `make install`
3. get access to user token via Hugging Face
4. create an env file and add said user tojen
5. run: `python main.py` and navigate to the locally hosted website
6. upload image or use default image
7. build docker image: `docker build --tag <insert image name> .`
8. login to azure cli: `az login`
9. deploy azuer web app: `az containerapp up --resource-group <insert resource group> --name <insert app name> --ingress external --target-port 50505 --source .`
10. view app via `conatiner apps` and docker image via `container regsitry` in azure web portal 

### Check Format and Test Errors: 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`

### References
1. https://github.com/nogibjj/python-ruff-template
2. https://huggingface.co/docs/api-inference/detailed_parameters
3. https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app?tabs=web-app-flask
4. https://stackoverflow.com/questions/72705471/how-to-reference-secrets-in-azure-container-apps
5. https://learn.microsoft.com/en-us/azure/container-apps/scale-app?pivots=azure-cli
6. https://huggingface.co/dandelin/vilt-b32-finetuned-vqa



