import cv2
import pytesseract
cam=cv2.VideoCapture("sample_video.mp4")
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
fps=cam.get(cv2.CAP_PROP_FPS)
print(fps)
n=0
i=0
second=1
with open("coordinate.txt", "w") as file:
    while True:
        ret,frame=cam.read()
        if n%(second*fps)==0:
            cropped_frame = frame[:50, -250:]
            cv2.imwrite("{}.jpg".format(i),frame)
            cv2.imwrite("cropped_{}.jpg".format(i), cropped_frame) #no need to save this image, just to show I have saved it
            text = pytesseract.image_to_string(cropped_frame)
            # Remove ":" at the start of the text
            # Remove ":" and all the text before it
            if ":" in text:
                text = text.split(":")[1].strip()
           
            # Replace double "--" with a single "-"
            text = text.replace("--", "-")
            text = text.strip()
            # Print the extracted text
            file.write(f"{text}\n")
            print(f"Text from image {i}: {text} ")
            i+=1
        n+=1
        if ret==False:
            break
cam.release()
cv2.destroyAllWindows()