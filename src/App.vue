<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import TopBar from "@/components/TopBar.vue";
import HomeView from "./views/HomeView.vue";
import TheWelcome from "./components/TheWelcome.vue";
import TopBarUser from "./components/TopBarUser.vue";

(function () {
    const script = document.createElement("script");
    // import jquery from google
    script.src = "https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js";
    script.async = false;
    document.head.appendChild(script);
})();

(function () {
    const script = document.createElement("script");
    script.src = "./src/scripts/variables.js";
    script.async = false;
    document.head.appendChild(script);
})();

</script>

<template>
    <header>
        <TopBarUser />
    </header>
    <RouterView />
</template>

<style>
* {
    margin: 0;
    padding: 0;
}

body {
    background-color: black;
    overflow: hidden;
    background: linear-gradient(120deg, #2980b9, #8e44ad);
}

</style>
