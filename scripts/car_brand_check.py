'''pattern grouping with
match case structure'''

def is_car_brand_german(brand):
    match brand:
        case "Opel" | "VW" | "Mercedes" | "BMW":
            return True
        case _:
            return False