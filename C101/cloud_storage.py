import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ap49KApdhreEqGyfgXL4NCVB--5rfmGjJGWZmZKK__7KRmdCnCHcLZnobDbh8HjIymUGQ4XibNJ1lXJGgYGc0edCK7XUXLKlLjKtZcloog8F87t3a79XNhxt2hSXbcoo4_pOoJA'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the full path to upload to DropBox: ")

    transferData.upload_file(file_from, file_to)
    print("File has been moved!!")

main()