---
layout: default
title: Final Report
---

Final Report
===============
## Video
<!---
[![video](/treeImage.png)](https://www.youtube.com/watch?v=OwxblhmB4qs&feature=youtu.be)
-->

## Project Summary
[comment]: <> (Since things may have changed since proposal \(even if they haven’t\), write a short paragraph summarizing the goals of the project \(updated/improved version from the proposal\))
CreativiTree is a deep learning tool that "hallucinates" new images of Trees and generates them for the player in-game.
CreativiTree is fed thousands of images of trees using generative adversarial networks in order to "hallucinate" new images of trees and then turning them into minecraft objects using malmo.

## Approaches
[comment]: <> (Give a detailed description of your approach, in a few paragraphs. You should summarize the main algorithm you are using, such as by writing out the update equation \(even if it is off-the-shelf\). You should also give details about the approach as it applies to your scenario. For example, if you are using reinforcement learning for a given scenario, describe the MDP in detail, i.e. how many states/actions you have, what does the reward function look like. A good guideline is to incorporate sufficient details so that most of your approach is reproducible by a reader. I encourage you to use figures, as appropriate, for this, as I provided in the writeup for the first assignment \(available here: http://sameersingh.org/courses/aiproj/sp17/assignments.html#assignment1\). I recommend at least 2-3 paragraphs.)

Following the orginal work of Ian Goodfellow on ["Generative Adverserial Networks"](https://arxiv.org/pdf/1406.2661.pdf), and consequently the work of several researchers from the University of Michigan on ["Generative Adversarial Text to Image Synthesis"](https://arxiv.org/pdf/1605.05396.pdf), this project focuses mainly on Image Systhesis \(Hallucinating Images\) and further explore its applications.

**What is a GAN, DCGAN, and "hallucinating" images?**

Our project involves "hallucinating" images--what do we mean by this?  Well, if we were to analogize this to human hallucination, we would say that "hallucinating" is seeing something that isn't there.  There may be the real, physical object that may influence or inspire the inspiration, but the hallucination itself does not represent reality.  

So, when we say that CreativiTree "hallucinates" trees, we are saying that it generates images of trees that it _thinks_ actually exists, but does not actually exist.  It does not just remember or learn what trees look like from images of trees, which is a technique that's closer to variational autoencoders (VAE).  Our AI instead thinks of random noise at first, and is taught to think of trees until it does a good job of thinking of trees--or "hallucinating" them.  The results are quite interesting, as it ends up hallucinating trees that can often look quite different than realistic trees.

In order for CreativiTree to "learn" about trees, we used a TensorFlow implementation of DCGAN that we found on [github](https://github.com/carpedm20/DCGAN-tensorflow). This, along with thousands of 32x32 color tree images from the [CIFAR-100 dataset](https://www.cs.toronto.edu/~kriz/cifar.html).

A quick overview of **neural networks**:
  * A neural network is a web of "neurons" that are interconnected with each other, structured in a way that may include multiple layers of these neurons.
  * These neurons are functions that take in a matrix of numbers, computes the matrix through some sort of activation function, and then outputs a matrix of changes that are to be applied elementwise for the next neuron in their activation function.

  A **GAN** is a generative adversarial neural network.  In our case, the "generative" aspect is generating images that resemble real photographs of trees.  The "adversarial" aspect is due to how the GAN is structured.
  * A GAN has two neural networks competing against each other in a zero-sum game.
  * One of the neural networks is called a _generator_.  Its job is to generate images as close to the "real" images as possible.
  * One of the neural networks is called a _discriminator_.  Its job is mainly to tell the generated images from the real images.  Its output is whether the image is real or generated ("fake"), and the generator adjusts its learning according to the discriminator's output.

  A **DCGAN** is a GAN that uses deep convolutional layers as part of its architecture.  You can think of it as a convolutional neural network (CNN) and a GAN combined.
  (https://cdn-images-1.medium.com/max/1000/1*39Nnni_nhPDaLu9AnTLoWw.png)
  * The discriminator is a convolutional neural net, with four convolutional layers.  
  * The generator is a deconvolutional neural net, with four deconvolutional layers.  You may notice that the generator is essentially the discriminator, but flipped.

  (http://www.timzhangyuxuan.com/static/images/project_DCGAN/structure.png)
  The way a DCGAN works is that we first set up the discriminator and the generator up, randomizing the weights and biases of the neurons with a Gaussian distribution.  Then, we have something for the generator to "generate" on: a _z_ vector of random numbers drawn from, again, a Gaussian distribution.  This _z_ vector can be thought of as a "seed" matrix.

  We then train the discriminator first:
  ```
    _, summary_str = self.sess.run([d_optim, self.d_sum],
      feed_dict={ self.inputs: batch_images, self.z: batch_z })
    self.writer.add_summary(summary_str, counter)
  ```


  Here, you can see that we feed the discriminator _both_ the real images ("batch_images") and the generated images ("batch_z").

  We then train the generator based on the feedback ("batch_labels") given by the discriminator:

  ```
      _, summary_str = self.sess.run([g_optim, self.g_sum],
        feed_dict={
          self.z: batch_z,
          self.y:batch_labels,
        })
      self.writer.add_summary(summary_str, counter)
  ```

**The Learning**  


We trained the DCGAN and found the higher number of epochs the better in general. The generated trees started looking better and better, but towards the end, the trees started looking strange. We think this is because the DCGAN is learning the background of the images, instead of the tree itself.

![epoch_2](/epoch_2.png)
![epoch_10](/epoch_10.png)
![epoch_75](/epoch_75.png)


Since the status update, we wanted to make some changes to make the tree generation better.

**Data Distortion**
We added extra data by distorted our original dataset slightly. We were able to go from 2500 datapoints to _____ datapoints.
Here are some of the new images generated:

tree1   tree2   tree3




**Learning rate**
In addition to the new dataset, we also changed the learning rate to see if that affected the tre generation.


epoch_original  epoch_learning_rate





Overall, the best epochs looked like this:
Default Settings                                  with Distorted Data                               Learning rate .0001





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

## Evaluation
[comment]: <> (An important aspect of your project, as we mentioned in the beginning, is evaluating your project. Be clear and precise about describing the evaluation setup, for both quantitative and qualitative results. Present the results to convince the reader that you have a working implementation. Use plots, charts, tables, screenshots, figures, etc. as needed. I expect you will need at least a few paragraphs to describe each type of evaluation that you perform.)
A large part of our evaluation is qualitative and we broke it down into two parts:

1.  Did our project generate tree images that actually look like trees?

2.  Do the Minecraft representations of the trees look like trees, and are they similar to the original images?

For the first evaluation, we analyzed the results of generator given different epochs.  At first we trained the DCGAN using 35 epochs, which gave us somewhat-realistic looking images.  After that we trained it using 45 epochs, which yielded even better results.  From then on we trained an additional 65 epochs, which started to develop detailed and even more realistic-looking results.  However, as the epochs approached 100, the GAN started learning the backgrounds of the trees, and generating strange looking trees, like they were on fire or pure blue sky. Images that came out of this 110-epoch neural net were hit-and-miss in the sense that some images looked good but others looked clearly strange, but as a whole we got enough samples for images that were suitable to use in Minecraft.

For the second evaluation, we converted the images into unscaled and scaled versions of the images in Minecraft. The unscaled images were much more realistic, and as seen above, they are quite good representations of the images! However, once we scaled the images down to 10x10 player size, the minecraft representation was not as similar to the original image, we think this is because of data loss in compressing the images, which dilutes the color in the image.

## References

We used the DCGAN github repository for our neural network, which can be found here:  https://github.com/carpedm20/DCGAN-tensorflow
