<template>
  <section id="app">
    <navBar> </navBar>
    <router-view></router-view>
  </section>
</template>

<script>
import navBar from './components/navBar.vue';
export default {
  name: 'App',
  components: {
    navBar: navBar,
  }
}
</script>

<style>
body {
  margin: 0px;
}
</style>
