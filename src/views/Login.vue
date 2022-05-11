<template>
    <div class="center">
        <form @submit="onSubmit" id="jquery-login">
            <h1>Login</h1>
            <h4>Inserisci le credenziali per accedere</h4>
            <div class="txt_field">
                <input type="text" id="public_key" required>
                <span></span>
                <label>Chiave pubblica</label>
            </div>
            <div class="txt_field">
                <input type="password" id="private_key" required>
                <span></span>
                <label>Chiave privata</label>
            </div>
            <input type="submit" value="Login">
            <div class="signup_link">
                Non sei registrato? 
                <router-link to="/signup" tag="a">Signup</router-link>
            </div>
        </form>
        <form @submit="onSubmit" id="jquery-logout">
            <h1>Log Out</h1>
            <h4>Premi per effettuare il log Out</h4>
            <input type="submit" value="Log Out">
        </form>
    </div>
</template>

<script>
$(document).ready(function() {
    if (publicKey == "")
    {
        $("#jquery-login").show();
        $("#jquery-logout").hide();
    }
    else
    {
        $("#jquery-login").hide();
        $("#jquery-logout").show();
    }
});
    export default {
        data (){
            return {
                public_key : '',
                private_key : ''
            }
        },
        methods : {
            onSubmit(e){
                e.preventDefault()
                publicKey = document.getElementById("public_key").value;
                privateKey = document.getElementById("private_key").value;

                checkAmount((balance) => {
                    obj.balance = balance;
                });
            }
        }
    }
</script>

<style scoped>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Poppins", sans-serif;
}

body {
    margin: 0;
    padding: 0;
    background: linear-gradient(120deg, #2980b9, #8e44ad);
    height: 100vh;
    overflow: hidden;
}

.center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 400px;
    background: white;
    border-radius: 10px;
    box-shadow: 10px 10px 15px rgba(0, 0, 0, 0.05);
}

.center h1 {
    text-align: center;
    padding: 20px 0;
    color: black;
}

.center form {
    padding: 0 40px;
    box-sizing: border-box;
}

form .txt_field {
    position: relative;
    border-bottom: 2px solid #adadad;
    margin: 30px 0;
}

.txt_field input {
    width: 100%;
    padding: 0 5px;
    height: 40px;
    font-size: 16px;
    border: none;
    background: none;
    outline: none;
}

.txt_field label {
    position: absolute;
    top: 50%;
    left: 5px;
    color: #adadad;
    transform: translateY(-50%);
    font-size: 16px;
    pointer-events: none;
    transition: .5s;
}

.txt_field span::before {
    content: '';
    position: absolute;
    top: 40px;
    left: 0;
    width: 0%;
    height: 2px;
    background: #2691d9;
    transition: .5s;
}

.txt_field input:focus~label,
.txt_field input:valid~label {
    top: -5px;
    color: #2691d9;
}

.txt_field input:focus~span::before,
.txt_field input:valid~span::before {
    width: 100%;
}

.pass {
    margin: -5px 0 20px 5px;
    color: #a6a6a6;
    cursor: pointer;
}

.pass:hover {
    text-decoration: underline;
}

input[type="submit"] {
    width: 100%;
    height: 50px;
    border: 1px solid;
    background: #2691d9;
    border-radius: 25px;
    font-size: 18px;
    color: #e9f4fb;
    font-weight: 700;
    cursor: pointer;
    outline: none;
}

input[type="submit"]:hover {
    border-color: #2691d9;
    transition: .5s;
}

.signup_link {
    margin: 30px 0;
    text-align: center;
    font-size: 16px;
    color: #666666;
}

.signup_link a {
    color: #2691d9;
    text-decoration: none;
}

.signup_link a:hover {
    text-decoration: underline;
}

@media (min-width: 1024px) {
    .test {
        min-height: 100vh;
    }
}
</style>