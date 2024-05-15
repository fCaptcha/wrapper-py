from fcaptcha import FCaptcha

solver = FCaptcha("key here!")
try:
    print(f"Balance: {solver.get_balance()}")
except Exception as e:
    print(f"Could not get balance: {e}")

try:
    print(f"HCAP Key: {solver.solve_hcaptcha(
        "227fe119-8d9e-490c-a0f0-5d9f8a41174d",
        "https://guns.lol",
        "proxy here"
    )}")
except Exception as e:
    print(f"Could not get solve: {e}")

    