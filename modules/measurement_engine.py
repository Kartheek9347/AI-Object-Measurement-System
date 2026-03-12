import cv2

# pixel to cm scale (demo scale)
PIXEL_TO_CM = 0.1


def estimate_size(image_path, detections):

    image = cv2.imread(image_path)

    measurements = []

    for obj in detections:

        x1, y1, x2, y2 = obj["bbox"]

        width_pixels = x2 - x1
        height_pixels = y2 - y1

        width_cm = width_pixels * PIXEL_TO_CM
        height_cm = height_pixels * PIXEL_TO_CM

        label = f"{obj['class']} W:{width_cm:.1f}cm H:{height_cm:.1f}cm"

        cv2.rectangle(image, (x1, y1), (x2, y2), (0,255,0), 2)

        cv2.putText(
            image,
            label,
            (x1, y1 - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )

        measurements.append(label)

    return image, measurements