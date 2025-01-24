import cv2
import requests
from PIL import Image
import io


# asasa
def display_image(image_path):
    img = cv2.imread(image_path)
    cv2.imshow("Local Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def image_to_bytes(image_path):
    with open(image_path, "rb") as image_file:
        return image_file.read()


def upload_to_imgbb(api_key, image_data):
    url = "https://api.imgbb.com/1/upload"
    payload = {"key": api_key, "image": image_data, "name": "IMG1"}

    response = requests.post(url, data=payload)
    return response.json()


def main():
    # Replace these with your actual values
    api_key = "6d62b087d54d436cbe021c5046380794"
    image_path = "./sample.png"  # Update this path

    # Display the image
    print("Displaying the image...")
    # display_image(image_path)

    # Convert image to bytes
    image_data = image_to_bytes(image_path)

    # # Upload the image
    # print("\nUploading the image to ImgBB...")
    result = upload_to_imgbb(api_key, image_data)

    print(result)


if __name__ == "__main__":
    main()
