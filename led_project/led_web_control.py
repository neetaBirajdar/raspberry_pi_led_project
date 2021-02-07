from http.server import BaseHTTPRequestHandler, HTTPServer
from gpiozero import LED
import codecs
import os

hostname = "192.168.178.46"
port = 8080

leds = {'R': LED(27),'G' : LED(17), 'Y':LED(18) }

class MyServer(BaseHTTPRequestHandler):

    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type","text/html")
        self.end_headers()

    def do_GET(self):
        with open('led_web_controller.txt','r') as rf:
            html = rf.read()
        temp = os.popen("/opt/vc/bin/vcgencmd measure_temp").read()
        self.do_HEAD()
        self.wfile.write(html.format(temp[5:]).encode("utf-8"))

    def _redirect(self,path):
        self.send_response(303)
        self.send_header('Content-type','text/html')
        self.send_header('Location',path)
        self.end_headers()

    def do_POST(self):
        content_len = int(self.headers['Content-Length']) #size of data
        post_data = self.rfile.read(content_len).decode('utf-8') #get the data
        print(post_data)
        request_data = post_data.split('=')[1]
        operation,req_color = request_data.split('-')
        for color,led in leds.items():
            if color == req_color and operation == 'On':
                led.on()
            elif color == req_color and operation == 'Off':
                led.off()
        print(f'LED is of color:{req_color} and operation:{operation}')
        self._redirect('/')




if __name__ == '__main__':
    http_server = HTTPServer((hostname,port),MyServer)
    print(f"Server starts - {hostname},{port}")

    try:
        http_server.serve_forever()
    except Exception as e:
        http_server.server_close()
        print(f"Invalid input.Error:{e}")
