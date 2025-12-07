import sys,time,random,stomp

if __name__ == '__main__':
    try:
        MSG = sys.argv[1]
    except IndexError:
        print("eorrore nell inserimento del MSG")
        sys.exit(-1)

    conn = stomp.Connection([('127.0.0.1',61613)])
    conn.connect(wait = True)

    txid = conn.begin()

    try:
        for i in range(3):

            print(f'#{i}Message: -',MSG,'-sending...')

            value = random.randint(0,1)
            if value == 0:
                raise IOError('problem while sending value')

            conn.send('/topic/mytesttopic ',MSG + "-"+str(i),transaction=txid)
            print(f"Message #{i} send {MSG} -sent!!!")
    
    except IOError as e:
        print(e)
        print("Abort Exception")
        conn.abort(txid)
    else:
        conn.commit(txid)
        print('transaction committed')

    conn.disconnect()




