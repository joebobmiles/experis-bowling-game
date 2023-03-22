if exists("alleygator_startup_v2.png"):
    click(Pattern("1679506935107.png").similar(0.50))
    type("X")
    if exists("1679512902132.png"):
        print("success")
    else:
        print("failure")

else:
    print("no application to test!")