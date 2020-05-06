# Taneira-Titan-Recommendation
A Custom Convolutional Neural Network Architecture based Recommendation System for [Taneira](https://www.taneira.com), [Titan](https://www.titancompany.in).

*This solution was one among 35 selected projects out of 250 projects showcased during the company's "Technology Day".*

## Disclaimer
The dataset (images of sarees, SKU details, and attributes file) are proprietary data of Titan Company Limited, and therefore have been ommited from this project repository.

## Objective
- To design a deep learning model to recognise patterns in [sarees](https://en.wikipedia.org/wiki/Sari#cite_note-2).
- By recognising patterns in sarees the model should be able to deliver similar sarees from database, which can be used in various use cases.

## Approach
- We would require the model to predict each characteristic feature/attributes (eg: zari, pallu, colour etc) individually and use the results collectively.

## Attributes
- A saree has multiple attributes, Origin, Weft, Warp, Colour, Loom, Zari, Pallu amongst others.

## Assumptions
- This POC we will look into two attributes that have been implemented- Zari (Present or Not) and Pallu (Contrast or Running).
- The user is allowed to enter the colour of the saree they desire.

## Results

<p align="center">
  <img src=Results/stats.png />
</p>

#### Zari Prediction
<p align="center">
  <img src=Results/result_zari.png />
</p>

One can see here in 6th prediction above, where the database entry was made wrong, although the prediction was accurate.

#### Pallu Prediction
<p align="center">
  <img src=Results/result_pallu.png />
</p>

#### Taneira Product used for finding similar products.
<p align="center">
  <img src=Results/taneira_rec.png />
</p>

#### Non-Taneira Product used for finding similar products.
##### 01
<p align="center">
  <img src=Results/non_taneira_rec_1.png />
</p>

##### 02
<p align="center">
  <img src=Results/non_taneira_rec_2.png />
</p>

