from fastapi import APIRouter, UploadFile, FastAPI, File
from domain.file_processor import FileProcessor



router = APIRouter()


@router.get('/ola')
def hello():
    return {"Menssagem":'Olá'}

@router.post("/file/create_file")
async def create_file():
    
    return  FileProcessor().create_file()


@router.post("/upload_file")
async def upload_file(file: UploadFile = File(...)):
    return await FileProcessor().upload_file(file)


@router.post("/file/add_data")
async def add_data(conta: str, agencia: str, texto: str, valor: float):
    data = {"conta": conta, "agencia": agencia, "texto": texto, "valor": valor}
    return await FileProcessor().add_data_to_file(data)


@router.get("/file/list_files")
async def list_files():
    items = await FileProcessor().list_data_file()
    return {"menssage": items}

@router.delete("/file/delete_data")
async def delete_data(select_line: int):
    # delete_file =  await FileProcessor().delete_file()
    delete_data = await FileProcessor().delete_data(select_line)
    return {"menssage": delete_data}
