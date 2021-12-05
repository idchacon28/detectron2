import subprocess
import argparse
import os

parser=argparse.ArgumentParser()
parser.add_argument('--mode', help='mode in which the program is going to be runned (test or demo)', type=str, default="demo")
parser.add_argument('--img', help='Image name for demo', type=str, default="cicla.jpg")
args = parser.parse_args()
print(args)

if args.mode == "test":
	os.system("python train_net.py --config-file configs/densepose_rcnn_R_50_FPN_s1x.yaml --eval-only MODEL.WEIGHTS exp4_best_model/model_0129999.pth")
elif args.mode == "demo":
	os.system("python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml exp4_best_model/model_0129999.pth " +args.img+ " bbox,dp_u -v --output u_coordinates.png")
	os.system("python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml exp4_best_model/model_0129999.pth " +args.img+ " bbox,dp_v -v --output v_coordinates.png")
	os.system("python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml exp4_best_model/model_0129999.pth " +args.img+ " bbox,dp_segm -v --output segmentation.png")
	os.system("python apply_net.py show configs/densepose_rcnn_R_50_FPN_s1x.yaml exp4_best_model/model_0129999.pth " +args.img+ " bbox,dp_contour -v --output contour.png")