[![CI](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week13_Individual/actions/workflows/cicd.yml)
## Auto Scaling Flask App Using Any Serverless Platform

[Study Not Study](https://studyorstudy.delightfulground-53e5bf44.westus2.azurecontainerapps.io)
[Youtube Link]()

### Project Summary 

### Overview:
The project is a Flask web application integrated with the Hugging Face model for Visual Question Answering (VQA). It utilizes Docker for containerizatio and showcases image processing capabilities.

### Key Components:

#### Flask Web Application:
- **Functionality:** The web app (`main.py`) incorporates routes for the index page, "not study" page, "study" page, and a prediction endpoint. Users can upload images to predict whether the person is studying or not.

- **HTML Templates:** The project contains HTML templates (`index.html`, `not_study.html`, `study.html`) providing a user-friendly interface.

#### Hugging Face Model Integration:
- **API Interaction:** The application interfaces with the Hugging Face VQA model (`query` function) via API calls. It sends images along with a predefined question to get predictions.

- **Prediction Logic:** Based on model predictions, the app determines whether the person in the image is studying or not. The decision is made by comparing confidence scores for "yes" and "no" answers from the model.

#### Docker Containerization:
- **Dockerfile:** The Dockerfile (`Dockerfile`) is provided to containerize the Flask app

#### Deployment to Azure Web App:
- **Azure Configuration:** Environment variables are utilized for sensitive information like API tokens. Azure-specific configurations are in place for secure deployment on Azure Web App.

### Functionality and Creativity:

- **Embedded Language Model:** The application integrates the Hugging Face VQA model

- **User Interaction:** Users can choose to upload an image for prediction or use a default image. The application processes the uploaded image or the default image using the integrated model.

### DockerHub and Azure Web App Deployment:

- **Azure Container Registry :** The Docker image is hosted on Azure Container Registry

- **Azure Web App Deployment:** The Flask app is successfully deployed on Azure Web App, providing a public endpoint for users to interact with the application.

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



