# 什么是 Keep Alive？Keep Alive Timeout 是干嘛的？
1. Keep-Alive 是一个在 HTTP 1.1 里介绍的 HTTP 功能。当发送一个 HTTP 请求时，这个客户端 (通常是一个网络浏览器) 可以设置一个 Keep-Alive 头来指示 http 服务器 (Sanic) 不要在发送响应后关闭 TCP 连接。这允许客户端复用存在的 TCP 连接来发送随后的 HTTP 请求，确保为客户端和服务端提供更加高效的网络质量。

2. KEEP_ALIVE 配置变量默认被设置为 True。如果你的应用程序不需要这个功能，设置 False 使所有客户端连接在响应被发送后立即关闭，无论请求的 Keep-Alive 头如何。

3. 服务器保持打开 TCP 连接的时间量由服务器自己决定。在 Sanic，这个值通过 KEEP_ALIVE_TIMEOUT 值来配置。默认是 5 秒，与 Apache HTTP 服务器一样的配置，这在允许足够的时间为客户端发送一个新的请求和不用一次性保持太多连接之间提供了很好的平衡。不要超过 75 秒除非你知道你的客户端使用了支持 TCP 长连接。
