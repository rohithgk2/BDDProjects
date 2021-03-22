

 Feature: login page

      Scenario: user logs in

          Given I go to login page
          When I click on login
          Then I should see error
          And I log out