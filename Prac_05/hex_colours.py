colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
           "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378"}
colourname=input("Name of colour: ")
while colourname !="":
    if colourname in colours:
        print("colour code for {} is {}".format(colourname,colours[colourname]))
    else:
        print("invalid colour name")
