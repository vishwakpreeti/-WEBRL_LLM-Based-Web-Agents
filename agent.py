import openai

# Azure OpenAI Configuration
openai.api_type = "azure"
openai.api_base = "https://testingapi.openai.azure.com/"
openai.api_version = "2023-12-01-preview"
openai.api_key = "967z4RksgDIq0KggjJfE2XYoRz9fD5GeZLGNNwUcCCvCyhh9L5NKJQQJ99BDACYeBjFXJ3w3AAABACOGhpis"

def get_action(prompt):
    print("Sending prompt to Azure OpenAI...")  # added for debug
    response = openai.ChatCompletion.create(
        engine="gpt-35-turbo-16k",  # IMPORTANT: Correct deployment name
        messages=[
            {"role": "system", "content": "You are a web navigation agent."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2,
        max_tokens=200,
    )
    print("Received response from Azure OpenAI!")  # added for debug
    action = response['choices'][0]['message']['content']
    return action
