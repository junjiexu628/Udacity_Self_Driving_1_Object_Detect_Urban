# Udacity_Self_Driving_1_Object_Detect_Urban
the project work for the object detection in urban environment
## Submission Template

### Project overview
This section should contain a brief description of the project and what we are trying to achieve. Why is object detection such an important component of self driving car systems?

---From Waymo dataset, make the EDA on the dataset,and then split the dataset to train and evulation. Based on the Tensorflow frame and Tensorflow detection API, create the training config file, and make the train on the train/eval dataset. Throught the initial train result, use the data augmentation options to modify the pipeline config file to retrain the model.Finally using the trained model to see the detection performance on the test dataset.

---We need to understand the overall the process of deep learning on self-driving and how to tune the training model, how to find the need documents, how to make own train on the future. 

---The object detection is the foundation for the avoidness with crash, lane keep,lane change,emergence stop and planning route.

### Set up
This section should contain a brief description of the steps to follow to run the code for this repository.

---Work on the workspace. So the set-up follows the readme procedure.

### Dataset
#### Dataset analysis
This section should contain a quantitative and qualitative description of the dataset. It should include images, charts and other visualizations.

---From EDA, the image data distributes in the different environments, downtown and suburb. more objects on some images and less object on some images. The light is also different, some are on the day, some are on the night. The weather is aslo different, some are on the sunny day, some are on the rainny and foggy day.
#### Cross validation
This section should detail the cross validation strategy and justify your approach.

---Use the random function, smaple 90% tfrecord of total into the train set, 10% in the eval set. I look up the libaray of sklearn.model_selection train_test_split. It is also a good option for this. But I don't use this libaray. Just use the random and shutil.

### Training
#### Reference experiment
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

---First run: using the default 'pipeline_new.config"

---First result: The tensorboard shows that the training loss curves oscicalates heavily and evaluation curves shows a dot. The evaluation curve shows strange. The total loss on train dataset is 9.0 and is 9.77 on the eval dataset.Learing_rate at the beginning 0.014 increase to 0.04 then decrease near to zero.From the loss curve we can see the at the beginning the loss increase, then the loss starts gradually to go down. It think the the learning rate is the part of the reason of this change trend. I think the cosine decay learning rate may be not suitable for this case. The learning rate should be change from the big to small, using step wise or exponential in the course.Why the overall loss is so high? I think image data are from all different weather and different light conditions. So the batch size is too small.Probably the first iteration uses the good light images, but the second iteration uses the dark images.And the loss curve shows be going down trend during 2500 steps. So increase the step number is another approach to make the loss down.

---Next action: add the 'data augmentation option'. The jupyter recommends the random_rgb_to_gray option. So add this script in the 'pipeline_new.config'. Raname the file to 'pipeline_new0.config'.Make the new folder 'experiment0' in the experiment folder. Put the pipeline_new0.config file in to this new folder. Run second.


#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.

---Second run(in experiment0 folder): using the'pipeline_new0.config" with data augmentation of random rgb-to-gray

---Second result: The terminal shows at the beginning the loss goes to the sky, achieving the 410000. And the next 100step, the loss is also around so so big value.So the loss discoverges. The jupyter recommend the data augmentation doesn't work. It is surprised me. I think that increasing the batch size to have a try based on the first run analysis.So kill this run. Delete all results.
---Next action: increase the batch size from 2 to 3. 

---Third run(in experiment0 folder): modify the'pipeline_new0.config" with batch size 3 

---Third result: The tensorboard shows that the training loss curves also oscicalates heavily, but the amplitude decrease a lot. The total loss on train dataset from first run result 9.0 is down to 2.3. The total loss on the evaluation data from the first run 9.77 is down to 2.97. Good optimization. But not enough. The goal is between 0 to 1.
---Next action: Increase the step is sure to make the loss down. So this isn't our purpose to try on the sure thing. I will try the exponential learing rate. initial_learning_rate =0.014,decay_steps =2500, decay_factor=0.95.

---Fourth run(in experiment1 folder): modify the'pipeline_new0.config" with exponential decay learning rate renamed 'pipeline_new1.config'

---Fourth result: The total loss on train dataset is 3.89,compared with the last 2.3. The total loss on the evaluation dataset is 4.4, not better than the last 2.97.It doesn't optimize.The trend of going down is too slow in comparison of the cosine decay.
---Next action: The exponential decay learning rate performs unsatisfied. It doesn't become better than the cosine decay learning rate. So try the Adam optimizer based on the cosine decay.

---Fifth run(in experiment2 folder): modify the'pipeline_new0.config" with Adam optimizer renamed 'pipeline_new2.config'

---Fifth result:  The total loss on train dataset is 8.6 at 2000step, no disk space,then terminated. It is not good,compared with the momentum optimizer. no space to run the eval.
---Conclusion: cosine decay learning rate, momentum optimizer, data augmentation of rgb_gray and batch size 3 are best combination in these runs.


---Further action:
try more data augmentation options
increase batch size to 4
tune learning rate parameter
run more steps to 5k or 10k

---Final run(in experiment3 folder): based on 'pipeline_new0.config' with data augmention option brightness, and batch size 4, slightly tune the learning rate base to 0.02.

---Final result: The total loss on train dataset is 0.8 and 1.0 on the evaluation dataset. This is the best result till now.The recall and precision on the meduium/large area achieve around 0.5. This is the best I can do.The detection animation shows all the vehicles what I can see by eyes are detected.


---My thoughts:
I splilted 80/20 for the train and eval. It performs better than the 90/10 split. Initial pipeline config the loss achieve 3.7. When batch size adds to 4, the loss converges near 1. Detection animation on the test perform not good, but it detects close vehicles beside the lane.More near vehicles cannot be detected. From EDA, the image distributes boardly, dark,light, rain....more image on day, less on night. So I split 90/10 for more data on training dataset in case of dark image cannot be trained.So 90/10 is hard to train good loss. This is my inference on the data split aspect.



