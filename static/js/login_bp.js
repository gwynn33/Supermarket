import { SendRequest } from "./fn/api.js";
import { email_validation,password_validation } from "./fn/validation.js";  

// process to distinct login operation
const userTypes = document.querySelectorAll('.user-type');
console.log(userTypes);
userTypes.forEach(type => {
    type.addEventListener('click', () => {
        userTypes.forEach(t => t.classList.remove('active'));
        type.classList.add('active')
    });
});
// storing the type Selected :) 
document.getElementById('loginForm').addEventListener('submit',async e => {
    e.preventDefault();
    const active_type = document.querySelector('.user-type.active').dataset.type;
    if (active_type === 'admin') {

        //getting form data :)
        const email = document.forms["loginForm"]["Email"].value;
        const password = document.forms["loginForm"]["password"].value;

        if (!email_validation(email) || !password_validation(password)) {
            if (!password_validation(password)) alert("the Password doesn't meet security requirements.");
            if (!email_validation(email)) alert("Please enter a valid email address (e.g. user@example.com)");
        } else {
            const admin_data = { 
            form_email : email,
            form_password : password,
            type : "admin"
            };

            const result = await SendRequest(admin_data,'/login');

            if (result.success && result.type === "admin") { 
                window.location.href = "/staff_page";
            }else {
                // window.location.href = "https://www.google.com/search?client=firefox-b-d&sca_esv=3e9e96290d2670da&sxsrf=AE3TifMqxe8aMSyY3K7cbo6VW-uHRLI1jg:1762806268850&udm=2&fbs=AIIjpHx4nJjfGojPVHhEACUHPiMQ_pbg5bWizQs3A_kIenjtcpTTqBUdyVgzq0c3_k8z34EAuM72an33lMW6RWde9ePJpwNFtZw3UQvFloZy04_0a6h4-6bsvducFHIbX97zZBYvb8RbW0KF92kZOjKqEHHKBRuHqGyYenLH35X1C5JiteXmy7xNM1XVcgexHEdDEKD5nuKVCyCgCPVVMt7ehJSRi5X20w&q=cats&sa=X&ved=2ahUKEwinuNmLteiQAxVgUkEAHeGrMHUQtKgLegQIJhAB"
                window.location.href = "/";
                console.log("Login failed:", result.error || result.status || "Unknown Error");
            };
        }

    }else {
        const email = document.forms["loginForm"]["Email"].value;
        const password = document.forms["loginForm"]["password"].value;

        if (!email_validation(email) || !password_validation(password)) {
            if (!email_validation(email)) alert("Please enter a valid email address (e.g. user@example.com)");
            if (!password_validation(password)) alert("the Password doesn't meet security requirements.");
            
        } else {
            const user_data = {
            form_email : email,
            form_password : password,
            type : "user"
            };

            const result = await SendRequest(user_data,'/login');

            if (result.success && result.type === "user") {
                window.location.href = "/Hormarket";
            } else {
                window.location.href = "https://www.google.com/search?client=firefox-b-d&sca_esv=3e9e96290d2670da&sxsrf=AE3TifMqxe8aMSyY3K7cbo6VW-uHRLI1jg:1762806268850&udm=2&fbs=AIIjpHx4nJjfGojPVHhEACUHPiMQ_pbg5bWizQs3A_kIenjtcpTTqBUdyVgzq0c3_k8z34EAuM72an33lMW6RWde9ePJpwNFtZw3UQvFloZy04_0a6h4-6bsvducFHIbX97zZBYvb8RbW0KF92kZOjKqEHHKBRuHqGyYenLH35X1C5JiteXmy7xNM1XVcgexHEdDEKD5nuKVCyCgCPVVMt7ehJSRi5X20w&q=cats&sa=X&ved=2ahUKEwinuNmLteiQAxVgUkEAHeGrMHUQtKgLegQIJhAB"
                throw new Error(result.error || "Unknown Error!");
            }
        }
    }
});