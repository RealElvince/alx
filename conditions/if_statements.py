deforestation_rate = 0.25
if deforestation_rate > 0.20:
    print("Critical deforestation level reached!")


# Nested if statements

deforestation_rate = 0.18
protected_area = True

if deforestation_rate > 0.15:
    if protected_area:
        print("Urgent action needed in protected area due to high deforestation rate!")
