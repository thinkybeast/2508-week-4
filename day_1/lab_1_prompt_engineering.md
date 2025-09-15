# Lab 1: Prompt Engineering

**Individual Exercise: 30 minutes**

## Part 1: Getting Familiar with OpenAI Playground

### 1. Read through [this article](https://www.promptingguide.ai/techniques/fewshot) that explains few-shot prompting.

### 2. Visit the [OpenAI Playground](https://platform.openai.com/playground/prompts) and try your hand at zero-shot vs few-shot prompting.

Try out the examples from the article or come up with your own. See if you can find a prompt that performs poorly with zero-shot, but can be improved with few-shot. Here's another example you can try:

**Prompt:** Create a sentence that incorrectly combines two similar metaphors.

**Example 1:** "We'll burn that bridge when we come to it" combines "We'll cross that bridge when we come to it" and "burning bridges"

**Example 2:** "Don't beat a gift horse" combines "Don't look a gift horse in the mouth" and "Don't beat a dead horse."

With zero-shot prompting, the response usually includes two metaphors, but they are not related.

### 3. Experiment with changing the 'temperature' of your response. 
If you don't know what 'temperature' is in this context, look it up. Do the same with 'Top P'.

---

## Part 2: Programming Exercise Generator

In this part, we'll practice the different prompt engineering techniques with a larger task, generating programming exercises for students.

We'll progress through three main techniques:

1. **Zero-shot prompting**
2. **Few-shot prompting**
3. **Self-consistency prompting**

### Zero-Shot Prompting

Zero-shot prompting is the simplest form of prompting, where we give the model a direct instruction without any examples. Let's start with a basic programming exercise prompt.

#### Exercise 1.1
Create a simple prompt asking for a programming exercise. Try something like:

```
Generate a basic programming exercise in Python.
```

#### Exercise 1.2
Now let's make our zero-shot prompt more specific by adding some constraints and requirements:

```
Generate a Python programming exercise for a beginner student learning loops. Include a problem description and expected output.
```

### Few-Shot Prompting

Few-shot prompting improves results by providing examples of the desired output format. We'll create prompts with examples to get more detailed and structured responses.

#### Exercise 2.1
Create a prompt with one example of a detailed programming exercise. Use this template:

```
Here's how to format a detailed programming exercise:

Language: Python
Topic: Variables and Data Types
Problem: Create a program that calculates the area of a rectangle
Requirements:
- Ask user for length and width
- Calculate area (length * width)
- Display result with proper formatting
Expected Output: "The area of the rectangle is: 24 square units"

Now generate a similar exercise:
Language: Python
Topic: Loops
```

#### Exercise 2.2
Enhance your few-shot prompt by adding more examples and specific details:

```
Here are examples of detailed programming exercises:

Language: Python
Topic: Variables and Data Types
Problem: Create a program that calculates the area of a rectangle
Requirements:
- Ask user for length and width (use float input)
- Calculate area (length * width)
- Display result with proper formatting
- Include input validation
Difficulty: Beginner
Estimated Time: 15 minutes
Expected Output: "The area of the rectangle is: 24.0 square units"

Language: JavaScript
Topic: Arrays
Problem: Create a function that finds the maximum number in an array
Requirements:
- Accept an array as parameter
- Return the maximum value
- Handle empty arrays
- Use a loop (not Math.max())
Difficulty: Intermediate
Estimated Time: 20 minutes
Expected Output: "The maximum number is: 42"

Now generate a similar detailed exercise:
Language: Python
Topic: Functions
```

### Self-Consistency Prompting

Self-consistency prompting involves generating multiple responses and finding consistent elements among them. We'll use this technique to create comprehensive and reliable programming exercises.

#### Exercise 3.1
Generate multiple exercises and compare them:

```
Generate 3 different programming exercises for learning Python functions. For each exercise include:
- Problem description
- Requirements and constraints
- Difficulty level
- Estimated completion time
- Sample input/output
- Learning objectives

After generating the exercises, identify the common elements and most effective teaching patterns across all three versions.
```

#### Exercise 3.2
Create a final prompt that combines all techniques:

```
Please generate 3 detailed programming exercises for learning Python functions. Follow this specific format:

Example Exercise Format:
Title: [Clear, descriptive title]
Language: [Programming language]
Topic: [Specific concept being taught]
Difficulty: [Beginner/Intermediate/Advanced]
Estimated Time: [Time in minutes]

Problem Description:
[Clear, engaging problem statement]

Requirements:
- [Specific requirement 1]
- [Specific requirement 2]
- [Specific requirement 3]

Learning Objectives:
- [What the student should learn]
- [Key concepts to understand]

Sample Input/Output:
Input: [Example input]
Output: [Expected output]

Hints:
- [Optional hint 1]
- [Optional hint 2]

After generating the three versions:
1. Highlight the most consistent teaching patterns
2. Explain why these exercises are effective
3. Provide a final optimized exercise combining the best elements

Please ensure all exercises include:
- Clear problem statements
- Appropriate difficulty levels
- Real-world relevance
- Progressive complexity
- Multiple solution approaches
```

---

## Lab Challenges

### Customization Challenge
Modify your prompts to account for different:
- **Programming languages** (Python, JavaScript, Java, etc.)
- **Student skill levels** (beginner, intermediate, advanced)
- **Learning styles** (visual, hands-on, theoretical, practical)
- **Topics** (algorithms, data structures, web development, etc.)

### Error Analysis
- Compare outputs from different prompting techniques
- Identify which method produces the most reliable and educational exercises
- Document cases where the model might generate incorrect code examples or solutions

### Prompt Optimization
- Experiment with different exercise formats
- Try varying levels of detail in your examples
- Test different ways of specifying learning objectives and constraints

---

## Best Practices

### Be Specific
Always include clear requirements for:
- **Programming language and version**
- **Student skill level and prerequisites**
- **Learning objectives and outcomes**
- **Expected completion time**

### Verify Information
Remember that LLMs can generate plausible-sounding but incorrect information. Always:
- Test generated code examples for syntax errors
- Verify that solutions are actually correct
- Check that difficulty levels are appropriate
- Ensure exercises follow best practices for the language

### Iterate and Refine
- Start with simple prompts
- Gradually add complexity
- Test different variations
- Document what works best for different student types
