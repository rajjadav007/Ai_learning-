def http_status(status):
    match status:
        case 200:
            print ("ok")
        case 404:
            print ("page not found")
        case 500:
            print ("internal server error ")
        case _:
            print ("unknown error")

print ((http_status(200)))
