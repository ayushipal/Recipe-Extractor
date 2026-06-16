def success(data=None, message="success"):
    return {
        "success": True,
        "message": message,
        "data": data
    }


def error(message="error", details=None):
    return {
        "success": False,
        "message": message,
        "error": details
    }