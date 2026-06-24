class Player:
    def __init__(self, player_id, name, speed_score, technique_score, goal_score):
        self.id = player_id
        self.name = name
        self.speed_score = speed_score
        self.technique_score = technique_score
        self.goal_score = goal_score
        self.average_score = 0.0
        self.performance_type = ""
        self.calculate_average()
        self.classify_performance()

    def calculate_average(self):
        self.average_score = round(self.speed_score * 0.3 + self.technique_score * 0.4 + self.goal_score * 0.3, 2)

    def classify_performance(self):
        score = self.average_score
        if score < 5.0:
            self.performance_type = "Dự bị yếu"
        elif score < 6.5:
            self.performance_type = "Trung bình"
        elif score < 8.0:
            self.performance_type = "Tốt"
        else:
            self.performance_type = "Ngôi sao"


class PlayerManager:
    def __init__(self):
        self.players = []

    def check_id(self, player_id):
        return any(p.id == player_id for p in self.players)

    def show_all(self):
        if not self.players:
            print("Danh sách cầu thủ đang rỗng!")
            return
        self.print_players(self.players)

    def add_player(self):
        while True:
            player_id = input("Nhập mã cầu thủ: ").strip()
            if not player_id:
                print("Mã cầu thủ không được rỗng!")
                continue
            if self.check_id(player_id):
                print("Mã cầu thủ đã tồn tại! Vui lòng nhập mã khác.")
                continue
            break

        while True:
            name = input("Nhập họ tên cầu thủ: ").strip()
            if not name:
                print("Họ tên không được rỗng!")
                continue
            break

        speed = self.get_valid_score("Nhập điểm tốc độ (0-10): ")
        tech = self.get_valid_score("Nhập điểm kỹ thuật (0-10): ")
        goal = self.get_valid_score("Nhập điểm ghi bàn (0-10): ")

        new_player = Player(player_id, name, speed, tech, goal)
        self.players.append(new_player)
        print("Thêm cầu thủ thành công!")

    def update_player(self):
        if not self.players:
            print("Danh sách cầu thủ đang rỗng!")
            return
        player_id = input("Nhập mã cầu thủ cần cập nhật: ").strip()
        player = next((p for p in self.players if p.id == player_id), None)
        
        if not player:
            print("Không tìm thấy cầu thủ cần cập nhật!")
            return

        print(f"Cập nhật thông tin cho cầu thủ: {player.name}")
        player.speed_score = self.get_valid_score("Nhập điểm tốc độ mới (0-10): ")
        player.technique_score = self.get_valid_score("Nhập điểm kỹ thuật mới (0-10): ")
        player.goal_score = self.get_valid_score("Nhập điểm ghi bàn mới (0-10): ")
        
        player.calculate_average()
        player.classify_performance()
        print("Cập nhật cầu thủ thành công!")

    def delete_player(self):
        if not self.players:
            print("Danh sách cầu thủ đang rỗng!")
            return
        player_id = input("Nhập mã cầu thủ cần xóa: ").strip()
        player = next((p for p in self.players if p.id == player_id), None)

        if not player:
            print("Không tìm thấy cầu thủ cần xóa!")
            return

        confirm = input(f"Bạn có chắc muốn xóa cầu thủ [{player.name}] không? (Y/N): ").strip().lower()
        match confirm:
            case 'y':
                self.players.remove(player)
                print("Xóa thành công!")
            case 'n':
                print("Đã hủy thao tác!")
            case _:
                print("Nhập kí tự khác → thông báo nhập chưa đúng!")

    def search_player(self):
        if not self.players:
            print("Danh sách cầu thủ đang rỗng!")
            return
        keyword = input("Nhập tên cầu thủ cần tìm kiếm: ").strip().lower()
        results = [p for p in self.players if keyword in p.name.lower()]
        
        if not results:
            print("Không tìm thấy cầu thủ phù hợp!")
            return
        self.print_players(results)

    def get_valid_score(self, prompt):
        while True:
            try:
                score = float(input(prompt))
                if 0 <= score <= 10:
                    return score
                print("Điểm phải nằm trong khoảng từ 0 đến 10!")
            except ValueError:
                print("Sai kiểu dữ liệu! Vui lòng nhập một số.")

    def print_players(self, player_list):
        print(f"{'Mã cầu thủ':<10} | {'Họ tên':<20} | {'Tốc độ':<7} | {'Kỹ thuật':<8} | {'Ghi bàn':<8} | {'ĐTB':<6} | {'Phân loại':<12}")
        print("-" * 85)
        for p in player_list:
            print(f"{p.id:<10} | {p.name:<20} | {p.speed_score:<7} | {p.technique_score:<8} | {p.goal_score:<8} | {p.average_score:<6} | {p.performance_type:<12}")


def main():
    manager = PlayerManager()
    while True:
        print("\n================ MENU ================")
        print("1. Hiển thị danh sách cầu thủ")
        print("2. Thêm cầu thủ mới")
        print("3. Cập nhật thông tin cầu thủ")
        print("4. Xóa cầu thủ")
        print("5. Tìm kiếm cầu thủ")
        print("6. Thoát")
        print("=====================================")
        choice = input("Nhập lựa chọn của bạn: ").strip()
        
        match choice:
            case "1":
                manager.show_all()
            case "2":
                manager.add_player()
            case "3":
                manager.update_player()
            case "4":
                manager.delete_player()
            case "5":
                manager.search_player()
            case "6":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý cầu thủ bóng đá!")
                break
            case _:
                print("Lựa chọn không hợp lệ! Vui lòng chọn từ 1 đến 6.")


if __name__ == "__main__":
    main()