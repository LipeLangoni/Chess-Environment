import requests

url = '  http://cc75-34-142-214-20.ngrok.io/process_string'
data = {'position': 'rnbqk1nr/pppp1ppp/8/4p3/1b1P4/2P2N2/PP2PPPP/RNBQKB1R b KQkq - 0 1'}
response = requests.post(url, json=data)

if response.status_code == 200:
    result = response.json()
    output_string = result.get('best move')
    print(f"best move: {output_string}")
else:
    print(f"Error: {response.text}")