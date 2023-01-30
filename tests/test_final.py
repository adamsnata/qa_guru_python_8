from allure_commons.types import Severity

from classes.user import User
from pages.practice_form import practice_form
import allure
from selene.support.shared import browser
from utils import attach

def test_final2():
    with allure.step('Init Form'):
        print('\ntest final')

