# 500G文件，一行


def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos + len(newline):]
        chunk = f.read(4096*10)
        if not chunk:
            yield buf
            break
        buf += chunk


with open('large.txt') as f:
    for line in myreadlines(f, '.'):
        print(line)