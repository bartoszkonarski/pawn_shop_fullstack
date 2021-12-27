<template>
  <section id="app">
    <navBar> </navBar>
    <router-view></router-view>
  </section>
</template>

<script>
//  import addItem from './components/content/addItem.vue';
//  import listItem from './components/content/listItem.vue';
import navBar from './components/navBar.vue';
export default {
  name: 'App',
  components: {
    //  addItem: addItem,
    //  listItem: listItem,
    navBar: navBar,
  }
}
</script>

<style>
body {
  margin: 0px;
}
</style>
