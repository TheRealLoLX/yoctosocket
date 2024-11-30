import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
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
    
    

    base_options = python.BaseOptions(model_asset_path='D:\Coding\pores\gesture_recognizer.task')
    options = vision.GestureRecognizerOptions(base_options=base_options)
    recognizer = vision.GestureRecognizer.create_from_options(options)
    
    cap = cv2.VideoCapture(0)

    try:
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture frame.")
                break
            mp_frame = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
            recognition_result = recognizer.recognize(mp_frame)
            gesture = None

            if recognition_result.gestures:
                top_gesture = recognition_result.gestures[0][0]
                gesture = {
                    "category": top_gesture.category_name,
                    "score": top_gesture.score
                }

            _, buffer = cv2.imencode('.jpg', frame)
            image_base64 = base64.b64encode(buffer).decode('utf-8')
            data = {"image": image_base64, "gesture": gesture}
            json_data = json.dumps(data)
            serialized_data = pickle.dumps(json_data)
            data_size = len(serialized_data)
            conn.sendall(pickle.dumps(data_size))
            conn.sendall(serialized_data)
            time.sleep(60/1000)
      
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cap.release()
        conn.close()
        server_socket.close()
        start_server()


if __name__ == "__main__":
    start_server()