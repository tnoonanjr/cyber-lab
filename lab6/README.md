## Question 1A - Find cookies in the browser UI
We can transfer some money using the bank site and check the network tab of the inspect function on Mozilla Firefox. There we can find headers, request, response, and cookies.

![Q1](https://github.com/user-attachments/assets/623ed43f-4e73-46cb-8077-a5aca014f808)
![Q1_2](https://github.com/user-attachments/assets/e33ce168-540a-431d-80a7-421d20622d0f)


## Question 1B - Set cookies
We import the request instance variable and the make_response method to create responses we can set cookies to. Cookie Q1B2 is limited to one endpoint by setting the argument path='/Q1B2'. Cookie Q1B3 is more secure because we set http_only and secure to true to prevent cross-site tampering.



https://github.com/user-attachments/assets/1d9221cb-1839-40c0-ae2f-bf82a0bc0d65



## Question 2 - CSRF attack
In this attack we automatically submit a form when a user enters our site via a HTML form that targets a hidden inline frame. The inline frame (iframe) silently loads and requests from the bank site and we send the money from the victim users logged in account to our account. Meanwhile, the supposed victim is none the wiser as the form is hidden and no pop-up appears because the iframe has no display.



https://github.com/user-attachments/assets/de4dbb2d-e3ed-4db4-9e06-799e153bc251



## Question 3 - XSS attack
We can test if a form is vulnerable to an XSS attack by attempting to inject a script in the box and submitting.  If the form is vulnerable to an XSS attack, it will give us an alert when it is interpreted as code. Then we can use the script '<script>alert(document.cookie);</script>' to find the cookie value.



https://github.com/user-attachments/assets/aef7de49-09fe-4b6a-87c5-ee8f80fa60ae



## Question 4 - XSS Backdoor
In this attack we brute force codes 000-999 for a backdoor, or a key disables santization on the form and allows us to inject a script. 


https://github.com/user-attachments/assets/f7db6ad5-da8f-4e66-bca4-6e22a39aa556


