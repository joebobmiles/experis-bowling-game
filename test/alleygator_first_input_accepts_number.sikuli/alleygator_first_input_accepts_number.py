if exists("alleygator_startup_v2.png"):

    fields = findAll(Pattern("1679514459077.png").similar(0.86))

    if fields:
        sorted_fields = sorted(fields, key=lambda m : m.x)
        
        for field in sorted_fields:
            click(field)
            type("1")
    
            if field.has("1679515145015.png"):
                print("success")
            else:
                print("failure")
    else:
        print("could not locate inputs!")

else:
    print("no application to test!")