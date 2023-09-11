### Luminous Model Family
The Luminous series is a family of large language models. Large language models are powerful technological tools that can process and produce human text. They have acquired this ability by “reading” enormous amounts of human text data during training. Similar to someone reading a whole library and half of the internet, large language models have acquired a structural understanding of language and accumulated information about the world.

The Luminous family currently consists of three vanilla models, which differ in complexity and ability. They are, from the smallest to the largest, Luminous-base, Luminous-extended and Luminous-supreme. All Luminous models have been trained in the five most commonly spoken European languages: English, German, French, Italian and Spanish. Contrary to other large language models, the Luminous family posseses the ability to work with images as well. We call this multimodality. All three vanilla models are also available in an instruction-finetuned version, our Luminous-control models.

 | Model | Description |
| --- | --- |
| Luminous-supreme | The largest model in the Luminous model family, it is capable of solving all tasks the smaller models can solve. |
| Luminous-extended | Our second-largest model, it is well suited for tasks like information extraction and language simplification. |
| Luminous-base | The smallest model in the Luminous model family, it is the fastest and cheapest model. |
| Luminous-control models | Our control models are versions of models optimized to follow instructions. One of their great advantages is that they have much better zero-shot performance compared to our vanilla models. They have been fine-tuned for a diverse set of tasks described by human-written instructions. They have much better zero-shot performance compared to our vanilla models. |

### Interacting with Luminous models
You can interact with a Luminous model by sending it a text. We call this a prompt. It will then produce text that continues your input and return it to you. This is what we call a completion. Generally speaking, our models attempt to find the best continuation for a given input. Practically, this means that the model first recognizes the style of the prompt and then attempts to continue it accordingly. Depending on the task at hand, the structure and content of the prompt are essential to generating completions that match the input task. By using a set of techniques, which we lay out in the following sections, you can instruct our models to solve a wide variety of text-based tasks. Note that increasing task complexity may require larger models.

### Semantic Embeddings
With our semantic_embed-endpoint you can create semantic embeddings for your text. 
This functionality can be used in a myriad of ways. 
For more information please check out our blog-post on Luminous-Explore, introducing the model behind the semantic_embed-endpoint. 
In order to effectively search through your own documents, it is important to ensure that they can be easily compared to each other. 
Our asymmetric embeddings are designed to help find the pieces of your documents that are most relevant to a query shorter than the documents in the database. 
Here we will use short queries and longer splits of law texts.


### Completion
You can interact with a Luminous model by sending it a text. We call this a prompt. 
It will then produce text that continues your input and return it to you. This is what we call a completion. 
Generally speaking, our models attempt to find the best continuation for a given input. 
Practically, this means that the model first recognizes the style of the prompt and then attempts to continue it accordingly.

### Zero-Shot Prompting
For certain tasks, simply providing a natural language instruction to the model may be sufficient to obtain a good completion. This is called zero-shot prompting. Let’s illustrate this using an example.

Provide a short description of AI: AI is a set of techniques that use machine learning to make computer programs learn from data.
This worked well! However, the model’s best continuation is not necessarily aligned with your desired continuation. Therefore, it may not be enough to simply give the model natural language instructions for its task.

### Few-Shot Prompting
For more complicated tasks, or those that require a specific format, you may have to explicitly show how to properly continue your prompt – by providing one or more examples. This is called few-shot learning (or one-shot learning in the case of just a single example). Let’s have a look at how this plays out in practice.

### Attention Manipulation (AtMan)
AtMan is our method to manipulate the attention of an input sequence (this can be a token, a word, or even a whole sentence) to steer the model's prediction in a different contextual direction. With AtMan, you can manipulate attention in both directions, either suppressing or amplifying an input sequence. If you would like to know more about the technical details of AtMan, you can refer to the paper we published.

Suppressing
Attention manipulation can suppress the attention that is given to a token (or a set of tokens) in an input. This opens up a lot of opportunities to design your prompt. The completion for the following prompt without any attention manipulation looks like this:

Hello, my name is Lucas. I like soccer and basketball. Today I will play soccer.
With AtMan, you can suppress any part of a text in your prompt to obtain a different completion. In this example, we will suppress "soccer":

Hello, my name is Lucas. I like soccer and basketball. Today I will play basketball with my friends.
We can see that the suppression of soccer led to a different completion.

Amplifying
AtMan does not only allow you to suppress but also amplify the attention given to a token. The completion for the following prompt without any attention manipulation looks like this:

I bought a game and a party hat. Tonight I will be wearing the party hat while playing the game.
Let's say that we really want to play the game tonight. In this case, we can amplify the attention paid to "game":

I bought a game and a party hat. Tonight I will be playing games with my friends.
Again, the attention manipulation led to a different completion.


### Evaluate
With our evaluate-endpoint you can score the likelihood of pre-defined completions. This is useful if you already know the output you would expect and which completion our models would return. The major advantage is that the evaluate-endpoint is significantly faster than the complete-endpoint.

Pricing
Our Luminous models come in different sizes and prices. To find out which one suits your needs, you can refer to our Introduction section.

One token is roughly equivalent to a short word or a syllable. As a rule of thumb, 1000 tokens are about 720 words. Images always have 144 tokens, regardless of their size and resolution.

Credits are Aleph Alpha’s internal calculation unit. We use them to better allocate the costs of your usage and to provide you with a detailed overview of your spending.

All prices shown are in credits and the respective EUR equivalent.

Token-based Model Pricing
In the table below you can find the base prices per model.

 | Model | Price per 1000 input tokens | Price per input image |
| --- | ---: | ---: |
| Base | 0.03 (€0.006) | 0.03024 (€0.006048) |
| Extended | 0.045 (€0.009) | 0.04536 (€0.009072) |
| Supreme | 0.175 (€0.035) | - |
| Base-control | 0.0375 (€0.0075) | - |
| Extended-control | 0.05625 (€0.01125) | - |
| Supreme-control | 0.21875 (€0.04375) | - |



