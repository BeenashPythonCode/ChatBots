#import important libraries
from langchain_ollama.llms import OllamaLLM
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough

llm=OllamaLLM(model="llama3.2:latest ")

search= DuckDuckGoSearchRun()

#chain with LCEL
# This is the prompt template, our instruction manual for the LLM
prompt = ChatPromptTemplate.from_template(
    """You are a helpful AI assistant. You must answer the user's question 
    based *only* on the following search results. If the search results 
    are empty or do not contain the answer, say 'I could not find 
    any information on that.'

    Search Results:
    {context}

    Question:
    {question}
    """
)

#RAG Chain
chain=(
    RunnablePassthrough.assign(
                # "context" is a new key we add to the dictionary.
        # Its value is the *output* of running the 'search' tool
        # with the original 'question' as input.
        context=lambda x: search.run(x["question"])
    )
    | prompt
    | llm
)

print("Hello! I am a real_time AI assistant. What's new?")
while True:
    try:
        user_query=input("You:")
        if user_query.lower() in ["exit","quit"]:
            print("Good Byy!")
            break

        print("Thinking...")

        #running rag process
        response=chain.invoke({"question":user_query})

        print(response)

    except Exception as e:
        print(f"An error occurred: {e}")