### 														Text Suggestion System



###### Descriptions

It's a Text Suggestion System using **Naive Bayes**. 

###### Note 

To evaluate my system, I used **python-language-tool** to check whether the system predict correctly or not.

###### Instruction

1. open  ```TextSuggestionSystem.ipynb``` in notebook (google colab, jupyter notebook) 

###### Limitations

Text Suggestion System highly depends on order of words in sentetences. For example "USA is the strongest country"  this makes sense, but "country the is USA strongest" doesn't make sense. As Naive Bayes ignores order of features, so this is a huge drawback.

###### Overcoming Some Limitations

Though Naive bayes ignores order of features, but this implemention overcomes some of it. Here I am ignoring order of features, but preserving order between features and target word. 

###### Main Idea

![](https://i.ibb.co/4WDBnBM/p1.jpg)

![](https://i.ibb.co/tJhBJbX/p2.jpg)

![](https://i.ibb.co/GvdRPZz/p3.jpg)

