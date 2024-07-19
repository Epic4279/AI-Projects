from fastai.vision.all import *
import time
import cv2
from utils.grabscreen import grab_screen


def label_func(x): return x.parent.name



def run():
    path = Path(r"C:\Users\Patel\Downloads\Fall-Guys-AI Skeleton\data")
    fnames = get_image_files(path) # Your code here - use get_image_files
    print(f"Total Images:{len(fnames)}")

    for fname in fnames[:5]:  # Print the first 5 file names
        print(f"Sample file name: {fname}, label: {label_func(fname)}")
    # Use fast.ai library to fine-tune a pre-trained model. 
    # Hint: ImageDataLoaders and cnn_learner will be relevant here
    dls = ImageDataLoaders.from_path_func(path, fnames, label_func,bs=40, num_workers=0)
    learn = cnn_learner(dls, resnet18, metrics=error_rate)
    print("Loaded")
    learn.fine_tune(4, base_lr=1.0e-02)

    # Export model
    learn.export()



    start_time = time.time()
    image = grab_screen(region=(0, 0, 2560, 1440))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image = cv2.Canny(image, threshold1=200, threshold2=300)
    image = cv2.resize(image, (224, 224))
    test = learn.predict(image)
    print("--- %s seconds ---" % (time.time() - start_time))
    print(test)


if __name__ == '__main__':
    run()