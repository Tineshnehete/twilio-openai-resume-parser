import json
from config import OPENAI_API_KEY
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

model = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY, temperature=0)
parser = JsonOutputParser()

prompt = ChatPromptTemplate.from_template("""
You are a professional resume parser.
Extract the following details from the text.

Return **only JSON** with these keys:
name, email, phone, skills, suitable_job_roles, years_of_experience, education_level, work_experience, certifications, summary
Example : {{
  "name": "...",
  "email": "...",
  "phone": "...",
  "skills": "...",
  "suitable_job_roles": "..." -> Text,
  "years_of_experience": "...",
  "education_level": "...",
  "work_experience": "..." -> Text ,
  "certifications": "...",
  "summary": "..."  
}}

Text:
{text}
""")

def extract_fields_with_langchain(text: str):
    try:
        chain = prompt | model | parser
        resp = chain.invoke({"text": text})
        print(resp)
        parsed =  resp
        return {
            "name": parsed.get("name"),
            "email": parsed.get("email"),
            "phone": parsed.get("phone"),
            "skills": parsed.get("skills"),
            "suitable_job_roles": parsed.get("suitable_job_roles"),
            "years_of_experience": parsed.get("years_of_experience"),
            "education_level": parsed.get("education_level"),
            "work_experience": parsed.get("work_experience"),
            "certifications": parsed.get("certifications"),
            "summary": parsed.get("summary")

        }
    except Exception as e:
        print("LangChain extraction failed:", e)
        return {"name": None, "email": None, "phone": None, "skills": None}
