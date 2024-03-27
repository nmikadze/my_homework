# მოიძიე ინტერნეტში, გაუშვი და დააკომენტარე ჩათის კოდი, რომელიც ფუნქციონირებს არა TCP_ის, არამედ UDP_ის გამოყენებით.

import socket
import threading

# ფუნქცია, რომელიც მიიღებს მესიჯებს UDP პროტოკოლით
def receive_messages(sock):
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"Received message from {addr}: {data.decode()}")

# ფუნქცია, რომელიც მესიჯების გაგზავნას აწერს UDP პროტოკოლით
def send_messages(sock):
    while True:
        message = input("Enter message to send: ")
        sock.sendto(message.encode(), (SERVER_IP, SERVER_PORT))

# სერვერის IP და პორტიმ
SERVER_IP = '127.0.0.1'
SERVER_PORT = 12345

# UDP სოკეტის შექმნა
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# სოკეტის სერვერის IP მისამართზე და პორტზე მიბმა
sock.bind((SERVER_IP, SERVER_PORT))

# მესიჯის გაგზავნის ფუნქციის გაშვება
receive_thread = threading.Thread(target=receive_messages, args=(sock,))
receive_thread.start()

# thread-ის მოსტარტვა მესიჯის გასაგზავნად
send_thread = threading.Thread(target=send_messages, args=(sock,))
send_thread.start()

# მოლოდინი სანამ დასრულდება  thread-ი
receive_thread.join()
send_thread.join()

# სოკეტის დახურვა
sock.close()