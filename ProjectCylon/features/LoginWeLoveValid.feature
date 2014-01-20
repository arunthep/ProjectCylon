Feature: Test login

@ReloadContext
@valid_login
Scenario: Valid Case
	Given User has [WeLoveHomePage] open
	When User clicks [login] Link
	Then The system displays [WeLoveSigninPage]
        When User enters '1234567890' to [username]
        And User enters '1234' to [password]
        And User clicks [login] button
        Then the system displays [WeloveHomePage]
        And the [currentuser] shows '1234567890'
