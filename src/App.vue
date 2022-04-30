<script setup>
import { RouterLink, RouterView } from "vue-router";
import HelloWorld from "@/components/HelloWorld.vue";
import TopBar from "@/components/TopBar.vue";
import HomeView from "./views/HomeView.vue";
import TheWelcome from "./components/TheWelcome.vue";
</script>

<template>
  <header>
    <TopBar />
  </header>
  <RouterView />
</template>

<style>
*{
  margin:0;
  padding:0;
}
body{
  background-color: black;
}
</style>
