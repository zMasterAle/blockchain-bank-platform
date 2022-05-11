<template>
    <div class="center">
        <form @submit="onSubmit">
            <h1>Sign Up</h1> <br> <br>
            <h4>Cliccando sul bottone "Registrati" riceverai una chiave pubblica e una privata, la seconda dovrai conservarla con cura in quanto servirà ad autenticarti</h4> <br>
            <div class="txt_field">
                <h5 onclick="copy(0)">Chiave pubblica (clicca per copiare)</h5>
                <input type="text" id="public_key" readonly>
                <span></span>
            </div>
            <div class="txt_field">
                <h5 onclick="copy(1)">Chiave privata (clicca per copiare)</h5>
                <input type="text" id="private_key" readonly>
                <span></span>
            </div>
            <input type="submit" value="Registrati">
            <div class="signup_link">
                Effettua il <router-link to="/login" tag="a">Login</router-link>
            </div>
        </form>
    </div>
</template>

<script>
(function () {
  const script = document.createElement("script");
  script.src = "./src/scripts/copyToClipboard.js";
  script.async = false;
  document.head.appendChild(script);
})();

export default {
        methods : {
            onSubmit(e){
                e.preventDefault()
                let keyPair = window.crypto.subtle.generateKey(
                {
                    name: "RSA-OAEP",
                    modulusLength: 4096,
                    publicExponent: new Uint8Array([1, 0, 1]),
                    hash: "SHA-256"
                },
                true,
                ["encrypt", "decrypt"]
                ).then((keyPair2) => {
                    window.crypto.subtle.exportKey("spki", keyPair2.publicKey).then(function(publicKeyJwk) {
                        const exported = publicKeyJwk;
                        const exportedAsString = String.fromCharCode.apply(null, new Uint8Array(exported));
                        const exportedAsBase64 = window.btoa(exportedAsString);
                        document.getElementById("public_key").value = exportedAsBase64;
                        publicKey = exportedAsBase64;
                        window.crypto.subtle.exportKey("pkcs8", keyPair2.privateKey).then(function(privateKeyJwk) {
                            const exported = privateKeyJwk;
                            const exportedAsString = String.fromCharCode.apply(null, new Uint8Array(exported));
                            const exportedAsBase64 = window.btoa(exportedAsString);
                            document.getElementById("private_key").value = exportedAsBase64;
                            privateKey = exportedAsBase64;
                        });
                    });
                }).then(() => {
                    obj.sender = "ciao";
                    obj.recipient = publicKey;
                    obj.amount = 100;
                    obj.balance = 100;
                    console.log(JSON.stringify(obj));
                    const Http = new XMLHttpRequest();
                    const url='http://localhost:5000/transactions/new';
                    Http.open("POST", url);
                    Http.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
                    Http.setRequestHeader('Content-Type', 'application/json');
                    Http.setRequestHeader('Access-Control-Allow-Origin', '*');
                    Http.send(JSON.stringify(obj));
                    Http.onreadystatechange = function() {
                        if(this.readyState == 4 && this.status == 200) {
                            console.log(this.responseText);
                        }
                    }
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

.txt_field input{
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

@media (min-width: 1024px) {
    .test {
        min-height: 100vh;
    }
}
</style>