import codecs


def genSQL():
    fd = codecs.open('data.txt', "r", "utf-8")
    lines = fd.readlines()

    deviceNames = ''
    for line in lines:
        line = line.replace('\n', '')
        txt = line.split(",", 1)

        sql = "update test set status=%s where id='%s';" % (txt[1], txt[0])
        print(sql)


genSQL()
