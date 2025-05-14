#!/bin/bash

# Set variables
ECR_REPO="quotegenerator"
IMAGE_TAG="latest"
AWS_REGION="eu-west-2"  # e.g., us-east-1
FUNCTION_PAYLOAD='{}'
AWS_ACCOUNT_ID="067795008911"

echo "🚀 Step 1: Rebuild Docker image"
docker build -t generate_quote_lambda .

echo "✅ Image built successfully!"

echo "🔐 Step 2: Log in to AWS ECR"
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin AWS_ACCOUNT_ID.dkr.ecr.eu-west-2.amazonaws.com

echo "🏷 Step 3: Tag image for ECR"
docker tag generate_quote_lambda:latest AWS_ACCOUNT_ID.dkr.ecr.eu-west-2.amazonaws.com/quotegenerator:latest

echo "📤 Step 4: Push image to ECR"
docker push AWS_ACCOUNT_ID.dkr.ecr.eu-west-2.amazonaws.com/quotegenerator:latest

echo "🎉 Deployment complete!"
