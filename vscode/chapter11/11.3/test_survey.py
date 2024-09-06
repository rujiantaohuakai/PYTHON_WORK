from survey import AnonymousSurvey
import pytest

@pytest.fixture
def language_survey():
    """一个可供所有测试函数使用的AnonymousSurvey实例"""
    question = "What language did you first learn to speak?"
    languagesurvey = AnonymousSurvey(question)
    return languagesurvey #  将此实例传给测试函数的形参(language_survey)
'''
def test_stroe_single_response():
    """测试只有一个回答时能否正常保存"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    language_survey.store_response("English")
    assert 'English' in language_survey.responses

def test_store_three_responses():
    """测试三个回答能否正常保存"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)
    for response in responses:
        assert response in language_survey.responses
'''
def test_stroe_single_response(language_survey):
    """测试只有一个回答时能否正常保存"""
    language_survey.store_response("English")
    assert 'English' in language_survey.responses

def test_store_three_responses(language_survey):
    """测试三个回答能否正常保存"""
    responses = ['English', 'Spanish', 'Mandarin']
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
    