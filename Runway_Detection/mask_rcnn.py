
# import pixellib
from pixellib.instance import custom_segmentation

def segment(path):
    segment_image = custom_segmentation()
    segment_image.inferConfig(num_classes= 1, class_names= ["BG","runway"])
    segment_image.load_model("models/best2.h5")
    segment_image.segmentImage(path, show_bboxes=False, output_image_name="sample_out.jpg")

if __name__=='__main__':
    segment('NWPU-RESISC45/runway/runway_671.jpg')
