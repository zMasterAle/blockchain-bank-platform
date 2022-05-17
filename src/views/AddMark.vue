<template>
    <div class="center">
        <div class="loading hidden">
            <div class='uil-ring-css' style='transform:scale(0.79);'>
                <div></div>
            </div>
        </div>
        <form @submit="onSubmit">
            <div class="signup_link"></div>
            <h1>Aggiungi voto</h1> <br> <br>
            <h4>Inserisci il voto per ricevere una somma di GiorgiCoin</h4> <br>
            <div class="txt_field">
                <input type="number" id="mark" placeholder="Inserisci il voto" required />
                <span></span>
            </div>
            <input type="submit" value="Registra il voto">
        </form>
    </div>
</template>

<script>
export default {
    methods: {
        data() {
            return {
                mark: ''
            }
        },
        onSubmit(e) {
            e.preventDefault()
            if (publicKey == "") {
                alert("Devi prima effettuare il Login");
            }
            else {
                loadingScreen();
                block.sender = bankPublicKey;
                block.recipient = publicKey;
                block.amount = ((document.getElementById("mark").value) * 10);
                sendTransaction();
            }
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
    height: 315px;
}

.center h1 {
    text-align: center;
    padding: 20px 0;
    color: black;
}

.center h5 {
    color: #adadad;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    user-select: none;
}

.center h5:hover {
    cursor: pointer;
}

.center h5:active {
    color: #2691d9;
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

/* ---------------------------- */
*.hidden {
    display: none !important;
}

div.loading {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(16, 16, 16, 0.5);
    z-index: 100;
    border-radius: 10px;
}

@-webkit-keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@-webkit-keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@-moz-keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@-ms-keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@-moz-keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@-webkit-keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@-o-keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

@keyframes uil-ring-anim {
    0% {
        -ms-transform: rotate(0deg);
        -moz-transform: rotate(0deg);
        -webkit-transform: rotate(0deg);
        -o-transform: rotate(0deg);
        transform: rotate(0deg);
    }

    100% {
        -ms-transform: rotate(360deg);
        -moz-transform: rotate(360deg);
        -webkit-transform: rotate(360deg);
        -o-transform: rotate(360deg);
        transform: rotate(360deg);
    }
}

.uil-ring-css {
    margin: auto;
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    width: 200px;
    height: 200px;
}

.uil-ring-css>div {
    position: absolute;
    display: block;
    width: 160px;
    height: 160px;
    top: 20px;
    left: 20px;
    border-radius: 80px;
    box-shadow: 0 6px 0 0 #ffffff;
    -ms-animation: uil-ring-anim 1s linear infinite;
    -moz-animation: uil-ring-anim 1s linear infinite;
    -webkit-animation: uil-ring-anim 1s linear infinite;
    -o-animation: uil-ring-anim 1s linear infinite;
    animation: uil-ring-anim 1s linear infinite;
}

/* ---------------------------- */

@media (min-width: 1024px) {
    .test {
        min-height: 100vh;
    }
}
</style>