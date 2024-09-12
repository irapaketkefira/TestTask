import time

from src.pages.OpenPositionsPage import OpenPositionsPage
import pytest

@pytest.mark.usefixtures("web_driver")
@pytest.mark.idtc2
class TestQAOpenPositionsPage:

    @pytest.fixture(scope='class')
    def setup(self, request):
        request.cls.qa_position_page = OpenPositionsPage(self.driver)

        yield


    def test_check_position_list_is_shown(self, setup):
        self.qa_position_page.go_to_qa_open_positions_page()
        self.qa_position_page.click_on_see_all_qa_jobs_button()
        # TODO: change timeout
        time.sleep(5)
        self.qa_position_page.check_department()
        self.qa_position_page.select_istanbul_location()
        self.qa_position_page.verify_position_list_is_shown()


    def test_check_redirection(self, setup):
        # TODO: change timeout
        time.sleep(5)
        self.qa_position_page.click_on_view_role_button()
        expected_url = "https://jobs.lever.co/useinsider/78ddbec0-16bf-4eab-b5a6-04facb993ddc"
        current_url = self.qa_position_page.get_new_tab_url()
        assert expected_url == current_url, f"Expected url is {expected_url} but current_url {current_url}"

    # def test_check_positions_description(self, setup):
    #     time.sleep(5)
    #     positions = self.qa_position_page.get_positions()
    #     position_amount = len(positions)
    #     exp_number_of_positions = 1
    #     assert position_amount == exp_number_of_positions, f"Expected {exp_number_of_positions} position to be displayed but found {position_amount}"
    #         # for i in position_amount: