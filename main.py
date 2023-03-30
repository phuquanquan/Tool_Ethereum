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

        print(response_dict)


if __name__ == "__main__":
    # module = "account"
    # action = "balancemulti"
    # address = "0xd0e45Ccf9B245fc848c910D49B8DE5834859980f,0xEF04aF269911C3EF2aadd77e2F610343Da0B49a4,0x0A1ecE6959B30DA3a46D86f02488FBf190f07dd0,"
    # tag = "latest"
    # apikey = "NSN54XGSU8M8I6C91FY4QY47GQ9D3V3RGM"
    #
    # Ethereum_Balance(module, action, address, tag, apikey).get_balance()

    with open('./data/Demo_Etherscan.txt', 'r') as file:

        # reading each line
        for line in file:

            # reading each word
            for word in line.split():
                # displaying the words
                print(word)
