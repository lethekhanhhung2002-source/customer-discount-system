from discount import calculate_discount

# Hai test case cơ bản (không phát hiện được lỗi)
def test_vip_customer():
    assert calculate_discount(60000000) == 0.1

def test_normal_customer():
    assert calculate_discount(30000000) == 0

# Các Test Case kiểm thử nghiệp vụ để phát hiện lỗi
def test_tc01():
    # TC01: Tổng trước 60M, hiện tại 2M -> Vẫn >= 50M -> Giảm 10% (0.1)
    assert calculate_discount(60000000, 2000000) == 0.1

def test_tc02():
    # TC02: Tổng trước 30M, hiện tại 2M -> Tổng 32M < 50M -> Không giảm (0)
    assert calculate_discount(30000000, 2000000) == 0

def test_tc03():
    # TC03: Tổng trước 49M, hiện tại 2M -> Tổng 51M >= 50M -> Phải giảm 10% (0.1)
    # Test case này sẽ FAIL vì code đang bị bug (không cộng thêm 2M)
    assert calculate_discount(49000000, 2000000) == 0.1
