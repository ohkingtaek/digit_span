import torch


def card_detect(img):
    model = torch.hub.load('./lib/yolov5', 'custom', path='./assets/best.pt', source='local')
    results = model(img)
    results.save('card.png')
    return results.pandas().xyxy[0]


if __name__ == "__main__":
    card_detect('../../assets/img/img1.jpg')