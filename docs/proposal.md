---
layout: default
title: proposal
---

Project Proposal
================

Summary of project
------------------

Our project allows the user to take a photo of a real-world object using their Android phone and, through a server, direct a Minecraft bot to recreate that same object using the tools/resources available inside the Minecraft world. Our application will make use of the following tools/techniques:

**1. Android application:** This application will allow the user to take a photo of an object and send it to Google Cloud Vision API for analysis.  
**2. Google Cloud Vision API:** This API will analyse the photo sent by the user via the smartphone application and label it.  
**3. Malmo (ML and DL techniques):** Using Malmo along with different Machine and Deep Learning techniques, we will take the information provided by the Google Cloud Vision API and recreate the label of the object inside the minecraft world.

AI/ML Algorithms
----------------
Hallucinating Minecraft objects with Deep Learning (Concept); this is actually three AI algorithms, collaborating adversarially: an AI that maps 2D images to text, a generative AI, which is the AI learning to recreate 3D objects from 2D images, and a discriminative AI, learning to judge the 3D image and correctly classify it to its corresponding 2D image.

Evaluation Plan
---------------
The success of our project will be evaluated based on how well the minecraft player is able to recreate the label of the object that appears in the photograph taken by the user. This means that the focus will not be on creating a minecraft object that looks identical to the object in the photograph, but rather one that shares similar features.

**1. Quantitative Analysis:** We will have quantitative analysis for each of the three AIs: We will measure the success rate of being able to convert the image to a label, being able to generate a 2D representation of the object, and being able to build the object. We will gather this data by building a variety of objects, running multiple times.  
**2. Qualitative Analysis:** Some sanity cases are: if we take a picture of a rock on our phone, does it actually build a rock?  Rocks are fairly simple objects, so if our AI can’t build a rock, it probably can’t build something as complex as a tree.  
Since our AI is really a couple of AI’s working together, we have to make sure all the components of the AI work right. Here are the components and the necessary tests to see if they work right:
The Android phone app: does it really take the photo and sends it to our AI server?
Does the AI server really receive the photo from the app?  Does the server send requests to the Minecraft server?  Does the AI server send the photo to Google Cloud Vision server and get the right answer?
Does the first AI program classify text.  
**3. Moonshot case:** Be able to hallucinate a minecraft object(s) based on descriptive labels (i.e. blue house in a field).
