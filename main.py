from src.requests_api import Ethereum_Balance
from src.data_sqlite import Data_Sqlite


def main(address):
    module = "account"
    action = "balancemulti"
    tag = "latest"
    apikey = "NSN54XGSU8M8I6C91FY4QY47GQ9D3V3RGM"

    try:
        result = Ethereum_Balance(module, action, address, tag, apikey).get_balance()
        print(result)
        # print(result['result'][0]['balance'])
        if result['status'] == '1':
            Data_Sqlite().create_wallet((address, result['result'][0]['balance'], 1))
        else:
            Data_Sqlite().create_wallet((address, '-1', 0))
    except Exception as e:
        print(e)
        main(address)


if __name__ == "__main__":

    with open('./data/20k_wallet.txt', 'r') as file:
        # reading each line
        for line in file:
            # reading each word
            for address in line.split():
                # displaying the words
                main(address)
