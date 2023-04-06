from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import LLMChain

from dotenv import load_dotenv


load_dotenv()


print("STARTING...")
llm = OpenAI(temperature=0.9, verbose=True)
prompt = PromptTemplate(
    input_variables=["product"],
    template="What is a good name for a company that makes {product}?",
)


chain = LLMChain(llm=llm, prompt=prompt)
x = chain.run(input("Product: "))
print(x)
print("THE END!")
