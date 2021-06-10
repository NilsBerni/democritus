# Democritus</h1>
 
We remember Democritus for his formulation of an atomic theory and this stunning quote: “Nothing exists except atoms and space, everything else is opinion.”
This means that we can never be sure of what we are thinking. Truth is at the level of atoms since there is nothing else but void, atoms and their interactions. What we believe is a result of these interactions, and we only get this result. We imagine that all of this depends on the interaction of atoms that we cannot get to since they remain in the depths. 
Democritus, therefore, was skeptical of our ability to know anything with certainty. Neural networks can help us to understand these interactions and make predictions about future atomic interactions on a higher level. 
With our imperfect understanding of atomic interactions, we can use predictive process monitoring to understand and predict probabilistic human process interactions on a higher level. This tool makes it easy to leverage the training and application of different state-of-the-art approaches.


## Functionalities

This framework can:
 - Analyze event logs and display their characteristics
 - Suggest a specific implementation for PPM using NN
 - Train neural network models with event logs

This framework is currently able to predict:
 - Next activity
 - Suffix


![Advisor](https://media.giphy.com/media/icSL0aOv32yCh5p88D/giphy.gif)
![Predict](https://media.giphy.com/media/jjFV7da0gMkqaDPoMF/giphy.gif)


 
## User Manual

### Downloads for Testing and Performing Experiments
- [Raw Datasets](https://github.com/NilsBerni/RealLifeEventLogs): Contains all raw data we used and tested.

### Applying the User Interface
The user interface is more of a concept than that. We can already use it productively in its current state. However, the user interface is not a mockup; if enough tested on different devices, we can use it to use productivity software. The interface is currently using models and training results in the cache to demonstrate its functionality. 

### Applying the Framework


### !!!WARNING!!!
We cannot guarantee a stable execution over the user interface. 
Due to its long execution times, testing all event logs, implementations and parameters would take multiple person-months.
To produce results for multiple implementations and event logs, please run [Experiments](https://github.com/NilsBerni/democritus/blob/master/Predictions/Execution/Experiment.py).
Another advantage of using this file is that it will automatically start the next prediction/training as soon as one is completed.
However, from experience, the script will run at least one week on a personal computer to produce results for all the methods.

## Project Structure
- [App](https://github.com/NilsBerni/democritus/tree/master/app): Contains all wrappers used to run the application.
- [Utils](https://github.com/NilsBerni/democritus/tree/master/Utils): Some extra implementations regarding datastructures, preprocessing and data generation
- [Data](https://github.com/NilsBerni/democritus/tree/master/Data): Data used for the experiments 
- [Predictions](https://github.com/NilsBerni/democritus/tree/master/Predictions): Prediction files
    - [Output](https://github.com/NilsBerni/democritus/tree/master/Predictions/Execution/Output): Models and training/prediction logs
    - [Experiments](https://github.com/NilsBerni/democritus/blob/master/Predictions/Execution/Experiment.py): Script to perform all experiments
- [Methods](https://github.com/NilsBerni/democritus/tree/master/Methods): Implementations of the other methods used to run the comparison experiments with
    - [Camargo](https://github.com/NilsBerni/democritus/tree/master/Methods/Camargo): Contains the slightly adapted implementation used in [1]
    - [DiMauro](https://github.com/NilsBerni/democritus/tree/master/Methods/DiMauro): Implementation used in [2]
    - [Lin](https://github.com/NilsBerni/democritus/tree/master/Methods/Lin): Our implementation of the method described in [3]
    - [Tax](https://github.com/NilsBerni/democritus/tree/master/Methods/Tax): Adapted implementation used in [4]
    - [Pauwels](https://github.com/NilsBerni/democritus/tree/master/Methods/EDBN): Contains implementation used in [5]

## References
1. Camargo, Manuel \& Dumas, Marlon \& González-Rojas, Oscar. (2019). Learning Accurate LSTM Models of Business Processes. 10.1007/978-3-030-26619-6\_19.
2. Di Mauro, Nicola \& Appice, Annalisa \& Basile, Teresa. (2019). Activity Prediction of Business Process Instances with Inception CNN Models. 10.1007/978-3-030-35166-3\_25.
3. Lin, Li \& Wen, Lijie \& Wang, Jianmin. (2019). MM-Pred: A Deep Predictive Model for Multi-attribute Event Sequence. 10.1137/1.9781611975673.14. 
4. Tax, Niek \& Verenich, Ilya \& La Rosa, Marcello \& Dumas, Marlon. (2017). Predictive Business Process Monitoring with LSTM Neural Networks. 477-492. 10.1007/978-3-319-59536-8\_30.
5. Pauwels, Stephen \& Calders, Toon. (2020). Bayesian Network Based Predictions of Business Processes. 10.1007/978-3-030-58638-6\_10. 
