from bitcoinlib.wallets import Wallet

def main():
    w = Wallet('MyTestWallet')
    key = w.get_key()
    print("Private key:", key.wif)
    print("Address:", key.address)

def create_wallet():
    w = Wallet.create('MyTestWallet', network='testnet')
    key = w.get_key()
    print("Private key:", key.wif)
    print("Address:", key.address)

if __name__ == "__main__":
    main()