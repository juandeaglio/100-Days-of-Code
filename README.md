# A name generator for a band that's personalized to you.

This is a simple project which can be summed up as string concatenation, but I decided to implement some modularity into it with design patterns. I'm going to extend the project to make use of some GPT API to help generate alternative names using the questions & answers provided.

Generates bands based on a list of questions.
Allows the user to answer via stdin or also use a list of strings to input multiple answers in one function call.

Going to implement integration with ChatGPT 3.5 APIs to generate names based on the question + answer pair.


# View the tests for an understanding of the implementation.
There are three (optionally a fourth test case with manual stdin input) that test and describe the functionality of the simple band name generator class.
