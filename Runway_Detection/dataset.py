from corebreakout.datasets import PolygonDataset
from corebreakout import defaults

#data_dir = defaults.DEFAULT_DATA_DIR    # parent of any separate annotation data directories
subset = 'train'                        # which subdirectory to read from

dataset = PolygonDataset(classes=defaults.DEFAULT_CLASSES)

# Collect all of the requied ID + path information
dataset.collect_annotated_images('annoted/masks', subset)

# Set all of the attrs required for use
dataset.prepare()

print(dataset)