class SinhVien:
    count = 0

    def __init__(self, diem):
        self.diem = diem
        SinhVien.count += 1

    @classmethod
    def get_count(cls):
        return cls.count