import os
from data.base_dataset import BaseDataset, get_transform
from data.image_folder import make_dataset
from PIL import Image
import random
from os import listdir
from os.path import join

def is_image_file(fileanme):
    return any(fileanme.endswith(extension) for extension in [".png", ".jpg", ".jpeg"])

class PixDataset(BaseDataset):
    
    def __init__(self, opt):
        BaseDataset.__init__(self, opt)
        self.dir_A = os.path.join(opt.dataroot, opt.phase + 'A')
        self.dir_B = os.path.join(opt.dataroot, opt.phase + 'B')
        '''
        self.A_paths = make_dataset(self.dir_A, opt.max_dataset_size)
        self.B_paths = make_dataset(self.dir_B, opt.max_dataset_size)
        '''
        self.image_filenames= [x for x in listdir(self.dir_A) if is_image_file(x)]
        
        assert(self.opt.load_size >= self.opt.crop_size)   # crop_size should be smaller than the size of loaded image
        self.input_nc = self.opt.output_nc if self.opt.direction == 'BtoA' else self.opt.input_nc
        self.output_nc = self.opt.input_nc if self.opt.direction == 'BtoA' else self.opt.output_nc
        
    def __getitem__(self, index):
        
        A_img = Image.open(join(self.dir_A, self.image_filenames[index])).convert('RGB')
        B_img = Image.open(join(self.dir_B, self.image_filenames[index])).convert('RGB')
        
        transform_A = get_transform(self.opt, grayscale=(self.input_nc == 1))
        transform_B = get_transform(self.opt, grayscale=(self.output_nc == 1))
        A = transform_A(A_img)
        B = transform_B(B_img)

        return {'A': A, 'B': B, 'A_paths': self.image_filenames[index], 'B_paths': self.image_filenames[index]}
        
    def __len__(self):
        """Return the total number of images in the dataset."""
        return len(self.image_filenames)    
    