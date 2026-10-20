from genlayer import *

class GenLayerIntro(gl.Contract):
    """
    Kontrak pengantar GenLayer — infrastruktur kepercayaan untuk era AI
    """
    deskripsi: str
    status: str

    def __init__(self):
        self.deskripsi = "Blockchain AI-native dengan Demokrasi Optimis"
        self.status = "aktif"

    @gl.public.view
    def info(self) -> str:
        return f"GenLayer: {self.deskripsi} | Status: {self.status}"

    @gl.public.write
    def perbarui_status(self, status_baru: str) -> str:
        self.status = status_baru
        return f"Status diperbarui: {self.status}"
      Tambah file genlayer_intro.py
