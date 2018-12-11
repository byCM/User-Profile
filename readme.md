**DESCRIPTION**<br />

Create a profile page that adds details to registered user. Display the details to the profile page that is visible on login.<br /> Create a page to edit the profile. <br />The profile page will include first name, last name, email, date of birth, confirm email, short bio and avatar upload.<br /> Set up validation for email, date of birth and bio. Date of Birth validation will check for a proper date format: YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY. <br />Email validation will check that the email addresses match and are in a valid format. Bio validation will check that the bio is 10 characters or longer and properly escapes HTML formatting.<br />
Create a "change password page", that updates the user password. <br />This page will ask for current password, new password and confirm password.<br /> Set up validation which checks that the current password is valid, that the new password and confirm password fields match, and that the new password follows the following policy<br />
<br />
-must not be the same as the current password <br />
-minimum password length of 14 characters. <br />
-must use of both uppercase and lowercase letters<br />
-must include of one or more numerical digits<br />
-must include of special characters, such as @, #, $<br />
-cannot contain the user name or parts of the user’s full name, such as his first name<br />
<br />
users can register and are required to fill in some information about them before they are allowed to explore the profile of other users
the admin user has no profile<br />
users can upload avatars and transform them on-site<br />
<br />
<br />
**INSTRUCTIONS** <br/>

Create Django model for user profile<br />
Add necessary routes<br />
Update “profile” view to display the user profile with the following fields: First Name, Last Name, Email, Date of Birth, Bio and Avatar.<br /> Include a link to edit the profile.<br />
Create “edit” view with the route “/profile/edit” that allows the user to edit the user profile with the following fields: First Name, Last Name, Email, Date of Birth, Confirm Email, Bio and Avatar.<br />
Validate user input "Email" field: check that the email addresses match and are in a valid format.<br />
Validate user input "Date of Birth" field: check for a proper date format (YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY)<br />
Validate user input "Bio" field: check that the bio is 10 characters or longer and properly escapes HTML formatting.<br />
Create “change-password” view with the route “/profile/change_password” that allows the user to update their password using User.set_password() and then User.save(). Form fields will be: current password, new password, confirm password<br />
Validate user input "Password" fields: check that the old password is correct using User.check_password() and the new password matches the confirm password field and follows the password policy.<br />
Use CSS to style headings, font, and form.<br />
