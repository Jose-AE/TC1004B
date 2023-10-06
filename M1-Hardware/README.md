# Module 1 - Hardware

## Table of contents:

- [Boolean Algebra and Logic Gates](#bool)
- [Combinatorial Logic](#logic)



<a id="bool"></a>

## Boolean Algebra and Logic Gates


Logic gates are fundamental building blocks of digital circuits. They perform basic logical functions on one or more binary inputs and produce a single binary output based on those inputs. These gates are the foundation of digital electronics and are used in various electronic devices and systems.

### Types of Logic Gates

There are several types of logic gates, each with its own unique behavior:

<blockquote>

# NOT Gate

<img src="https://cdn1.byjus.com/wp-content/uploads/2020/11/Basic-Logic-Gates-3.png" alt="drawing" width="300"/>


The NOT gate (also known as an inverter) has one input and one output. It simply inverts the input, meaning if the input is 0, the output is 1, and if the input is 1, the output is 0.

Truth Table:

| Input (A) | Output (Q) |
| --------- | ---------- |
| 0         | 1          |
| 1         | 0          |


</blockquote>


<blockquote>

# AND Gate

<img src="https://cdn1.byjus.com/wp-content/uploads/2020/11/Basic-Logic-Gates-2.png" alt="drawing" width="300"/>


The AND gate has two or more inputs and one output. It produces an output of 1 only when all of its inputs are 1; otherwise, the output is 0.

Truth Table for a 2-input AND gate:

| Input A | Input B | Output Q |
| ------- | ------- | -------- |
| 0       | 0       | 0        |
| 0       | 1       | 0        |
| 1       | 0       | 0        |
| 1       | 1       | 1        |

</blockquote>


<blockquote>


# OR Gate

<img src="https://cdn1.byjus.com/wp-content/uploads/2020/11/Basic-Logic-Gates-1.png" alt="drawing" width="300"/>


The OR gate, like the AND gate, has two or more inputs and one output. It produces an output of 1 if any of its inputs are 1.

Truth Table for a 2-input OR gate:

| Input A | Input B | Output Q |
| ------- | ------- | -------- |
| 0       | 0       | 0        |
| 0       | 1       | 1        |
| 1       | 0       | 1        |
| 1       | 1       | 1        |
</blockquote>

<blockquote>


# XOR Gate

<img src="https://cdn1.byjus.com/wp-content/uploads/2020/11/Basic-Logic-Gates-5.png" alt="drawing" width="300"/>


The XOR (exclusive OR) gate has two inputs and one output. It produces an output of 1 if exactly one of its inputs is 1 (exclusive OR).

Truth Table for a 2-input XOR gate:

| Input A | Input B | Output Q |
| ------- | ------- | -------- |
| 0       | 0       | 0        |
| 0       | 1       | 1        |
| 1       | 0       | 1        |
| 1       | 1       | 0        |

</blockquote>


## Universal Logic Gates

Universal logic gates are gates that can be used to create all other types of logic gates. Two commonly used universal gates are the NAND gate and the NOR gate.

<blockquote>


# NAND Gate

The NAND gate is a universal gate because it can be used to create all other basic logic gates (AND, OR, NOT, XOR). It produces the opposite output of an AND gate.

Truth Table for a 2-input NAND gate:

| Input A | Input B | Output Q |
| ------- | ------- | -------- |
| 0       | 0       | 1        |
| 0       | 1       | 1        |
| 1       | 0       | 1        |
| 1       | 1       | 0        |
<img src="https://i.imgur.com/p2diA71.png" alt="drawing" width="300"/>



</blockquote>


<blockquote>


# NOR Gate

The NOR gate is another universal gate because it can also be used to create all other basic logic gates. It produces the opposite output of an OR gate.

Truth Table for a 2-input NOR gate:

| Input A | Input B | Output Q |
| ------- | ------- | -------- |
| 0       | 0       | 1        |
| 0       | 1       | 0        |
| 1       | 0       | 0        |
| 1       | 1       | 0        |


<img src="https://i.imgur.com/rf7bKFd.png" alt="drawing" width="300"/>



</blockquote>











