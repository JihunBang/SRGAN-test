from mode import *
import argparse


parser = argparse.ArgumentParser()

def str2bool(v):
    return v.lower() in ('true')

#parser.add_argument("--LR_path", type = str, default = 'C:/Users/jihun/SRGAN-PyTorch/dataset/DIV2K/DIV2K_train_LR_bicubic/X4')
parser.add_argument("--LR_path", type = str, default = 'C:/Users/USER/Bicubic/set01_V001_lwir')
#parser.add_argument("--LR_path", type = str, default = 'C:/Users/jihun/SRGAN-PyTorch/dataset/DIV2K/DIV2K_train_LR_bicubic/x2')
#parser.add_argument("--LR_path", type = str, default = 'C:/Users/jihun/SRGAN-PyTorch/dataset/DIV2K/DIV2K_train_LR_x8')
#parser.add_argument("--GT_path", type = str, default = 'C:/Users/jihun/SRGAN-PyTorch/dataSet/DIV2K/DIV2K_train_HR/')
parser.add_argument("--GT_path", type = str, default = 'C:/Users/USER/dataset/set01/V001/visible')
parser.add_argument("--res_num", type = int, default = 16)
parser.add_argument("--num_workers", type = int, default = 0)
parser.add_argument("--batch_size", type = int, default = 19)
parser.add_argument("--L2_coeff", type = float, default = 1.0)
parser.add_argument("--adv_coeff", type = float, default = 1e-3)
parser.add_argument("--tv_loss_coeff", type = float, default = 0.0)
parser.add_argument("--pre_train_epoch", type = int, default = 100)
#parser.add_argument("--pre_train_epoch", type = int, default = 8000)
parser.add_argument("--fine_train_epoch", type = int, default = 200000)
#parser.add_argument("--fine_train_epoch", type = int, default = 4000)
parser.add_argument("--scale", type = int, default = 2)
parser.add_argument("--patch_size", type = int, default = 24)
parser.add_argument("--feat_layer", type = str, default = 'relu5_4')
parser.add_argument("--vgg_rescale_coeff", type = float, default = 0.006)
parser.add_argument("--fine_tuning", type = str2bool, default = False)
parser.add_argument("--in_memory", type = str2bool, default = True)
parser.add_argument("--generator_path", type = str)
#parser.add_argument("--generator_path", type = str , default = r'C:\Users\USER\SRGAN\model\SRGAN_gene_050.pt')
#default = r'C:\Users\USER\SRGAN\model\try1\pre_trained_model_4000.pt'
#parser.add_argument("--generator_path", type = str, default = 'C:/Users/jihun/SRGAN-PyTorch/model/SRGAN.pt')
parser.add_argument("--mode", type = str, default = 'train')

args = parser.parse_args()

if args.mode == 'train':
    train(args)
    
elif args.mode == 'test':
    test(args)
    
elif args.mode == 'test_only':
    test_only(args)

