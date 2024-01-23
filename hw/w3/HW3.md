
# Task 1:
___
#### 1. dibetes.csv
| Class Name | Count |  Percentage of Total   |
|------------|-------|------------------------|
| Positive   |   268 | 268/786 * 100 = 34.09% |
| Negative   |   500 | 500/768 * 100 = 65.10% |

#### 2. soybean.csv

|         Class Name          | Count | Percentage of Total |
|-----------------------------|-------|---------------------|
| 2-4-d-injury                |    16 | 2.34%               |
| alternarialeaf-spot         |    91 | 13.32%              |
| anthracnose                 |    44 | 6.44%               |
| bacterial-blight            |    20 | 2.93%               |
| bacterial-pustule           |    20 | 2.93%               |
| brown-spot                  |    92 | 13.47%              |
| brown-stem-rot              |    44 | 6.44%               |
| charcoal-rot                |    20 | 2.93%               |
| cyst-nematode               |    14 | 2.04%               |
| diaporthe-pod-&-stem-blight |    15 | 2.19%               |
| diaporthe-stem-canker       |    20 | 2.93%               |
| downy-mildew                |    20 | 2.93%               |
| frog-eye-leaf-spot          |    91 | 13.32%              |
| herbicide-injury            |     8 | 1.17%               |
| pyllosticta-leaf-spot       |    20 | 2.93%               |
| phytophthora-rot            |    88 | 12.88%              |
| powdery-mildew              |    20 | 2.93%               |
| purple-seed-stain           |    20 | 2.93%               |
| rhizoctonia-root-rot        |    20 | 2.93%               |  
  

# Task 3
___
##### **Accuracy:**  0.9947229551451188 -> 99% (for k=1 and m=2)  
  


# Task 4
___
##### K and M setting recommendations:
##### - For Diabetes.csv: We took k=1 and m=2. Since, there are no low frequency classes in this data, k and m can also be zero.  

##### - For Soyabean.csv: k=2 and m=0 (0.001) gives the highest accuracy of 89.45%