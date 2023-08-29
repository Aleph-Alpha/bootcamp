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