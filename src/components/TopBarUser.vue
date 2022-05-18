<template> 
    <div class="topnavUser" id="myTopnavUser">
        <div class="logo">
            <router-link to="/login" tag="a">BlockBank</router-link>
        </div>
        <div class="options">
            <router-link to="/addMark" tag="a">Aggiungi voto</router-link>
            <router-link to="/sendMoney" tag="a">Invia denaro</router-link>
            <router-link to="/mine" tag="a">Mina GiorgiCoin</router-link>
            <router-link to="/checkMoney" tag="a">Controlla il saldo</router-link>
        </div>
        <div class="login">
            <router-link to="/login" tag="a" class="login-btn">Login</router-link>

        </div>
    </div>
</template>

<style scoped>
    .topnavUser {
    background: rgb(29, 29, 29);
    overflow: hidden;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: "Open Sans", sans-serif;
    padding: 0px 20px;
    }
    .topnavUser .logo a{
    float: left;
    display: block;
    color: white;
    text-align: center;
    text-decoration: none;
    font-size: 20px;
    margin-right: 3px;
    }
    .topnavUser .options a{
    float: left;
    display: block;
    color: white;
    text-align: center;
    padding: 9px 11px;
    text-decoration: none;
    font-size: 17px;
    margin-right: 3px;
    }
    .topnavUser .options{
        padding: 7px 9px;
    }
    .login a{
    float: left;
    display: block;
    color: black;
    text-align: center;
    padding: 9px 11px;
    text-decoration: none;
    font-size: 17px;
    border-radius: 50px;
    background-color: #2691d9;
    }
    .topnavUser .options a:hover {
    color: #2691d9
    }
    .topnavUser .login a:hover {
    color: black;
    transition: 0.3s;
    background-color: #156ea8;
    }
    .topnavUser .login a:not(:hover) {
        transition: 0.3s;
    }
    .topnavUser a.active {
    color: #2691d9;
    }

    .topnavUser .icon {
    display: none;
    }
    @media screen and (max-width: 600px) {
    .topnavUser a:not(:first-child) {display: none;}
    .topnavUser a.icon {
        float: right;
        display: block;
    }
    }

    @media screen and (max-width: 600px) {
    .topnavUser.responsive {position: relative;}
    .topnavUser.responsive .icon {
        position: absolute;
        right: 0;
        top: 0;
    }
    .topnavUser.responsive a {
        float: none;
        display: block;
        text-align: left;
    }
    }
</style>