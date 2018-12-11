**DESCRIPTION**<br />

User Profile with Django

**INSTRUCTIONS** <br/>

>- Use HTML/CSS to build and style the profile page and bio page.
>- Create a Django model for the user profile.
>- Add routes to display a profile, edit a profile, and change the password.
>- Create a “profile” view to display a user profile with the following fields: First Name, Last Name, Email, Date of Birth, Bio and Avatar. Include a link to edit the profile.
>- Create an “edit” view with the route “/profile/edit” that allows the user to edit the user profile with the following fields: First Name, Last Name, Email, Date of Birth, Confirm Email, Bio and Avatar.
>- Validate user input "Date of Birth" field: check for a proper date format (YYYY-MM-DD, MM/DD/YYYY, or MM/DD/YY)
>- Validate user input "Email" field: check that the email addresses match and are in a valid format.
>- Validate user input "Bio" field: check that the bio is 10 characters or longer and properly escapes HTML formatting.
>- Add the ability to upload and save a user’s avatar image.
>- Create “change-password” view with the route “/profile/change_password” that allows the user to update their password using User.set_password() and then User.save(). Form fields will be: current password, new password, confirm password
>- Use CSS to style headings, font, and form.
>- Coding Style - Make sure your coding style complies with PEP 8.
>- JavaScript is utilized for a date dropdown for the Date of Birth validation feature.
>- JavaScript is utilized for text formatting for the Bio validation feature.
>- Add an online image editor to the avatar. Include the basic functionality: rotate, crop and flip. PNG mockup supplied.
>- A password strength “meter” is displayed when validating passwords.
>- Validate user input "Password" fields: check that the old password is correct using User.check_password() and the new password matches the confirm password field and follows the following password policy. Password must meet requirements.



**PASSWORD REQUIREMENTS**<br />
>- Must not be the same as the current password <br />
>- Minimum password length of 14 characters. <br />
>- Must use of both uppercase and lowercase letters<br />
>- Must include of one or more numerical digits<br />
>- Must include of special characters, such as @, #, $<br />
>- Cannot contain the user name or parts of the user’s full name, such as his first name<br />
<br />
Users can register and are required to fill in some information about themselves before they are allowed to explore the profile of other users. The admin user has no profile<br />
Users can upload avatars and transform them on-site<br />
<br />
