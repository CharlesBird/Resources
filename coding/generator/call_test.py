import asyncio


def get_html(sleep_times, loop):
    print("sleep {} success".format(sleep_times))
    print("now time: {}".format(loop.time()))

def stoploop(loop):
    loop.stop()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    # loop.call_soon(get_html, 2)
    # loop.call_soon(get_html, 3)
    # loop.call_soon(get_html, 4)

    # loop.call_later(2, get_html, 2)
    # loop.call_later(3, get_html, 3)
    # loop.call_later(4, get_html, 4)
    # loop.call_soon(get_html, 5)
    now = loop.time()
    loop.call_at(now+2, get_html, 2, loop)
    loop.call_at(now+3, get_html, 3, loop)
    loop.call_at(now+4, get_html, 4, loop)

    # loop.call_soon(stoploop, loop)
    loop.run_forever()