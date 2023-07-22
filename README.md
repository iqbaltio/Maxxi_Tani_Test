## Base URL :
https://maxi-tani-rvqmui4jmq-et.a.run.app/

## API Intern Test

### Endpoint
| Method | Endpoint | Description |
|:------:|:--------:|-------------|
|GET|`/pegawai`|untuk menampilkan data seluruh data pegawai|
|GET|`/pegawai/<nomor-pegawai>`|menampilkan detail dari 1 pegawai tertentu|
|GET|`/pegawai/divisi/<id-divisi> `|menampilkan list pegawai dari divisi tertentu|
|PUT|`/pegawai/<nomor-pegawai>`|untuk merubah data pegawai|
|POST|`/pegawai `|untuk menambah data pegawai|
|DELETE|`/pegawai/ `|untuk menghapus data pegawai|

### Example Usage
**Request**\
POST /pegawai/\
Content-Type: application/json
```JSON
{
    "nomor_pegawai": 16,
    "nama": "Ana Romanov",
    "email": "ana@example.com",
    "nomor_hp": "081217309999",
    "alamat": "Jalan Kali Judan",
    "id_divisi": 7
}
```

**Response**\
HTTP/1.1 200 OK\
Content-Type: application/json
```JSON
{
    "message": "Pegawai added successfully",
    "data": {
        "nomor_pegawai": "16",
        "nama": "Ana Romanov",
        "email": "ana@example.com",
        "nomor_hp": "081217309999",
        "alamat": "Jalan Kali Judan",
        "id_divisi": 7
    }
}
