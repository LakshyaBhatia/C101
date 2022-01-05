import dropbox

class TransferData:
    def __init__(self,access_token):
        self.access_token=access_token
    def upload_file(self,file_from,file_to):
        dbx=dropbox.Dropbox(self.access_token)
        with open(file_from,'rb')as f:
            dbx.files_upload(f.read(),file_to)

def main():
    access_token = "1hgul_hv9bwAAAAAAAAAATO0clngIRY47Ioh-W1Ke8Sj6KtvgNBePK-2Waono5Mo"
    transferData = TransferData(access_token)
    file_from = input("enter the path of the file")
    file_to = input("enter the path of the file to be uploaded")
    transferData.upload_file(file_from,file_to)

main()

#copy path of file then paste it in file from,then /namefolder/name of the file.extension 