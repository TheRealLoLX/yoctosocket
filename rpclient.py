import socket
import pickle
import cv2
import base64
import numpy as np
import json
import time

ASCII_CHARS = " .:-=+*%@#"

def image_to_ascii(image, width=80):
    """Átkonvertál egy képet ASCII művészetté."""
    # Az eredeti kép átméretezése a kívánt szélességre, megőrizve az arányokat
    height, orig_width = image.shape[:2]
    aspect_ratio = orig_width / height
    new_height = int(width / aspect_ratio / 2)  # A terminál karaktermagassága miatt osztunk 2-vel
    resized_image = cv2.resize(image, (width, new_height))
    
    # Grayscale-re konvertálás
    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
    
    # Átkonvertálás ASCII karakterekké
    ascii_art = ""
    for row in grayscale_image:
        for pixel in row:
            ascii_art += ASCII_CHARS[pixel * len(ASCII_CHARS) // 256]
        ascii_art += "\n"
    return ascii_art

def start_client(host='192.168.1.129', port=65432, buffer_size=1024):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    ack_size = {"size": "ACK SIZE", "timestamp": time.time()}
    ack_data = {"message": "ACK DATA", "timestamp": time.time()}
    
    coded_size = pickle.dumps(json.dumps(ack_size))
    coded_data = pickle.dumps(json.dumps(ack_data))

    wrong_size = {"size": "WRONG SIZE", "timestamp": time.time()}
    wrong_data = {"message": "WRONG DATA", "timestamp": time.time()}
    
    coded_size_wrong = pickle.dumps(json.dumps(wrong_size))
    coded_data_wrong = pickle.dumps(json.dumps(wrong_data))

    try:
        while True:
            size_data = json.loads(pickle.loads(client_socket.recv(buffer_size)))
            if not size_data:
                client_socket.sendall(coded_size_wrong)
            else:
                client_socket.sendall(coded_size)
            received_data = b""
            try:
                while len(received_data) < size_data["size"]:
                    packet = client_socket.recv(buffer_size)
                    if not packet:
                        client_socket.sendall(coded_data_wrong)
                    received_data += packet
                deserialized_data = pickle.loads(received_data)
                client_socket.sendall(coded_data)
                deserialized_data = json.loads(deserialized_data)
                image_data = base64.b64decode(deserialized_data["image"])
                image_array = np.frombuffer(image_data, dtype=np.uint8)
                image = cv2.imdecode(image_array, cv2.IMREAD_COLOR) 
                ascii_frame = image_to_ascii(image, width=80)
        
                # ASCII megjelenítése a terminálban
                print("\033c", end="")  # Tisztítja a terminált
                print(ascii_frame)
                print("\n")
                print(deserialized_data["gesture"])
                
            except Exception as e:
                print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

if __name__ == "__main__":
    start_client()



    
