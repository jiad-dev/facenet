import torch
import torch.nn.functional as F
from models import FaceNetModel
from torchvision import transforms

from .boot import app


class ModelLoaded:
    model = None
    acc = 0

    @staticmethod
    def get_model():
        if not ModelLoaded.model:
            model = FaceNetModel()
            state = torch.load(app.config['USE_MODEL'], map_location='cpu')
            model.load_state_dict(state['state_dict'])
            ModelLoaded.acc = state['accuracy']
            ModelLoaded.model = torch.nn.DataParallel(model)
        return ModelLoaded.model


trfrm = transforms.Compose([
    lambda x: x.convert('RGB'),
    transforms.Resize(224),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])])
topil = transforms.ToPILImage()
totensor = transforms.Compose(trfrm.transforms[:-1])


def get_distance(img1, img2):
    model = ModelLoaded.get_model()
    with torch.no_grad():
        x1 = trfrm(img1).unsqueeze(0)
        x2 = trfrm(img2).unsqueeze(0)
        embed1 = model(x1)
        embed2 = model(x2)
        return F.pairwise_distance(embed1, embed2)


def is_same(img1, img2, threshold=0.5):
    distance = get_distance(img1, img2)
    return distance, distance <= threshold
