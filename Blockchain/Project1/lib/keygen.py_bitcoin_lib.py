from bitcoinlib.wallets import Wallet

def main():
    create_wallet()

def show_wallet():
    w = Wallet('MyTestWallet2')
    key = w.get_key()
    print("Private key:", key.wif)
    print("Address:", key.address)

def create_wallet():
    w = Wallet.create('MyTestWallet2', network='testnet')
    key = w.get_key()
    print("Private key:", key.wif)
    print("Address:", key.address)

if __name__ == "__main__":
    main()