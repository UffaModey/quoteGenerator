# quoteGenerator
This project uses AWS Lambda, EventBridge, and OpenAI’s API to generate motivational quotes automatically on a schedule (like every morning). The Lambda function is containerized and deployed using Amazon ECR (Elastic Container Registry).

## 🔧 What It Does
- Uses a Python Lambda function to call the OpenAI Chat API and generate a motivational quote.
- Schedules the function to run at specific times using AWS EventBridge.
- Logs each quote to AWS CloudWatch Logs.
- Entirely serverless and fits within AWS free tier (if used reasonably).

## 🧱 Tech Used

- **Python 3.11** – Used to write the Lambda function that sends a prompt to OpenAI and processes the response.
- **AWS Lambda (Container Image)** – Runs the function code inside a Docker container deployed to AWS.
- **Amazon ECR** – Stores the Docker container image that was built locally and used to deploy the Lambda function.
- **EventBridge (Cloud Scheduler)** – Triggers the Lambda function automatically on a set schedule (e.g., daily at 9 AM).
- **OpenAI GPT API** – Generates the motivational quote by responding to a custom prompt using OpenAI's language model.
- **CloudWatch Logs** – Captures and displays logs from each Lambda run so you can see the generated quote and debug if needed.

## ▶️ How to Run It

- clone the project locally
- update your environment variables in a `.env` file within the `generate_quotes` folder
  `- OPENAI_API_KEY=
  - REGION_NAME=
  - AWS_KEY_ID=
  - AWS_SECRET_ACCESS_KEY=`
- run script 
  - `bash local_lambda_deploy.sh`
