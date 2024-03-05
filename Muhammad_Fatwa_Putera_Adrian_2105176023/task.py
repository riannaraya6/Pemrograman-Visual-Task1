class Mahasiswa:
    def _init_(self, nama, kelas, prodi, fakultas, tempat_tinggal, asal):
        self.nama = nama
        self.kelas = kelas
        self.prodi = prodi
        self.fakultas = fakultas
        self.tempat_tinggal = tempat_tinggal
        self.asal = asal

    def tampilkan_info(self):
        print(f"Nama: {self.nama}")
        print(f"Kelas: {self.kelas}")
        print(f"Prodi: {self.prodi}")
        print(f"Fakultas: {self.fakultas}r")
        print(f"Tempat Tinggal: {self.tempat_tinggal}")
        print(f"Asal: {self.asal}")


# Contoh penggunaan
mahasiswa1 = Mahasiswa("Rian", "A1", "Pendidikan Komputer", "Pendidik", "Kalimantan", "Jakarta")
mahasiswa1.tampilkan_info()
