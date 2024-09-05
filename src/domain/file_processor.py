import os
import csv

from fastapi import HTTPException, UploadFile, status

class FileProcessor:
    # Manager of files and folders profcessor.
    def __init__(self):
        self.file_path = 'data/seu_file.csv'
        self.directory = 'data'


    def create_file(self):
        
        if not os.path.exists(self.directory):
            os.makedirs(os.path.dirname(self.file_path), exist_ok = True)
            with open(self.file_path, 'w', newline = '') as file:
                writer = csv.writer(file)
                writer.writerow(['Conta', 'agencia', 'texto', 'valor'])
                return {"mensagem": f' o arquivo {self.file_path} criado com sucesso!!!'}
        else:
            # rise = parada | não esperado
            # return = sucesso
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, 
                                detail="Arquivo já existe.")
        
    async def upload_file(self, file: UploadFile):
        """
        upload a file to raed and print data
        :param file: uploade file
        """
        if file.filename.endswith('.csv'):
            try:
                csv_reader = csv.DictReader(file.file)
                for row in csv_reader:
                    data = {"conta": row[0],
                            "agencia": row[1],
                            "texto": row[2],
                            "valor": float(row[3])}
                print(data)
                return {"menssage": f'Arqiuvo {file.filename} processado com sucesso'}
            except Exception as e:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                    detail='Falha ao precessar')
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE, 
                                detail="apenas csv.")