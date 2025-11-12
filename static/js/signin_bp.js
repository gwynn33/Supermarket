import { email_validation , password_validation , password_matching} from "./fn/validation.js";
import { SendRequest } from "./fn/api.js";

document.getElementById('signupForm').addEventListener('submit', async e => {
    e.preventDefault();
    
    try {
        const full_name = document.forms["signupForm"]["fullname"].value;
        const city = document.forms["signupForm"]["cty"].value;
        const phone_number = document.forms["signupForm"]["phone_number"].value;
        const email = document.forms["signupForm"]["Email"].value;
        const birth = document.forms["signupForm"]["Date"].value;
        const gender = document.forms["signupForm"]["gender"].value;
        const password = document.forms["signupForm"]["password"].value;
        const confirmed_password = document.forms["signupForm"]["confirmed_password"].value;
        const terms = document.forms["signupForm"]["terms1"].checked;
    
        if (!password_matching(password,confirmed_password) ||
         !password_validation(password) ||
         !email_validation(email) ||
        terms !== true ) {
            if (!email_validation(email)) alert("Please enter a valid email address (e.g. user@example.com)");
            if (!password_validation(password)) alert("the Password doesn't meet security requirements.");
            if (password_matching(password,confirmed_password)) alert("Password doesn't match!");
            if (terms !== true) alert("You have to accept our terms first!");
            alert("Password doesn't match");
        } else { 
            const data = { 
            full_name : full_name.trim(),
            city : city.trim(),
            phone : phone_number.trim(),
            email : email.trim(),
            birth : birth,
            gender : gender,
            password : password.trim(),
            };
        
            const result = await SendRequest(data,'/signin');
        
            if (result.success) { 
                console.log("hi");
                console.log(result.message);
                window.location.href = "/login";
            } else {
                console.log(result.error || "Unknown Error");
                window.location.href = "/"
            }
        }

    } catch (err) {
        console.error(err);
    }
})