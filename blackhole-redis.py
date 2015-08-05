import redislite

server = redislite.Redis(serverconfig={'port': '6379'})

while True:
        server.blpop('logstash', 300)
