import kagglehub

# Download latest version
path = kagglehub.dataset_download("ritesaluja/bank-note-authentication-uci-data")

print("Path to dataset files:", path)

#path = "/home/roy_ar/.cache/kagglehub/datasets/ritesaluja/bank-note-authentication-uci-data/versions/1/BankNote_Authentication.csv"