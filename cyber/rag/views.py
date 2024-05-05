import os

from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings

from .models import Pdf_Model, Questions

OPENAI_API_KEY = ""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
media_pdf_path = os.path.join(BASE_DIR, 'media', 'pdfs')
print(media_pdf_path)
if os.path.exists(media_pdf_path):
    loader = PyPDFDirectoryLoader(media_pdf_path, glob="**/*.pdf")
    docs = loader.load()
    print('-------', len(docs))  # Print number of loaded PDFs
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20, length_function=len,
                                                   is_separator_regex=False, )
    documents = text_splitter.split_documents(docs)

else:
    print("The media/pdf directory does not exist.")


def chunking_doc():
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20, length_function=len,
                                                   is_separator_regex=False, )
    documents = text_splitter.split_documents(docs)
    print(len(documents))


def home(request):
    document_names = []
    if request.method == "POST":
        user = request.user
        documents = request.FILES.getlist("pdf")
        document_names = [document.name for document in documents]
        documents_list = [Pdf_Model(file=document, user=user) for document in documents]
        Pdf_Model.objects.bulk_create(documents_list)
        print("Uploaded PDF names:", document_names)
        # initialize_system()
        messages.success(request, "PDF Uploaded")
    return render(request, 'rag/home.html', {'document_names': document_names})


# print('----------------------')
# # print(len(documents[0]))
# print(documents[0])
# print('----------------------')

template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer. Use three sentences maximum. Keep the answer as concise as possible. Always Give me answer in HTML format.
use h1 for headings and <b> for bold text and <a> for links.
{context}
Question: {question}
Helpful Answer: """
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)  # Run chain


def qa_llm():
    llm = ChatOpenAI(
        openai_api_key=OPENAI_API_KEY,
        model_name='gpt-4',
        temperature=0.0
    )
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = Chroma.from_documents(docs, embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever, return_source_documents=True,
                                     chain_type_kwargs={"prompt": QA_CHAIN_PROMPT})
    return qa


# qa = qa_llm()
# instruction = "What is the CJIS?"
# generated_text = qa(instruction)
# print('----------------------')
# print(generated_text['result'])
# print('----------------------')


# # Create your views here.
# def home(request):
#     return render(request, 'home.html')

def staff_chatbot(request):
    chat_history = request.session.get('chat_history', [])
    if request.method == 'POST':
        question = request.POST.get('question')

        if "ahsa" in question.lower() or "american high school academy" in question.lower():
            response = 'test'
        else:
            qa = qa_llm()
            response = qa(question)['result']
            print(response)

            if response:
                chat_history.append({'question': question, 'response': response})
                request.session['chat_history'] = chat_history
                request.session.save()

                # Save user feedback to the database
                is_positive = request.POST.get('is_positive', None)
                print(is_positive)

            else:
                response = "No matching found."
        return JsonResponse({'response': response, 'chat_history': chat_history})
    random_questions = Questions.objects.order_by('?')[:4]
    context = {
        'random_questions': random_questions
    }
    return render(request, 'rag/rag_chatbot.html', context=context)


def chatbot_response(request):
    return render(request, 'rag/index.html')
