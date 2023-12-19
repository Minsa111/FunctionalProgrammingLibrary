class Perpustakaan:
    def __init__(self):
        self.buku_tersedia = {}

    def tambah_buku(self, judul, pengarang):
        if judul not in self.buku_tersedia:
            self.buku_tersedia[judul] = {'pengarang': pengarang, 'dipinjam': False}
            print(f"Buku '{judul}' oleh {pengarang} telah ditambahkan ke perpustakaan.")
        else:
            print(f"Buku '{judul}' sudah ada dalam perpustakaan.")

class AkunUser:
    def __init__(self):
        self.buku_dipinjam = []

    def pinjam_buku(self, judul, perpustakaan):
        if judul in perpustakaan.buku_tersedia:
            buku = perpustakaan.buku_tersedia[judul]
            if not buku['dipinjam']:
                buku['dipinjam'] = True
                self.buku_dipinjam.append(judul)
                print(f"Anda telah meminjam buku '{judul}'.")
            else:
                print(f"Buku '{judul}' sedang dipinjam oleh orang lain.")
        else:
            print(f"Buku '{judul}' tidak ada dalam perpustakaan.")

    def kembalikan_buku(self, judul, perpustakaan):
        if judul in self.buku_dipinjam:
            buku = perpustakaan.buku_tersedia[judul]
            buku['dipinjam'] = False
            self.buku_dipinjam.remove(judul)
            print(f"Anda telah mengembalikan buku '{judul}'.")
        else:
            print("Buku ini tidak ada dalam daftar peminjaman Anda.")

if __name__ == "__main__":
    perpustakaan = Perpustakaan()
    user1 = AkunUser()
    user2 = AkunUser()

    perpustakaan.tambah_buku("Harry Potter", "J.K. Rowling")
    perpustakaan.tambah_buku("To Kill a Mockingbird", "Harper Lee")

    user1.pinjam_buku("Harry Potter", perpustakaan)
    user2.pinjam_buku("Harry Potter", perpustakaan)  # Gagal, buku sudah dipinjam

    user1.kembalikan_buku("Harry Potter", perpustakaan)
    user2.pinjam_buku("Harry Potter", perpustakaan)  # Sukses, buku sudah dikembalikan oleh user1
