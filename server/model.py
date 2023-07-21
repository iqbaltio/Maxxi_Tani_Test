from pydantic import BaseModel

#Model untuk pegawai
class Pegawai(BaseModel):
    nomor_pegawai: int
    nama: str
    email: str
    nomor_hp: str
    alamat: str
    id_divisi: int

#Model untuk divisi
class Divisi(BaseModel):
    id_divisi: int
    nama_divisi: str

class Config:
    schema_extra = {
        "example": {
            "nomor_pegawai": 0,
            "nama": "Example Man",
            "email": "man@gmail.com",
            "nomor_hp": "081417409999",
            "alamat": "Jalan Malang",
            "id_divisi": 0
        }
    }

class ConfigDivisi:
    schema_extra = {
        "example": {      
            "id_divisi": 0,
            "nama_divisi": "Example"
        }
    }