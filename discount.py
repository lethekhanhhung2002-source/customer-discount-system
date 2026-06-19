def calculate_discount(previous_total, current_order=0):
    # Đã sửa lỗi: Cộng dồn cả đơn hàng hiện tại
    if (previous_total + current_order) >= 50000000:
        return 0.1
    return 0.0
