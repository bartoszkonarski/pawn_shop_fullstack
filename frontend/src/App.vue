<template>
  <section id="app">
    <navBar 
    @logOut="loggOut()"
    > </navBar>
    <router-view
    @logIn="loggIn($event)"
    ></router-view>
  </section>
</template>

<script>
import navBar from './components/navBar.vue';

export default {
  name: 'App',
  components: {
    navBar: navBar,
  },
  data: function() {
    return{
    }
  },
  methods:{
    loggOut: function() {
      this.$session.destroy();
      this.$router.push('/log');
      window.location.reload();
    },
    loggIn: function(tokken) {
      this.$session.start();
      this.$session.set('tokken',tokken)
      this.$router.push('/');
      window.location.reload();
    },
  },
}
</script>

<style>
body {
  margin: 0px;
  background: #663EFF;
}
</style>
