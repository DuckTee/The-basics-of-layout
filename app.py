import http.server
import socketserver
import os

PORT = 5000


class CustomHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Устанавливаем тип контента
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Читаем содержимое HTML-файла
        try:
            with open('templates/contacts.html', 'rb') as file:
                content = file.read()
                self.wfile.write(content)
        except FileNotFoundError:
            self.send_error(404, "File not found")


# Запуск сервера
with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print("Сервер остановлен")
