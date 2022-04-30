<template>
    <div class="topnav" id="myTopnav">
        <div class="logo">
            <router-link to="/" tag="a">BlockBank</router-link>
        </div>
        <div class="options">
            <router-link to="/" tag="a">Home</router-link>
            <router-link to="/contact" tag="a">Contact</router-link>
            <router-link to="/about" tag="a">About</router-link>
        </div>
        <div class="login">
            <a href="#" class="login-btn">Login</a>
        </div>
    </div>
</template>

<style scoped>
    .topnav {
    background: rgb(29, 29, 29);
    overflow: hidden;
    display: flex;
    justify-content: space-between;
    align-items: center;
    font-family: "Open Sans", sans-serif;
    padding: 0px 20px;
    }
    .topnav .logo a{
    float: left;
    display: block;
    color: white;
    text-align: center;
    text-decoration: none;
    font-size: 20px;
    margin-right: 3px;
    }
    .topnav .options a{
    float: left;
    display: block;
    color: white;
    text-align: center;
    padding: 9px 11px;
    text-decoration: none;
    font-size: 17px;
    margin-right: 3px;
    }
    .topnav .options{
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
    background-color: rgb(0, 136, 139);
    }
    .topnav .options a:hover {
    color: rgb(0, 136, 139)
    }
    .topnav .login a:hover {
    color: black;
    transition: 0.3s;
    background-color: rgb(0, 104, 105);
    }
    .topnav .login a:not(:hover) {
        transition: 0.3s;
    }
    .topnav a.active {
    color: rgb(0, 136, 139);
    }

    .topnav .icon {
    display: none;
    }
    @media screen and (max-width: 600px) {
    .topnav a:not(:first-child) {display: none;}
    .topnav a.icon {
        float: right;
        display: block;
    }
    }

    @media screen and (max-width: 600px) {
    .topnav.responsive {position: relative;}
    .topnav.responsive .icon {
        position: absolute;
        right: 0;
        top: 0;
    }
    .topnav.responsive a {
        float: none;
        display: block;
        text-align: left;
    }
    }
</style>