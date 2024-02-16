from openai import OpenAI
import json
import logging

logging.basicConfig(filename="gpt_prompt.log", level=logging.INFO)
data = {}
client = OpenAI()

# Load the prompts into a list for iteration
try:
    with open("train_questions.txt", 'r') as file:
        # Read the file lines into a list
        prompt_list = file.readlines()
except FileNotFoundError:
    logging.error("The file was not found.")
except Exception as e:
    logging.error(f"An error occurred: {e}")

# Iterate through the list, and sending the prompt to GPT4 for inference
for i in range(len(prompt_list)):
    prompt = prompt_list.pop()


    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "system",
                "content": "You are an expert analyst with extensive training in psychology, linguistics, forensics, and many other broad areas, and you are excellent at predicting implicit information about the user based on a conversation excerpt provided as a JSON. You will respond by giving another JSON as output.  Derive as much information you can from the input, including the psychological status, the writing style, semantic information, the person's personality, and any logical inferences that can be drawn.\nThink step by step and be exhaustive in the output.  Output as many derived inferences as you can, minimum 10.\n\nInput:\n{\n\"user\": \"what's a good birthday gift for my husband?\"\n}\n\nOutput:\n{\n\"is_married\": \"true\",\n\"is_adult\": \"true\",\n\"is_child\": \"false\",\n\"has_spending_power\": \"true\",\n\"is_caring\": \"true\",\n\"likes_to_plan\": \"true\",\n}\n\nInput:\n{\n\"user\": \"I am traveling to India. What is the weather there?\",\n\"user\": \"What are some good vegan restaurants in Bangalore?\",\n\"user\": \"When does my flight leave New York?\",\n\"user\": \"Will I get metformin in India?\"\n}\n\nOutput:\n{\n\"is_traveling\": \"true\",\n\"traveling_to\": \"India\",\n\"current_location\": \"New York\",\n\"eats_out\": \"true\",\n\"likes_to_plan\": \"true\",\n\"is_curious\": \"true\",\n\"has_spending_power\": \"true\"\n\"is_vegan\": \"true\",\n\"nonvegetarian\": \"unlikely\",\n\"has_health_condition\": \"true\",\n\"has_diabetes\": \"true\",\n\"on_medication\": \"metformin\"\n}"
            },
            {
                "role": "user",
                "content": '{{\n"user": "{}",\n}}'.format(prompt)
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_text = response.choices[0].message.content

    print(response_text)
    logging.info(f"{prompt}:{response_text}")
    data[prompt] = response_text


file_path = 'prompt_inference.json'

# Write the dictionary to a JSON file
with open(file_path, 'w') as json_file:
    json.dump(data, json_file, indent=4)
