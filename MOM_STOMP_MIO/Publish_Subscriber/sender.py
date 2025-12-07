import sys,stomp

if __name__ == '__main__':
    try:
        MSG = sys.argv[1]
    except IndexError:
        print('Please insert correct MSG')
        sys.exit(-1)

    conn = stomp.Connection([('127.0.0.1',61613)],auto_content_length=False)
    
    conn.connect(wait=True)

    conn.send('/topic/mytesttopic',MSG)

    print('MESSAGE: -',MSG,'-sent')

    conn.disconnect()
    

