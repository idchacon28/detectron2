# Running R3D  :diamonds: 🕸️ :diamonds:
<p align="center">
 <img src="https://github.com/idchacon28/detectron2/blob/main/projects/DensePose/gifcicla.gif" alt="animated" />
</p>
                                                                                                    
## Detectron2
<img src=".github/Detectron2-Logo-Horz.svg" width="300" > 

Detectron2 is FAIR's next-generation platform for object detection, segmentation and other visual recognition tasks. 

### Environment Installation
It is essential that you have a detectron2 environment:

See [installation instructions](https://detectron2.readthedocs.io/tutorials/install.html).

## Replicating Robust 3D Human Dense Pose Estimation Results
Please run the following command to have a softlink to the best model weights, where your directory is the folder in which you cloned the repository:

```
 ln -s /media/user_home1/idchacon/detectron2/projects/DensePose/exp4_best_model your_directory/detectron2/projects/DensePose
```

You will also need a softlink to the dataset:

```
ln -s /media/user_home1/idchacon/detectron2/datasets your_directory/detectron2/projects/DensePose
```

You will find the *main.py* by running the following command:

```
cd projects/Densepose
```
## Running main.py
To replicate the results of the best model described in the paper you can run the following command:
```
python main.py --mode test
```
To visualize the performance of the model over an image you can run the following command:
```
python main.py --mode demo --img image_0.png
```
where *image_0.png* is the image that will be tested. By default, you will encounter the image *cicla.jpg*. 

After this process, you will obtain a series of images according to the U_coordinates, V_coordinates, Segmentation and Contour_plots. 


