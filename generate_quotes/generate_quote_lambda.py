import openai
import requests
from openai import OpenAI
import os

# Set API keys and secrets using environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")

response = requests.get("https://www.google.com")
print(f"test internet access: {response.status_code}")


def generate_Qoute_from_open_ai():
    client = OpenAI(api_key=openai.api_key)
    print("Generating a motivational")

    prompt = (
        f"Write a short quote of no more than 10 - 20 words that includes these elements: "
        f"motivational, inspirational, funny"
    )

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": f"You are an inspiring leader who is a public figure and a thought leader.",
                },
                {"role": "user", "content": prompt},
            ],
        )

        generated_content = completion.choices[0].message.content
        print("Content generated from openAI API")

        return {"quote": generated_content}

    except Exception as e:
        return {"statusCode": 500, "error": str(e)}


def lambda_handler(event, context):

    try:

        result = generate_Qoute_from_open_ai()
        print("Successfully generated the story")

        return {"statusCode": 200, "body": result}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
