if exists("alleygator_startup_v2.png"):
    click("1679506935107.png")
    type("/")
    if exists(Pattern("1679512770333.png").similar(0.80)):
        print("success")
    else:
        print("failure")

else:
    print("no application to test!")