def err400(msg):
    return {
            'status': 'Error',
            'msg': msg
        }, 400