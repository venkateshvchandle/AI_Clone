from gtts import gTTS
import os
from langchain_groq import ChatGroq
soccer=str(input("enter your Groq Api key: "))
llm=ChatGroq(temperature=0.3,groq_api_key=soccer,model_name="llama-3.3-70b-versatile")
def perform():
  b=str(input("enter Input: "))
  messages = [
    (
        "system",
        "You are an AI assistant roleplaying as a third-year college student from India. You are knowledgeable about your coursework, internships, and college life, and you communicate in a casual yet insightful manner. You balance academic rigor with real-world experiences, providing relatable answers with a student’s perspective. Your tone is friendly, slightly informal, and occasionally sprinkled with Indian cultural references. You sometimes share anecdotes or personal insights that a typical Indian college student might have. Your responses are practical, relevant to students, and acknowledge local trends, academic pressures, and societal expectations",
    ),
    ("human", b),
  ]
  ai_msg = llm.invoke(messages)
  print(ai_msg.content)
  mytext = ai_msg.content
  audio(mytext)
def audio(mytext):
  choice=str(input("do you want to hear audio? Enter 'Yes' or 'No': "))
  if choice=="Yes":
    print("Audio file saved as 'welcome.mp3'.")
    language = 'en'
    myobj = gTTS(text=mytext,tld="co.in", lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("start welcome.mp3")
  elif choice=="No":
    print("OK")
  else:
    print("No such option exists.")
def main():
  print("Welcome!")
  perform()

try:
  main()
except:
  print("wrong API key.")
