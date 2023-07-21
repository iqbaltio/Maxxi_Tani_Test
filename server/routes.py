from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from server.model import Pegawai, Divisi

router = APIRouter()

#Data Dummy Pegawai
data_pegawai = {
    "1": {
        "nomor_pegawai": 1,
        "nama": "Iqbal Tio",
        "email": "iqbal@gmail.com",
        "nomor_hp": "081217409999",
        "alamat": "Jalan Kali Urang",
        "id_divisi": 1
    },
    "2": {
        "nomor_pegawai": 2,
        "nama": "Example Man 2",
        "email": "man2@gmail.com",
        "nomor_hp": "081415409999",
        "alamat": "Jalan Malang Utara",
        "id_divisi": 1
    }
}

#Data Dummy Divisi
data_divisi = {
    "1": {
        "id_divisi": 1,
        "nama_divisi": "Marketing"
    },
    "2": {
        "id_divisi": 2,
        "nomor_pegawai": "RnD"
    }
}

@router.get("/pegawai")
async def get_pegawai() -> dict:
    if len(data_pegawai) == 0:
        return {"message": "Data is Empty"}
    else:
        return {"data": data_pegawai}

@router.get("/pegawai/{id}")
async def get_pegawai(id: str) -> dict:
    if id not in data_pegawai:
        return {
            "error": "Invalid Pegawai ID"
        }
    return {
        "data": data_pegawai[id]
    }

@router.get("/pegawai/divisi/{id_divisi}")
async def get_divisi_pegawai(id_divisi: int):
    pegawai_divisi = [pegawai for pegawai in data_pegawai.values() if pegawai["id_divisi"] == id_divisi]
    
    if not pegawai_divisi:
        return {
            "error": "Invalid Divisi ID"
        }
    
    return {
        "data": pegawai_divisi
    }


@router.post("/pegawai")
async def add_pegawai(pegawai: Pegawai = Body(...)) -> dict():
    pegawai.nomor_pegawai = str(len(data_pegawai) + 1)
    data_pegawai[pegawai.nomor_pegawai] = jsonable_encoder(pegawai)
    
    return {
        "message": "Note added successfully",
        "data": data_pegawai[pegawai.nomor_pegawai]
    }

@router.put("/pegawai/{id}")
def update_pegawai(id: str, pegawai: Pegawai):
    stored_pegawai = data_pegawai[id]
    if stored_pegawai:
        stored_pegawai_model = Pegawai(**stored_pegawai)
        update_data = pegawai.dict(exclude_unset=True)
        updated_pegawai = stored_pegawai_model.copy(update=update_data)
        data_pegawai[id] = jsonable_encoder(updated_pegawai)
        return {
            "message": "Pegawai updated successfully"
        }
    return {
        "error": "No such with ID passed exists."
    }

@router.delete("/pegawai/{id}")
def delete_pegawai(id: str) -> dict:
    if int(id) > len(data_pegawai):
        return {
            "error": "Invalid note ID"
        }

    for pegawai in data_pegawai.keys():
        if pegawai == id:
            del data_pegawai[pegawai]
            return {
                "message": "Pegawai deleted"
            }

    return {
        "error": "Pegawai with {} doesn't exist".format(id)
    }

@router.get("/divisi")
async def get_divisi() -> dict:
    return {
        "data": data_divisi
    }

@router.get("/divisi/{id}")
async def get_divisi(id: str) -> dict:
    if id not in data_divisi:
        return {
            "error": "Invalid Divisi ID"
        }
    return {
        "data": data_divisi[id]
    }

@router.post("/divisi")
async def add_divisi(divisi: Divisi = Body(...)) -> dict():
    divisi.id_divisi = str(len(data_divisi) + 1)
    data_divisi[divisi.id_divisi] = jsonable_encoder(divisi)
    
    return {
        "message": "Divisi added successfully",
        "data": data_divisi[divisi.id_divisi]
    }

@router.put("/divisi/{id}")
def update_divisi(id: str, divisi: Divisi) -> dict:
    stored_divisi = data_divisi[id]
    if stored_divisi:
        update_data_divisi = divisi.dict(exclude_unset=True)
        update_data_divisi.update({"nama_divisi": divisi.nama_divisi})
        updated_divisi = Divisi(**update_data_divisi)
        data_divisi[id] = jsonable_encoder(updated_divisi)
        return {
            "message": "Divisi updated successfully"
        }
    return {
        "error": "No such with ID passed exists."
    }

@router.delete("/divisi/{id}")
def delete_divisi(id: str) -> dict:
    if int(id) > len(data_divisi):
        return {
            "error": "Invalid note ID"
        }

    for divisi in data_divisi.keys():
        if divisi == id:
            del data_divisi[divisi]
            return {
                "message": "Divisi deleted"
            }

    return {
        "error": "Divisi with {} doesn't exist".format(id)
    }
