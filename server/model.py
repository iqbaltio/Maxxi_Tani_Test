from pydantic import BaseModel

#Model untuk pegawai
class Pegawai(BaseModel):
    nomor_pegawai: int
    nama: str
    email: str
    nomor_hp: str
    alamat: str

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
            "alamat": "Jalan Malang"
        }
    }

class ConfigDivisi:
    schema_extra = {
        "example": {
            "nama_divisi": "Example"
        }
    }