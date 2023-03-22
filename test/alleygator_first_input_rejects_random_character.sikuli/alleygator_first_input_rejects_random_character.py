if exists("alleygator_startup_v2.png"):
    click(Pattern("1679506935107.png").similar(0.50))
    type("a")
    if exists(Pattern("1679506935107-1.png").similar(0.80)):
        print("success")
    else:
        print("failure")

else:
    print("no application to test!")