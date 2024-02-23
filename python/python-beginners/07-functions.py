# def generate_report(main_tank, external_tank, hydrogen_tank):
#     output = f"""Fuel Report:
#     Main Tank: {main_tank}
#     External Tank: {external_tank}
#     Hydrogen Tank: {hydrogen_tank}
#     """
#     print(output)

# generate_report(80, 70, 75)

def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f"{name}: {value}")

fuel_report(main= 50, external = 100, emercengy = 60)