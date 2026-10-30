def add(a, b):
    """回傳 a 與 b 的和。"""
    return a + b


def divide(a, b):
    """回傳 a 除以 b；b 為 0 時拋出 ValueError。"""
    if b == 0:
        raise ValueError("除數不可為 0")
    return a / b
