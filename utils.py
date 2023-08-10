from aleph_alpha_client import Client, CompletionRequest, CompletionResponse, SemanticEmbeddingRequest, ExplanationRequest, ExplanationResponse, TextControl, SemanticRepresentation, Prompt
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams, Batch
from scipy.spatial.distance import cosine

import os
from dotenv import load_dotenv

load_dotenv()

# You can add new information here
texts = ["Jackets cost 500€.", "There is no free lunch.", "Aleph Alpha is an AI company located in Heidelberg, Germany."]

class ChatAgent:
    
    def __init__(self, user_name:str, agent_name:str):
        self.user_name = user_name
        self.agent_name = agent_name
        self.client = Client(token=os.getenv("AA_TOKEN"))
        self.memory = []
        self.q_client = QdrantClient(path="db")
        self.init_database()
        self.classes = self.init_classes()

        
    
    def init_database(self):
        
        self.q_client.recreate_collection(
            collection_name="test_collection",
            vectors_config=VectorParams(size=128, distance=Distance.COSINE),
        )
        
        embeddings = []
        for text in texts:
            # TODO: embed the texts
            embeddings.append(self.client.semantic_embed(SemanticEmbeddingRequest(prompt=Prompt.from_text(text), representation=SemanticRepresentation.Document, compress_to_size=128), model="luminous-base").embedding)
                
        
        
        # now we can upsert the data into Qdrant
        ids = list(range(len(texts)))
        payloads = [{"text": text} for text in texts]

        self.q_client.upsert(
            collection_name="test_collection",
            points=Batch(
            ids=ids,
            payloads=payloads,
            vectors=embeddings
            )
        )

    def chat(self, message:str) -> str:
        """
        This function takes a message as input and returns a response.
        It is the main function of the chatbot.
        It can also call other functions like search or classify, however, these functions are not implemented yet.
        
        Args:
            message (str): The message that the user sent to the chatbot.
            
        Returns:
            str: The response of the chatbot.
        """
        
        # classifying the message
        class_ = self.classify(message)
        
        # Create a string that contains the chat history
        history_str = "\n".join([f"{m['role']}: {m['content']}" for m in self.memory])
        
        if class_ == "small_talk":
            prompt = f"""### your instruction using the {history_str}, the {self.user_name}: the {message} and the {self.agent_name}:"""

        else:
            
            return "Not implemented yet"
            
            context = self.search(message)
        
            prompt = f"""### your instruction using the {history_str}, the {self.user_name}: the {message} and the {self.agent_name}:"""
        # Create a completion request
        completion_request = None # TODO: create a completion request
        # Send the request to the Aleph Alpha API
        completion_response = self.client.complete(completion_request, model="luminous-extended-control")
        
        # Store the message and the response in the memory
        self.memory.append({"role": self.user_name, "content": message})
        self.memory.append({"role": self.agent_name, "content": completion_response.completions[0].completion})
        
        print(f"history: {self.memory}")
        
        return completion_response.completions[0].completion





    def search(self, query:str)     -> str:
        """
        This function takes a query as input and returns a context.
        It is used to find a context for the chatbot's response.

        Args:
            query (str): The query that the chatbot should search for.

        Returns:
            str: The context that the chatbot should use for its response.
            
        """
        
        embedded_question = None # TODO: embed the query using the semantic_embed function
    
        # Then we search for the most similar text
        search_result = self.q_client.search(
            collection_name="test_collection",
            query_vector=embedded_question        )
                
        # Then we get the text from the search result
        text = search_result[0].payload["text"]
        
        return text
    

    def classify(self, query:str):
        """
        This function takes a query as input and returns a class.
        It is used to find a class for the chatbot's response.
        """
        
        return "small_talk" # TODO: replace this with your code
        
        # First, we embed the query
        embedded_query = None # TODO: embed the query using the semantic_embed function
        
        # Then we calculate the cosine similarity between the query and each class
        
        similarities = {}
        
        for cls, embeddings in self.classes.items():
            # TODO: calculate the cosine similarity between the query and each class
            
            # TODO: store the similarity in the similarities dictionary
            pass
            
        return max(similarities, key=similarities.get)


    def init_classes(self):
        """
        This is a helper function that initializes the classes of the chatbot.
        You don't need to change anything here.
        """

        it_support = ["Hey IT support team, I'm experiencing some issues with the software. It keeps crashing whenever I try to open a certain file. Can you please look into this and help me resolve the problem? Thanks!",
        "Hi there, I need some assistance with the software's latest update. Ever since I installed it, some features seem to be missing, and the interface looks a bit different. Could you guide me on how to restore the missing functionalities or revert to the previous version? Your help is much appreciated!",
        "Hello IT support, I'm having trouble connecting the software to my printer. It was working fine before, but now I can't seem to print any documents. Could you please walk me through the troubleshooting steps or provide any necessary drivers to fix this issue? Thanks a lot for your help!",
        "Dear IT team, I'm a new user of this software, and I'm finding it a bit confusing to navigate through its features. Is there any user guide or online tutorial available that can help me get started and make the most of its capabilities? Your guidance would be invaluable!",
        "Hi support, I accidentally deleted some important data within the software, and now I'm worried about recovering it. Is there a built-in recovery option, or do you have any recommendations for data recovery tools that work well with this software? Any help to retrieve the lost data would be fantastic! Thank you!",
        ]

        hr = [
        "Hello, I would like to inquire about the employee benefits and the process to enroll in the company's benefits program. Could you please provide me with more information?",
        "Hi there, I recently changed my address and need to update my personal information with the company. Can you guide me on how to do that, or do I need to fill out a form?",
        "Dear team, I'm interested in exploring internal job opportunities within the organization. Are there any current openings, and could you direct me to the appropriate department or person to discuss this further?",
        "Good morning, I have a question about the paid time off policy. I'd like to understand how much accrued leave I currently have and how to request time off. Thank you!",
        "Hey, I wanted to share some positive feedback about a colleague who went above and beyond to assist me on a project. Is there a recognition or appreciation program in place, and if so, how can I nominate this person for their outstanding efforts?",
        ]

        sales = [
        "Hello, I'm interested in purchasing your software product. Could you please provide me with more details about its features, pricing, and licensing options? I'm excited to explore how it can benefit my business!",
        "Hi there, I've been researching software solutions for my specific needs, and your product seems like a perfect fit. Can you offer a demo or trial version so I can evaluate its capabilities before making a purchase decision?",
        "Dear sales team, I'm impressed with the positive reviews and recommendations I've seen about your software. I'm ready to proceed with the purchase and would like to know the steps for placing an order and making payment. Looking forward to getting started with it!",
        "Good day, I'm a long-time user of your free version, and I'm now ready to upgrade to the premium version for more advanced features. Can you please guide me on how to upgrade my account and take advantage of the additional functionalities?",
        "Hi, I run a small business, and I believe your software can streamline our operations significantly. I'm interested in purchasing multiple licenses for my team. Can you provide any special discounts or packages for bulk orders? Thank you!"
        ]
        
        small_talk = [
        "Hello, how are you?",
        "Hi, how's it going?",
        "What's up?",
        "What is your name?",
        "How old are you?",
        "How is the weather today?",
        "What is your favorite color?",
        "What is your favorite food?",
        ]
        
        embeddings_class_1 = [self.client.semantic_embed(SemanticEmbeddingRequest(prompt=Prompt.from_text(text), representation=SemanticRepresentation.Symmetric), model="luminous-base").embedding for text in it_support]
        embeddings_class_2 = [self.client.semantic_embed(SemanticEmbeddingRequest(prompt=Prompt.from_text(text), representation=SemanticRepresentation.Symmetric), model="luminous-base").embedding for text in hr]
        embeddings_class_3 = [self.client.semantic_embed(SemanticEmbeddingRequest(prompt=Prompt.from_text(text), representation=SemanticRepresentation.Symmetric), model="luminous-base").embedding for text in sales]
        embeddings_class_4 = [self.client.semantic_embed(SemanticEmbeddingRequest(prompt=Prompt.from_text(text), representation=SemanticRepresentation.Symmetric), model="luminous-base").embedding for text in small_talk]
        return {"it_support": embeddings_class_1, "hr": embeddings_class_2, "sales": embeddings_class_3, "small_talk": embeddings_class_4}
