const registrationForm = document.getElementById("registrationForm");

let fname = registrationForm.querySelector("#fname");
let lname = registrationForm.querySelector("#lname");
let email = registrationForm.querySelector("#email");
let phone = registrationForm.querySelector("#phone");
let password = registrationForm.querySelector("#password");
let dob = registrationForm.querySelector("#dob");
let country = registrationForm.querySelector("#country");
let city = registrationForm.querySelector("#city");

registrationForm?.addEventListener("submit", function (e) {

    e.preventDefault();

    let fnameValue = fname?.value?.trim();
    let lnameValue = lname?.value?.trim();
    let passwordValue = password?.value?.trim();
    let emailValue = email?.value?.trim();
    let phoneValue = phone?.value?.trim();
    let dobValue = dob?.value;
    let countryValue = country?.value?.trim();
    let cityValue = city?.value?.trim();

    // Gender
    let gender = registrationForm.querySelector("[name='gender']:checked");
    let genderValue = gender?.value;

    // Skills
    let skills = registrationForm.querySelectorAll(".skill:checked");


    let fnameError = false;
    let lnameError = false;
    let emailError = false;
    let phoneError = false;
    let passwordError = false;
    let dobError = false;
    let genderError = false;
    let countryError = false;
    let cityError = false;
    let skillsError = false;


    // First Name
    if (!fname || !checkfName(fnameValue, fname)) {
        fnameError = true;
    }


    // Last Name
    if (!lname || !checklName(lnameValue, lname)) {
        lnameError = true;
    }


    // Email
    if (!email || !checkEmail(emailValue, email)) {
        emailError = true;
    }


    // Phone
    if (!phone || !checkPhone(phoneValue, phone)) {
        phoneError = true;
    }


    // Password
    if (!password || !checkPassword(passwordValue, password)) {
        passwordError = true;
    }


    // DOB
    if (!dob || !checkDOB(dobValue, dob)) {
        dobError = true;
    }


    // Gender
    if (!checkGender(genderValue)) {
        genderError = true;
    }


    // Country
    if (!country || !checkCountry(countryValue, country)) {
        countryError = true;
    }


    // City
    if (!city || !checkCity(cityValue, city)) {
        cityError = true;
    }


    // Skills
    if (!checkSkills(skills)) {
        skillsError = true;
    }


    // Final Result
    if (
        !fnameError &&
        !lnameError &&
        !emailError &&
        !phoneError &&
        !passwordError &&
        !dobError &&
        !genderError &&
        !countryError &&
        !cityError &&
        !skillsError
    ) {

        console.log("No Error Found. Form can be submitted now.");

        alert("Registration Successful!");

    } else {

        console.log("Please fill the form correctly and submit again.");

    }

});


// First Name Validation
function checkfName(fname, el) {

    let passed = true;

    let pattern = /^(?=.{3,100}$)[\p{L}]+(?:[ '-][\p{L}]+)*$/u;

    passed = pattern.test(fname);

    let errorel = el?.closest("form")?.querySelector(".fname-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// Last Name Validation
function checklName(lname, el) {

    let passed = true;

    let pattern = /^(?=.{3,100}$)[\p{L}]+(?:[ '-][\p{L}]+)*$/u;

    passed = pattern.test(lname);

    let errorel = el?.closest("form")?.querySelector(".lname-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// Email Validation
function checkEmail(email, el) {

    let passed = true;

    let pattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    passed = pattern.test(email);

    let errorel = el?.closest("form")?.querySelector(".email-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// Phone Validation
function checkPhone(phone, el) {

    let passed = true;

    // Exactly 10 digits
    let pattern = /^[6-9][0-9]{9}$/;

    passed = pattern.test(phone);

    let errorel = el?.closest("form")?.querySelector(".phone-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// Password Validation
function checkPassword(password, el) {

    let passed = true;

    let pattern =
        /^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[!@#$%^&*]).{6,}$/;

    passed = pattern.test(password);

    let errorel = el?.closest("form")?.querySelector(".password-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// DOB Validation
function checkDOB(dob, el) {

    let passed = dob !== "";

    let errorel = el?.closest("form")?.querySelector(".dob-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// Gender Validation
function checkGender(gender) {

    let passed = gender !== undefined;

    let errorel = registrationForm.querySelector(".gender-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// Country Validation
function checkCountry(country, el) {

    let passed = country !== "";

    let errorel = el?.closest("form")?.querySelector(".country-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// City Validation
function checkCity(city, el) {

    let passed = city.length >= 3;

    let errorel = el?.closest("form")?.querySelector(".city-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// Skills Validation
function checkSkills(skills) {

    let passed = skills.length > 0;

    let errorel = registrationForm.querySelector(".skills-error");

    if (!passed) {
        errorel?.classList.add("show");
    } else {
        errorel?.classList.remove("show");
    }

    return passed;
}


// First Name Change Event
fname?.addEventListener("change", function () {
    checkfName(fname.value.trim(), fname);
});


// Last Name Change Event
lname?.addEventListener("change", function () {
    checklName(lname.value.trim(), lname);
});


// Email Change Event
email?.addEventListener("change", function () {
    checkEmail(email.value.trim(), email);
});


// Phone Change Event
phone?.addEventListener("change", function () {
    checkPhone(phone.value.trim(), phone);
});


// Password Change Event
password?.addEventListener("change", function () {
    checkPassword(password.value.trim(), password);
});


// DOB Change Event
dob?.addEventListener("change", function () {
    checkDOB(dob.value, dob);
});


// Country Change Event
country?.addEventListener("change", function () {
    checkCountry(country.value, country);
});


// City Change Event
city?.addEventListener("change", function () {
    checkCity(city.value.trim(), city);
});


// Gender Change Event
registrationForm.querySelectorAll("[name='gender']").forEach(function (radio) {

    radio.addEventListener("change", function () {

        let gender = registrationForm.querySelector(
            "[name='gender']:checked"
        );

        checkGender(gender?.value);

    });

});


// Skills Change Event
registrationForm.querySelectorAll(".skill").forEach(function (skill) {

    skill.addEventListener("change", function () {

        let skills = registrationForm.querySelectorAll(".skill:checked");

        checkSkills(skills);

    });

});