def calculate_discount(previous_total, current_order=0):
    """
    Tính phần trăm giảm giá cho khách hàng thân thiết.
    """
    if previous_total >= 50000000:
        return 0.1
    return 0.0
