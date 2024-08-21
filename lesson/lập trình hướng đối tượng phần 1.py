#class có thể giúp người dùng tạo kiểu dữ liệu riêng cho mình
class ad:
    def __init__(self, name, weapon, color):
        self.tên = name
        self.vũ_khí = weapon
        self.màu = color

ad_cary = ad("ezreal", "súng", "vàng")
#ezreal có vị trí ở name, mà ta gọi name bằng self.tên
#súng có vị trí ở weapon, ...
#vàng có vị trí ở color, ...

print("tên của ad là", ad_cary.tên)
print("tên của vũ khí là", ad_cary.vũ_khí)
print("màu của nhân vật là", ad_cary.màu)

