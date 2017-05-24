---
layout: default
title:  Home
---

Welcome to CreativiTree!

We are using a Generative Adversarial Network to build novel images of Trees, and then building them in Minecraft! We are constructing forests of player-size trees that are computer-generated.

![A randomly generated forest!](/treeImage.png)

We built our own dataset using the CIFAR-100 dataset of 32x32 images. This dataset has 2500 images, and we are planning to add more using web scrapers the Python Imaging Library. 

We trained the GAN with the data and our own custom settings to give the best results.

Furthermore, we build our own image-to-malmo python scripts which remove the background, and convert pixels to colors. 

This technique could be applied to things other than Trees, but for now we want to focus on trees, and that is why we are CreativiTree!

Our github: http://github.com/jtjanecek/CreativiTree
GAN library: http://github.com/carpedm20/DCGAN-tensorflow

