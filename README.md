# pca-on-the-command-line
With this repository, you can visualize quickly any data in a csv format that you want. Here is specified how you can use it exactly.

## How to install it
First, open type cmd on windows

```bash
C:\>git clone https://github.com/alektebel/pca-on-the-command-line.git
```

And all the files will be downloaded in the directory you are currently (Ignore the images, you can delete them). You should have already installed some modules, so here is a command to install all them at once.
```bash
C:\>pip install numpy pandas matplotlib sklearn

```
If some error pops out, you should first try to upgrade pip:

```bash
C:\>python -m pip install --upgrade pip

```
## How to use pca.py
The program is designed to be runned from the terminal. The general structure is the following:
```bash
C:\>pca.py path/to/dataset.csv [(regression=r|classification=c)] [target variable]

```
arguments surrounded by [] are optional. [(regression=r|classification=c)] means that it can be a r or a c, and the program will now that it's a problem of regression or classification. Depending on the problem, the program will plot the data with different colors (in classification, one color for each class, and in regression, a tone between blue and red, where blue means big and red means small respect to the dataset). If there is no [r|c] argument, the program will just show in the screen the 2D and 3D representation of the data using the PCA algorithm, in blue color. If the target variable is not specified, the program will asume the target variable is the column of the end.
Here is one example with a Pokemon dataset:
```bash
C:\>pca.py ./datasets/pokemon.csv c Legendary

```
That outputs the following plots:
![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/pokemons.png)

We can see that the data is very well separated in the numerical attributes, even for small dimensions. The program also outputs the 2D version of PCA:

![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/pokemons2D.png)

Probably, the purple dots that are very next to the green dots (the legendary pokemon) are the pseudo legendary pokemon!
If we type this command on the command line:
```bash
C:\>pca.py ./datasets/housing.csv r median_house_value

```
The plots would be the following:

![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/housing3D.png)

![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/housing2D.png)

As we can see, we have really expensive and really cheap houses in our datasets, due to the fact that the majority of houses are blue or red.
Next, we can see another example, where this time is a problem of "regression" of the probability that a student is accepted.

![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/admission_chance3D.png)

![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/chance_of_admit2D.png)

We can see a clear transition to low-probability-of-admission students to high-probability-of-admission students, with a lot of students in between with average probabilities.

And, last but not least, the final example. It's about predicting the chance that a worker will change of job or not.

![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/aug3D.png)

![plot](https://github.com/alektebel/pca-on-the-command-line/blob/main/aug2D.png)
