import socket
import pickle
import cv2
import base64
import numpy as np
import json
import time

def start_client(host='127.0.0.1', port=65432, buffer_size=1024):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    try:
        while True:
            size_data = client_socket.recv(buffer_size)
            if not size_data:
                break
            data_size = pickle.loads(size_data)
            received_data = b''
            try:
                while len(received_data) < data_size:
                    packet = client_socket.recv(buffer_size)
                    if not packet:
                        break
                    received_data += packet
                deserialized_data = pickle.loads(received_data)
                deserialized_data = json.loads(deserialized_data)
                image_data = base64.b64decode(deserialized_data["image"])
                image_array = np.frombuffer(image_data, dtype=np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR) 
                if image is not None:
                    flipped_image = cv2.flip(image, 1)
                    cv2.imshow("image_name", flipped_image)
                    
                    print(deserialized_data["gesture"])
                    cv2.waitKey(1)
            except Exception as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()



    