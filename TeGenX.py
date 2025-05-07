#library
import streamlit as st
from happytransformer import HappyGeneration, GENSettings
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer






#gnerate text
@st.cache_resource
def texGenOne(text):
       #model
       happy_gen = HappyGeneration('GPT-NEO','EleutherAI/gpt-neo-125m')
       #using the model (hugging face)(although is not better, it is not heavy for our job)
       top_k_sampling_settings = GENSettings(
       do_sample=True,
       top_k=40,
       top_p=0.9,
       temperature=0.7,
       max_length=150,
       early_stopping=False,
       no_repeat_ngram_size=3
       )
       #text generate
       result = happy_gen.generate_text(text, args=top_k_sampling_settings)
       return result.text

@st.cache_resource
def textGenTwo(text):
       #model
       tokenizer = AutoTokenizer.from_pretrained("distilgpt2") 
       model = AutoModelForCausalLM.from_pretrained("distilgpt2")  

       input_text = text
       input_ids = tokenizer.encode(input_text, return_tensors="pt")

       output = model.generate(
       input_ids,
       max_length=100,
       temperature=0.9,
       top_k=50,
       top_p=0.95,
       repetition_penalty=1.2,
       do_sample=True,
       num_return_sequences=1
       )
       generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
       return generated_text 

@st.cache_resource
def textGenThree(text):
       #model
       tokenizer = AutoTokenizer.from_pretrained("gpt2-medium")
       model = AutoModelForCausalLM.from_pretrained("gpt2-medium")  

       input_text = text
       input_ids = tokenizer.encode(input_text, return_tensors="pt")

       output = model.generate(
       input_ids,
       max_length=100,
       temperature=0.9,
       top_k=50,
       top_p=0.95,
       repetition_penalty=1.2,
       do_sample=True,
       num_return_sequences=1
       )

       generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
       return generated_text
       
@st.cache_resource
def textGenFour(text):
       tokenizer = GPT2Tokenizer.from_pretrained("HooshvareLab/gpt2-fa")
       model = GPT2LMHeadModel.from_pretrained("HooshvareLab/gpt2-fa")
       input_ids = tokenizer.encode(text, return_tensors="pt")
       outputs = model.generate(
              input_ids,
              max_length=100,
              num_beams=5,
              no_repeat_ngram_size=2,
              early_stopping=True
       )
       return tokenizer.decode(outputs[0], skip_special_tokens=True)
       
st.title("🧠 TeGenX Text Generator")
#model option
'''## English Model'''
mod = st.checkbox('EleutherAI/gpt-neo-125m',key='model1')
mod2 = st.checkbox('distilgpt2',key='model3')
mod3 = st.checkbox('gpt2-medium',key='model2')
st.info('User can use better models. Visit the hugging face and then search about gpt-neo model, they are better, however heavier')
'''## Persian model'''
mod4 = st.checkbox('HooshvareLab/gpt2-fa',key='model4')

#chat input
upl = st.chat_input('write something and then wait for be genrated :)')
#call the function with the selected model
if upl:
       if mod:
              work_model = texGenOne(upl)
       elif mod2:
              work_model = textGenTwo(upl)
       if mod3:
              work_model = textGenThree(upl)
       if mod4:
              work_model = textGenFour(upl)
       
       
       '''# Result'''
       html_code = f'<div style="background-color:gray;color:gold;font-size:40px;padding: 10px; border-radius: 6px;">{work_model}</div>'
       
       st.markdown(html_code,unsafe_allow_html=True)
