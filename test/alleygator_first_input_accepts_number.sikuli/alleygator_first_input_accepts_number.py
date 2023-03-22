if exists("alleygator_startup_v2.png"):
    click(Pattern("1679506935107.png").similar(0.50))
    type("1")
    if exists("1679505206614.png"):
        print("success")
    else:
        print("failure")

else:
    print("no application to test!")