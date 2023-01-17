import cv2


def MarkerID(image, markerID, top_left, match):
    if match:
        cv2.putText(image, str(markerID), (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 255, 0), 2)
    else:
        cv2.putText(image, str(markerID), (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                        (0, 0, 255), 2)


def ImageText(image, w):
    cv2.putText(image, str(w), (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)