# 🛡️ Market Financials Auth Lambda

This repository contains an AWS Lambda function responsible for API authentication. It validates API keys against a DynamoDB table to authorize requests. The function is containerized using Docker and deployed via GitHub Actions.

## 📂 Repository Structure

* **`app.py`**: The main Python application containing the Lambda handler logic.
* **`Dockerfile`**: Configuration for building the Docker image based on the AWS Lambda Python 3.14 runtime.
* **`.github/workflows/build-deploy.yml`**: CI/CD pipeline for building the image, pushing it to Amazon ECR, and updating the Lambda function.

## 🏗️ Architecture & Logic

The Lambda function expects an event containing HTTP headers. It specifically looks for an `x-api-key` header to validate authorization.

1.  **📥 Input:** The handler extracts headers from the incoming event.
2.  **🔍 Validation:**
    * It checks for the presence of `x-api-key`.
    * If present, it queries a DynamoDB table (defined by the `DYNAMODB_AUTH_TABLE_NAME` environment variable) to see if the key exists.
3.  **📤 Output:** Returns a dictionary indicating authorization status:
    * `{ "isAuthorized": True }` if the key exists in DynamoDB.
    * `{ "isAuthorized": False }` if the key is missing or invalid.

## 🚀 Deployment

Deployment is handled automatically via GitHub Actions when manually triggered on the `develop` branch.

### 🔄 CI/CD Pipeline
The workflow `build-deploy.yml` performs the following steps:
1.  **Build**:
    * Checks out the code and logs into Amazon ECR.
    * Generates a short SHA for versioning.
    * Builds the Docker image and tags it with both `:latest` and the short SHA.
    * Pushes both tags to the ECR registry at `x.dkr.ecr.af-south-1.amazonaws.com/<registry_name>`.
2.  **Deploy**:
    * Configures AWS credentials.
    * Updates the Lambda function code to use the newly pushed image URI (tagged with the short SHA).

### ⚙️ Environment Configuration
The deployment pipeline uses the following AWS configuration:
* **🌍 Region**
* **📦 ECR Registry**
* **⚡ Lambda Function Name**

## 💻 Local Development

To build the container locally:

```bash
docker build -t <image_name> .
```
*Note: This project uses the `public.ecr.aws/lambda/python:3.14-x86_64` base image.*

## ✅ Requirements

* **🔑 AWS Credentials**: The GitHub repository secrets must include `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` for deployment.
* **📝 Environment Variables**: The Lambda function requires `DYNAMODB_AUTH_TABLE_NAME` to be set in the runtime environment to locate the correct database table.

## 🔨Tools used:
[![My Skills](https://skillicons.dev/icons?i=py,aws,docker,git,githubactions&perline=6)](https://skillicons.dev)
