from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from pymongo import MongoClient
import os
from dotenv import load_dotenv
load_dotenv()
from bson import ObjectId

# # client = MongoClient(os.getenv('MONGO_URI'))
# db = client['mysite']
# question = db.polls_question
# print('all collections', db.list_collection_names())
# # db.polls_question.insert_one({
# #     'question_text': 'What is your favorite color?',
# #     'pub_date': datetime.now()
# # })
# print('----Availiable Questions----')
# all_questions = db.polls_question.find()
# q_num = 1
# for q in all_questions:
#     print('Question number '+str(q_num)+': '+q['question_text']+' (Published on: '+str(q['pub_date'])+')')
#     q_num += 1
# print('')

# new_q = {"question_text": "What's new?", "pub_date": datetime.now()}

# does_new_q_exist_in_db = False

# for q in db.polls_question.find():
#     if q['question_text'] == new_q['question_text']:
#         does_new_q_exist_in_db = True
#         break
# if not does_new_q_exist_in_db:
#     db.polls_question.insert_one(new_q)
#     print('New question added to the database!')
# else:
#     print('Question already exists in the database!')
# print('')

# # TODO search by question_text
# qtext_s = question.find_one({ 'question_text' : "What database do we use for Django?" })
# print('Search by question_text= '+ qtext_s['question_text']+ '(published on: ' +str(qtext_s['pub_date'])+ ')' )
# # TODO Search a question by a certain text
# search_text = 'favorite'
# qtext_s_g = question.find_one({ '$question_text' : 'favorite' })
# print('contains favorite: '+ qtext_s_g['question_text']+ '(published on: ) '+ str(qtext_s_g['pub_date']+ ')'))


# # # TODO Search all questions by one date
# # target_date = datetime.now()

# # # Create a query condition to find questions published on the target date.
# # query_condition = {"pub_date": "2024-02-03T14:28:36.663+00:00"}

# # # Use the find method to search for questions that match the query condition.
# # matching_questions = db.polls_question.find(query_condition)

# # # Print the matching questions.
# # print(f'Questions published on {target_date}:')
# # for question in matching_questions:
#     print(f'Question Text: {question["question_text"]}')
#     print(f'Published Date: {question["pub_date"]}')
#     print()

# # TODO Update a question (pub_date -> needs to be set to current date)
# question.update_one({ '_id':ObjectId('65bebe14d8ccf4c3fe097eb5') }, {
#     "$set": {
#         "question_text": "Are you Jamaican?",
#         "pub_date": datetime.now()
#         }
# })
# update_result = question.find_one({ '_id':ObjectId('65bebe14d8ccf4c3fe097eb5') })
# print('Updated Question= '+ update_result['question_text']+ '(published on: ' +str(update_result['pub_date'])+ ')' )



# # # TODO Delete a question

# # delete_question = {"question_text": "What's new?"}
# # result = db.polls_question.delete_one(delete_question)
# # if result.deleted_count > 0:
# #     print(f'Successfully deleted {result.deleted_count} question(s).')
# # else:
# #     print('No questions matched the deletion condition.')


# Create your views here.
# views = routes
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")