import requests
import os
import sys

_test_url = 'https://www.examenglish.com/PET/audio/pet_listening3.mp3'
download_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') 
print(download_path)

arguments = {}
for item in sys.argv:
    data = item.split('=')
    if len(data) > 1:
        arguments[data[0]] = data[1]

_required_params = ['url', 'filename']

for i in _required_params:
    if arguments.get(i) == None:
        print(f"Error, {i} not found.")
        sys.exit()

if arguments.get('path') and os.path.exists(arguments.get('path')):
    download_path = os.path.join(arguments.get('path'), arguments.get('filename'))
else:
    download_path = os.path.join(download_path, arguments.get('filename'))


def download(url, filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(os.path.join(download_path, filename), 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
                print("Writing:", type(chunk))

    print("\nSaved.")


try:
    download(arguments.get('url'), arguments.get('filename'))
except Exception as wtf:
    print(wtf)
sys.exit()