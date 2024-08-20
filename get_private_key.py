from eth_account import Account


Account.enable_unaudited_hdwallet_features()

def extract_first_address_and_key(mnemonic):
    # 从助记词创建账户
    account = Account.from_mnemonic(mnemonic.strip())
    # 获取第一个地址和私钥
    address = account.address
    private_key = account.key.hex()  # 私钥为十六进制格式

    return address, private_key

# 示例用法，假设你有一个助记词
mnemonic = "助记词"
print(f"Address: {address}, Private Key: {private_key}")


with open(filename, 'r') as file:
    for line_number, mnemonic in enumerate(file, 1):
        address, private_key = extract_first_address_and_key(mnemonic)

address, private_key = extract_first_address_and_key(mnemonic)
print(f"Address: {address}, Private Key: {private_key}")


