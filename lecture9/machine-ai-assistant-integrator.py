from openai import OpenAI
import dotenv
import json
import requests

client = OpenAI(api_key=dotenv.get_key(dotenv_path=".env", key_to_get="OPENAI_API_KEY"))

messages = [{
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "Jesteś asystentem sterującym pracą maszyny. Zwracasz wyłącznie JSON z komendami sterującymi: \n\n{\"command\": \"start|stop\", \"program\": \"nazwa programu obróbkowego\", \"partsToProduce\": liczba części do wyprodukowania} \n\nPamiętaj, zwracasz tylko JSON, bez żadnych dodatkowych tekstów. Odpowiadasz krótko."
        }
      ]
    }]


def askGptMachineAssistant(userInput : str):
    messages.append({
        "role": "user",
        "content": [
        {
            "type": "text",
            "text": userInput
        }
        ]
    })

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        response_format={
            "type": "text"
        },
        temperature=1,
        max_completion_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response

def sendCommandToMachine(commandJson):
    return requests.post("http://192.168.88.11:1880/control", json=commandJson)

while True:
    print("> ")
    userInput = input()

    response = askGptMachineAssistant(userInput)
    commandJson = json.loads(response.choices[0].message.content)

    machineResponse = sendCommandToMachine(commandJson)
    print(f"Machine response: {machineResponse}")
    