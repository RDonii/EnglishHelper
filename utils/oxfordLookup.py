import requests
from data import config

app_id = config.APP_ID
app_key = config.APP_KEY

language = "en-gb"


def getDefinitions(word_id: str):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    r = requests.get(url, headers={"app_id": app_id, "app_key": app_key}).json()
    data = []
    if 'error' in r.keys():
        return False

    for result in r['results']:
        primary_data = {
            'definitions': [],
            'audios': []
        }
        if 'lexicalEntries' in result.keys():
            for lexicalEntry in result['lexicalEntries']:
                if 'entries' in lexicalEntry.keys():
                    for entry in lexicalEntry['entries']:
                        if 'senses' in entry.keys():
                            for sense in entry['senses']:
                                if 'definitions' in sense.keys():
                                    for definition in sense['definitions']:
                                        primary_data['definitions'].append(f'🔸{definition}')
                                if 'pronunciations' in entry.keys():
                                    for pronunciation in entry['pronunciations']:
                                        if 'audioFile' in pronunciation.keys():
                                            if pronunciation['audioFile'] not in primary_data['audios']: #lexicalEntry ko'p bo'lganda audio lar takrorlanar ekan, bizda takrorlanishi oldini olindi
                                                primary_data['audios'].append(pronunciation['audioFile'])
        if len(primary_data['definitions'])>0 or len(primary_data['audios'])>0:
            data.append(primary_data)
    
    return data

if __name__ == '__main__':
    from pprint import pprint as print
    data = getDefinitions('orange')
    print(data)