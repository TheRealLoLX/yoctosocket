import socket
import pickle
import json
import time
import cv2
import base64

def start_server(host='127.0.0.1', port=65432):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")
    
    image1 = cv2.imread("D:\\Coding\\pores\\18.jpg")
    image2 = cv2.imread("D:\\Coding\\pores\\28.jpg")
    
    try:
        flag = True
        while True:
            _, buffer = cv2.imencode('.jpg', image1 if flag == True else image2)
            image_base64 = base64.b64encode(buffer).decode('utf-8')
            data = {"message": image_base64, "name": '18' if flag == True else '28'}
            json_data = json.dumps(data)
            serialized_data = pickle.dumps(json_data)
            data_size = len(serialized_data)
            conn.sendall(pickle.dumps(data_size))
            conn.sendall(serialized_data)
            print(f"Sent: {data}")
            time.sleep(60/1000)
            flag = not flag
      
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
        server_socket.close()
        start_server()


if __name__ == "__main__":
    start_server()