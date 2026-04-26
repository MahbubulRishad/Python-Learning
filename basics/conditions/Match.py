
def http_status_code(code):
    match code:
        case 200:
            return "Success - Ok"

        case 400:
            return "Error - Bad Request"

        case 401:
            return "Error - Unauthorized"

        case 404:
            return "Error - Not Found"

        case 500:
            return "Error - Internal Server Error"

        case 504:
            return "Error - Gateway Timeout"

        case _:
            return "Unknown Error"


print(http_status_code(200))
print(http_status_code(400))
print(http_status_code(401))
print(http_status_code(404))
print(http_status_code(500))
print(http_status_code(504))
print(http_status_code(503))
print(http_status_code(502))
