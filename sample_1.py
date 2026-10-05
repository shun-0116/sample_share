#!python3
import cv2

def test_1():
  cap = cv2.VideoCapture(0)
  
  ret, frame = cap.read()
  
  return frame

if __name__ == "__main__":
  print("Test")
  test_1()
