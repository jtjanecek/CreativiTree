---
layout: default
title: Status
---

Progress Report
===============
Video Here:
[![video](/treeImage.png)](https://www.youtube.com/watch?v=OwxblhmB4qs&feature=youtu.be)


[Source]: <> (http://sameersingh.org/courses/aiproj/sp17/writeups/status.pdf)

# Project Summary
[comment]: <> (Since things may have changed since proposal \(even if they haven’t\), write a short paragraph summarizing the goals of the project \(updated/improved version from the proposal\))
CreativiTree is a deep learning tool that "hallucinates" new images of Trees and generates them for the player in-game.
CreativiTree is fed thousands of images of trees using generative adversarial networks in order to "hallucinate" new images of trees and then turning them into minecraft objects using malmo. 

# Approach
[comment]: <> (Give a detailed description of your approach, in a few paragraphs. You should summarize the main algorithm you are using, such as by writing out the update equation \(even if it is off-the-shelf\). You should also give details about the approach as it applies to your scenario. For example, if you are using reinforcement learning for a given scenario, describe the MDP in detail, i.e. how many states/actions you have, what does the reward function look like. A good guideline is to incorporate sufficient details so that most of your approach is reproducible by a reader. I encourage you to use figures, as appropriate, for this, as I provided in the writeup for the first assignment \(available here: http://sameersingh.org/courses/aiproj/sp17/assignments.html#assignment1\). I recommend at least 2-3 paragraphs.)

Following the orginal work of Ian Goodfellow on ["Generative Adverserial Networks"](https://arxiv.org/pdf/1406.2661.pdf), and consequently the work of several researchers from the University of Michigan on ["Generative Adversarial Text to Image Synthesis"](https://arxiv.org/pdf/1605.05396.pdf), this project focuses mainly on Image Systhesis \(Hallucinating Images\) and further explore its applications.

**The Learning**  
In order for CreativiTree to "learn" about trees, we used a TensorFlow implementation of Deep Convolutional Generative Adverserial Network (DCGAN) that we found on [github](https://github.com/carpedm20/DCGAN-tensorflow). This, along with thousands of 32x32 color tree images from the [CIFAR-100 dataset](https://www.cs.toronto.edu/~kriz/cifar.html). 

We trained the DCGAN and found the higher number of epochs the better in general. The generated trees started looking better and better, but towards the end, the trees started looking strange. We think this is because the DCGAN is learning the background of the images, instead of the tree itself. 

![epoch_2](/epoch_2.png)
![epoch_10](/epoch_10.png)
![epoch_75](/epoch_75.png)

In the future, we would remove the background before training the GAN, instead of removing the background when we process the image in Malmo. 



**Malmo**
We used the Python Imaging Library to convert each image to RGB representations in Python. We then used the webcolors API, to convert each pixel to a color that can be rendered in Minecraft. At first, we needed to tweak the colors so that it would accurately convert to the correct colors, and the resulting (unscaled) images are as follows:


Next, we scaled the representations into 10x10 models, which looked kind of strange, but they were player size. Something we could improve on is scaling the images to look more like the unscaled versions.

The results of our prototype:

**Unscaled 32x32 tree images converted into Minecraft:**

![t1](/t1_unscaled_full.png)
![t5](/t5_unscaled_full.png)
![t3](/t3_unscaled_full.png)

**Scaled 10x10 trees in Minecraft (player size):**

![t1](/t1_scaled_full.png)
![t5](/t5_scaled_full.png)
![t3](/t3_scaled_full.png)

**Final product**

![trees](/treeImage.png)

![alt text](https://github.com/adam-p/markdown-here/raw/master/src/common/images/icon48.png "Logo Title Text 1")

# Evaluation
[comment]: <> (An important aspect of your project, as we mentioned in the beginning, is evaluating your project. Be clear and precise about describing the evaluation setup, for both quantitative and qualitative results. Present the results to convince the reader that you have a working implementation. Use plots, charts, tables, screenshots, figures, etc. as needed. I expect you will need at least a few paragraphs to describe each type of evaluation that you perform.)
A large part of our evaluation is qualitative and we broke it down into two parts:

1.  Did our project generate tree images that actually look like trees? 

2.  Do the Minecraft representations of the trees look like trees, and are they similar to the original images? 

For the first evaluation, we analyzed the results of generator given different epochs.  At first we trained the DCGAN using 35 epochs, which gave us somewhat-realistic looking images.  After that we trained it using 45 epochs, which yielded even better results.  From then on we trained an additional 65 epochs, which started to develop detailed and even more realistic-looking results.  However, as the epochs approached 100, the GAN started learning the backgrounds of the trees, and generating strange looking trees, like they were on fire or pure blue sky. Images that came out of this 110-epoch neural net were hit-and-miss in the sense that some images looked good but others looked clearly strange, but as a whole we got enough samples for images that were suitable to use in Minecraft. 

For the second evaluation, we converted the images into unscaled and scaled versions of the images in Minecraft. The unscaled images were much more realistic, and as seen above, they are quite good representations of the images! However, once we scaled the images down to 10x10 player size, the minecraft representation was not as similar to the original image, we think this is because of data loss in compressing the images, which dilutes the color in the image.

# Remaining Goals and Challenges
[comment]: <> (In a few paragraphs, describe your goals for the  next 2-3 weeks, when the final report is due. At the very least, describe how you consider your prototype to be limited, and what you want to add to make it a complete contribution. Note that if you think your algorithm is quite good, but have not performed sufficient evaluation, doing them can also be a reasonable goal. Similarly, you may propose some baselines \(such as a hand-coded policy\) that you did not get a chance to implement, but want to compare against for the final submission. Finally, given your experience so far, describe some of the challenges you anticipate facing by the time your final report is due, how crippling you think it might be, and what you might do to solve them.)

Our prototype currently uses an off the shelf DCGAN in order to perform image synthesis. Our main objective over the next 2-3 weeks is to code our own Generative Adversarial Neural Network and have more flexibility when it comes to improving its individual parts in order to hallucinate more realistic looking trees.

We would like to remove the backgrounds from the dataset before training, as some of our epochs showed that the GAN was actually learning from the background instead of the tree image and shape itself (sometimes it was pure blue as in the sky).

In scaling the images, we would like to make the scaled versions of the images more realistic, and more representative of the unscaled images in Minecraft.

In addition, we would like to expand our DCGAN to generate images of objects other than trees. 

