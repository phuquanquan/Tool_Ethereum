import requests

class Ethereum_Balance:
    def __init__(self, module, action, address, tag, apikey):
        self.module = module
        self.action = action
        self.address = address
        self.tag = tag
        self.apikey = apikey

    # Lay thong tin tai khoan
    def get_balance(self):
        url = f'https://api.etherscan.io/api?module={self.module}&action={self.action}&address={self.address}&tag={self.tag}&apikey={self.apikey}'
        response_user = requests.get(url)
        response_dict = response_user.json()

        return response_dict

        # print(response_dict['result'])

