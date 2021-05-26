# Democritus</h1>
 
 
 Democritus is remembered for his formulation of an atomic theory, and this stunning quote: “Nothing exists except atoms and space, everything else is opinion.”
 This means that we can never be sure of what we are thinking. Truth is at the level of atoms. Since there is nothing else but atoms and void and their interactions. What we think is 
 a result of these interactions and we only get this result. What we imagine, all of this depends on the interaction of atoms which we cannot get to since they remain in the depths. 
 Democritus therefore was sceptical of our ability to know anything with certainty. Neural networks can help us to understand these interactions and make predictions about future atomic interactions on a higher level. 
 With our imperfect understanding of atomic interactions we can on a higher level use predictive process monitoring to understand and predict probabilistic human process interactions.
 
 
 All experiments in the paper can be reproduced using the files in the App directory in the project.

## Project Structure
- [App](https://github.com/NilsBerni/edbn/tree/master/Anomalies): Contains all wrappers used to run the application.
- [Utils](https://github.com/NilsBerni/edbn/tree/master/Utils): Some extra implementations regarding datastructures, preprocessing and data generation
- [Data](https://github.com/NilsBerni/edbn/tree/master/Data): Data used for the experiments 
- [RelatedMethods](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods): Implementations of the other methods used to run the comparison experiments with
    - [Bohmer](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Bohmer): Contains our own implementation of the Likelihood Graphs introduced by Bohmer et al in [3]
    - [Camargo](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Camargo): Contains the slightly adapted implementation used in [4]
    - [DiMauro](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/DiMauro): Implementation used in [5]
    - [Lin](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Lin): Our implementation of the method described in [6]
    - [Nolle](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Nolle): Contains the original implementations used by Nolle et al in [2]
    - [Tax](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Tax): Adapted implementation used in [7]
    - [Pasquadibisceglie](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Pasquadibisceglie): Adapted implementation used in [8]
    - [Taymouri](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Taymouri): Adapted implementation used in [9]
    - [Premiere](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/Premiere): Adapted implementation used in [10]
    - [Pauwels](https://github.com/NilsBerni/edbn/tree/master/RelatedMethods/eDBN): Contains implementation used in [1]

## References
1. Pauwels, Stephen, and Toon Calders. "Incremental Predictive Process Monitoring: The Next Activity Case" Accepted for BPM 2021.
2. [Böhmer, Kristof, and Stefanie Rinderle-Ma. "Multi-perspective anomaly detection in business process execution events." OTM Confederated International Conferences" On the Move to Meaningful Internet Systems". Springer, Cham, 2016.](https://eprints.cs.univie.ac.at/4785/1/cr.pdf)
3. [Nolle, Timo, et al. "BINet: Multi-perspective Business Process Anomaly Classification." arXiv preprint arXiv:1902.03155 (2019).](https://arxiv.org/pdf/1902.03155.pdf)
4. Camargo, M., Dumas, M., Gonz ́alez-Rojas, O.: Learning accurate lstm models ofbusiness processes. In: International Conference on Business Process Management.pp. 286–302. Springer (2019)
5. Di  Mauro,  N.,  Appice,  A.,  Basile,  T.M.:  Activity  prediction  of  business  processinstances  with  inception  cnn  models.  In:  International  Conference  of  the  ItalianAssociation for Artificial Intelligence. pp. 348–361. Springer (2019)
6.  Lin, L., Wen, L., Wang, J.: Mm-pred: a deep predictive model for multi-attributeevent  sequence.  In:  Proceedings  of  the  2019  SIAM  International  Conference  onData Mining. pp. 118–126. SIAM (2019)
7.  Tax, N., Verenich, I., La Rosa, M., Dumas, M.: Predictive business process mon-itoring with lstm neural networks. In: International Conference on Advanced In-formation Systems Engineering. pp. 477–492. Springer (2017)
8. Pasquadibisceglie, V., Appice, A., Castellano, G., & Malerba, D. (2019, June). Using convolutional neural networks for predictive process analytics. In 2019 International Conference on Process Mining (ICPM) (pp. 129-136). IEEE.
9. Taymouri, F., La Rosa, M., Erfani, S., Bozorgi, Z. D., & Verenich, I. (2020). Predictive Business Process Monitoring via Generative Adversarial Nets: The Case of Next Event Prediction. arXiv preprint arXiv:2003.11268.
10. Pasquadibisceglie V., Appice A., Castellano G., Malerba D. (2020) Predictive Process Mining Meets Computer Vision. In: Fahland D., Ghidini C., Becker J., Dumas M. (eds) Business Process Management Forum. BPM 2020. Lecture Notes in Business Information Processing, vol 392. Springer, Cham.
