# Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - unripe, Yellow - Ripe, Brown - Overripe)

fruit = "Banana"
color = "Green"

if fruit == "Banana":
    if color == "Green":
        print("unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("Overripe")
else:
    print(f"We don't have enough information regarding {fruit}")
