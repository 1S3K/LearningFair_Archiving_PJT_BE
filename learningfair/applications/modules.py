statusCode = {
    'OK': 200,
    'CREATED': 201,
    'NO_CONTENT': 204,
    'BAD_REQUEST': 400,
    'UNAUTHORIZED': 401,
    'FORBIDDEN': 403,
    'NOT_FOUND': 404,
    'INTERNAL_SERVER_ERROR': 500,
    'SERVICE_UNAVAILABLE': 503,
    'DB_ERROR': 600,
}

resMessage = {
    'SUCCESS': "Request 성공",
    'NULL_VALUE': "필요한 값이 없습니다.",
    'OUT_OF_VALUE': "파라미터 값이 잘못되었습니다.",
    'WRONG_INDEX': "잘못된 인덱스 접근입니다.",
    'ONLY_ADMIN_PERMISSION': "접근하실 수 없습니다.",
    'UNSUPPORTED_TYPE': "지원하지 않는 파일 형식입니다.",
    'DB_ERROR': "DB 오류",
    'BAD_REQUEST': "잘못된 접근 방식입니다."
}

def success(status, message, data):
    return {
        'status' : status,
        'success' : True,
        'message' : message,
        'data' : data
    }

def fail(status, message):
    return {
        'status' : status,
        'success' : False,
        'message' : message
    }