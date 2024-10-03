from django import template

register = template.Library()

@register.filter
def get_answer(answers, subquestion_id):
    """
    Custom filter to get the answer for a subquestion with a dynamic key.
    """
    key = f'subquestion{subquestion_id}'
    return answers.get(key, '')

@register.filter
def get_response(response, question_id):
    key = f'question{question_id}'
    return response.get(key, '')