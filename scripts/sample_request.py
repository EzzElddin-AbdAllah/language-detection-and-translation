import requests
import json


def sample_translation():
    url = "http://localhost:5000/lang_detection"

    payload = json.dumps({
    "sentence": "تعرف على ما إذا كان شخص ما يقول نكتة رائعة يمكنك أن تقول إنها جيدة."
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)



def sample_lang_detection():
    url = "http://localhost:5000/translation"

    payload = json.dumps({
    "sentence": "It was discontinued in February 2018."
    })
    headers = {
    'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(json.dumps(response.json(), ensure_ascii=False))



if __name__ == '__main__':
    sample_translation()
    sample_lang_detection()