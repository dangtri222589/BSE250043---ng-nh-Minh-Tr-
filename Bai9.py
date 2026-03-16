class SinhVien:
    def __init__(self, diem):
        self.diem = diem

    def __eq__(self, other):
        if isinstance(other, SinhVien):
            return self.diem == other.diem
        return NotImplemented