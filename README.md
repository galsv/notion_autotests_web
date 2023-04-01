## Test UI automation project for Notion
<p align="center">
  <img width="50%" title="Notion" src="notion_autotest_web/resources/images/logo_stacks/notion.png">
</p>
Notion is a freemium productivity and note-taking web application developed by Notion Labs Inc. It offers organizational tools including task management, project tracking, to-do lists, bookmarking, and more.

<!-- Technology -->

### Tools and a technologies
<p  align="center">
  <code><img width="5%" title="Pycharm" src="notion_autotest_web/resources/images/logo_stacks/pycharm.png"></code>
  <code><img width="5%" title="Python" src="notion_autotest_web/resources/images/logo_stacks/python.png"></code>
  <code><img width="5%" title="Pytest" src="notion_autotest_web/resources/images/logo_stacks/pytest.png"></code>
  <code><img width="5%" title="Requests" src="notion_autotest_web/resources/images/logo_stacks/requests.png"></code>
  <code><img width="5%" title="GitHub" src="notion_autotest_web/resources/images/logo_stacks/github.png"></code>
  <code><img width="5%" title="Jenkins" src="notion_autotest_web/resources/images/logo_stacks/jenkins.png"></code>
  <code><img width="5%" title="Allure Report" src="notion_autotest_web/resources/images/logo_stacks/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="notion_autotest_web/resources/images/logo_stacks/allure_testops.png"></code>
  <code><img width="5%" title="Jira" src="notion_autotest_web/resources/images/logo_stacks/jira.png"></code>
  <code><img width="5%" title="Telegram" src="notion_autotest_web/resources/images/logo_stacks/tg.png"></code>
</p>


<!-- Тest Case -->

### Test cases
* Create/Delete page
* Change page title
* Create/Update/Delete block
* Add/Remove member
* Restore/Permanently delete from trash 



<!-- Jenkins -->

### <img width="3%" title="Jenkins" src="notion_autotest_web/resources/images/logo_stacks/jenkins.png"> Run in Jenkins
### [Job](https://jenkins.autotests.cloud/job/notion_ui_autotests/)
##### Main page of the build:
![This is an image](notion_autotest_web/resources/images/screenshots/jenkins.png)
##### After the build is done the test results are available in Allure Report and Allure TestOps

<!-- Allure report -->

### <img width="3%" title="Allure Report" src="notion_autotest_web/resources/images/logo_stacks/allure_report.png"> Allure report
##### Main page of Allure report contains the following blocks:

>- <code><strong>*ALLURE REPORT*</strong></code> - displays date and time of the test, overall number of launched tests,
>- <code><strong>*TREND*</strong></code> - displays trend of running tests for all runs
>- <code><strong>*SUITES*</strong></code> - displays distribution of tests by suites
>- <code><strong>*CATEGORIES*</strong></code> - displays distribution of unsuccessful tests by defect types

![This is an image](notion_autotest_web/resources/images/screenshots/allure_dashboard.png)


##### On the page the list of the tests grouped by suites with status shown for each test. Full info about each test can be shown: tags, severity, duration, detailed steps.
![This is an image](notion_autotest_web/resources/images/screenshots/allure_suites.png)

##### Test run clip
![This is an image](notion_autotest_web/resources/images/screenshots/test_ui.gif)

<!-- Allure TestOps -->

### <img width="3%" title="Allure TestOps" src="notion_autotest_web/resources/images/logo_stacks/allure_testops.png"> Allure TestOps Integration
### [Dashboard](https://allure.autotests.cloud/project/2086/dashboards)
##### Results are uploaded there and the automated test-cases can be automatically updated accordingly to the recent changes in the code.
![This is an image](notion_autotest_web/resources/images/screenshots/allure_testops_dashboard.png)

Test-cases in the project are imported and constantly updated from the code,
so there is no need in complex process of synchronization manual test-cases and autotests.\
It is enough to create and update an autotest in the code and the test-case in TMS always will be in actual state.\
Manual test-cases also can be added in TMS in case of need(via web interface or via code).

![This is an image](notion_autotest_web/resources/images/screenshots/allure_testops_suites.png)


<!-- Jira -->

### <img width="3%" title="Jira" src="notion_autotest_web/resources/images/logo_stacks/jira.png"> Jira integration
##### After configuration TestOps we can integrate results launches in Jira

![This is an image](notion_autotest_web/resources/images/screenshots/jira.png)


<!-- Telegram -->

### <img width="3%" title="Telegram" src="notion_autotest_web/resources/images/logo_stacks/tg.png"> Telegram Notifications
##### Telegram bot sends a brief report to a specified telegram chat by results of each build.

![This is an image](notion_autotest_web/resources/images/screenshots/tg_bot.png)
