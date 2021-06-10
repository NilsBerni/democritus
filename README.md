# Democritus</h1>
 
We remember Democritus for his formulation of an atomic theory and this stunning quote: “Nothing exists except atoms and space, everything else is opinion.”
This means that we can never be sure of what we are thinking. Truth is at the level of atoms since there is nothing else but void, atoms and their interactions. What we believe is a result of these interactions, and we only get this result. We imagine that all of this depends on the interaction of atoms that we cannot get to since they remain in the depths. 
Democritus, therefore, was skeptical of our ability to know anything with certainty. Neural networks can help us to understand these interactions and make predictions about future atomic interactions on a higher level. 
With our imperfect understanding of atomic interactions, we can use predictive process monitoring to understand and predict probabilistic human process interactions on a higher level.

All experiments in the paper can be reproduced using the files in the App directory in the project.

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


 
## !!!WARNING!!!
We cannot guarantee a stable execution over the user interface. 
Due to its long execution times, testing all event logs, implementations and parameters would take multiple person-months.
To produce results for multiple implementations and event logs. Please run the Predictions/Execution/Experiments.py. 
Another advantage of using this file is that it will automatically start the next prediction/training as soon as one is completed.
However, from experience, the script will run at least one week on a personal computer to produce results for all the methods.

## Project Structure
- [App](https://github.com/NilsBerni/democritus/tree/master/app): Contains all wrappers used to run the application.
- [Utils](https://github.com/NilsBerni/democritus/tree/master/Utils): Some extra implementations regarding datastructures, preprocessing and data generation
- [Data](https://github.com/NilsBerni/democritus/tree/master/Data): Data used for the experiments 
- [Predictions](https://github.com/NilsBerni/democritus/tree/master/Predictions): Prediction files
    - [Output](https://github.com/NilsBerni/democritus/tree/master/Predictions/Execution/Output): Models and training/prediction logs
    - [Experiments](https://github.com/NilsBerni/democritus/tree/master/Predictions/Execution/Experiments.py): Script to perform all experiments
- [Methods](https://github.com/NilsBerni/democritus/tree/master/Methods): Implementations of the other methods used to run the comparison experiments with
    - [Camargo](https://github.com/NilsBerni/democritus/tree/master/Methods/Camargo): Contains the slightly adapted implementation used in [1]
    - [DiMauro](https://github.com/NilsBerni/democritus/tree/master/Methods/DiMauro): Implementation used in [2]
    - [Lin](https://github.com/NilsBerni/democritus/tree/master/Methods/Lin): Our implementation of the method described in [3]
    - [Tax](https://github.com/NilsBerni/democritus/tree/master/Methods/Tax): Adapted implementation used in [4]
    - [Pauwels](https://github.com/NilsBerni/democritus/tree/master/Methods/EDBN): Contains implementation used in [5]

## References
1. Pauwels, Stephen, and Toon Calders. "Incremental Predictive Process Monitoring: The Next Activity Case" Accepted for BPM 2021.
2. Camargo, M., Dumas, M., Gonz ́alez-Rojas, O.: Learning accurate lstm models ofbusiness processes. In: International Conference on Business Process Management.pp. 286–302. Springer (2019)
3. Di  Mauro,  N.,  Appice,  A.,  Basile,  T.M.:  Activity  prediction  of  business  processinstances  with  inception  cnn  models.  In:  International  Conference  of  the  ItalianAssociation for Artificial Intelligence. pp. 348–361. Springer (2019)
4. Lin, L., Wen, L., Wang, J.: Mm-pred: a deep predictive model for multi-attributeevent  sequence.  In:  Proceedings  of  the  2019  SIAM  International  Conference  onData Mining. pp. 118–126. SIAM (2019)
5. Tax, N., Verenich, I., La Rosa, M., Dumas, M.: Predictive business process mon-itoring with lstm neural networks. In: International Conference on Advanced In-formation Systems Engineering. pp. 477–492. Springer (2017)
