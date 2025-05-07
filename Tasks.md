# LLama Workshop Tasks

## Prompt Engineering - System Prompts

* **Task 1:** Create a prompt that asks the model to summarize a given text.
* **Task 2:** Design a prompt that instructs the model to generate a list of pros and cons for a given topic.
* **Task 3:** Write a prompt that asks the model to generate a creative story based on a given theme.

Example:

```python
messages = [{"role": "system", "content": "Please summarize the following text."}]
```

## Prompt Engineering - Providing Examples

* **Task 4:** Create a prompt that provides an example of a question and answer, and then asks the model to generate a similar question and answer.
* **Task 5:** Design a prompt that asks the model to respose in a specific format, such as JSON or XML.

Example:

```python
messages = [{"role": "system", "content": "Here is an example of a question and answer: Q: What is the capital of France? A: The capital of France is Paris. Now, please generate a similar question and answer for the country provided."}]
```

## Prompt Engineering - Restricting Output

* **Task 6:** Write a prompt that instructs the model to limit its response to a certain number of words or characters.
* **Task 7:** Create a prompt that asks the model to provide a response in a specific style or tone, such as formal or informal.
* **Task 8:** Design a prompt that asks the model to avoid certain topics or phrases in its response.

Example:

```python
messages = [{"role": "system", "content": "Please provide a response in a formal tone and limit your answer to 100 words."}]
```
